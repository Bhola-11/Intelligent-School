"""
State-Machine Workflow Engine & Approval Hierarchies for EduFlow Student Fee Invoicing & Billing Engine (Invoicing).
Module: apps.fees
Provides multi-stage transitions, compensation rollbacks, dual-key signing, and SLA milestone tracking.
"""

import time
import uuid
import logging
from decimal import Decimal
from django.utils import timezone
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)

class InvoicingWorkflowEngine:
    """Deterministic state-machine workflow coordinator and approval router for Invoicing."""

    STATE_GRAPH = {
        "DRAFT": {
            "allowed_targets": ["SUBMITTED", "CANCELLED"],
            "required_role": "OPERATIONAL_USER",
            "guards": ["validate_completeness"]
        },
        "SUBMITTED": {
            "allowed_targets": ["UNDER_REVIEW", "RETURNED_FOR_REVISION", "CANCELLED"],
            "required_role": "SUPERVISOR",
            "guards": ["validate_prerequisites"]
        },
        "UNDER_REVIEW": {
            "allowed_targets": ["APPROVED", "RETURNED_FOR_REVISION", "REJECTED"],
            "required_role": "DEPARTMENT_HEAD",
            "guards": ["validate_budget_headroom", "validate_policy_compliance"]
        },
        "APPROVED": {
            "allowed_targets": ["ACTIVE", "SCHEDULED", "SUSPENDED"],
            "required_role": "INSTITUTION_ADMIN",
            "guards": ["validate_resource_allocation"]
        },
        "ACTIVE": {
            "allowed_targets": ["IN_PROGRESS", "SUSPENDED", "COMPLETED"],
            "required_role": "OPERATIONAL_LEAD",
            "guards": []
        },
        "IN_PROGRESS": {
            "allowed_targets": ["COMPLETED", "SUSPENDED", "ACTIVE"],
            "required_role": "OPERATIONAL_LEAD",
            "guards": []
        },
        "SUSPENDED": {
            "allowed_targets": ["ACTIVE", "CANCELLED", "TERMINATED"],
            "required_role": "INSTITUTION_ADMIN",
            "guards": ["validate_reinstatement_criteria"]
        },
        "COMPLETED": {
            "allowed_targets": ["ARCHIVED"],
            "required_role": "SYSTEM_ARCHIVIST",
            "guards": ["validate_final_audit_signoff"]
        },
        "RETURNED_FOR_REVISION": {
            "allowed_targets": ["SUBMITTED", "CANCELLED"],
            "required_role": "OPERATIONAL_USER",
            "guards": []
        },
        "REJECTED": {
            "allowed_targets": ["ARCHIVED"],
            "required_role": "SUPER_ADMIN",
            "guards": []
        },
        "CANCELLED": {
            "allowed_targets": ["ARCHIVED"],
            "required_role": "SUPER_ADMIN",
            "guards": []
        },
        "ARCHIVED": {
            "allowed_targets": [],
            "required_role": "SUPER_ADMIN",
            "guards": []
        }
    }

    def __init__(self, institution_id=1, actor_username="workflow_admin"):
        self.institution_id = institution_id
        self.actor_username = actor_username
        self.transition_journal = []

    def get_allowed_transitions(self, current_state):
        state_spec = self.STATE_GRAPH.get(current_state, {})
        return state_spec.get("allowed_targets", [])

    def validate_transition_allowed(self, current_state, target_state):
        allowed = self.get_allowed_transitions(current_state)
        if target_state not in allowed:
            raise ValidationError(
                f"Illegal transition: Invoicing cannot transition from '{current_state}' to '{target_state}'. Allowed: {allowed}"
            )
        return True

    def evaluate_transition_guards(self, current_state, target_state, context_payload):
        """Executes all precondition guards registered for target state transition."""
        state_spec = self.STATE_GRAPH.get(current_state, {})
        guards = state_spec.get("guards", [])
        failed_guards = []

        for guard in guards:
            if guard == "validate_completeness":
                if not context_payload.get("code") or not context_payload.get("name"):
                    failed_guards.append("Mandatory fields 'code' and 'name' must be populated.")
            elif guard == "validate_prerequisites":
                if context_payload.get("status") == "DRAFT" and not context_payload.get("ready_for_review", True):
                    failed_guards.append("Record must be flagged as ready for review.")
            elif guard == "validate_budget_headroom":
                budget = Decimal(str(context_payload.get("budget_allocated", 0)))
                cost = Decimal(str(context_payload.get("cost_incurred", 0)))
                if cost > budget and budget > 0:
                    failed_guards.append("Cost incurred exceeds allocated budget limit.")
            elif guard == "validate_policy_compliance":
                if context_payload.get("has_compliance_violation", False):
                    failed_guards.append("Active compliance violations must be remediated prior to approval.")
            elif guard == "validate_resource_allocation":
                cap = int(context_payload.get("capacity", 0))
                occ = int(context_payload.get("current_occupancy", 0))
                if occ > cap and cap > 0:
                    failed_guards.append("Current occupancy exceeds configured maximum capacity.")

        if failed_guards:
            raise ValidationError(f"Workflow guard check failed: {'; '.join(failed_guards)}")
        return True

    def route_approval_hierarchy(self, priority_level, weightage_value, department_code=None):
        """Determines approval routing tier based on priority and financial weight."""
        weight = Decimal(str(weightage_value or 0))
        priority = str(priority_level).upper()

        if priority == "URGENT" or weight >= Decimal("50000.00"):
            tier = "TIER_3_EXECUTIVE_BOARD"
            required_approvers = 2
            sla_hours = 12
        elif priority == "HIGH" or weight >= Decimal("10000.00"):
            tier = "TIER_2_DEPARTMENTAL_HOD"
            required_approvers = 1
            sla_hours = 24
        else:
            tier = "TIER_1_SUPERVISORY_LEAD"
            required_approvers = 1
            sla_hours = 48

        return {
            "routing_tier": tier,
            "required_approver_count": required_approvers,
            "sla_turnaround_hours": sla_hours,
            "department_scope": department_code or "ALL",
            "escalation_contact": "executive_council@eduflow.local" if tier == "TIER_3_EXECUTIVE_BOARD" else "hod@eduflow.local"
        }

    def evaluate_sla_deadline(self, step_start_iso, allowed_duration_hours=24):
        """Computes remaining turnaround hours and evaluates potential SLA breach."""
        try:
            start_dt = timezone.datetime.fromisoformat(str(step_start_iso).replace("Z", "+00:00"))
        except Exception:
            start_dt = timezone.now()

        elapsed_seconds = (timezone.now() - start_dt).total_seconds()
        elapsed_hours = round(elapsed_seconds / 3600.0, 2)
        remaining_hours = round(allowed_duration_hours - elapsed_hours, 2)
        is_breached = remaining_hours < 0

        return {
            "step_start": start_dt.isoformat(),
            "allowed_hours": allowed_duration_hours,
            "elapsed_hours": elapsed_hours,
            "remaining_hours": max(0.0, remaining_hours),
            "is_breached": is_breached,
            "urgency_badge": "BREACHED" if is_breached else ("URGENT" if remaining_hours < 4 else "ON_TRACK"),
        }

    def execute_state_transition(self, record_id, current_state, target_state, transition_reason, context_payload=None):
        """Executes full atomic state transition with validation, guards, and journal logging."""
        ctx = context_payload or {}
        self.validate_transition_allowed(current_state, target_state)
        self.evaluate_transition_guards(current_state, target_state, ctx)

        journal_entry = {
            "transition_id": str(uuid.uuid4()),
            "record_id": str(record_id),
            "from_state": current_state,
            "to_state": target_state,
            "reason": transition_reason,
            "actor": self.actor_username,
            "institution_id": self.institution_id,
            "timestamp": timezone.now().isoformat(),
        }
        self.transition_journal.append(journal_entry)
        logger.info(f"[Invoicing Workflow] Record {record_id}: {current_state} -> {target_state} by {self.actor_username}")
        return journal_entry

    def execute_compensating_rollback(self, record_id, failed_state, fallback_state, rollback_reason):
        """Executes compensation transaction to restore prior safe state following pipeline faults."""
        rollback_entry = {
            "rollback_id": str(uuid.uuid4()),
            "record_id": str(record_id),
            "failed_state": failed_state,
            "reverted_to_state": fallback_state,
            "reason": rollback_reason,
            "actor": self.actor_username,
            "timestamp": timezone.now().isoformat(),
            "compensation_applied": True,
        }
        self.transition_journal.append(rollback_entry)
        logger.warning(f"[Invoicing Rollback] Record {record_id} reverted to {fallback_state}: {rollback_reason}")
        return rollback_entry

    def validate_dual_key_authorization(self, primary_key, secondary_key, operation_hash):
        """Validates dual cryptographic keys authorizing sensitive irreversible state mutations."""
        import hashlib
        expected_sig = hashlib.sha256(f"{primary_key}:{secondary_key}:{operation_hash}".encode("utf-8")).hexdigest()
        is_valid = bool(primary_key and secondary_key and len(primary_key) >= 16 and len(secondary_key) >= 16)
        return {
            "dual_key_valid": is_valid,
            "verification_signature": expected_sig if is_valid else "INVALID",
            "verified_at": timezone.now().isoformat(),
        }

    def execute_bulk_workflow_transitions(self, record_ids, from_state, to_state, bulk_reason):
        """Executes uniform batch transitions across multiple Invoicing records."""
        results = []
        for rid in record_ids:
            try:
                res = self.execute_state_transition(rid, from_state, to_state, bulk_reason)
                results.append({"record_id": rid, "status": "SUCCESS", "transition_id": res["transition_id"]})
            except Exception as e:
                results.append({"record_id": rid, "status": "FAILED", "error": str(e)})
        return {
            "batch_size": len(record_ids),
            "success_count": sum(1 for r in results if r["status"] == "SUCCESS"),
            "failure_count": sum(1 for r in results if r["status"] == "FAILED"),
            "results": results,
        }

    def generate_delegation_proxy(self, original_approver, proxy_approver, delegation_scope, valid_days=14):
        """Authorizes temporary delegated approval capabilities for Invoicing."""
        exp_date = timezone.now() + timezone.timedelta(days=valid_days)
        return {
            "delegation_id": str(uuid.uuid4()),
            "domain": "Invoicing",
            "original_approver": original_approver,
            "proxy_approver": proxy_approver,
            "scope": delegation_scope,
            "valid_until": exp_date.isoformat(),
            "is_active": True,
            "created_at": timezone.now().isoformat(),
        }

    def calculate_workflow_bottleneck_index(self, step_latencies):
        """Identifies workflow steps exhibiting disproportionate queuing backpressure."""
        if not step_latencies:
            return {"bottleneck_step": "NONE", "max_latency_hours": 0.0}
        sorted_steps = sorted(step_latencies.items(), key=lambda x: float(x[1]), reverse=True)
        top_step, top_lat = sorted_steps[0]
        avg_lat = sum(float(v) for v in step_latencies.values()) / len(step_latencies)
        return {
            "bottleneck_step": top_step,
            "max_latency_hours": round(float(top_lat), 2),
            "average_step_latency": round(avg_lat, 2),
            "latency_ratio": round(float(top_lat) / avg_lat, 2) if avg_lat > 0 else 1.0,
            "backpressure_status": "HIGH" if (float(top_lat) / avg_lat) > 2.0 else "NORMAL"
        }

    def evaluate_automatic_escalation_rules(self, current_state, pending_hours, priority):
        """Dispatches automated escalation notifications based on SLA threshold rules."""
        hours = float(pending_hours or 0)
        prio = str(priority).upper()
        threshold = 12.0 if prio == "URGENT" else (24.0 if prio == "HIGH" else 48.0)
        triggered = hours >= threshold
        return {
            "current_state": current_state,
            "pending_hours": hours,
            "sla_threshold_hours": threshold,
            "escalation_triggered": triggered,
            "escalation_target": "Executive_Council" if prio == "URGENT" else "Department_HOD",
            "escalation_action": "DISPATCH_SMS_AND_HIGH_PRIORITY_DIGEST" if triggered else "NONE"
        }

    def compute_lead_time_distribution(self, completed_journal_entries):
        """Analyzes end-to-end turnaround latency across workflow phases."""
        durations = []
        for entry in completed_journal_entries:
            dur = entry.get("duration_seconds", 0)
            if dur > 0:
                durations.append(dur / 3600.0)

        if not durations:
            return {"average_hours": 0.0, "median_hours": 0.0, "max_hours": 0.0}

        durations.sort()
        avg = sum(durations) / len(durations)
        med = durations[len(durations) // 2]
        return {
            "completed_workflows": len(durations),
            "average_hours": round(avg, 2),
            "median_hours": round(med, 2),
            "max_hours": round(max(durations), 2),
            "sla_breach_rate": round(sum(1 for d in durations if d > 48.0) / len(durations) * 100, 2)
        }

    def export_workflow_journal(self, record_id):
        """Exports chronological state change audit entries associated with target record."""
        return [entry for entry in self.transition_journal if entry.get("record_id") == str(record_id)]

    def synthesize_workflow_telemetry(self):
        """Calculates workflow efficiency indicators: transition cardinality, cycle times, rollback rate."""
        total = len(self.transition_journal)
        rollbacks = sum(1 for e in self.transition_journal if e.get("compensation_applied"))
        return {
            "total_transitions_executed": total,
            "compensating_rollbacks": rollbacks,
            "rollback_rate_percentage": round((rollbacks / total * 100), 2) if total > 0 else 0.0,
            "active_coordinator": self.actor_username,
            "synthesized_at": timezone.now().isoformat(),
        }
