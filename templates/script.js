const input = document.getElementById("searchInput");
const btn = document.getElementById("submitBtn");
const box = document.querySelector(".box");

btn.style.display = "none";

input.addEventListener("input", () => {
    if (input.value.trim() !== "") {
        btn.style.display = "inline-block";
        box.classList.add("open");   // keep open
    } else {
        btn.style.display = "none";
        box.classList.remove("open"); // collapse again only when empty
    }
});
