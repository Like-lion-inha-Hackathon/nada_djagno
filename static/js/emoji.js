var pluss = document.querySelectorAll(".fa-smile")
var menu = document.querySelector(".menu")
var icon = document.querySelector(".icon")
var emoji=document.querySelector(".emoji")

pluss.forEach(function(plus){
    plus.addEventListener("click",function(e){
        if (menu.style.display===""){
            menu.style.display="block"
            icon.classList.remove("far")
            icon.classList.remove("fa-smile")
            icon.classList.add("fas")
            icon.classList.add("fa-times") 
        } 
        else{
            menu.style.display=""
            icon.classList.add("fa-smile")
            icon.classList.remove("fa-times")
        }
    })
    
    
})

var emoji_blue= document.querySelector(".emoji--like")
var emoji_red=document.querySelector(".emoji--love")
var emoji_yellow=document.querySelector(".emoji--wow")

emoji_blue.addEventListener("click",function(e){
    var emojy = document.querySelector(".emojy")
    emojy.appendChild(e.target)
    icon.classList.remove("fas")
    icon.classList.remove("fa-times") 
    menu.style.display=""
    // emoji_blue.classList.add("emoji--like")
})



emoji_red.addEventListener("click",function(e){
    
})

emoji_yellow.addEventListener("click",function(e){
    
})