// Highlight completed tasks
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("td[data-status]").forEach(cell => {
        const status = cell.dataset.status;

        if (status === "Completed") {
            cell.classList.add("status", "completed");
        } else if (status === "Pending") {
            cell.classList.add("status", "pending");
        } else {
            cell.classList.add("status", "progress");
        }
    });
});

// Confirm before adding task
function confirmAdd() {
    return confirm("Are you sure you want to add this task?");
}