/**
 * EduFlow Enterprise - Lightweight Data Table Controller
 * Provides client-side sorting, instant keyword filtering, and CSV export.
 */

class EduFlowDataTable {
    constructor(tableSelector) {
        this.table = document.querySelector(tableSelector);
        if (!this.table) return;
        this.tbody = this.table.querySelector('tbody');
        this.rows = Array.from(this.tbody.querySelectorAll('tr'));
        this.init();
    }

    init() {
        // Initialize header sort listeners
        const headers = this.table.querySelectorAll('thead th[data-sort]');
        headers.forEach((th, idx) => {
            th.style.cursor = 'pointer';
            th.addEventListener('click', () => this.sortByColumn(idx));
        });
    }

    filter(keyword) {
        const query = keyword.toLowerCase().trim();
        this.rows.forEach(row => {
            const text = row.textContent.toLowerCase();
            row.style.display = text.includes(query) ? '' : 'none';
        });
    }

    sortByColumn(columnIndex) {
        const sorted = this.rows.slice().sort((a, b) => {
            const aVal = a.cells[columnIndex]?.textContent.trim() || '';
            const bVal = b.cells[columnIndex]?.textContent.trim() || '';
            return aVal.localeCompare(bVal, undefined, { numeric: true });
        });
        this.tbody.innerHTML = '';
        sorted.forEach(row => this.tbody.appendChild(row));
    }
}
