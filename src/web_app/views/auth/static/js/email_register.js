document.addEventListener("DOMContentLoaded", async function() {
    const email = document.getElementById("email");
    const email_confirmation = document.getElementById("email_confirmation");
    email_confirmation.disabled = true;
    email_confirmation.style.pointerEvents = "none";
    const email_error_text_box = document.getElementById("email_error_text_box");
    const email_error_text = document.getElementById("email_error_text");
    const email_base_error_text = await get_email_error_text();
    const extra_text_error = document.getElementById("extra_text_error");

    async function get_email_error_text(){
        try{
            const response = await fetch("/register/get_email_error_text");
            const response_data = await response.json();
            return response_data;
        }
        catch(error){
            console.error(error)
        }
    }

    function is_valid_email(em){
        const a_index = em.indexOf('@');
        const dot_after_a_index = em.indexOf('.', a_index);
        const last_dot_index = em.lastIndexOf('.');
        if (a_index>0 && dot_after_a_index>a_index+1 && last_dot_index<em.length-1) {
            return true;    
        }
        return false
    }

    email.addEventListener("input", ()=>{
        if(email.value.length==0){
            email_confirmation.value=""
            email_confirmation.classList.remove("invalid_input");     
            email_confirmation.disabled = true;
            email_confirmation.style.pointerEvents = "none";
            email_error_text_box.classList.remove("display");
            email.classList.remove("invalid_input");     
        }
        else if (is_valid_email(email.value)){
            email_confirmation.value=""
            email_confirmation.classList.remove("invalid_input");     
            email_confirmation.disabled = false;
            email_confirmation.style.pointerEvents = "auto"
            email_error_text_box.classList.remove("display");
            email.classList.remove("invalid_input");                
        }
        else{
            email_confirmation.value=""
            email_confirmation.classList.remove("invalid_input");     
            email_confirmation.disabled = true;
            email_confirmation.style.pointerEvents = "none";
            email_error_text.textContent = email_base_error_text["error_text"]
                                                ["email_error_pattern"];
            email_error_text_box.classList.add("display");
            email.classList.add("invalid_input");
                 
        }
    });

    email_confirmation.addEventListener("input", ()=>{
        if(email_confirmation.value.length==0){
            email.classList.remove("invalid_input");     
            email_error_text_box.classList.remove("display");
            email_confirmation.classList.remove("invalid_input");
        }
        else if(email.value == email_confirmation.value){
            email_error_text_box.classList.remove("display");
            email.classList.remove("invalid_input");
            email_confirmation.classList.remove("invalid_input");
        }
        else{
            email_error_text.textContent = email_base_error_text["error_text"]
                                            ["email_error_not_equal"];
            email_error_text_box.classList.add("display");
            email.classList.add("invalid_input");
            email_confirmation.classList.add("invalid_input");
        } 
    });
});