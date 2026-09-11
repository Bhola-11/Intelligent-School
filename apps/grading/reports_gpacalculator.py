"""
Operational Reporting Engine for EduFlow GPA, CGPA, Term Average & Rank Engine (GPACalculator).
Generates aggregated metrics, utilization breakdowns, financial variance, and CSV datasets.
"""

import csv
import io
from decimal import Decimal
from django.utils import timezone
from django.db.models import Avg, Sum, Count, Min, Max

try:
    from .models import GPACalculatorMaster, GPACalculatorItem, GPACalculatorAllocation
except ImportError:
    pass

class GPACalculatorReportGenerator:
    """Generates analytical reports and summary matrices for GPACalculator."""

    @classmethod
    def generate_utilization_summary(cls):
        """Computes institutional utilization metrics across all active entities."""
        records = GPACalculatorMaster.objects.all() if 'GPACalculatorMaster' in globals() else []
        total_records = len(records)
        total_capacity = sum(r.capacity for r in records)
        total_occupancy = sum(r.current_occupancy for r in records)
        total_budget = sum(r.budget_allocated for r in records)
        total_cost = sum(r.cost_incurred for r in records)

        overall_utilization = round((total_occupancy / total_capacity * 100), 2) if total_capacity > 0 else 0.0

        return {
            'total_records': total_records,
            'total_capacity': total_capacity,
            'total_occupancy': total_occupancy,
            'overall_utilization_rate': overall_utilization,
            'total_budget': float(total_budget),
            'total_cost': float(total_cost),
            'net_variance': float(total_budget - total_cost),
            'generated_at': timezone.now().isoformat(),
        }

    @classmethod
    def export_summary_csv(cls):
        """Builds a formatted CSV string of all entities."""
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Code', 'Name', 'Category', 'Tier', 'Status', 'Capacity', 'Occupancy', 'Utilization (%)', 'Budget ($)', 'Cost ($)'])

        records = GPACalculatorMaster.objects.all() if 'GPACalculatorMaster' in globals() else []
        for r in records:
            writer.writerow([
                r.code, r.name, r.category, r.tier, r.status,
                r.capacity, r.current_occupancy, r.utilization_rate,
                r.budget_allocated, r.cost_incurred
            ])

        return output.getvalue()
