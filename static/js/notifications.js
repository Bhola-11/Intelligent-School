/**
 * EduFlow Enterprise - Realtime Notification Feed & Toast Dispatcher
 */
class EduFlowNotificationHub {
    static pollInterval = 30000;

    static init() {
        if (!document.getElementById('notification-bell')) return;
        setInterval(() => this.fetchUnreadCount(), this.pollInterval);
    }

    static async fetchUnreadCount() {
        try {
            const resp = await fetch('/notifications/api/unread-count/');
            if (resp.ok) {
                const data = await resp.json();
                const badge = document.getElementById('notification-badge');
                if (badge) {
                    badge.textContent = data.unread_count > 0 ? data.unread_count : '';
                    badge.style.display = data.unread_count > 0 ? 'inline-block' : 'none';
                }
            }
        } catch (e) {
            console.debug('Notification poll throttled:', e);
        }
    }
}
document.addEventListener('DOMContentLoaded', () => EduFlowNotificationHub.init());
