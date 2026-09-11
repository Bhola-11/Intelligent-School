/**
 * EduFlow Enterprise - Interactive Timetable Matrix Grid & Conflict Highlighter
 */
class EduFlowTimetableGrid {
    constructor(gridSelector) {
        this.container = document.querySelector(gridSelector);
        if (!this.container) return;
        this.initDragDrop();
    }

    initDragDrop() {
        const slots = this.container.querySelectorAll('.timetable-cell');
        slots.forEach(slot => {
            slot.addEventListener('dragover', (e) => e.preventDefault());
            slot.addEventListener('drop', (e) => this.handleSlotDrop(e, slot));
        });
    }

    handleSlotDrop(event, slot) {
        event.preventDefault();
        const periodId = event.dataTransfer.getData('text/plain');
        if (periodId) {
            slot.classList.add('bg-primary-subtle');
            console.info(`Assigned period ${periodId} to slot ${slot.dataset.slotId}`);
        }
    }
}
