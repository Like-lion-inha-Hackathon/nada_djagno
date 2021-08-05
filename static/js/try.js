var plus = document.querySelector(".plus")
plus.addEventListener("click",function(e){
    var menu = document.querySelector(".menu")
    var icon = document.querySelector(".icon")
    if (menu.style.display===""){
        menu.style.display="block"
        icon.classList.remove("fa-plus")
        icon.classList.add("fa-times")
    } else{
        menu.style.display=""
        icon.classList.add("fa-plus")
        icon.classList.remove("fa-times")
    }
})