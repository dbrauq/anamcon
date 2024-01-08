document.addEventListener("DOMContentLoaded", async function() {
    const username = document.getElementById("username");
    const password = document.getElementById("password");
    const login_button = document.getElementById("login_button");
    const login_form = document.getElementById("login_form");
    const login_error_text_box = document.getElementById("login_error_text_box");

    async function log_in(username_value, password_value){
        const request_log_in = {
            method:"POST",
            headers:{
                "Content-Type":"application/json",
            },
            body: JSON.stringify({
                username:username_value,
                password:password_value
            })
        }
        try{
            const response = await fetch("/login/process", request_log_in);
            const response_data = await response.json()
            return response_data
        }
        catch(error){
            console.error(error)
        }
    }

    username.addEventListener("input", async()=>{
        login_error_text_box.classList.remove("display")
    });

    password.addEventListener("input", async()=>{
        login_error_text_box.classList.remove("display")
    });

    login_button.addEventListener("click", async function(event){
        event.preventDefault();
        if(username.value.length < 5 || password.value.length < 8){
            login_error_text_box.classList.add("display")
        }
        else{
            const response = await log_in(username.value, password.value)
            valid_credentials = response["valid_credentials"]
            if(valid_credentials){
                login_error_text_box.classList.remove("display")
                window.location.href = "/anamnesis";
            }
            else{
                login_error_text_box.classList.add("display")
            }
        }
    });
});
