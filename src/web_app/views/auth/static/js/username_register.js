document.addEventListener("DOMContentLoaded", async function() {
    const username = document.getElementById("username");
    const check_username = document.getElementById("check_username");
    const username_error_text_box = document.getElementById("username_error_text_box");
    const username_error_text = document.getElementById("username_error_text");
    const username_base_error_text = await get_username_error_text()
    const check_username_base_text = check_username.textContent;
    const forbidden_username_chars = 
    ["$", "#", "@", "(", ")", "\"","\'",",",";",":","=",
    "¿","?","!","¡","+","-","<",">","*","/","\\","|"," "];

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
    async function get_username_error_text(){
        try{
            const response = await fetch("/register/get_username_error_text")
            const response_data = await response.json()
            return response_data
        }
        catch(error){
            console.error(error)
        }
    }

    function contains_forbiden_characters(){
        username_test = username.value
        for (let i=0; i<forbidden_username_chars.length; i++){
            if (username_test.includes(forbidden_username_chars[i])){
                return true;
            }
        }
        return false;
    }

    username.addEventListener("input", async()=>{
        if(username.value.length==0){
            check_username.classList.add("disabled");
            check_username.classList.remove("valid_username");
            check_username.classList.remove("invalid_username");
            check_username.textContent=check_username_base_text
            username_error_text_box.classList.remove("display");
            username.classList.remove("invalid_input");
        }
        else if((username.value.length<5) || (username.value.length>30) 
            || contains_forbiden_characters()){
            check_username.classList.add("disabled");
            check_username.classList.remove("valid_username");
            check_username.classList.remove("invalid_username");
            check_username.textContent=check_username_base_text
            username_error_text.textContent = username_base_error_text["error_text"]
            username_error_text_box.classList.add("display");
            username.classList.add("invalid_input");
        }
        else{
            check_username.classList.remove("disabled");
            check_username.classList.remove("valid_username");
            check_username.classList.remove("invalid_username");
            check_username.textContent=check_username_base_text
            username_error_text_box.classList.remove("display");
            username.classList.remove("invalid_input");
        }
    })

    check_username.addEventListener("click", async()=>{
        const response = await available_username(username.value);
        check_username.textContent = response["available_button_text"]
        username_error_text.textContent = response["error_text"]
        if (response["available"]==true){
            check_username.classList.add("valid_username");
            check_username.classList.add("disabled");
            username_error_text_box.classList.remove("display");
            username.classList.remove("invalid_input");
        }
        else{
            check_username.classList.add("disabled");
            check_username.classList.add("invalid_username");
            username_error_text_box.classList.add("display");
            username.classList.add("invalid_input");

        }
    });
});