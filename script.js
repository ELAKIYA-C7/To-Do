function addTask() {
    const input = document.getElementById('taskInput');
    const task = input.value.trim();

    if (task === '') {
        alert('Please enter a task');
        return;
    }

    const li = document.createElement('li');
    li.textContent = task;

    // Click on a task to remove it
    li.onclick = function() {
        this.remove();
    };

    document.getElementById('taskList').appendChild(li);

    input.value = ''; // clear input
}