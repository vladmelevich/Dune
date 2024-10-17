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


function open_motion1() {
    document.querySelectorAll(".motion1").forEach(el => {
        el.classList.add("open")
    });

}

function close_motion1() {
    document.querySelectorAll(".motion1").forEach(el => {
        el.classList.remove("open")
    });

}

function open_motion2() {
    document.querySelectorAll(".motion2").forEach(el => {
        el.classList.add("open")
    });

}

function close_motion2() {
    document.querySelectorAll(".motion2").forEach(el => {
        el.classList.remove("open")
    });

}

function open_motion3() {
    document.querySelectorAll(".motion3").forEach(el => {
        el.classList.add("open")
    });

}

function close_motion3() {
    document.querySelectorAll(".motion3").forEach(el => {
        el.classList.remove("open")
    });

}


function open_error() {
    document.querySelectorAll(".error").forEach(el => {
        el.classList.add("open")
    });

}


function delete_error() {
    document.querySelectorAll(".error").forEach(el => {
        el.classList.remove("open")
    });

}