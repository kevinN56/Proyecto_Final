window.addEventListener("scroll",()=>{

const navbar=document.querySelector(".navbar");

if(window.scrollY>80){

navbar.classList.add("shadow");

}

else{

navbar.classList.remove("shadow");

}

});