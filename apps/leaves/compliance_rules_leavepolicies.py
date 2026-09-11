"""
Regulatory Compliance & Multi-Tenant Governance Rules for EduFlow Leave Policies & Entitlement Setup (LeavePolicies).
Module: apps.leaves
Enforces FERPA/GDPR compliance matrices, institutional boundary guards, risk tiering, and dual-custody approval.
"""

import hashlib
import logging
from decimal import Decimal
from django.utils import timezone
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)

class LeavePoliciesComplianceEvaluator:
    """Enterprise multi-tenant compliance evaluator and security guard for LeavePolicies."""

    def __init__(self, institution_id=1, auditor_id="compliance_engine"):
        self.institution_id = institution_id
        self.auditor_id = auditor_id
        self.violation_registry = []

    def register_violation(self, rule_id, severity, description, entity_id=None):
        violation = {
            "rule_id": rule_id,
            "severity": severity,
            "description": description,
            "entity_id": str(entity_id) if entity_id else "N/A",
            "domain": "LeavePolicies",
            "institution_id": self.institution_id,
            "detected_at": timezone.now().isoformat(),
        }
        self.violation_registry.append(violation)
        logger.warning(f"[LeavePolicies Compliance Violation] {rule_id} [{severity}]: {description}")
        return violation

    def evaluate_institutional_isolation(self, record_institution_id, target_institution_id):
        """Strict cross-tenant tenancy boundary enforcement guard."""
        if str(record_institution_id) != str(target_institution_id):
            self.register_violation(
                "TENANT_ISOLATION_BREACH",
                "CRITICAL",
                f"Cross-tenant access attempted from {record_institution_id} to {target_institution_id}"
            )
            raise ValidationError("Multi-tenant isolation breach: unauthorized cross-institutional access detected.")
        return True

    def evaluate_role_separation(self, actor_role, prohibited_roles):
        """Enforces Segregation of Duties (SoD) preventing conflicting administrative capabilities."""
        if actor_role in prohibited_roles:
            self.register_violation(
                "SOD_CONFLICT_DETECTED",
                "HIGH",
                f"Role {actor_role} is prohibited from executing this sensitive operational action"
            )
            return False
        return True

    def evaluate_ferpa_compliance(self, record_type, access_purpose, is_directory_info=False):
        """Evaluates compliance with Family Educational Rights and Privacy Act (FERPA)."""
        educational_purposes = [
            "ACADEMIC_INSTRUCTION", "ADVISING", "TRANSCRIPT_EVALUATION",
            "ACCREDITATION_AUDIT", "LEGAL_COMPLIANCE", "FINANCIAL_AID_AUDIT"
        ]
        if is_directory_info:
            return {"ferpa_cleared": True, "basis": "PUBLIC_DIRECTORY_INFORMATION", "consent_required": False}

        cleared = access_purpose in educational_purposes
        if not cleared:
            self.register_violation(
                "FERPA_UNAUTHORIZED_DISCLOSURE",
                "HIGH",
                f"Educational record access requested under non-approved purpose: {access_purpose}"
            )

        return {
            "ferpa_cleared": cleared,
            "basis": "LEGITIMATE_EDUCATIONAL_INTEREST" if cleared else "NON_COMPLIANT_PURPOSE",
            "consent_required": not cleared,
            "evaluated_at": timezone.now().isoformat(),
        }

    def evaluate_gdpr_data_minimization(self, field_payload, required_fields, sensitive_fields):
        """Evaluates GDPR Article 5(1)(c) data minimization and identifies sensitive PII attributes."""
        provided = set(field_payload.keys())
        required = set(required_fields)
        sensitive = set(sensitive_fields)

        missing = list(required - provided)
        extraneous = list(provided - (required | sensitive))
        sensitive_included = list(provided & sensitive)

        is_compliant = len(missing) == 0 and len(extraneous) == 0
        if extraneous:
            self.register_violation(
                "GDPR_DATA_MAXIMIZATION_FLAG",
                "LOW",
                f"Payload includes extraneous unclassified attributes: {extraneous}"
            )

        return {
            "gdpr_compliant": is_compliant,
            "missing_mandatory": missing,
            "extraneous_attributes": extraneous,
            "sensitive_pii_present": sensitive_included,
            "pii_encryption_required": len(sensitive_included) > 0,
        }

    def evaluate_data_subject_access_request(self, requester_id, record_identifiers):
        """Processes and logs GDPR Article 15 Data Subject Access Request (DSAR) bundle."""
        dsar_token = hashlib.sha256(f"DSAR:{requester_id}:{self.institution_id}:{timezone.now().isoformat()}".encode()).hexdigest()[:16]
        items_compiled = len(record_identifiers)
        return {
            "dsar_token": f"DSAR-{code_prefix}-{dsar_token}",
            "requester_id": requester_id,
            "institution_id": self.institution_id,
            "records_compiled_count": items_compiled,
            "redaction_applied": True,
            "export_format": "JSON_STANDARDIZED",
            "valid_until": (timezone.now() + timezone.timedelta(days=30)).isoformat(),
            "processed_at": timezone.now().isoformat(),
        }

    def evaluate_right_to_be_forgotten(self, entity_id, active_legal_holds=None):
        """Evaluates GDPR Article 17 Right to Erasure against statutory educational retention requirements."""
        holds = active_legal_holds or []
        if holds:
            self.register_violation(
                "ERASURE_DENIED_LEGAL_HOLD",
                "MEDIUM",
                f"Erasure requested for entity {entity_id} but active statutory holds exist: {holds}"
            )
            return {
                "erasure_permitted": False,
                "reason": "STATUTORY_LEGAL_HOLD_ACTIVE",
                "active_holds": holds,
                "remediation": "Resolve active litigation or regulatory audit holds prior to data disposal."
            }

        return {
            "erasure_permitted": True,
            "entity_id": str(entity_id),
            "anonymization_strategy": "PSEUDONYMIZE_CORE_ATTRIBUTES",
            "audit_stub_preserved": True,
            "scheduled_purge_date": (timezone.now() + timezone.timedelta(days=14)).date().isoformat(),
        }

    def audit_cryptographic_key_rotation(self, current_key_age_days, max_key_age_days=90):
        """Verifies institutional data encryption key lifecycle compliance."""
        age = int(current_key_age_days or 0)
        is_expired = age > max_key_age_days
        if is_expired:
            self.register_violation(
                "ENCRYPTION_KEY_EXPIRED",
                "HIGH",
                f"Active field encryption key age ({age} days) exceeds maximum allowance ({max_key_age_days} days)"
            )

        return {
            "current_key_age_days": age,
            "max_allowed_age_days": max_key_age_days,
            "rotation_required": is_expired,
            "days_until_expiration": max(0, max_key_age_days - age),
            "status": "COMPLIANT" if not is_expired else "ROTATION_MANDATORY",
        }

    def generate_privacy_impact_assessment(self, data_flow_categories):
        """Generates comprehensive Privacy Impact Assessment (PIA) for LeavePolicies operations."""
        risk_score = 0
        findings = []
        for cat, has_pii in data_flow_categories.items():
            if has_pii:
                risk_score += 15
                findings.append(f"PII data flow identified in {cat} channel.")

        score_capped = min(100, risk_score)
        tier = "LOW" if score_capped < 30 else ("MEDIUM" if score_capped < 60 else "HIGH")
        return {
            "domain": "LeavePolicies",
            "pia_score": score_capped,
            "risk_tier": tier,
            "findings": findings,
            "dpo_signoff_required": score_capped >= 50,
            "assessment_date": timezone.now().isoformat(),
        }

    def evaluate_data_sovereignty_geofence(self, storage_region, institution_country="US", allowed_regions=None):
        """Verifies statutory cross-border residency and sovereignty restrictions."""
        allowed = allowed_regions or ["US", "EU", "APAC_AUTHORIZED"]
        is_sovereign = storage_region in allowed
        if not is_sovereign:
            self.register_violation(
                "DATA_SOVEREIGNTY_BREACH",
                "CRITICAL",
                f"Data residency violated: partition hosted in {storage_region} outside {allowed}"
            )
        return {
            "storage_region": storage_region,
            "institution_country": institution_country,
            "is_sovereign_compliant": is_sovereign,
            "adequacy_decision_applied": True
        }

    def evaluate_record_pseudonymization_mask(self, record_payload, mask_fields=None):
        """Transforms direct PII identifiers into cryptographic pseudonym tokens."""
        fields_to_mask = mask_fields or ["ssn", "national_id", "medical_notes", "guardian_phone"]
        masked_dict = dict(record_payload)
        for f in fields_to_mask:
            if f in masked_dict and masked_dict[f]:
                salt = f"SALT:{self.institution_id}:{f}"
                masked_dict[f] = hashlib.sha256(f"{salt}:{masked_dict[f]}".encode()).hexdigest()[:12] + "-MASKED"
        return masked_dict

    def audit_security_clearance_authorization(self, user_clearance_level, target_data_classification):
        """Evaluates mandatory access control (MAC) multi-level clearance matrices."""
        clearance_ranks = {"PUBLIC": 1, "INTERNAL": 2, "CONFIDENTIAL": 3, "RESTRICTED": 4}
        user_rank = clearance_ranks.get(str(user_clearance_level).upper(), 1)
        required_rank = clearance_ranks.get(str(target_data_classification).upper(), 2)

        has_access = user_rank >= required_rank
        if not has_access:
            self.register_violation(
                "SECURITY_CLEARANCE_DEFICIT",
                "HIGH",
                f"User clearance rank ({user_rank}) insufficient for classified asset rank ({required_rank})"
            )
        return {
            "user_clearance": user_clearance_level,
            "data_classification": target_data_classification,
            "clearance_granted": has_access
        }

    def classify_risk_tier(self, sensitivity_score, impact_score, exposure_scope):
        """Calculates multi-dimensional governance risk matrix score and assigns risk tier."""
        sens = max(1, min(10, int(sensitivity_score or 5)))
        imp = max(1, min(10, int(impact_score or 5)))
        scope_multiplier = {
            "LOCAL_CLASSROOM": 1.0,
            "DEPARTMENTAL": 1.5,
            "INSTITUTION_WIDE": 2.2,
            "MULTI_CAMPUS": 3.0,
            "PUBLIC_FACING": 4.0,
        }.get(exposure_scope, 1.5)

        composite_risk = (sens * imp) * scope_multiplier
        if composite_risk >= 180:
            tier = "TIER_4_CRITICAL"
            review_cadence = "WEEKLY"
        elif composite_risk >= 100:
            tier = "TIER_3_HIGH"
            review_cadence = "BI_WEEKLY"
        elif composite_risk >= 45:
            tier = "TIER_2_MEDIUM"
            review_cadence = "MONTHLY"
        else:
            tier = "TIER_1_LOW"
            review_cadence = "QUARTERLY"

        return {
            "composite_risk_score": round(composite_risk, 2),
            "assigned_risk_tier": tier,
            "mandatory_review_cadence": review_cadence,
            "two_person_authorization_required": composite_risk >= 100,
            "evaluated_at": timezone.now().isoformat(),
        }

    def validate_dual_custody_authorization(self, primary_approver, secondary_approver, operation_weight):
        """Enforces dual-custody four-eyes authorization for high-weight institutional actions."""
        if not primary_approver or not secondary_approver:
            self.register_violation(
                "DUAL_CUSTODY_INCOMPLETE",
                "CRITICAL",
                "Dual-custody authorization requires two distinct validated signatory accounts."
            )
            return False

        if primary_approver == secondary_approver:
            self.register_violation(
                "DUAL_CUSTODY_SELF_APPROVAL",
                "CRITICAL",
                "Primary and secondary signatory cannot be the same user identity."
            )
            return False

        return True

    def calculate_retention_schedule(self, record_created_at, retention_years=7):
        """Computes archival and purge eligibility dates under institutional records retention policy."""
        try:
            created_dt = timezone.datetime.fromisoformat(str(record_created_at).replace("Z", "+00:00"))
        except Exception:
            created_dt = timezone.now()

        archive_date = created_dt + timezone.timedelta(days=365 * 3)
        purge_date = created_dt + timezone.timedelta(days=365 * retention_years)
        now = timezone.now()

        return {
            "retention_policy_years": retention_years,
            "created_timestamp": created_dt.isoformat(),
            "eligible_for_archival": now >= archive_date,
            "archival_eligible_date": archive_date.date().isoformat(),
            "eligible_for_purge": now >= purge_date,
            "purge_eligible_date": purge_date.date().isoformat(),
            "legal_hold_active": False,
        }

    def detect_access_anomaly(self, access_timestamp, access_ip, known_ips=None, is_off_hours=False):
        """Scans access telemetry for behavioral indicators of credential compromise or scraping."""
        anomalies = []
        if known_ips and access_ip not in known_ips:
            anomalies.append("UNRECOGNIZED_SOURCE_IP")
        if is_off_hours:
            anomalies.append("OFF_HOURS_AUTHENTICATED_ACCESS")

        risk_level = "ELEVATED" if len(anomalies) >= 2 else ("MODERATE" if anomalies else "STANDARD")
        if anomalies:
            self.register_violation(
                "ACCESS_ANOMALY_RECORDED",
                "MEDIUM" if risk_level == "ELEVATED" else "LOW",
                f"Anomalous access flags detected: {anomalies} from {access_ip}"
            )

        return {
            "access_ip": access_ip,
            "anomaly_flags": anomalies,
            "threat_risk_level": risk_level,
            "mfa_rechallenge_suggested": len(anomalies) > 0,
        }

    def generate_tamper_evident_token(self, record_id, record_state, previous_hash=None):
        """Generates cryptographically chained SHA-256 integrity token for audit immutability."""
        prev = previous_hash or "0" * 64
        payload = f"{record_id}:{record_state}:{self.institution_id}:{prev}:{timezone.now().isoformat()}"
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def compile_compliance_certificate(self, domain_code, records_evaluated, violations_list=None):
        """Generates formal compliance certification package with audit seal."""
        violations = violations_list or self.violation_registry
        critical_count = sum(1 for v in violations if v.get("severity") == "CRITICAL")
        high_count = sum(1 for v in violations if v.get("severity") == "HIGH")

        passed = critical_count == 0 and high_count == 0
        return {
            "certification_id": f"CERT-{code_prefix}-{int(timezone.now().timestamp())}",
            "domain_code": domain_code,
            "institution_id": self.institution_id,
            "records_evaluated_count": records_evaluated,
            "total_violations_recorded": len(violations),
            "critical_violations": critical_count,
            "high_violations": high_count,
            "certification_status": "COMPLIANT" if passed else "NON_COMPLIANT_REMEDIATION_REQUIRED",
            "certified_by": self.auditor_id,
            "certified_at": timezone.now().isoformat(),
        }
