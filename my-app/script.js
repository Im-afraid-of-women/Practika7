const input = document.getElementById("taskInput");
const button = document.getElementById("addTaskBtn");
const list = document.getElementById("taskList");

button.addEventListener("click", () => {
    const text = input.value.trim();

    if (text === "") {
        return;}

    const li = document.createElement("li");
    li.textContent = text;

    li.addEventListener("click", () => {
        li.classList.toggle("completed");
    });

    li.addEventListener("dblclick", () => {
        li.remove();
    });

    list.appendChild(li);
    input.value = "";
});