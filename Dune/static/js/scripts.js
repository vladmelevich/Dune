document.querySelectorAll(".button_status1").forEach(el => {
    el.addEventListener("click", function() {
        document.getElementById("add-modal-block-blogers").classList.add("open")
    })
}
)

document.getElementById("open-add-blogers").addEventListener("click", function() {
    document.getElementById("add-modal-block-blogers").classList.add("open")
})
//5
document.getElementById("close-add-blogers").addEventListener("click", function() {
    document.getElementById("add-modal-block-blogers").classList.remove("open")
})

//4

document.getElementById("commit-add-blogers").addEventListener("click", function() {
    document.getElementById("add-modal-block-blogers").classList.remove("open")
})

//3

document.addEventListener('keydown', (e) => {
    if(e.key === "Escape") {
        document.getElementById("add-modal-block-blogers").classList.remove("open")
    }
})

//2
document.querySelector("modal_add .modal-box").addEventListener('click', event => {
    event._isClickWithInModal = true
})