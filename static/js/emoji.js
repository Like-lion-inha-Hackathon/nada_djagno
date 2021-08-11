var emojys = document.querySelectorAll(".emojy")
var menus = document.querySelectorAll(".menu")
emojys.forEach(function(emoji){
    emoji.addEventListener("click",function(e){
        var menu = emoji.nextElementSibling
        if (menu.style.display===""){
            menu.style.display="block"
        }else if (emoji.children[0].classList[0]==="emoji"){
            console.log("zz")

        }
        else{
            menu.style.display=""
        }
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
})