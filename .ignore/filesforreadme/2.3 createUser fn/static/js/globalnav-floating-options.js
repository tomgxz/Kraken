document.getElementById("globalnav-hamburger").addEventListener("click",()=>{
    document.getElementById("globalnav-hamburger").classList.toggle('is-active');
    document.querySelectorAll(".globalnav-floating-options").forEach((e)=>{e.classList.toggle("is-active")});
    document.querySelectorAll(".globalnav-floating-options-backdrop").forEach((e)=>{e.classList.toggle("is-active")});
});

document.querySelectorAll(".globalnav-floating-options-backdrop").forEach((e)=>{
    e.addEventListener("click",()=>{
        document.getElementById("globalnav-hamburger").classList.remove('is-active');
        document.querySelectorAll(".globalnav-floating-options").forEach((e)=>{e.classList.remove("is-active")});
        document.querySelectorAll(".globalnav-floating-options-backdrop").forEach((e)=>{e.classList.remove("is-active")});
    })
});
