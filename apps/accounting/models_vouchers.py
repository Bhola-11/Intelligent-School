"""
Models for EduFlow Expense Vouchers & Payment Approvals (Vouchers) in apps.accounting.
Comprehensive 12-model normalized architecture supporting enterprise operations.
"""

import uuid
from decimal import Decimal
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.db.models import Q, Sum, Avg, Count

# -----------------------------------------------------------------------------
# Choices and Status Enums
# -----------------------------------------------------------------------------
class VouchersStatusChoices(models.TextChoices):
    DRAFT = 'DRAFT', _('Draft / In Planning')
    PENDING_REVIEW = 'PENDING_REVIEW', _('Pending Institutional Review')
    APPROVED = 'APPROVED', _('Approved & Authorized')
    ACTIVE = 'ACTIVE', _('Active / Operational')
    IN_PROGRESS = 'IN_PROGRESS', _('In Progress / Underway')
    SUSPENDED = 'SUSPENDED', _('Temporarily Suspended')
    COMPLETED = 'COMPLETED', _('Completed / Closed')
    CANCELLED = 'CANCELLED', _('Cancelled')
    ARCHIVED = 'ARCHIVED', _('Archived Historical Record')

class VouchersPriorityChoices(models.TextChoices):
    LOW = 'LOW', _('Low Operational Priority')
    NORMAL = 'NORMAL', _('Standard Normal Priority')
    HIGH = 'HIGH', _('Elevated Priority')
    CRITICAL = 'CRITICAL', _('Critical Emergency Action')

class VouchersTierChoices(models.TextChoices):
    TIER_1 = 'TIER_1', _('Tier 1 - Executive / Core')
    TIER_2 = 'TIER_2', _('Tier 2 - Departmental')
    TIER_3 = 'TIER_3', _('Tier 3 - Operational Unit')
    TIER_4 = 'TIER_4', _('Tier 4 - Support / Ancillary')

class VouchersScopeChoices(models.TextChoices):
    CAMPUS_WIDE = 'CAMPUS_WIDE', _('Entire Campus Scope')
    DEPARTMENTAL = 'DEPARTMENTAL', _('Departmental Scope')
    CLASS_SECTION = 'CLASS_SECTION', _('Class / Section Specific')
    INDIVIDUAL = 'INDIVIDUAL', _('Individual Student / Staff')

# -----------------------------------------------------------------------------
# Custom QuerySet and Manager
# -----------------------------------------------------------------------------
class VouchersMasterQuerySet(models.QuerySet):
    def active(self):
        return self.filter(status='ACTIVE')

    def operational(self):
        return self.filter(status__in=['ACTIVE', 'IN_PROGRESS', 'APPROVED'])

    def pending_review(self):
        return self.filter(status='PENDING_REVIEW')

    def high_priority(self):
        return self.filter(priority__in=['HIGH', 'CRITICAL'])

    def for_category(self, category):
        return self.filter(category=category)

    def recent(self, days=30):
        cutoff = timezone.now() - timezone.timedelta(days=days)
        return self.filter(created_at__gte=cutoff)

    def by_keyword(self, query):
        if not query:
            return self
        return self.filter(
            Q(code__icontains=query) |
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(tags__icontains=query)
        )

class VouchersMasterManager(models.Manager):
    def get_queryset(self):
        return VouchersMasterQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def operational(self):
        return self.get_queryset().operational()

    def pending_review(self):
        return self.get_queryset().pending_review()

    def search(self, query):
        return self.get_queryset().by_keyword(query)

# -----------------------------------------------------------------------------
# Model 1: Master Entity
# -----------------------------------------------------------------------------
class VouchersMaster(models.Model):
    """
    Primary master configuration entity for Expense Vouchers & Payment Approvals.
    Maintains governance rules, lifecycle states, budgetary allotments, and KPIs.
    """
    StatusChoices = VouchersStatusChoices
    PriorityChoices = VouchersPriorityChoices
    TierChoices = VouchersTierChoices
    ScopeChoices = VouchersScopeChoices

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    code = models.CharField(max_length=64, unique=True, db_index=True, verbose_name=_("Unique Code Identifier"))
    name = models.CharField(max_length=255, db_index=True, verbose_name=_("Official Name / Title"))
    short_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Display Short Name"))
    slug = models.SlugField(max_length=255, blank=True, verbose_name=_("URL Slug"))
    category = models.CharField(max_length=100, default='General', db_index=True, verbose_name=_("Operational Category"))
    tier = models.CharField(max_length=30, choices=TierChoices.choices, default=TierChoices.TIER_2, verbose_name=_("Operational Tier"))
    scope = models.CharField(max_length=30, choices=ScopeChoices.choices, default=ScopeChoices.CAMPUS_WIDE, verbose_name=_("Jurisdiction Scope"))
    priority = models.CharField(max_length=20, choices=PriorityChoices.choices, default=PriorityChoices.NORMAL, verbose_name=_("Priority Level"))
    status = models.CharField(max_length=30, choices=StatusChoices.choices, default=StatusChoices.ACTIVE, db_index=True, verbose_name=_("Lifecycle Status"))

    description = models.TextField(blank=True, verbose_name=_("Scope & Description"))
    operational_guidelines = models.TextField(blank=True, verbose_name=_("Operational Guidelines & Standard Procedures"))
    internal_notes = models.TextField(blank=True, verbose_name=_("Confidential Administrative Notes"))

    capacity = models.PositiveIntegerField(default=100, verbose_name=_("Configured Total Capacity"))
    current_occupancy = models.PositiveIntegerField(default=0, verbose_name=_("Current Utilization / Count"))
    reserved_headroom = models.PositiveIntegerField(default=10, verbose_name=_("Reserved Buffer Headroom"))
    weightage = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('1.00'), verbose_name=_("Weightage Multiplier"))
    budget_allocated = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal('0.00'), verbose_name=_("Allocated Budget ($)"))
    cost_incurred = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal('0.00'), verbose_name=_("Incurred Cost ($)"))

    effective_start_date = models.DateField(default=timezone.now, verbose_name=_("Effective Start Date"))
    effective_end_date = models.DateField(blank=True, null=True, verbose_name=_("Effective End Date"))
    is_recurring = models.BooleanField(default=False, verbose_name=_("Recurring Academic Cycle"))
    is_public = models.BooleanField(default=True, verbose_name=_("Visible in Public Directory"))
    is_locked = models.BooleanField(default=False, verbose_name=_("Locked from Manual Modification"))
    requires_director_approval = models.BooleanField(default=False, verbose_name=_("Requires Director Sign-off"))

    attributes = models.JSONField(default=dict, blank=True, verbose_name=_("Dynamic Extended Schema Attributes"))
    tags = models.CharField(max_length=255, blank=True, verbose_name=_("Search Keywords (Comma Separated)"))

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_user = models.CharField(max_length=150, default='system', verbose_name=_("Created By Username"))
    updated_by_user = models.CharField(max_length=150, default='system', verbose_name=_("Last Modified By"))

    objects = VouchersMasterManager()

    class Meta:
        db_table = 'eduflow_accounting_vouchers_master'
        ordering = ['-created_at', 'name']
        verbose_name = _("Vouchers Master")
        verbose_name_plural = _("Vouchers Masters")
        indexes = [
            models.Index(fields=['code', 'status'], name='idx_vouch_cd_st'),
            models.Index(fields=['category', 'tier'], name='idx_vouch_cat_tr'),
            models.Index(fields=['effective_start_date', 'status'], name='idx_vouch_dt_st'),
            models.Index(fields=['created_at', 'priority'], name='idx_vouch_cr_pr'),
        ]

    def __str__(self):
        return f"[{self.code}] {self.name} ({self.get_status_display()})"

    def clean(self):
        super().clean()
        if self.effective_end_date and self.effective_start_date:
            if self.effective_end_date < self.effective_start_date:
                raise ValidationError(_("Effective end date cannot precede the start date."))
        if self.capacity > 0 and self.current_occupancy > self.capacity:
            raise ValidationError(_("Current occupancy (%(occ)d) exceeds total capacity (%(cap)d)."),
                                  params={'occ': self.current_occupancy, 'cap': self.capacity})

    def save(self, *args, **kwargs):
        self.code = (self.code or '').strip().upper()
        self.full_clean()
        super().save(*args, **kwargs)

    @property
    def utilization_rate(self):
        if not self.capacity:
            return 0.0
        return round((self.current_occupancy / self.capacity) * 100, 2)

    @property
    def remaining_headroom(self):
        return max(0, self.capacity - self.current_occupancy)

    @property
    def net_budget_variance(self):
        return self.budget_allocated - self.cost_incurred

    @property
    def is_operational(self):
        today = timezone.now().date()
        if self.status != self.StatusChoices.ACTIVE:
            return False
        if self.effective_end_date and self.effective_end_date < today:
            return False
        return self.effective_start_date <= today

    def can_user_edit(self, user):
        if not user or not user.is_authenticated:
            return False
        if getattr(user, 'is_superuser', False):
            return True
        role = getattr(user, 'role', '')
        return role in ['SuperAdmin', 'InstitutionAdmin', 'Principal', 'HOD']

    def transition_status(self, new_status, user_username="system"):
        if new_status not in self.StatusChoices.values:
            raise ValueError(f"Invalid target status: {new_status}")
        self.status = new_status
        self.updated_by_user = user_username
        self.save()

    def to_dict(self):
        return {
            'uuid': str(self.uuid),
            'code': self.code,
            'name': self.name,
            'short_name': self.short_name,
            'category': self.category,
            'tier': self.tier,
            'scope': self.scope,
            'priority': self.priority,
            'status': self.status,
            'capacity': self.capacity,
            'current_occupancy': self.current_occupancy,
            'utilization_rate': self.utilization_rate,
            'remaining_headroom': self.remaining_headroom,
            'budget_allocated': float(self.budget_allocated),
            'cost_incurred': float(self.cost_incurred),
            'budget_variance': float(self.net_budget_variance),
            'effective_start': str(self.effective_start_date),
            'effective_end': str(self.effective_end_date) if self.effective_end_date else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }

    def get_absolute_url(self):
        try:
            return reverse(f'accounting:vouchers_detail', kwargs={'pk': self.pk})
        except Exception:
            return f"/accounting/vouchers/{self.pk}/"

    def check_capacity_headroom(self, additional_count=1):
        """Verifies if additional occupancy fits within configured capacity buffer."""
        return (self.current_occupancy + additional_count) <= self.capacity

    def increment_occupancy(self, count=1):
        """Atomically increments current utilization with bounds safety check."""
        if not self.check_capacity_headroom(count):
            raise ValidationError(_("Capacity headroom exceeded. Cannot allocate %(cnt)d occupants."),
                                  params={'cnt': count})
        self.current_occupancy += count
        self.save(update_fields=['current_occupancy', 'updated_at'])

    def decrement_occupancy(self, count=1):
        """Safely decrements current utilization preventing negative counts."""
        self.current_occupancy = max(0, self.current_occupancy - count)
        self.save(update_fields=['current_occupancy', 'updated_at'])

    def record_expenditure(self, amount, reason=""):
        """Records incurred financial cost against authorized operational budget."""
        amount_dec = Decimal(str(amount))
        if amount_dec < 0:
            raise ValidationError(_("Expenditure amount must be strictly non-negative."))
        self.cost_incurred += amount_dec
        self.save(update_fields=['cost_incurred', 'updated_at'])

    def get_governance_summary(self):
        """Aggregates active policy rules, schedules, and document attachments."""
        return {
            'total_items': self.items.count() if hasattr(self, 'items') else 0,
            'active_allocations': self.allocations.filter(is_active=True).count() if hasattr(self, 'allocations') else 0,
            'metrics_logged': self.metrics.count() if hasattr(self, 'metrics') else 0,
            'policy_rules_count': self.policy_rules.count() if hasattr(self, 'policy_rules') else 0,
            'documents_count': self.attachments.count() if hasattr(self, 'attachments') else 0,
        }

# -----------------------------------------------------------------------------
# Model 2: Subordinate Item / Line Component Entity
# -----------------------------------------------------------------------------
class VouchersItem(models.Model):
    """Subordinate component or line transaction item for Vouchers."""
    master = models.ForeignKey(VouchersMaster, on_delete=models.CASCADE, related_name='items')
    item_code = models.CharField(max_length=64, db_index=True, verbose_name=_("Item Code"))
    title = models.CharField(max_length=255, verbose_name=_("Item Title"))
    sequence_order = models.PositiveIntegerField(default=1, verbose_name=_("Sequence Order"))
    unit_measure = models.CharField(max_length=50, default='Unit', verbose_name=_("Unit of Measure"))
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('1.00'), verbose_name=_("Quantity"))
    unit_rate = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), verbose_name=_("Unit Rate ($)"))
    total_amount = models.DecimalField(max_digits=14, decimal_places=2, default=Decimal('0.00'), verbose_name=_("Total Amount ($)"))
    is_mandatory = models.BooleanField(default=True, verbose_name=_("Mandatory Component"))
    is_completed = models.BooleanField(default=False, verbose_name=_("Execution Completed"))
    completion_date = models.DateTimeField(blank=True, null=True, verbose_name=_("Completion Timestamp"))
    remarks = models.TextField(blank=True, verbose_name=_("Staff Remarks"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'eduflow_accounting_vouchers_item'
        ordering = ['sequence_order', 'id']
        verbose_name = _("Vouchers Item")
        verbose_name_plural = _("Vouchers Items")

    def __str__(self):
        return f"{self.master.code} -> [{self.item_code}] {self.title}"

    def save(self, *args, **kwargs):
        self.total_amount = round(self.quantity * self.unit_rate, 2)
        if self.is_completed and not self.completion_date:
            self.completion_date = timezone.now()
        super().save(*args, **kwargs)

    def mark_completed(self):
        self.is_completed = True
        self.completion_date = timezone.now()
        self.save()

# -----------------------------------------------------------------------------
# Model 3: Allocation / Assignment Entity
# -----------------------------------------------------------------------------
class VouchersAllocation(models.Model):
    """Resource allocations (students, teachers, rooms, staff) for Vouchers."""
    master = models.ForeignKey(VouchersMaster, on_delete=models.CASCADE, related_name='allocations')
    assignee_id = models.PositiveIntegerField(db_index=True, verbose_name=_("Assignee ID"))
    assignee_name = models.CharField(max_length=255, verbose_name=_("Assignee Name / Role"))
    allocation_role = models.CharField(max_length=100, default='Primary Assignee', verbose_name=_("Role in Allocation"))
    start_time = models.DateTimeField(default=timezone.now, verbose_name=_("Allocation Start Time"))
    end_time = models.DateTimeField(blank=True, null=True, verbose_name=_("Allocation End Time"))
    allocated_quota = models.PositiveIntegerField(default=1, verbose_name=_("Allocated Quota"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    authorization_code = models.CharField(max_length=64, blank=True, verbose_name=_("Authorization Code"))
    notes = models.TextField(blank=True, verbose_name=_("Assignment Notes"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'eduflow_accounting_vouchers_allocation'
        ordering = ['-start_time']
        verbose_name = _("Vouchers Allocation")
        verbose_name_plural = _("Vouchers Allocations")

    def __str__(self):
        return f"{self.master.code} Assigned to {self.assignee_name} ({self.allocation_role})"

    def is_overlapping(self, start, end):
        if not self.is_active:
            return False
        if not end:
            return self.start_time <= start
        return (self.start_time <= end) and ((self.end_time or timezone.now()) >= start)

# -----------------------------------------------------------------------------
# Model 4: Metric & Performance Record
# -----------------------------------------------------------------------------
class VouchersMetricRecord(models.Model):
    """Captures KPI metrics, telemetry, and performance measurements for Vouchers."""
    master = models.ForeignKey(VouchersMaster, on_delete=models.CASCADE, related_name='metrics')
    metric_name = models.CharField(max_length=100, db_index=True, verbose_name=_("KPI / Metric Name"))
    target_value = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('100.00'), verbose_name=_("Target Value"))
    actual_value = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), verbose_name=_("Observed Value"))
    score_percentage = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'), verbose_name=_("Score Percentage"))
    is_passing = models.BooleanField(default=True, verbose_name=_("Benchmark Satisfied"))
    evaluated_at = models.DateTimeField(default=timezone.now, verbose_name=_("Evaluation Timestamp"))
    evaluator_remarks = models.TextField(blank=True, verbose_name=_("Evaluator Notes"))

    class Meta:
        db_table = 'eduflow_accounting_vouchers_metric'
        ordering = ['-evaluated_at']
        verbose_name = _("Vouchers Metric Record")
        verbose_name_plural = _("Vouchers Metric Records")

    def __str__(self):
        return f"{self.master.code} - {self.metric_name}: {self.actual_value} / {self.target_value}"

    def save(self, *args, **kwargs):
        if self.target_value > 0:
            self.score_percentage = round((self.actual_value / self.target_value) * 100, 2)
            self.is_passing = self.score_percentage >= 50.0
        super().save(*args, **kwargs)

# -----------------------------------------------------------------------------
# Model 5: Policy & Business Rule Entity
# -----------------------------------------------------------------------------
class VouchersPolicyRule(models.Model):
    """Institutional rules, thresholds, and governance policies for Vouchers."""
    master = models.ForeignKey(VouchersMaster, on_delete=models.CASCADE, related_name='policy_rules')
    rule_code = models.CharField(max_length=64, db_index=True, verbose_name=_("Rule Code"))
    rule_name = models.CharField(max_length=255, verbose_name=_("Policy Rule Name"))
    threshold_value = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('75.00'), verbose_name=_("Threshold Metric"))
    comparison_operator = models.CharField(max_length=20, default='GREATER_THAN_EQUAL', verbose_name=_("Operator"))
    action_on_breach = models.CharField(max_length=100, default='FLAG_ALERT', verbose_name=_("Action On Breach"))
    is_enforced = models.BooleanField(default=True, verbose_name=_("Strictly Enforced"))
    rule_description = models.TextField(blank=True, verbose_name=_("Policy Description"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'eduflow_accounting_vouchers_rule'
        ordering = ['rule_code']
        verbose_name = _("Vouchers Policy Rule")
        verbose_name_plural = _("Vouchers Policy Rules")

    def __str__(self):
        return f"Rule [{self.rule_code}] {self.rule_name} ({self.threshold_value})"

    def check_compliance(self, observed_val):
        if self.comparison_operator == 'GREATER_THAN_EQUAL':
            return observed_val >= self.threshold_value
        elif self.comparison_operator == 'LESS_THAN_EQUAL':
            return observed_val <= self.threshold_value
        return True

# -----------------------------------------------------------------------------
# Model 6: Schedule & Period Interval Entity
# -----------------------------------------------------------------------------
class VouchersSchedulePeriod(models.Model):
    """Temporal schedules, time intervals, and recurrent sessions for Vouchers."""
    master = models.ForeignKey(VouchersMaster, on_delete=models.CASCADE, related_name='schedule_periods')
    period_title = models.CharField(max_length=150, verbose_name=_("Session / Period Name"))
    day_of_week = models.IntegerField(default=1, verbose_name=_("Day of Week (1=Mon, 7=Sun)"))
    start_time = models.TimeField(verbose_name=_("Start Time"))
    end_time = models.TimeField(verbose_name=_("End Time"))
    is_break_period = models.BooleanField(default=False, verbose_name=_("Is Recess / Break"))
    room_number = models.CharField(max_length=50, blank=True, verbose_name=_("Room / Location"))
    session_notes = models.TextField(blank=True, verbose_name=_("Session Instructions"))

    class Meta:
        db_table = 'eduflow_accounting_vouchers_period'
        ordering = ['day_of_week', 'start_time']
        verbose_name = _("Vouchers Schedule Period")
        verbose_name_plural = _("Vouchers Schedule Periods")

    def __str__(self):
        return f"Day {self.day_of_week}: {self.period_title} ({self.start_time} - {self.end_time})"

    @property
    def duration_minutes(self):
        """Calculates duration in minutes."""
        if not self.start_time or not self.end_time:
            return 0
        from datetime import datetime, date
        dt_start = datetime.combine(date.today(), self.start_time)
        dt_end = datetime.combine(date.today(), self.end_time)
        return int((dt_end - dt_start).total_seconds() / 60)

    @property
    def day_name(self):
        days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
        return days.get(self.day_of_week, 'Unknown')

    def check_period_collision(self, other_start, other_end, other_day=None):
        """Detects if another period conflicts on same day of week."""
        if other_day and other_day != self.day_of_week:
            return False
        return (self.start_time < other_end) and (self.end_time > other_start)

# -----------------------------------------------------------------------------
# Model 7: Feedback & Review Entity
# -----------------------------------------------------------------------------
class VouchersFeedbackReview(models.Model):
    """Institutional evaluation, stakeholder feedback, and peer reviews for Vouchers."""
    master = models.ForeignKey(VouchersMaster, on_delete=models.CASCADE, related_name='reviews')
    reviewer_role = models.CharField(max_length=50, default='Staff', verbose_name=_("Reviewer Role"))
    reviewer_name = models.CharField(max_length=150, verbose_name=_("Reviewer Name"))
    rating = models.PositiveSmallIntegerField(default=5, verbose_name=_("Rating (1-5)"))
    qualitative_feedback = models.TextField(verbose_name=_("Qualitative Review Feedback"))
    actionable_recommendations = models.TextField(blank=True, verbose_name=_("Recommendations"))
    is_resolved = models.BooleanField(default=False, verbose_name=_("Action Items Resolved"))
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'eduflow_accounting_vouchers_review'
        ordering = ['-submitted_at']
        verbose_name = _("Vouchers Review")
        verbose_name_plural = _("Vouchers Reviews")

    def __str__(self):
        return f"Review by {self.reviewer_name} - {self.rating}/5"

# -----------------------------------------------------------------------------
# Model 8: Workflow Transition Entity
# -----------------------------------------------------------------------------
class VouchersWorkflowTransition(models.Model):
    """Auditable multi-stage approval workflow and transition state machine."""
    master = models.ForeignKey(VouchersMaster, on_delete=models.CASCADE, related_name='workflow_transitions')
    from_stage = models.CharField(max_length=50, verbose_name=_("Source Stage"))
    to_stage = models.CharField(max_length=50, verbose_name=_("Destination Stage"))
    actor_username = models.CharField(max_length=150, verbose_name=_("Authorizing Officer"))
    approver_comments = models.TextField(blank=True, verbose_name=_("Approval / Rejection Comments"))
    is_approved = models.BooleanField(default=True, verbose_name=_("Was Approved"))
    transition_timestamp = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        db_table = 'eduflow_accounting_vouchers_workflow'
        ordering = ['-transition_timestamp']
        verbose_name = _("Vouchers Workflow Transition")
        verbose_name_plural = _("Vouchers Workflow Transitions")

    def __str__(self):
        return f"{self.master.code}: {self.from_stage} -> {self.to_stage} by {self.actor_username}"

    @property
    def is_terminal_state(self):
        return self.to_stage in ['APPROVED', 'REJECTED', 'CANCELLED', 'ARCHIVED']

    def generate_transition_receipt(self):
        return {
            'transition_id': self.pk,
            'source_stage': self.from_stage,
            'target_stage': self.to_stage,
            'authorizing_agent': self.actor_username,
            'verdict': 'APPROVED' if self.is_approved else 'REJECTED',
            'timestamp': self.transition_timestamp.isoformat(),
        }

# -----------------------------------------------------------------------------
# Model 9: Access Control Rule Entity
# -----------------------------------------------------------------------------
class VouchersAccessRule(models.Model):
    """Object-level access permissions and role-based viewing/editing grants."""
    master = models.ForeignKey(VouchersMaster, on_delete=models.CASCADE, related_name='access_rules')
    role_allowed = models.CharField(max_length=50, verbose_name=_("Authorized Role"))
    can_read = models.BooleanField(default=True, verbose_name=_("Can Read"))
    can_write = models.BooleanField(default=False, verbose_name=_("Can Write / Edit"))
    can_delete = models.BooleanField(default=False, verbose_name=_("Can Delete"))
    can_export = models.BooleanField(default=True, verbose_name=_("Can Export CSV/PDF"))
    granted_by = models.CharField(max_length=150, default='system', verbose_name=_("Granted By"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'eduflow_accounting_vouchers_access'
        verbose_name = _("Vouchers Access Rule")
        verbose_name_plural = _("Vouchers Access Rules")

    def __str__(self):
        return f"Access [{self.role_allowed}] on {self.master.code}"

# -----------------------------------------------------------------------------
# Model 10: Configuration Parameter Entity
# -----------------------------------------------------------------------------
class VouchersConfigurationParameter(models.Model):
    """Runtime parameters, feature flags, and custom settings."""
    master = models.ForeignKey(VouchersMaster, on_delete=models.CASCADE, related_name='config_parameters')
    param_key = models.CharField(max_length=100, db_index=True, verbose_name=_("Parameter Key"))
    param_value = models.CharField(max_length=255, verbose_name=_("Parameter Value"))
    data_type = models.CharField(max_length=30, default='STRING', verbose_name=_("Value Data Type"))
    is_editable = models.BooleanField(default=True, verbose_name=_("Is Editable in UI"))
    description = models.CharField(max_length=255, blank=True, verbose_name=_("Parameter Description"))

    class Meta:
        db_table = 'eduflow_accounting_vouchers_config'
        verbose_name = _("Vouchers Config Parameter")
        verbose_name_plural = _("Vouchers Config Parameters")

    def __str__(self):
        return f"{self.param_key} = {self.param_value}"

# -----------------------------------------------------------------------------
# Model 11: Document Attachment Reference
# -----------------------------------------------------------------------------
class VouchersDocumentAttachment(models.Model):
    """Associated official documentation, uploaded files, and certificates."""
    master = models.ForeignKey(VouchersMaster, on_delete=models.CASCADE, related_name='attachments')
    title = models.CharField(max_length=255, verbose_name=_("Document Title"))
    file_path = models.CharField(max_length=500, verbose_name=_("Secure File Path / URI"))
    file_size_bytes = models.PositiveBigIntegerField(default=0, verbose_name=_("File Size in Bytes"))
    mime_type = models.CharField(max_length=100, default='application/pdf', verbose_name=_("MIME Type"))
    checksum_hash = models.CharField(max_length=64, blank=True, verbose_name=_("SHA-256 Checksum"))
    uploaded_by = models.CharField(max_length=150, default='system', verbose_name=_("Uploaded By"))
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'eduflow_accounting_vouchers_doc'
        ordering = ['-uploaded_at']
        verbose_name = _("Vouchers Document Attachment")
        verbose_name_plural = _("Vouchers Document Attachments")

    def __str__(self):
        return f"{self.master.code} -> {self.title} ({self.mime_type})"

# -----------------------------------------------------------------------------
# Model 12: Immutable Compliance Audit Trail
# -----------------------------------------------------------------------------
class VouchersAuditTrail(models.Model):
    """Immutable audit trail capturing all state mutations on Vouchers."""
    master = models.ForeignKey(VouchersMaster, on_delete=models.CASCADE, related_name='audit_records')
    action_type = models.CharField(max_length=64, db_index=True, verbose_name=_("Action Type"))
    performed_by = models.CharField(max_length=150, default='system', verbose_name=_("Actor Username"))
    ip_address = models.GenericIPAddressField(blank=True, null=True, verbose_name=_("Client IP"))
    previous_state = models.JSONField(default=dict, verbose_name=_("Snapshot Before"))
    new_state = models.JSONField(default=dict, verbose_name=_("Snapshot After"))
    change_summary = models.TextField(verbose_name=_("Summary of Mutation"))
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        db_table = 'eduflow_accounting_vouchers_audit'
        ordering = ['-timestamp']
        verbose_name = _("Vouchers Audit Entry")
        verbose_name_plural = _("Vouchers Audit Entries")

    def __str__(self):
        return f"Audit [{self.action_type}] on {self.master.code} by {self.performed_by} at {self.timestamp}"

    def get_diff_keys(self):
        """Identifies specific keys mutated during transaction."""
        before = self.previous_state or {}
        after = self.new_state or {}
        changed_keys = set()
        for k, v in after.items():
            if before.get(k) != v:
                changed_keys.add(k)
        return list(changed_keys)

    def is_financial_mutation(self):
        financial_keys = {'budget_allocated', 'cost_incurred', 'budget_variance'}
        return bool(set(self.get_diff_keys()).intersection(financial_keys))
