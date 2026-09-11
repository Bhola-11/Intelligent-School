"""
Domain Validators for EduFlow Library Circulation, Borrow & Returns (Circulation).
Encapsulates business rule checks, threshold guards, and security constraints.
"""

from decimal import Decimal
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class CirculationValidator:
    """Domain validator implementing enterprise business rules for Circulation."""

    @staticmethod
    def validate_code_format(code):
        if not code or len(code.strip()) < 3:
            raise ValidationError(_("Identifier code must have at least 3 alphanumeric characters."))
        if any(c in code for c in [' ', '@', '#', '$', '%', '&', '*']):
            raise ValidationError(_("Identifier code cannot contain spaces or special punctuation symbols."))
        return code.strip().upper()

    @staticmethod
    def validate_capacity_bounds(capacity, occupancy):
        if capacity < 0:
            raise ValidationError(_("Capacity cannot be negative."))
        if occupancy < 0:
            raise ValidationError(_("Occupancy count cannot be negative."))
        if capacity > 0 and occupancy > capacity:
            raise ValidationError(_("Current occupancy cannot exceed configured total capacity ceiling."))

    @staticmethod
    def validate_date_intervals(start_date, end_date):
        if start_date and end_date:
            if end_date < start_date:
                raise ValidationError(_("Effective end date cannot precede the start date."))

    @staticmethod
    def validate_budget_appropriation(allocated, incurred):
        if allocated < Decimal('0.00'):
            raise ValidationError(_("Budget allocation cannot be negative."))
        if incurred < Decimal('0.00'):
            raise ValidationError(_("Incurred expenditures cannot be negative."))

    @staticmethod
    def validate_allocation_window(start_time, end_time):
        if start_time and end_time:
            if end_time <= start_time:
                raise ValidationError(_("Allocation completion time must strictly succeed the start time."))

    @staticmethod
    def validate_policy_threshold(threshold, operator):
        if threshold < Decimal('0.00'):
            raise ValidationError(_("Policy rule threshold metric cannot be negative."))
        valid_ops = {'GREATER_THAN_EQUAL', 'LESS_THAN_EQUAL', 'EQUAL', 'NOT_EQUAL'}
        if operator not in valid_ops:
            raise ValidationError(_("Invalid policy operator. Must be one of %(ops)s"), params={'ops': list(valid_ops)})

    @staticmethod
    def validate_line_item(unit_rate, quantity):
        if unit_rate < Decimal('0.00'):
            raise ValidationError(_("Item rate cannot be negative."))
        if quantity <= Decimal('0.00'):
            raise ValidationError(_("Quantity must be strictly positive."))

    @staticmethod
    def validate_feedback_rating(rating):
        if rating < 1 or rating > 5:
            raise ValidationError(_("Rating score must be between 1 and 5 inclusive."))

    @staticmethod
    def validate_workflow_stages(from_stage, to_stage):
        if from_stage == to_stage:
            raise ValidationError(_("Source stage and destination stage cannot be identical in a transition."))
