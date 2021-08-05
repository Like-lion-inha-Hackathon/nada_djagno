

console.log("aaaa")
var heart = document.querySelector(".heartclick")
heart.addEventListener("click",function(e){
    e.preventDefault();
    heart.classList.toggle("hearttored")
})
