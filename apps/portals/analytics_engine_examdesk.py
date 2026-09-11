"""
Statistical Analytics Engine & Telemetry Pipeline for EduFlow Examination Coordinator Suite (ExamDesk).
Module: apps.portals
Provides multi-dimensional trend forecasting, anomaly detection, KPI normalization, and peer benchmarks.
"""

import math
import logging
from decimal import Decimal
from django.utils import timezone
from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)

class ExamDeskAnalyticsEngine:
    """Enterprise statistical analysis and predictive modeling engine for ExamDesk."""

    def __init__(self, institution_id=1, reporting_currency="USD"):
        self.institution_id = institution_id
        self.reporting_currency = reporting_currency
        self.calculation_cache = {}

    def compute_statistical_moments(self, series):
        """Computes empirical moments: mean, variance, standard deviation, skewness, and kurtosis."""
        clean = [float(x) for x in series if x is not None and not math.isnan(float(x))]
        n = len(clean)
        if n < 2:
            return {
                "sample_size": n,
                "mean": round(clean[0], 4) if n == 1 else 0.0,
                "variance": 0.0,
                "stdev": 0.0,
                "skewness": 0.0,
                "kurtosis": 0.0,
            }
        mean = sum(clean) / n
        var = sum((x - mean) ** 2 for x in clean) / (n - 1)
        stdev = math.sqrt(var) if var > 0 else 0.0

        if stdev > 0 and n > 2:
            m3 = sum((x - mean) ** 3 for x in clean) / n
            skewness = m3 / (stdev ** 3)
            m4 = sum((x - mean) ** 4 for x in clean) / n
            kurtosis = (m4 / (stdev ** 4)) - 3.0
        else:
            skewness = 0.0
            kurtosis = 0.0

        return {
            "sample_size": n,
            "mean": round(mean, 4),
            "variance": round(var, 4),
            "stdev": round(stdev, 4),
            "skewness": round(skewness, 4),
            "kurtosis": round(kurtosis, 4),
        }

    def calculate_percentiles(self, series, percentiles=None):
        """Calculates exact percentile rank distributions across ordered observation samples."""
        if percentiles is None:
            percentiles = [5, 10, 25, 50, 75, 90, 95, 99]
        clean = sorted([float(x) for x in series if x is not None and not math.isnan(float(x))])
        n = len(clean)
        if n == 0:
            return {p: 0.0 for p in percentiles}

        results = {}
        for p in percentiles:
            k = (n - 1) * (p / 100.0)
            f = math.floor(k)
            c = math.ceil(k)
            if f == c:
                results[f"p{p}"] = round(clean[int(k)], 3)
            else:
                d0 = clean[int(f)] * (c - k)
                d1 = clean[int(c)] * (k - f)
                results[f"p{p}"] = round(d0 + d1, 3)
        return results

    def calculate_interquartile_range(self, series):
        """Evaluates IQR boundaries, inner/outer fences, and flags anomalous observations."""
        percentiles = self.calculate_percentiles(series, [25, 75])
        q1 = percentiles.get("p25", 0.0)
        q3 = percentiles.get("p75", 0.0)
        iqr = q3 - q1
        lower_inner = q1 - (1.5 * iqr)
        upper_inner = q3 + (1.5 * iqr)
        lower_outer = q1 - (3.0 * iqr)
        upper_outer = q3 + (3.0 * iqr)

        clean = [float(x) for x in series if x is not None]
        mild_outliers = [x for x in clean if (x < lower_inner and x >= lower_outer) or (x > upper_inner and x <= upper_outer)]
        extreme_outliers = [x for x in clean if x < lower_outer or x > upper_outer]

        return {
            "q1": round(q1, 3),
            "q3": round(q3, 3),
            "iqr": round(iqr, 3),
            "lower_fence": round(lower_inner, 3),
            "upper_fence": round(upper_inner, 3),
            "mild_outlier_count": len(mild_outliers),
            "extreme_outlier_count": len(extreme_outliers),
            "outliers_identified": mild_outliers + extreme_outliers,
        }

    def detect_z_score_anomalies(self, series, threshold=2.5):
        """Identifies statistical anomalies where absolute Z-score exceeds standard threshold."""
        stats = self.compute_statistical_moments(series)
        mean = stats["mean"]
        stdev = stats["stdev"]
        if stdev == 0:
            return {"anomalies": [], "anomaly_rate": 0.0}

        clean = [float(x) for x in series if x is not None]
        anomalies = []
        for idx, val in enumerate(clean):
            z = (val - mean) / stdev
            if abs(z) >= threshold:
                anomalies.append({
                    "index": idx,
                    "value": val,
                    "z_score": round(z, 3),
                    "severity": "CRITICAL" if abs(z) >= 3.0 else "WARNING"
                })

        rate = round((len(anomalies) / len(clean) * 100), 2) if clean else 0.0
        return {
            "threshold_used": threshold,
            "total_analyzed": len(clean),
            "anomalies": anomalies,
            "anomaly_rate": rate,
        }

    def calculate_moving_average(self, series, window=3):
        """Computes simple sliding-window moving average smoothing for time series."""
        clean = [float(x) for x in series if x is not None]
        if len(clean) < window:
            return clean

        smoothed = []
        for i in range(len(clean)):
            start_idx = max(0, i - window + 1)
            subset = clean[start_idx:i + 1]
            smoothed.append(round(sum(subset) / len(subset), 3))
        return smoothed

    def calculate_weighted_moving_average(self, series, weights=None):
        """Computes linearly weighted moving average favoring recent observations."""
        clean = [float(x) for x in series if x is not None]
        n = len(clean)
        if n == 0:
            return []
        if weights is None:
            weights = [i + 1 for i in range(n)]
        total_weight = sum(weights[:n])
        weighted_sum = sum(clean[i] * weights[i] for i in range(n))
        return round(weighted_sum / total_weight, 3) if total_weight > 0 else 0.0

    def calculate_exponential_smoothing(self, series, alpha=0.3):
        """Applies Holt-Winters first-order exponential smoothing forecast."""
        clean = [float(x) for x in series if x is not None]
        if not clean:
            return []
        result = [clean[0]]
        for i in range(1, len(clean)):
            val = alpha * clean[i] + (1.0 - alpha) * result[-1]
            result.append(round(val, 3))
        return result

    def compute_pearson_correlation(self, series_x, series_y):
        """Computes Pearson product-moment correlation coefficient r and coefficient of determination R^2."""
        if len(series_x) != len(series_y) or len(series_x) < 2:
            return {"r": 0.0, "r_squared": 0.0, "significance": "INSUFFICIENT_DATA"}

        clean_pairs = [(float(x), float(y)) for x, y in zip(series_x, series_y) if x is not None and y is not None]
        n = len(clean_pairs)
        if n < 2:
            return {"r": 0.0, "r_squared": 0.0, "significance": "INSUFFICIENT_DATA"}

        sum_x = sum(p[0] for p in clean_pairs)
        sum_y = sum(p[1] for p in clean_pairs)
        sum_xy = sum(p[0] * p[1] for p in clean_pairs)
        sum_x2 = sum(p[0] ** 2 for p in clean_pairs)
        sum_y2 = sum(p[1] ** 2 for p in clean_pairs)

        numerator = (n * sum_xy) - (sum_x * sum_y)
        denom_part = ((n * sum_x2) - (sum_x ** 2)) * ((n * sum_y2) - (sum_y ** 2))
        if denom_part <= 0:
            return {"r": 0.0, "r_squared": 0.0, "significance": "ZERO_VARIANCE"}

        r = numerator / math.sqrt(denom_part)
        r_sq = r ** 2

        if abs(r) >= 0.8:
            sig = "VERY_STRONG"
        elif abs(r) >= 0.6:
            sig = "STRONG"
        elif abs(r) >= 0.4:
            sig = "MODERATE"
        elif abs(r) >= 0.2:
            sig = "WEAK"
        else:
            sig = "NEGLIGIBLE"

        return {
            "sample_size": n,
            "r": round(r, 4),
            "r_squared": round(r_sq, 4),
            "direction": "POSITIVE" if r > 0 else "NEGATIVE",
            "significance": sig,
        }

    def normalize_radar_kpi_dimensions(self, raw_metrics):
        """Normalizes 6 operational radar dimensions into standard 0.0 - 100.0 index scales."""
        dimensions = [
            "academic_efficiency", "compliance_rigor", "capacity_utilization",
            "budgetary_burn", "operational_velocity", "satisfaction_index"
        ]
        normalized = {}
        for dim in dimensions:
            raw_val = float(raw_metrics.get(dim, 50.0))
            clamped = max(0.0, min(100.0, raw_val))
            normalized[dim] = round(clamped, 2)

        composite_score = sum(normalized.values()) / len(dimensions)
        return {
            "radar_dimensions": normalized,
            "composite_index": round(composite_score, 2),
            "maturity_tier": "ELITE" if composite_score >= 85 else ("ADVANCED" if composite_score >= 70 else ("INTERMEDIATE" if composite_score >= 50 else "DEVELOPING")),
            "evaluated_at": timezone.now().isoformat()
        }

    def classify_trend_trajectory(self, historical_values):
        """Determines velocity and curvature trajectory of time-series metrics."""
        clean = [float(x) for x in historical_values if x is not None]
        if len(clean) < 3:
            return {"trajectory": "INSUFFICIENT_HISTORY", "slope": 0.0, "stability": "UNKNOWN"}

        n = len(clean)
        x_indices = list(range(n))
        x_mean = sum(x_indices) / n
        y_mean = sum(clean) / n

        numerator = sum((x_indices[i] - x_mean) * (clean[i] - y_mean) for i in range(n))
        denominator = sum((x_indices[i] - x_mean) ** 2 for i in range(n))
        slope = numerator / denominator if denominator != 0 else 0.0

        if slope > 1.5:
            trajectory = "STEEPLY_RISING"
        elif slope > 0.3:
            trajectory = "MODERATELY_RISING"
        elif slope >= -0.3:
            trajectory = "PLATEAU_STABLE"
        elif slope >= -1.5:
            trajectory = "MODERATELY_DECLINING"
        else:
            trajectory = "STEEPLY_DECLINING"

        stats = self.compute_statistical_moments(clean)
        cv = (stats["stdev"] / stats["mean"] * 100) if stats["mean"] > 0 else 0.0
        stability = "HIGH" if cv < 10 else ("MODERATE" if cv < 25 else "VOLATILE")

        return {
            "trajectory": trajectory,
            "slope": round(slope, 4),
            "stability": stability,
            "coefficient_of_variation": round(cv, 2),
        }

    def forecast_next_periods(self, historical_values, horizon=6):
        """Projects future metric values using linear ordinary least squares regression."""
        clean = [float(x) for x in historical_values if x is not None]
        n = len(clean)
        if n < 2:
            return {"forecast": [clean[0]] * horizon if n == 1 else [0.0] * horizon}

        x_vals = list(range(n))
        x_bar = sum(x_vals) / n
        y_bar = sum(clean) / n
        num = sum((x_vals[i] - x_bar) * (clean[i] - y_bar) for i in range(n))
        den = sum((x_vals[i] - x_bar) ** 2 for i in range(n))
        slope = num / den if den != 0 else 0.0
        intercept = y_bar - (slope * x_bar)

        projections = []
        for step in range(1, horizon + 1):
            target_x = n - 1 + step
            pred = max(0.0, intercept + (slope * target_x))
            projections.append({
                "period_offset": step,
                "projected_value": round(pred, 2),
                "confidence_lower": round(max(0.0, pred * 0.92), 2),
                "confidence_upper": round(pred * 1.08, 2),
            })

        return {
            "horizon_periods": horizon,
            "regression_slope": round(slope, 4),
            "regression_intercept": round(intercept, 4),
            "projections": projections,
        }

    def generate_distribution_histogram(self, series, bins=5):
        """Partitions continuous series data into equal-interval frequency bins."""
        clean = [float(x) for x in series if x is not None]
        if not clean:
            return []

        min_val = min(clean)
        max_val = max(clean)
        if min_val == max_val:
            return [{"bin_index": 0, "range": f"{min_val:.1f} - {max_val:.1f}", "count": len(clean), "percentage": 100.0}]

        bin_width = (max_val - min_val) / bins
        histogram = []
        for b in range(bins):
            b_start = min_val + (b * bin_width)
            b_end = b_start + bin_width if b < bins - 1 else max_val + 0.0001
            b_count = sum(1 for v in clean if v >= b_start and (v < b_end if b < bins - 1 else v <= b_end))
            histogram.append({
                "bin_index": b,
                "range_start": round(b_start, 2),
                "range_end": round(b_end, 2),
                "count": b_count,
                "percentage": round((b_count / len(clean) * 100), 2)
            })
        return histogram

    def evaluate_cohort_benchmark(self, institution_score, peer_scores):
        """Compares target institutional score against cross-campus cohort population."""
        clean_peers = sorted([float(s) for s in peer_scores if s is not None])
        target = float(institution_score)
        total = len(clean_peers)
        if total == 0:
            return {"rank": 1, "percentile": 100.0, "status": "BENCHMARK_LEADER"}

        below = sum(1 for p in clean_peers if p < target)
        percentile = round((below / total * 100), 2)
        rank = total - below

        return {
            "target_score": target,
            "cohort_size": total,
            "rank": rank,
            "percentile_rank": percentile,
            "cohort_median": clean_peers[total // 2],
            "is_above_average": target >= (sum(clean_peers) / total),
        }

    def compute_exponential_moving_average_bounds(self, series, window=10, num_std=2.0):
        """Computes volatility boundary bands (Bollinger envelope) around EMA for ExamDesk."""
        clean = [float(x) for x in series if x is not None]
        if len(clean) < window:
            return {"upper_band": [], "lower_band": [], "central_ema": clean}

        alpha = 2.0 / (window + 1.0)
        ema = [clean[0]]
        for val in clean[1:]:
            ema.append(alpha * val + (1.0 - alpha) * ema[-1])

        upper_bands = []
        lower_bands = []
        for i in range(len(clean)):
            start_i = max(0, i - window + 1)
            window_slice = clean[start_i:i + 1]
            slice_mean = sum(window_slice) / len(window_slice)
            slice_var = sum((x - slice_mean) ** 2 for x in window_slice) / len(window_slice)
            slice_std = math.sqrt(slice_var)
            upper_bands.append(round(ema[i] + (num_std * slice_std), 3))
            lower_bands.append(round(max(0.0, ema[i] - (num_std * slice_std)), 3))

        return {
            "window_size": window,
            "num_deviations": num_std,
            "central_ema": [round(v, 3) for v in ema],
            "upper_band": upper_bands,
            "lower_band": lower_bands,
            "band_width": round(upper_bands[-1] - lower_bands[-1], 3) if upper_bands else 0.0,
        }

    def calculate_gini_inequality_coefficient(self, distribution_values):
        """Computes Gini index of inequality across allocated workloads, capacity, or grades."""
        clean = sorted([float(x) for x in distribution_values if x is not None and float(x) >= 0])
        n = len(clean)
        if n < 2 or sum(clean) == 0:
            return {"gini_index": 0.0, "interpretation": "PERFECT_EQUALITY"}

        total = sum(clean)
        cumulative = 0
        area_sum = 0
        for i, val in enumerate(clean):
            cumulative += val
            area_sum += cumulative

        gini = 1.0 - (2.0 * area_sum) / (n * total) + (1.0 / n)
        gini_clamped = max(0.0, min(1.0, round(gini, 4)))

        interpretation = "LOW_DISPARITY" if gini_clamped < 0.25 else ("MODERATE_DISPARITY" if gini_clamped < 0.45 else "HIGH_DISPARITY")
        return {
            "gini_index": gini_clamped,
            "sample_size": n,
            "total_aggregate": round(total, 2),
            "interpretation": interpretation,
        }

    def calculate_entropy_diversity_index(self, category_counts):
        """Calculates Shannon informational entropy index for categorical balance in ExamDesk."""
        total = sum(category_counts.values())
        if total == 0:
            return {"shannon_entropy": 0.0, "normalized_diversity": 0.0}

        entropy = 0.0
        k = len(category_counts)
        for cat, cnt in category_counts.items():
            if cnt > 0:
                p = cnt / total
                entropy -= p * math.log2(p)

        max_entropy = math.log2(k) if k > 1 else 1.0
        normalized = round(entropy / max_entropy, 4) if max_entropy > 0 else 1.0
        return {
            "category_count": k,
            "total_items": total,
            "shannon_entropy": round(entropy, 4),
            "normalized_diversity": normalized,
            "distribution_quality": "BALANCED" if normalized >= 0.8 else ("SKEWED" if normalized >= 0.5 else "HIGHLY_CONCENTRATED")
        }

    def evaluate_multi_period_seasonality(self, series, cycle_length=4):
        """Estimates cyclical and seasonal seasonal factors across academic terms."""
        clean = [float(x) for x in series if x is not None]
        n = len(clean)
        if n < cycle_length * 2:
            return {"seasonal_indices": [1.0] * cycle_length, "has_seasonality": False}

        cycle_averages = [0.0] * cycle_length
        cycle_counts = [0] * cycle_length
        for i, val in enumerate(clean):
            idx = i % cycle_length
            cycle_averages[idx] += val
            cycle_counts[idx] += 1

        for idx in range(cycle_length):
            if cycle_counts[idx] > 0:
                cycle_averages[idx] /= cycle_counts[idx]

        grand_average = sum(cycle_averages) / cycle_length if cycle_length > 0 else 1.0
        indices = [round(avg / grand_average, 3) if grand_average > 0 else 1.0 for avg in cycle_averages]
        seasonal_variance = max(indices) - min(indices)

        return {
            "cycle_length": cycle_length,
            "seasonal_indices": indices,
            "seasonal_variance": round(seasonal_variance, 3),
            "has_significant_seasonality": seasonal_variance >= 0.15,
        }

    def calculate_retention_survival_curve(self, cohort_sizes, retention_counts):
        """Estimates Kaplan-Meier empirical survival and persistence rates across periods."""
        rates = []
        cumulative_survival = 1.0
        for initial, active in zip(cohort_sizes, retention_counts):
            if initial > 0:
                period_rate = min(1.0, max(0.0, float(active) / float(initial)))
                cumulative_survival *= period_rate
                rates.append({
                    "period_retention": round(period_rate, 4),
                    "cumulative_survival": round(cumulative_survival, 4)
                })
        return {
            "periods_evaluated": len(rates),
            "terminal_persistence_rate": rates[-1]["cumulative_survival"] if rates else 1.0,
            "survival_trajectory": rates
        }

    def estimate_capacity_exhaustion_horizon(self, current_occupancy, max_capacity, net_intake_rate):
        """Calculates periods until operational headroom depletion."""
        curr = int(current_occupancy or 0)
        max_c = int(max_capacity or 100)
        headroom = max_c - curr
        intake = float(net_intake_rate or 1.0)
        if intake <= 0:
            return {"periods_to_exhaustion": -1, "risk": "NO_NET_GROWTH"}
        periods = max(0.0, round(headroom / intake, 1))
        return {
            "remaining_headroom": headroom,
            "net_periodic_intake": intake,
            "periods_to_exhaustion": periods,
            "exhaustion_risk": "IMMEDIATE" if periods < 2.0 else ("NEAR_TERM" if periods < 6.0 else "SUSTAINABLE")
        }

    def generate_pareto_distribution_summary(self, category_weights):
        """Evaluates 80/20 operational contribution distribution."""
        sorted_items = sorted(category_weights.items(), key=lambda x: float(x[1]), reverse=True)
        total_val = sum(float(v) for _, v in sorted_items)
        if total_val == 0:
            return {"pareto_items": [], "concentration_ratio": 0.0}

        running_sum = 0.0
        vital_few = []
        for cat, val in sorted_items:
            running_sum += float(val)
            pct = round((running_sum / total_val * 100), 2)
            vital_few.append({"category": cat, "weight": float(val), "cumulative_percentage": pct})
            if pct >= 80.0 and len(vital_few) >= 1:
                break

        return {
            "vital_few_categories": vital_few,
            "vital_few_count": len(vital_few),
            "total_categories": len(category_weights),
            "concentration_ratio": round((len(vital_few) / len(category_weights) * 100), 2) if category_weights else 0.0
        }

    def export_analytical_digest(self, domain_code, metric_records):
        """Compiles comprehensive multi-dimensional analytical report dictionary."""
        aggregates = self.compute_statistical_moments(metric_records)
        percentiles = self.calculate_percentiles(metric_records)
        iqr_data = self.calculate_interquartile_range(metric_records)
        histogram = self.generate_distribution_histogram(metric_records)

        return {
            "domain_code": domain_code,
            "institution_id": self.institution_id,
            "timestamp": timezone.now().isoformat(),
            "sample_metrics": aggregates,
            "percentile_distribution": percentiles,
            "dispersion_bounds": iqr_data,
            "frequency_histogram": histogram,
            "certified_valid": True,
        }
