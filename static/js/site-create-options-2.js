var textOptions = document.querySelectorAll(".new-site-form.three .text-option");

textOptions.forEach((e)=>{
    e.addEventListener("click",()=>{
        textOptions.forEach((f)=>{
            f.classList.remove("active")
            f.querySelector(".text-option-list").name="new_site_font_face_list_inactive"
        });
        e.classList.add("active")
        e.querySelector(".text-option-list").name="new_site_font_face_list_active"
    });
});
