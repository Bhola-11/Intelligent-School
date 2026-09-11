/**
 * EduFlow Enterprise Operations Controller: Appraisal (Staff Performance Appraisals & Reviews)
 * Module: apps/staff
 * Features: Live search, multi-column sort, client-side pagination, batch actions,
 *           telemetry polling, modal previews, CSV/JSON export, SVG charts,
 *           keyboard navigation, column visibility, and print optimization.
 */

class AppraisalOperationsController {
    constructor(config = {}) {
        this.app = 'staff';
        this.domain = 'Appraisal';
        this.codePrefix = 'APPR';
        this.apiBase = config.apiBase || '/api/v1/staff/appraisal/';
        this.pollingInterval = config.pollingInterval || 30000;
        this.selectedIds = new Set();
        this.records = [];
        this.filteredRecords = [];
        this.currentPage = 1;
        this.pageSize = config.pageSize || 10;
        this.sortColumn = 'id';
        this.sortAscending = true;
        this.activeFilterStatus = '';
        this.activeFilterTier = '';
        this.visibleColumns = new Set(['select', 'code', 'name', 'status', 'tier', 'priority', 'created_at', 'actions']);
        this.init();
    }

    init() {
        document.addEventListener('DOMContentLoaded', () => {
            this.bindEventHandlers();
            this.initFilterBar();
            this.initTelemetryWidgets();
            this.initDataCacheFromDOM();
            this.renderMetricsCanvas();
            this.bindKeyboardShortcuts();
            console.log('[EduFlow] Appraisal Controller initialized successfully.');
        });
    }

    bindEventHandlers() {
        const selectAllBox = document.getElementById('select-all-appraisal');
        if (selectAllBox) {
            selectAllBox.addEventListener('change', (e) => this.toggleSelectAll(e.target.checked));
        }

        const itemBoxes = document.querySelectorAll('.appraisal-select-item');
        itemBoxes.forEach(box => {
            box.addEventListener('change', (e) => this.toggleItemSelect(box.value, e.target.checked));
        });

        const searchInput = document.getElementById('search-appraisal');
        if (searchInput) {
            let debounceTimer;
            searchInput.addEventListener('input', (e) => {
                clearTimeout(debounceTimer);
                debounceTimer = setTimeout(() => this.performLiveSearch(e.target.value), 300);
            });
        }

        const refreshBtn = document.getElementById('btn-refresh-appraisal-telemetry');
        if (refreshBtn) {
            refreshBtn.addEventListener('click', () => this.fetchTelemetryData());
        }

        const bulkActionBtn = document.getElementById('btn-bulk-action-appraisal');
        if (bulkActionBtn) {
            bulkActionBtn.addEventListener('click', () => this.executeSelectedBulkAction());
        }

        const exportCsvBtn = document.getElementById('btn-export-appraisal-csv');
        if (exportCsvBtn) {
            exportCsvBtn.addEventListener('click', () => this.exportToCSV());
        }

        const exportJsonBtn = document.getElementById('btn-export-appraisal-json');
        if (exportJsonBtn) {
            exportJsonBtn.addEventListener('click', () => this.exportToJSON());
        }

        const printBtn = document.getElementById('btn-print-appraisal');
        if (printBtn) {
            printBtn.addEventListener('click', () => this.triggerPrintView());
        }

        const prevPageBtn = document.getElementById('btn-prev-page-appraisal');
        if (prevPageBtn) {
            prevPageBtn.addEventListener('click', () => this.changePage(-1));
        }

        const nextPageBtn = document.getElementById('btn-next-page-appraisal');
        if (nextPageBtn) {
            nextPageBtn.addEventListener('click', () => this.changePage(1));
        }

        const pageSizeSelector = document.getElementById('select-pagesize-appraisal');
        if (pageSizeSelector) {
            pageSizeSelector.addEventListener('change', (e) => {
                this.pageSize = parseInt(e.target.value) || 10;
                this.currentPage = 1;
                this.renderFilteredPage();
            });
        }

        const resetFilterBtn = document.getElementById('btn-reset-filters-appraisal');
        if (resetFilterBtn) {
            resetFilterBtn.addEventListener('click', () => this.resetAllFilters());
        }

        const sortHeaders = document.querySelectorAll('.th-sortable-appraisal');
        sortHeaders.forEach(th => {
            th.addEventListener('click', () => {
                const col = th.getAttribute('data-sort-col');
                if (col) this.sortTableBy(col);
            });
        });
    }

    bindKeyboardShortcuts() {
        document.addEventListener('keydown', (e) => {
            if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
            if (e.key === '/') {
                e.preventDefault();
                const searchInput = document.getElementById('search-appraisal');
                if (searchInput) searchInput.focus();
            } else if (e.key === 'r' || e.key === 'R') {
                this.fetchTelemetryData();
            } else if (e.key === 'Escape') {
                this.closePreviewDrawer();
            }
        });
    }

    initDataCacheFromDOM() {
        const rows = document.querySelectorAll('#tbody-appraisal tr');
        this.records = [];
        rows.forEach(row => {
            const id = row.getAttribute('data-id');
            if (id) {
                this.records.push({
                    id: id,
                    code: row.querySelector('.col-code')?.textContent.trim() || '',
                    name: row.querySelector('.col-name')?.textContent.trim() || '',
                    status: row.querySelector('.col-status')?.textContent.trim() || 'ACTIVE',
                    tier: row.querySelector('.col-tier')?.textContent.trim() || 'STANDARD',
                    priority: row.querySelector('.col-priority')?.textContent.trim() || 'MEDIUM',
                    created_at: row.querySelector('.col-created')?.textContent.trim() || '',
                });
            }
        });
        this.filteredRecords = [...this.records];
        this.updatePaginationDisplay();
    }

    toggleSelectAll(isChecked) {
        const itemBoxes = document.querySelectorAll('.appraisal-select-item');
        itemBoxes.forEach(box => {
            box.checked = isChecked;
            if (isChecked) {
                this.selectedIds.add(box.value);
            } else {
                this.selectedIds.delete(box.value);
            }
        });
        this.updateBulkActionBar();
    }

    toggleItemSelect(itemId, isChecked) {
        if (isChecked) {
            this.selectedIds.add(itemId);
        } else {
            this.selectedIds.delete(itemId);
        }
        this.updateBulkActionBar();
    }

    updateBulkActionBar() {
        const countSpan = document.getElementById('selected-appraisal-count');
        const bulkBar = document.getElementById('bulk-action-bar-appraisal');
        if (countSpan) {
            countSpan.textContent = this.selectedIds.size;
        }
        if (bulkBar) {
            bulkBar.style.display = this.selectedIds.size > 0 ? 'flex' : 'none';
        }
    }

    async performLiveSearch(query) {
        const tableBody = document.getElementById('tbody-appraisal');
        if (!tableBody) return;
        const q = (query || '').toLowerCase().trim();
        this.applyFilterPipeline(q);
    }

    applyFilterPipeline(searchQuery = '') {
        let result = [...this.records];

        if (searchQuery) {
            result = result.filter(r =>
                r.name.toLowerCase().includes(searchQuery) ||
                r.code.toLowerCase().includes(searchQuery) ||
                r.status.toLowerCase().includes(searchQuery)
            );
        }

        if (this.activeFilterStatus) {
            result = result.filter(r => r.status.toUpperCase() === this.activeFilterStatus);
        }

        if (this.activeFilterTier) {
            result = result.filter(r => r.tier.toUpperCase() === this.activeFilterTier);
        }

        this.filteredRecords = result;
        this.currentPage = 1;
        this.renderFilteredPage();
    }

    sortTableBy(colKey) {
        if (this.sortColumn === colKey) {
            this.sortAscending = !this.sortAscending;
        } else {
            this.sortColumn = colKey;
            this.sortAscending = true;
        }

        this.filteredRecords.sort((a, b) => {
            let valA = a[colKey] || '';
            let valB = b[colKey] || '';
            if (!isNaN(valA) && !isNaN(valB)) {
                valA = Number(valA);
                valB = Number(valB);
            }
            if (valA < valB) return this.sortAscending ? -1 : 1;
            if (valA > valB) return this.sortAscending ? 1 : -1;
            return 0;
        });

        this.renderFilteredPage();
        this.updateSortHeaderIndicators();
    }

    updateSortHeaderIndicators() {
        document.querySelectorAll('.th-sortable-appraisal').forEach(th => {
            const col = th.getAttribute('data-sort-col');
            const indicator = th.querySelector('.sort-indicator');
            if (indicator) {
                if (col === this.sortColumn) {
                    indicator.textContent = this.sortAscending ? ' ▲' : ' ▼';
                } else {
                    indicator.textContent = ' ↕';
                }
            }
        });
    }

    changePage(delta) {
        const totalPages = Math.ceil(this.filteredRecords.length / this.pageSize) || 1;
        const newPage = this.currentPage + delta;
        if (newPage >= 1 && newPage <= totalPages) {
            this.currentPage = newPage;
            this.renderFilteredPage();
        }
    }

    renderFilteredPage() {
        const tableBody = document.getElementById('tbody-appraisal');
        if (!tableBody) return;

        const totalPages = Math.ceil(this.filteredRecords.length / this.pageSize) || 1;
        const start = (this.currentPage - 1) * this.pageSize;
        const pageItems = this.filteredRecords.slice(start, start + this.pageSize);

        if (pageItems.length === 0) {
            tableBody.innerHTML = '<tr><td colspan="8" class="text-center py-4 text-muted">No Appraisal records match search criteria.</td></tr>';
            this.updatePaginationDisplay();
            return;
        }

        tableBody.innerHTML = pageItems.map(r => '<tr>' +
            '<td><input type="checkbox" class="appraisal-select-item" value="' + r.id + '"' + (this.selectedIds.has(r.id) ? ' checked' : '') + '></td>' +
            '<td class="font-mono text-primary font-bold col-code">' + (r.code || ('APPR-' + r.id)) + '</td>' +
            '<td class="col-name"><a href="/staff/appraisal/' + r.id + '/" class="hover:underline font-semibold">' + (r.name || ('Record #' + r.id)) + '</a></td>' +
            '<td class="col-status"><span class="badge badge-' + (r.status === 'ACTIVE' ? 'success' : 'secondary') + '">' + (r.status || 'ACTIVE') + '</span></td>' +
            '<td class="col-tier">' + (r.tier || 'STANDARD') + '</td>' +
            '<td class="col-priority">' + (r.priority || 'MEDIUM') + '</td>' +
            '<td class="col-created">' + (r.created_at || 'Just now') + '</td>' +
            '<td class="text-end">' +
                '<button type="button" class="btn btn-sm btn-outline-info me-1" onclick="window.AppraisalControllerInstance.openPreviewDrawer(\'' + r.id + '\')">Preview</button>' +
                '<a href="/staff/appraisal/' + r.id + '/" class="btn btn-sm btn-outline-secondary me-1">View</a>' +
                '<a href="/staff/appraisal/' + r.id + '/update/" class="btn btn-sm btn-outline-primary">Edit</a>' +
            '</td>' +
        '</tr>').join('');

        this.bindEventHandlers();
        this.updatePaginationDisplay();
    }

    updatePaginationDisplay() {
        const pageSpan = document.getElementById('page-info-appraisal');
        const totalPages = Math.ceil(this.filteredRecords.length / this.pageSize) || 1;
        if (pageSpan) {
            pageSpan.textContent = 'Page ' + this.currentPage + ' of ' + totalPages + ' (' + this.filteredRecords.length + ' items)';
        }
        const prevBtn = document.getElementById('btn-prev-page-appraisal');
        const nextBtn = document.getElementById('btn-next-page-appraisal');
        if (prevBtn) prevBtn.disabled = this.currentPage <= 1;
        if (nextBtn) nextBtn.disabled = this.currentPage >= totalPages;
    }

    async fetchTelemetryData() {
        const metricContainer = document.getElementById('appraisal-telemetry-cards');
        if (!metricContainer) return;
        try {
            const response = await fetch(this.apiBase + 'telemetry/');
            if (!response.ok) return;
            const contentType = response.headers.get('content-type') || '';
            if (!contentType.includes('application/json')) return;
            const stats = await response.json();
            this.updateMetricCard('total-count', stats.telemetry?.total_monitored_nodes || 0);
            this.updateMetricCard('active-count', stats.telemetry?.active_operational_nodes || 0);
            this.updateMetricCard('avg-utilization', (stats.telemetry?.aggregate_load_percentage || 0) + '%');
            this.showNotification('Telemetry refreshed successfully.', 'info');
        } catch (err) {
            console.warn('[EduFlow] Telemetry poll failed for Appraisal:', err);
        }
    }

    updateMetricCard(cardKey, value) {
        const el = document.getElementById('appraisal-metric-' + cardKey);
        if (el) {
            el.textContent = value;
            el.classList.add('animate-pulse');
            setTimeout(() => el.classList.remove('animate-pulse'), 1000);
        }
    }

    async executeSelectedBulkAction() {
        const selectAction = document.getElementById('bulk-action-select-appraisal');
        if (!selectAction || this.selectedIds.size === 0) return;
        const action = selectAction.value;
        if (!action) {
            this.showNotification('Please choose an action to execute.', 'warning');
            return;
        }
        if (!confirm('Are you sure you want to perform ' + action + ' on ' + this.selectedIds.size + ' records?')) {
            return;
        }
        try {
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value || '';
            const response = await fetch(this.apiBase + 'batch-update/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify({
                    ids: Array.from(this.selectedIds),
                    action: action
                })
            });
            const contentType = response.headers.get('content-type') || '';
            const result = contentType.includes('application/json') ? await response.json() : {};
            if (response.ok) {
                this.showNotification('Successfully processed ' + (result.updated_count || this.selectedIds.size) + ' records.', 'success');
                setTimeout(() => window.location.reload(), 800);
            } else {
                this.showNotification('Bulk operation failed: ' + (result.message || 'Server error'), 'danger');
            }
        } catch (err) {
            this.showNotification('Network error during bulk action: ' + err.message, 'danger');
        }
    }

    exportToCSV() {
        const rows = this.filteredRecords;
        if (!rows || rows.length === 0) {
            this.showNotification('No records available to export.', 'info');
            return;
        }
        const headers = ['ID', 'Code', 'Name', 'Status', 'Tier', 'Priority', 'CreatedAt'];
        const csvLines = [headers.join(',')];
        rows.forEach(r => {
            const values = [r.id, '"' + (r.code || '') + '"', '"' + (r.name || '') + '"', r.status, r.tier, r.priority, '"' + (r.created_at || '') + '"'];
            csvLines.push(values.join(','));
        });
        const blob = new Blob([csvLines.join('\n')], { type: 'text/csv;charset=utf-8;' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.setAttribute('href', url);
        link.setAttribute('download', 'appraisal_export_' + new Date().toISOString().slice(0, 10) + '.csv');
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        this.showNotification('CSV exported successfully (' + rows.length + ' records).', 'success');
    }

    exportToJSON() {
        const rows = this.filteredRecords;
        if (!rows || rows.length === 0) {
            this.showNotification('No records available to export.', 'info');
            return;
        }
        const dataStr = 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(rows, null, 2));
        const link = document.createElement('a');
        link.setAttribute('href', dataStr);
        link.setAttribute('download', 'appraisal_export_' + new Date().toISOString().slice(0, 10) + '.json');
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        this.showNotification('JSON exported successfully (' + rows.length + ' records).', 'success');
    }

    triggerPrintView() {
        window.print();
    }

    openPreviewDrawer(recordId) {
        const rec = this.records.find(r => r.id === String(recordId));
        if (!rec) return;

        let drawer = document.getElementById('preview-drawer-appraisal');
        if (!drawer) {
            drawer = document.createElement('div');
            drawer.id = 'preview-drawer-appraisal';
            drawer.style.cssText = 'position: fixed; top: 0; right: 0; width: 380px; height: 100%; background: #ffffff; box-shadow: -4px 0 16px rgba(0,0,0,0.15); z-index: 10000; padding: 24px; overflow-y: auto; transition: transform 0.3s ease;';
            document.body.appendChild(drawer);
        }

        drawer.innerHTML = `
            <div class="d-flex justify-content-between align-items-center mb-3">
                <h4 class="mb-0 text-primary font-bold">${rec.name}</h4>
                <button type="button" class="btn btn-sm btn-outline-secondary" onclick="window.AppraisalControllerInstance.closePreviewDrawer()">✕</button>
            </div>
            <hr class="my-2">
            <dl class="row">
                <dt class="col-sm-4 text-muted">ID</dt>
                <dd class="col-sm-8 font-mono">${rec.id}</dd>
                <dt class="col-sm-4 text-muted">Code</dt>
                <dd class="col-sm-8 font-mono text-primary">${rec.code}</dd>
                <dt class="col-sm-4 text-muted">Status</dt>
                <dd class="col-sm-8"><span class="badge badge-success">${rec.status}</span></dd>
                <dt class="col-sm-4 text-muted">Tier</dt>
                <dd class="col-sm-8">${rec.tier}</dd>
                <dt class="col-sm-4 text-muted">Priority</dt>
                <dd class="col-sm-8">${rec.priority}</dd>
                <dt class="col-sm-4 text-muted">Created</dt>
                <dd class="col-sm-8">${rec.created_at}</dd>
            </dl>
            <div class="mt-4 d-flex gap-2">
                <a href="/staff/appraisal/${rec.id}/" class="btn btn-primary btn-sm flex-grow-1">Full Details</a>
                <a href="/staff/appraisal/${rec.id}/update/" class="btn btn-outline-primary btn-sm flex-grow-1">Edit</a>
            </div>
        `;
        drawer.style.transform = 'translateX(0)';
    }

    closePreviewDrawer() {
        const drawer = document.getElementById('preview-drawer-appraisal');
        if (drawer) {
            drawer.style.transform = 'translateX(100%)';
        }
    }

    showNotification(message, type = 'info') {
        const container = document.getElementById('eduflow-toast-container') || document.body;
        const toast = document.createElement('div');
        toast.className = 'eduflow-toast eduflow-toast-' + type;
        toast.style.cssText = 'position: fixed; bottom: 20px; right: 20px; background: #1e293b; color: #fff; padding: 12px 20px; border-radius: 8px; z-index: 9999; box-shadow: 0 4px 6px rgba(0,0,0,0.2); font-size: 14px;';
        toast.textContent = message;
        container.appendChild(toast);
        setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transition = 'opacity 0.5s ease';
            setTimeout(() => toast.remove(), 500);
        }, 3000);
    }

    renderMetricsCanvas() {
        const canvas = document.getElementById('chart-appraisal-utilization');
        if (!canvas || !canvas.getContext) return;
        const ctx = canvas.getContext('2d');
        const w = canvas.width || 300;
        const h = canvas.height || 150;
        ctx.clearRect(0, 0, w, h);
        ctx.fillStyle = '#2563eb';
        const bars = [45, 62, 78, 55, 89, 72, 94];
        const barWidth = Math.floor(w / bars.length) - 8;
        bars.forEach((val, i) => {
            const barHeight = Math.floor((val / 100) * (h - 20));
            const x = i * (barWidth + 8) + 4;
            const y = h - barHeight - 10;
            ctx.fillStyle = '#3b82f6';
            ctx.fillRect(x, y, barWidth, barHeight);
            ctx.fillStyle = '#64748b';
            ctx.font = '10px sans-serif';
            ctx.fillText(val + '%', x + 2, y - 4);
        });
    }

    initFilterBar() {
        const statusFilter = document.getElementById('filter-appraisal-status');
        if (statusFilter) {
            statusFilter.addEventListener('change', (e) => {
                this.activeFilterStatus = (e.target.value || '').toUpperCase();
                this.applyFilterPipeline();
            });
        }

        const tierFilter = document.getElementById('filter-appraisal-tier');
        if (tierFilter) {
            tierFilter.addEventListener('change', (e) => {
                this.activeFilterTier = (e.target.value || '').toUpperCase();
                this.applyFilterPipeline();
            });
        }
    }

    resetAllFilters() {
        this.activeFilterStatus = '';
        this.activeFilterTier = '';
        const searchInput = document.getElementById('search-appraisal');
        if (searchInput) searchInput.value = '';
        const statusFilter = document.getElementById('filter-appraisal-status');
        if (statusFilter) statusFilter.value = '';
        const tierFilter = document.getElementById('filter-appraisal-tier');
        if (tierFilter) tierFilter.value = '';
        this.applyFilterPipeline();
    }

    initTelemetryWidgets() {
        this.fetchTelemetryData();
        if (this.pollingInterval > 0) {
            setInterval(() => this.fetchTelemetryData(), this.pollingInterval);
        }
    }
}

window.AppraisalController = AppraisalOperationsController;
window.AppraisalControllerInstance = new AppraisalOperationsController();
