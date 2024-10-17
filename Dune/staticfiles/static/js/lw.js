//5
document.getElementById("close-addings").addEventListener("click", function() {
    document.getElementById("add-modal-block_of_blogers").classList.remove("open")
})

//3

document.addEventListener('keydown', (e) => {
    if(e.key === "Escape") {
        document.getElementById("add-modal-block_of_blogers").classList.remove("open")
    }
})

document.getElementById("add-application").addEventListener("click", function() {
    document.getElementById("add-modal-block_of_blogers").classList.add("open")
})

document.getElementById("commit-adding").addEventListener("click", function() {
    document.getElementById("add-modal-block_of_blogers").classList.remove("open")
})