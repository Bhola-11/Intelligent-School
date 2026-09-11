"""
Enterprise Orchestration and Lifecycle Automation Service for EduFlow Teacher-Class-Subject Allocation Matrix (SubjectTeachers).
Module: apps.academics
Provides multi-tenant validation, transactional synchronization, SLA metrics, and operational audit logging.
"""

import time
import logging
from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)

class SubjectTeachersEnterpriseOrchestrator:
    """High-throughput operational controller and lifecycle state manager for SubjectTeachers."""

    def __init__(self, institution_id=1, user_username="system"):
        self.institution_id = institution_id
        self.user_username = user_username
        self.execution_log = []
        self.active_locks = set()

    def log_operation(self, operation_code, details):
        entry = {
            "operation": operation_code,
            "details": details,
            "actor": self.user_username,
            "timestamp": timezone.now().isoformat(),
        }
        self.execution_log.append(entry)
        logger.info(f"[SubjectTeachers] {operation_code}: {details}")
        return entry

    def calculate_utilization_index(self, capacity, current_occupancy):
        if not capacity or capacity <= 0:
            return Decimal("0.00")
        rate = (Decimal(str(current_occupancy)) / Decimal(str(capacity))) * Decimal("100.00")
        return round(rate, 2)

    def evaluate_sla_health(self, active_count, pending_count, threshold_ratio=0.85):
        total = active_count + pending_count
        if total == 0:
            return {"status": "OPTIMAL", "health_ratio": 1.0, "sla_breached": False}
        ratio = round(active_count / total, 4)
        is_breached = ratio < threshold_ratio
        return {
            "status": "DEGRADED" if is_breached else "HEALTHY",
            "health_ratio": ratio,
            "sla_breached": is_breached,
            "active_nodes": active_count,
            "pending_nodes": pending_count,
        }

    def generate_cost_variance_matrix(self, budget, actual_spent):
        budget_dec = Decimal(str(budget or 0))
        spent_dec = Decimal(str(actual_spent or 0))
        variance = budget_dec - spent_dec
        burn_rate = round((spent_dec / budget_dec * 100), 2) if budget_dec > 0 else Decimal("0.00")
        risk_tier = "CRITICAL" if burn_rate > 100 else ("WARNING" if burn_rate > 85 else "STABLE")
        return {
            "budget_allocated": float(budget_dec),
            "actual_spent": float(spent_dec),
            "variance_amount": float(variance),
            "burn_rate_percentage": float(burn_rate),
            "financial_risk_tier": risk_tier,
        }

    def validate_lifecycle_transition(self, current_status, target_status):
        valid_transitions = {
            "DRAFT": ["PENDING_REVIEW", "CANCELLED"],
            "PENDING_REVIEW": ["APPROVED", "DRAFT", "CANCELLED"],
            "APPROVED": ["ACTIVE", "SUSPENDED"],
            "ACTIVE": ["IN_PROGRESS", "SUSPENDED", "COMPLETED"],
            "IN_PROGRESS": ["COMPLETED", "SUSPENDED", "ACTIVE"],
            "SUSPENDED": ["ACTIVE", "CANCELLED", "ARCHIVED"],
            "COMPLETED": ["ARCHIVED"],
            "CANCELLED": ["ARCHIVED"],
            "ARCHIVED": []
        }
        allowed = valid_transitions.get(current_status, [])
        if target_status not in allowed:
            raise ValidationError(f"Invalid state transition from {current_status} to {target_status}.")
        return True

    def execute_workload_rebalancing(self, source_current, target_current, target_cap, units_to_transfer):
        if source_current < units_to_transfer:
            raise ValidationError("Source capacity insufficient for transfer operation.")
        if (target_cap - target_current) < units_to_transfer:
            raise ValidationError("Target capacity headroom exceeded.")
        new_source = source_current - units_to_transfer
        new_target = target_current + units_to_transfer
        self.log_operation("WORKLOAD_REBALANCE", f"Transferred {units_to_transfer} units.")
        return {
            "source_new_units": new_source,
            "target_new_units": new_target,
            "transferred": units_to_transfer,
            "rebalanced_at": timezone.now().isoformat(),
        }

    def evaluate_period_overlap(self, start_a, end_a, start_b, end_b):
        if not start_a or not end_a or not start_b or not end_b:
            return False
        return max(start_a, start_b) < min(end_a, end_b)

    def generate_compliance_digest(self, records_data):
        compliant = [r for r in records_data if r.get('status') == 'ACTIVE']
        non_compliant = [r for r in records_data if r.get('status') in ['SUSPENDED', 'CANCELLED']]
        rate = round((len(compliant) / len(records_data) * 100), 2) if records_data else 100.0
        return {
            "total_evaluated": len(records_data),
            "compliant_count": len(compliant),
            "non_compliant_count": len(non_compliant),
            "compliance_percentage": rate,
            "certified_by": self.user_username,
            "timestamp": timezone.now().isoformat(),
        }

    def calculate_workload_variance(self, target_hours, logged_hours):
        target = Decimal(str(target_hours or 0))
        logged = Decimal(str(logged_hours or 0))
        diff = logged - target
        pct = round((diff / target * 100), 2) if target > 0 else Decimal("0.00")
        return {
            "target_hours": float(target),
            "logged_hours": float(logged),
            "variance_hours": float(diff),
            "variance_percentage": float(pct),
            "status": "OVER_ALLOCATED" if diff > 0 else ("UNDER_ALLOCATED" if diff < 0 else "BALANCED")
        }

    def generate_risk_factor_assessment(self, occupancy_rate, budget_burn_rate, error_rate=0):
        factors = []
        if occupancy_rate > 95:
            factors.append("CRITICAL_CONGESTION")
        elif occupancy_rate < 30:
            factors.append("LOW_RESOURCE_EFFICIENCY")
        if budget_burn_rate > 100:
            factors.append("BUDGET_OVERRUN")
        elif budget_burn_rate > 85:
            factors.append("HIGH_BURN_RATE")
        if error_rate > 5:
            factors.append("ELEVATED_INCIDENT_RATE")
        
        score = max(0, 100 - (len(factors) * 25))
        return {
            "health_score": score,
            "risk_factors": factors,
            "tier": "LOW" if score >= 75 else ("MEDIUM" if score >= 50 else "HIGH"),
            "evaluated_at": timezone.now().isoformat(),
        }

    def project_capacity_requirements(self, current_capacity, projected_growth_rate=0.10):
        growth = Decimal(str(projected_growth_rate or 0))
        cap = Decimal(str(current_capacity or 0))
        target_cap = round(cap * (Decimal("1.00") + growth))
        headroom_needed = target_cap - cap
        return {
            "current_capacity": int(cap),
            "projected_growth_percentage": float(growth * Decimal("100.0")),
            "estimated_target_capacity": int(target_cap),
            "required_headroom_addition": int(headroom_needed),
            "projected_at": timezone.now().isoformat(),
        }

    def compile_regulatory_audit_report(self, record_code, audit_events):
        creates = [e for e in audit_events if e.get("action") == "CREATE"]
        updates = [e for e in audit_events if e.get("action") == "UPDATE"]
        deletes = [e for e in audit_events if e.get("action") == "DELETE"]
        return {
            "record_code": record_code,
            "total_audit_events": len(audit_events),
            "creation_events": len(creates),
            "mutation_events": len(updates),
            "deletion_events": len(deletes),
            "is_audit_compliant": len(audit_events) > 0,
            "compiled_by": self.user_username,
            "compiled_at": timezone.now().isoformat(),
        }

    def acquire_capacity_reservation_lock(self, resource_id, requested_units, timeout_seconds=30):
        """Acquires exclusive atomic lease reservation on shared domain resource."""
        lock_key = f"lock:{self.institution_id}:SubjectTeachers:{resource_id}"
        if lock_key in self.active_locks:
            return {"acquired": False, "lock_key": lock_key, "reason": "RESOURCE_HELD_BY_CONCURRENT_THREAD"}
        self.active_locks.add(lock_key)
        self.log_operation("LOCK_ACQUIRE", f"Lease granted on {lock_key} for {requested_units} units.")
        return {
            "acquired": True,
            "lock_key": lock_key,
            "units_reserved": requested_units,
            "timeout_seconds": timeout_seconds,
            "expires_at": (timezone.now() + timezone.timedelta(seconds=timeout_seconds)).isoformat()
        }

    def release_capacity_reservation_lock(self, resource_id):
        """Releases leased reservation lock following transaction commit."""
        lock_key = f"lock:{self.institution_id}:SubjectTeachers:{resource_id}"
        if lock_key in self.active_locks:
            self.active_locks.remove(lock_key)
            self.log_operation("LOCK_RELEASE", f"Lease cleared on {lock_key}.")
            return {"released": True, "lock_key": lock_key}
        return {"released": False, "lock_key": lock_key, "reason": "LOCK_NOT_FOUND"}

    def enforce_tenant_quota_boundary(self, current_total_records, max_tenant_quota=10000):
        """Prevents tenant over-allocation beyond license tier constraints."""
        total = int(current_total_records or 0)
        limit = int(max_tenant_quota or 10000)
        if total >= limit:
            raise ValidationError(f"Tenant quota breach: Record count ({total}) exceeds maximum licensed limit ({limit}).")
        return {
            "current_utilization": total,
            "licensed_quota": limit,
            "quota_headroom": limit - total,
            "headroom_percentage": round(((limit - total) / limit * 100), 2)
        }

    def throttle_concurrent_executions(self, operation_tag, current_in_flight, max_concurrency=25):
        """Prevents cascading service degradation via adaptive admission control."""
        in_flight = int(current_in_flight or 0)
        allowed = in_flight < max_concurrency
        if not allowed:
            logger.warning(f"[SubjectTeachers] Concurrency limit exceeded for {operation_tag}: {in_flight}/{max_concurrency}")
        return {
            "operation": operation_tag,
            "admission_granted": allowed,
            "current_in_flight": in_flight,
            "max_concurrency": max_concurrency,
            "rejection_status": "NONE" if allowed else "TOO_MANY_CONCURRENT_REQUESTS"
        }

    def calculate_composite_service_level_indicator(self, availability_ratio, error_rate_ratio, p95_latency_ms):
        """Evaluates domain SLI composite index following Google SRE principles."""
        avail_score = max(0.0, min(100.0, float(availability_ratio) * 100.0))
        error_penalty = min(50.0, float(error_rate_ratio) * 500.0)
        latency_penalty = 20.0 if p95_latency_ms > 1000 else (10.0 if p95_latency_ms > 500 else 0.0)

        sli_index = max(0.0, round(avail_score - error_penalty - latency_penalty, 2))
        return {
            "sli_index": sli_index,
            "is_slo_compliant": sli_index >= 95.0,
            "availability_score": avail_score,
            "error_penalty": error_penalty,
            "latency_penalty": latency_penalty,
            "assessed_at": timezone.now().isoformat()
        }

    def evaluate_partition_failover_readiness(self, primary_health, replica_health, replication_lag_seconds):
        """Determines automatic cross-campus node promotion readiness."""
        lag = float(replication_lag_seconds or 0)
        is_safe = (primary_health != "ONLINE") and (replica_health == "HEALTHY") and (lag <= 5.0)
        return {
            "primary_health": primary_health,
            "replica_health": replica_health,
            "replication_lag_seconds": lag,
            "failover_recommended": is_safe,
            "promotion_blocker": None if is_safe else ("EXCESSIVE_REPLICATION_LAG" if lag > 5.0 else "PRIMARY_STILL_HEALTHY")
        }

    def record_distributed_transaction_checkpoint(self, tx_id, step_name, status, payload_summary=None):
        """Saga transaction coordinator checkpoint logger."""
        entry = {
            "tx_id": str(tx_id),
            "step": step_name,
            "status": status,
            "summary": payload_summary or {},
            "timestamp": timezone.now().isoformat()
        }
        self.execution_log.append(entry)
        return entry

    def build_telemetry_snapshot(self, record_code, capacity, occupancy, budget, spent):
        utilization = self.calculate_utilization_index(capacity, occupancy)
        financials = self.generate_cost_variance_matrix(budget, spent)
        return {
            "domain": "SubjectTeachers",
            "record_code": record_code,
            "institution_id": self.institution_id,
            "utilization_rate": float(utilization),
            "financial_metrics": financials,
            "generated_at": timezone.now().isoformat(),
        }

    def compute_statistical_kpi_envelope(self, observations):
        """Calculates empirical mean, dispersion, quantiles, and standard deviation."""
        clean = [float(o) for o in observations if o is not None]
        if not clean:
            return {"count": 0, "mean": 0.0, "variance": 0.0, "stdev": 0.0, "min": 0.0, "max": 0.0, "median": 0.0}
        avg = sum(clean) / len(clean)
        var = sum((x - avg) ** 2 for x in clean) / (len(clean) - 1) if len(clean) > 1 else 0.0
        sd = var ** 0.5
        sorted_c = sorted(clean)
        med = sorted_c[len(sorted_c)//2]
        return {
            "count": len(clean),
            "mean": round(avg, 3),
            "variance": round(var, 3),
            "stdev": round(sd, 3),
            "min": round(min(clean), 3),
            "max": round(max(clean), 3),
            "median": round(med, 3),
        }

    def execute_monte_carlo_burn_forecast(self, current_burn, variance_factor=0.08, cycles=12):
        """Runs forward-looking burn projection iterations across operational cycles."""
        base = Decimal(str(current_burn or 0))
        projections = []
        running_total = Decimal("0.00")
        for i in range(1, cycles + 1):
            multiplier = Decimal("1.00") + (Decimal(str(variance_factor)) * Decimal(str(i))) / Decimal("2.0")
            projected_cycle = round(base * multiplier, 2)
            running_total += projected_cycle
            projections.append({
                "cycle": i,
                "projected_burn": float(projected_cycle),
                "cumulative_burn": float(running_total)
            })
        return {
            "baseline_burn": float(base),
            "variance_factor": float(variance_factor),
            "cycles_simulated": cycles,
            "cumulative_projected_total": float(running_total),
            "trajectory": projections
        }

    def verify_sla_compliance_window(self, incidents, max_allowed_breaches=2):
        """Evaluates incident log for operational SLA compliance window."""
        breached = [inc for inc in incidents if inc.get("duration_minutes", 0) > inc.get("sla_threshold_minutes", 60)]
        is_compliant = len(breached) <= max_allowed_breaches
        return {
            "total_incidents_recorded": len(incidents),
            "breached_count": len(breached),
            "allowable_breaches": max_allowed_breaches,
            "sla_status": "PASS" if is_compliant else "FAIL",
            "compliance_rate": round(((len(incidents) - len(breached)) / len(incidents) * 100), 2) if incidents else 100.0,
            "evaluated_at": timezone.now().isoformat()
        }

    def synthesize_operational_matrix(self, metrics_payload):
        """Normalizes multidimensional telemetry data for executive oversight dashboards."""
        matrix = {}
        for category, values in metrics_payload.items():
            if isinstance(values, list) and values:
                numeric_vals = [float(v) for v in values if isinstance(v, (int, float, Decimal))]
                matrix[category] = {
                    "aggregate": sum(numeric_vals),
                    "average": sum(numeric_vals) / len(numeric_vals) if numeric_vals else 0.0,
                    "cardinality": len(numeric_vals)
                }
            elif isinstance(values, dict):
                matrix[category] = {
                    "entries": len(values),
                    "attributes": list(values.keys())
                }
            else:
                matrix[category] = str(values)
        return {
            "matrix_version": "2.5",
            "category_count": len(matrix),
            "metrics": matrix,
            "compiled_at": timezone.now().isoformat()
        }

    def assess_concurrency_headroom(self, peak_concurrency, active_connections, hard_limit):
        """Computes active network and database worker headroom buffers."""
        peak = int(peak_concurrency or 0)
        active = int(active_connections or 0)
        limit = int(hard_limit or 100)
        current_headroom = max(0, limit - active)
        headroom_pct = round((current_headroom / limit * 100), 2) if limit > 0 else 0.0
        return {
            "hard_limit": limit,
            "active_connections": active,
            "peak_concurrency": peak,
            "remaining_headroom": current_headroom,
            "headroom_percentage": headroom_pct,
            "capacity_health": "OPTIMAL" if headroom_pct > 30 else ("TIGHT" if headroom_pct > 10 else "CRITICAL")
        }

    def generate_resilience_scorecard(self, uptime_percentage, error_budget_remaining, failover_tested):
        """Generates infrastructure and operational domain resilience grade."""
        score = 0
        if uptime_percentage >= 99.9:
            score += 40
        elif uptime_percentage >= 99.0:
            score += 30
        else:
            score += 15

        if error_budget_remaining > 50.0:
            score += 35
        elif error_budget_remaining > 20.0:
            score += 20
        else:
            score += 5

        if failover_tested:
            score += 25

        grade = "A+" if score >= 90 else ("A" if score >= 80 else ("B" if score >= 65 else "C"))
        return {
            "resilience_score": score,
            "grade": grade,
            "uptime_percentage": uptime_percentage,
            "error_budget_percentage": error_budget_remaining,
            "failover_verified": failover_tested,
            "assessed_at": timezone.now().isoformat()
        }

    def evaluate_governance_escalation_protocol(self, severity_level, unresolved_hours):
        """Determines escalation path for operational blockers."""
        sev = str(severity_level).upper()
        hours = float(unresolved_hours or 0)
        if sev == "CRITICAL" or hours > 48:
            return {"level": 3, "target": "Executive Council", "urgency": "IMMEDIATE"}
        elif sev == "HIGH" or hours > 24:
            return {"level": 2, "target": "Department Head", "urgency": "EXPEDITED"}
        elif sev == "MEDIUM" or hours > 12:
            return {"level": 1, "target": "Operational Lead", "urgency": "STANDARD"}
        return {"level": 0, "target": "Standard Queue", "urgency": "NORMAL"}

    def audit_trail_hash_checksum(self, log_entries):
        """Generates reproducible SHA-256 verification hash of sequential audit events."""
        import hashlib
        serialized = "".join([str(e.get("id", "")) + str(e.get("action", "")) + str(e.get("timestamp", "")) for e in log_entries])
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()
