/**
 * EduFlow Enterprise - Canvas Chart Rendering Utility
 * Renders SVG and Canvas bar charts, donut charts, and progress graphs.
 */

class EduFlowChart {
    static renderBarChart(canvasId, labels, values, color = '#2563eb') {
        const canvas = document.getElementById(canvasId);
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const maxVal = Math.max(...values, 100);
        const barWidth = (canvas.width / values.length) * 0.7;
        const gap = (canvas.width / values.length) * 0.3;

        ctx.clearRect(0, 0, canvas.width, canvas.height);

        values.forEach((val, i) => {
            const x = i * (barWidth + gap) + gap / 2;
            const barHeight = (val / maxVal) * (canvas.height - 40);
            const y = canvas.height - barHeight - 20;

            ctx.fillStyle = color;
            ctx.fillRect(x, y, barWidth, barHeight);

            ctx.fillStyle = '#64748b';
            ctx.font = '11px sans-serif';
            ctx.textAlign = 'center';
            ctx.fillText(labels[i] || '', x + barWidth / 2, canvas.height - 5);
        });
    }
}
