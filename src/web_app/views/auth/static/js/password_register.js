document.addEventListener("DOMContentLoaded", async function() {
    const username = document.getElementById("username");
    const password = document.getElementById("password");
    const password_confirmation = document.getElementById("password_confirmation");
    password_confirmation.disabled = true;
    password_confirmation.style.pointerEvents = "none"
    const password_error_text = document.getElementById("password_error_text");
    const password_error_text_box = document.getElementById("password_error_text_box")
    const password_base_error_text = await get_password_error_text();

    async function get_password_error_text(){
        try{
            const response = await fetch("/register/get_password_error_text")
            const response_data = await response.json()
            return response_data
        }
        catch(error){
            console.error(error)
        }
    }

    function contains_all_required(pass){
        const upper_letters = "abcdefghijklmnopqrstuvwxyz";
        const lower_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        const numbers = "0123456789"
        let has_upper = false;
        let has_lower = false;
        let has_number = false;
        for (let i=0; i<pass.length; i++) {
            char = pass[i]
            if (upper_letters.includes(char)) has_upper = true;
            else if (lower_letters.includes(char)) has_lower = true;
            else if (numbers.includes(char)) has_number = true;
        }
        if (has_upper && has_lower && has_number) return true;
        return false;
    }

    password.addEventListener("input", ()=>{
        if(password.value.length==0){
            password_confirmation.value="";
            password_error_text_box.classList.remove("display");
            password.classList.remove("invalid_input");
            password_confirmation.classList.remove("invalid_input");
            password_confirmation.disabled = true;
            password_confirmation.style.pointerEvents = "none"
        }
        else if((password.value.length<8) || (password.value.length>60) || 
                (!contains_all_required(password.value))){
            password_confirmation.value="";
            password_error_text_box.classList.add("display");
            password_error_text.textContent = password_base_error_text["error_text"]
                                                ["password_error_text_invalid"];
            password.classList.add("invalid_input");
            password_confirmation.classList.remove("invalid_input");
            password_confirmation.disabled = true;
            password_confirmation.style.pointerEvents = "none"
        }
        else{
            password_confirmation.value="";
            password.classList.remove("invalid_input");
            password_confirmation.classList.remove("invalid_input");
            password_error_text_box.classList.remove("display");
            password_confirmation.disabled = false;
            password_confirmation.style.pointerEvents = "auto"
        }
        
    });
    password_confirmation.addEventListener("input", ()=>{
        if(password_confirmation.value.length==0){
            password_confirmation.value="";
            password.classList.remove("invalid_input");
            password_confirmation.classList.remove("invalid_input");
            password_error_text_box.classList.remove("display");
            password_confirmation.disabled = false;
            password_confirmation.style.pointerEvents = "auto"
        }
        else if((password_confirmation.value.length>0) && (password.value != password_confirmation.value)){
            password_error_text_box.classList.add("display");
            password_error_text.textContent = password_base_error_text["error_text"]
                                                ["password_error_text_not_equal"];
            password.classList.add("invalid_input");
            password_confirmation.classList.add("invalid_input");
        }
        else{
            password_error_text_box.classList.remove("display");
            password.classList.remove("invalid_input");
            password_confirmation.classList.remove("invalid_input");
            password_error_text_box.classList.remove("display");
            password_confirmation.disabled = false;
            password_confirmation.style.pointerEvents = "auto"
        }
    });
});