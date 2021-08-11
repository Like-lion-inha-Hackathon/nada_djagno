<<<<<<< Updated upstream
var emojys = document.querySelectorAll(".emojy")
var menus = document.querySelectorAll(".menu")
emojys.forEach(function(emoji){
    emoji.addEventListener("click",function(e){
        var menu = emoji.nextElementSibling
=======
var pluss = document.querySelectorAll(".fa-smile")
var menu = document.querySelectorAll(".menu")
var icon = document.querySelector(".icon")
var emoji=document.querySelector(".emoji")

pluss.forEach(function(plus){
    plus.addEventListener("click",function(e){
>>>>>>> Stashed changes
        if (menu.style.display===""){
            menu.style.display="block"
        }else if (emoji.children[0].classList[0]==="emoji"){
            console.log("zz")

        }
        else{
            menu.style.display=""
        }
<<<<<<< Updated upstream
        var like = menu.children[0].children[0]
        like.addEventListener("click",function(e){
            emoji.removeChild(emoji.children[0])
            emoji.appendChild(like)
            menu.style.display=""
            console.log("like")
            
        })
        var love = menu.children[1].children[0]
        love.addEventListener("click",function(e){
            emoji.removeChild(emoji.children[0])
            emoji.appendChild(love)
            menu.style.display=""
            console.log("love")
            
        })
        var wow = menu.children[2].children[0]
        wow.addEventListener("click",function(e){
            emoji.removeChild(emoji.children[0])
            emoji.appendChild(wow)
            menu.style.display=""
            console.log("wow")

        })
        console.log(emoji)
    })
=======
    })
    
    
})

var emoji_blue= document.querySelector(".emoji--like")
var emoji_red=document.querySelector(".emoji--love")
var emoji_yellow=document.querySelector(".emoji--wow")

emoji_blue.addEventListener("click",function(e){
    menu.style.display=""
    var emojy = document.querySelector(".emojy")
    emojy.appendChildz(e.target)
    icon.classList.remove("fas")
    icon.classList.remove("fa-times") 
    // emoji_blue.classList.add("emoji--like")
})



emoji_red.addEventListener("click",function(e){
    menu.style.display=""
    var emojy = document.querySelector(".emojy")
    console.log(e.target)
    emojy.appendChild(e.target)
    icon.classList.remove("fas")
    icon.classList.remove("fa-times") 
})

emoji_yellow.addEventListener("click",function(e){
    menu.style.display=""
    var emojy = document.querySelector(".emojy")
    emojy.appendChild(e.target)
    icon.classList.remove("fas")
    icon.classList.remove("fa-times") 
>>>>>>> Stashed changes
})