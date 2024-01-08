document.addEventListener("DOMContentLoaded", async function(){
    const username = document.getElementById("username");
    const password = document.getElementById("password");
    const password_confirmation = document.getElementById("password_confirmation");
    const email = document.getElementById("email");
    const email_confirmation = document.getElementById("email_confirmation");
    const username_error_text_box = document.getElementById("username_error_text_box");
    const password_error_text_box = document.getElementById("password_error_text_box");
    const email_error_text_box = document.getElementById("email_error_text_box");
    const terms = document.getElementById("terms");
    const check_username = document.getElementById("check_username");

    const mandatory_fields_errors = document.getElementById("mandatory_fields_errors");
    mandatory_fields_errors.classList.add("display");
    const mandatory_input_errors = document.getElementById("mandatory_input_errors");
    const accept_terms_error = document.getElementById("accept_terms_error");
    accept_terms_error.classList.add("display");

    const register_button = document.getElementById("register_button");
    const register_form = document.getElementById("register_form");

    const observerConfig ={attributes:true, attributeFilter:["class"]};

    let all_mandatory = false;
    let username_error = false;
    let password_error = false;
    let email_error = false;
    let terms_error = true

    function manage_all_items(){
        manage_mandatory_fields_text();
        manage_errors_field_text();
        manage_register_button();
    }

    function manage_register_button(){
        if((all_mandatory) && (!username_error) && (!password_error) && (!email_error) && (!terms_error)){
            register_button.classList.remove("disabled");
        }
        else{
            register_button.classList.add("disabled")
        }
    }

    function manage_mandatory_fields_text(){
        if((username.value.length>0) && (password.value.length>0) && (password_confirmation.value.length>0) &&
        (email.value.length>0) && (email_confirmation.value.length>0)){
            mandatory_fields_errors.classList.remove("display");
            all_mandatory = true;
        }
        else{
            mandatory_fields_errors.classList.add("display");
            all_mandatory = false;
        }
    }

    function manage_errors_field_text(){
        if(!username_error && !password_error && !email_error){
            mandatory_input_errors.classList.remove("display");
        }
        else{
            mandatory_input_errors.classList.add("display");
        }
    }

    const observer_user_error = new MutationObserver(function(mutations){
        mutations.forEach(function(mutation){
            if (mutation.target.classList.contains("display")){
                username_error = true;
                manage_all_items();
            }
            else if(!mutation.target.classList.contains("display")){
                username_error = false;
                manage_all_items();
            }
        });
    });
    const observer_pass_error = new MutationObserver(function(mutations){
        mutations.forEach(function(mutation){
            if (mutation.target.classList.contains("display")){
                password_error = true;
                manage_all_items();
            }
            else if(!mutation.target.classList.contains("display")){
                password_error = false;
                manage_all_items();
            }
        });
    });
    const observer_email_error = new MutationObserver(function(mutations){
        mutations.forEach(function(mutation){
            if (mutation.target.classList.contains("display")){
                email_error = true;
                manage_all_items();
            }
            else if(!mutation.target.classList.contains("display")){
                email_error = false;
                manage_all_items();
            }
        });
    });
    observer_user_error.observe(username_error_text_box, observerConfig);
    observer_pass_error.observe(password_error_text_box, observerConfig);
    observer_email_error.observe(email_error_text_box, observerConfig);


    username.addEventListener("input", async ()=>{
        manage_all_items();
    });
    password.addEventListener("input", async ()=>{
        manage_all_items();
    });
    password_confirmation.addEventListener("input", async ()=>{
        manage_all_items();
    });
    email.addEventListener("input", async ()=>{
        manage_all_items();
    });
    email_confirmation.addEventListener("input", async ()=>{
        manage_all_items();
    });

    terms.addEventListener("change", function(){
        if (terms.checked){
            terms_error = false;
            accept_terms_error.classList.remove("display")
            manage_register_button();
        }
        else{
            terms_error = true;
            accept_terms_error.classList.add("display")
            manage_register_button();
        }
    });

    async function available_username(username_value){
        const request_username_validation = {
            method:"POST",
            headers:{
                "Content-Type":"application/json",
            },
            body: JSON.stringify({
                username:username_value
            })
        }
        try{
            const response = await fetch("/register/available_username", request_username_validation);
            const response_data = await response.json()
            return response_data
        }
        catch(error){
            console.error(error)
        }
    }

    register_button.addEventListener("click", async function(event){
        event.preventDefault();
        const response = await available_username(await username.value);
        const valid_username = response["available"];
        if (!valid_username){
            check_username.click();
            manage_all_items();
        }
        else{
            register_form.submit();
        }
    });
});