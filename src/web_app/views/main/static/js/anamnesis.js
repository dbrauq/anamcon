document.addEventListener("DOMContentLoaded", async function () {
    await validate_active_session();
    //setInterval(await validate_active_session, 5000);
    const anamnesis_title = document.getElementById("title_input");
    let current_anamnesis_status;
    var anamnesis_title_to_change = true;
    const anamnesis_texts = await get_anamnesis_navigation_texts();
    const delete_confirm_text = anamnesis_texts["delete_confirm_text"];
    const no_navigation_icon_text = anamnesis_texts["no_navigation_icon_text"];
    const no_navigation_main_text = anamnesis_texts["no_navigation_main_text"];

    const no_anamnesis_icon_text = anamnesis_texts["no_anamnesis_icon_text"];
    const no_anamnesis_main_text = anamnesis_texts["no_anamnesis_main_text"];
    const no_dialog_main_text = anamnesis_texts["no_dialog_main_text"];

    const start_anamnesis_text_1 = anamnesis_texts["start_anamnesis_text_1"];
    const start_anamnesis_text_2 = anamnesis_texts["start_anamnesis_text_2"];
    const start_anamnesis_text_3_1 = anamnesis_texts["start_anamnesis_text_3_1"];
    const start_anamnesis_text_3_2 = anamnesis_texts["start_anamnesis_text_3_2"];
    const start_anamnesis_text_4 = anamnesis_texts["start_anamnesis_text_4"];
    const start_anamnesis_text_5_1 = anamnesis_texts["start_anamnesis_text_5_1"];
    const start_anamnesis_text_5_2 = anamnesis_texts["start_anamnesis_text_5_2"];
    const start_anamnesis_text_6 = anamnesis_texts["start_anamnesis_text_6"];
    const start_anamnesis_text_7 = anamnesis_texts["start_anamnesis_text_7"];
    const start_anamnesis_text_8 = anamnesis_texts["start_anamnesis_text_8"];
    const start_anamnesis_text_9 = anamnesis_texts["start_anamnesis_text_9"];

    const summary_title_text_1 = anamnesis_texts["summary_title_text_1"];
    const summary_title_text_2 = anamnesis_texts["summary_title_text_2"];
    const summary_title_text_3 = anamnesis_texts["summary_title_text_3"];
    const summary_data_type_text = anamnesis_texts["summary_data_type_text"];
    const summary_data_state_text = anamnesis_texts["summary_data_state_text"];
    const summary_data__duration_text = anamnesis_texts["summary_data__duration_text"];
    const summary_data_creation_datetime_text = anamnesis_texts["summary_data_creation_datetime_text"];
    const summary_data_last_interaction_datetime_text = anamnesis_texts["summary_data_last_interaction_datetime_text"];
    const summary_data_num_interactions_text = anamnesis_texts["summary_data_num_interactions_text"];

    const available_anamnesis = await get_available_anamnesis();
    const available_anamnesis_modes = available_anamnesis["available_anamnesis_modes"];
    const available_anamnesis_modes_icons = available_anamnesis["available_anamnesis_modes_icons"]
    const available_anamnesis_status = { "created": "🆕", "recording": "▶️", "paused": "⏸️", "completed": "✅", "error": "❌" }
    const anamnesis_modes = {};
    for (let i = 0; i < available_anamnesis_modes.length; i++) {
        const mode = available_anamnesis_modes[i];
        const icon = available_anamnesis_modes_icons[i];
        anamnesis_modes[mode] = icon;
    }
    const mode_elements = {};
    available_anamnesis_modes.forEach(mode => {
        const mode_element_id = "anamnesis_type_pack_" + mode;
        const mode_element = document.getElementById(mode_element_id);
        mode_elements[mode] = mode_element;
    });
    const navigation_anamnesis_box = document.getElementById("content_box_main_left")
    let anamnesis_box_elements = {};
    let delete_anamnesis_box_elements = {};
    let all_navigation_anamnesis;
    let active_anamnesis_timestamp;
    const content_box_main_conversation = document.getElementById("content_box_main_conversation")
    const content_box_main_summary = document.getElementById("content_box_main_right")
    let selected_anamnesis = false;
    await get_active_anamnesis();
    await set_navigation_box_content();
    let anamnesis_dialog_data;
    const audio_off_button = document.getElementById("audio_off_button");
    const audio_on_button = document.getElementById("audio_on_button");
    let audio_on = true;
    const main_message_input = document.getElementById("main_message_input");
    const send_text_button = document.getElementById("send_text_button");
    const send_audio_button = document.getElementById("send_audio_button");
    let recording_audio = false;
    let media_recorder;
    let recorded_audio_data = [];
    let recorded_audio_data_blob = new Blob();
    const download_report_button = document.getElementById("download_report_button");
    await set_anamnesis_dialog_content();

    async function get_anamnesis_navigation_texts() {
        try {
            const response = await fetch("/anamnesis/navigation_texts");
            const response_data = await response.json();
            return response_data;
        }
        catch (error) {
            console.error(error);
        }
    }

    async function get_active_anamnesis() {
        try {
            const response = await fetch("/anamnesis/get_active_anamnesis");
            const response_data = await response.json();
            active_anamnesis_timestamp = response_data["active_anamnesis"];
            return response_data;
        }
        catch (error) {
            console.error(error);
        }
    }

    async function validate_active_session() {
        try {
            const response = await fetch("/anamnesis/active_session");
            const response_data = await response.json();
            active = response_data["active_session"];
            if (!active) {
                window.location.href = "/login";
            }
        }
        catch (error) {
            console.error(error);
        }
    }

    async function get_available_anamnesis() {
        try {
            const response = await fetch("/anamnesis/get_available_anamnesis");
            const response_data = await response.json();
            return response_data;
        }
        catch (error) {
            console.error(error);
        }
    }

    async function get_all_navigation_anamnesis() {
        try {
            const response = await fetch("/anamnesis/get_all_navigation_anamnesis");
            const response_data = await response.json();
            return response_data["navigation_anamnesis"];
        }
        catch (error) {
            console.error(error);
        }
    }

    async function new_anamnesis(anamnesis_mode) {
        const request_log_in = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                anamnesis_mode: anamnesis_mode
            })
        }
        try {
            const response = await fetch("/anamnesis/new_anamnesis", request_log_in);
            const response_data = await response.json()
            return response_data
        }
        catch (error) {
            console.error(error)
        }
    }

    async function delete_anamnesis(anamnesis_timestamp) {
        const request_log_in = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                anamnesis_timestamp: anamnesis_timestamp
            })
        }
        try {
            const response = await fetch("/anamnesis/delete_anamnesis", request_log_in);
            const response_data = await response.json()
            return response_data
        }
        catch (error) {
            console.error(error)
        }
    }

    async function set_active_anamnesis(anamnesis_timestamp, anamnesis_mode) {
        active_anamnesis_timestamp = anamnesis_timestamp;
        const request_log_in = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                anamnesis_timestamp: anamnesis_timestamp,
                anamnesis_mode: anamnesis_mode
            })
        }
        try {
            const response = await fetch("/anamnesis/set_active_anamnesis", request_log_in);
            const response_data = await response.json()
            return response_data
        }
        catch (error) {
            console.error(error)
        }
    }

    async function set_navigation_box_content(new_content = false) {
        let anamnesis_box_html_content = "";
        all_navigation_anamnesis = await get_all_navigation_anamnesis()
        if (all_navigation_anamnesis != null) {
            for (const anamnesis_item in all_navigation_anamnesis) {
                active_class_text = ""
                if (new_content || active_anamnesis_timestamp == null) {
                    await set_active_anamnesis(all_navigation_anamnesis[anamnesis_item]["creation_timestamp"],
                        all_navigation_anamnesis[anamnesis_item]["anamnesis_mode"])
                    new_content = false;
                }
                if (active_anamnesis_timestamp == all_navigation_anamnesis[anamnesis_item]["creation_timestamp"]) {
                    if (anamnesis_title_to_change) {
                        anamnesis_title.value = all_navigation_anamnesis[anamnesis_item]["title"]
                    }
                    active_class_text = "active_box"
                    selected_anamnesis = true;
                    navigation_anamnesis_box.classList.add("selected_anamnesis")
                }
                let short_title = all_navigation_anamnesis[anamnesis_item]["title"];
                if (short_title.length > 12) {
                    short_title = short_title.substring(0, 11) + ".."
                }
                anamnesis_box_html_content = anamnesis_box_html_content +
                    '<div class="anamnesis_navigator_box '
                    + active_class_text +
                    '" id="nav_box_'
                    + all_navigation_anamnesis[anamnesis_item]["creation_timestamp"] +
                    '">\
                                <div class="anamnesis_navigator_box_left_type">\
                                    <p class="anamnesis_navigation_text_left_type">'
                    + anamnesis_modes[all_navigation_anamnesis[anamnesis_item]["anamnesis_mode"]] +
                    '</p>\
                                </div>\
                                <div class="anamnesis_navigator_box_left_status">\
                                    <p class="anamnesis_navigation_text_right">'
                    + available_anamnesis_status[all_navigation_anamnesis[anamnesis_item]["status"]] +
                    '</p>\
                                </div>\
                                <div class="anamnesis_navigator_box_center">\
                                    <p class="anamnesis_navigation_text_center">'
                    + all_navigation_anamnesis[anamnesis_item]["creation_date"] +
                    '<br>'
                    + short_title +
                    '</p>\
                                </div>\
                                <div class="anamnesis_navigator_box_right_delete" id="delete_nav_box_'
                    + all_navigation_anamnesis[anamnesis_item]["creation_timestamp"] +
                    '">\
                                    <p class="anamnesis_navigation_text_right">\
                                        🗑️\
                                    </p>\
                                </div>\
                            </div>';
            }
            navigation_anamnesis_box.innerHTML = anamnesis_box_html_content;
            all_navigation_anamnesis.forEach(element => {
                const box_element_id = "nav_box_" + element["creation_timestamp"];
                const box_element = document.getElementById(box_element_id);
                anamnesis_box_elements[element["creation_timestamp"]] = box_element;
                box_element.addEventListener("click", async () => {
                    anamnesis_title_to_change = true;
                    await set_active_anamnesis(element["creation_timestamp"],
                        element["anamnesis_mode"]);
                    await set_navigation_box_content();
                    await set_anamnesis_dialog_content();
                });
                const delete_box_element_id = "delete_nav_box_" + element["creation_timestamp"];
                const delete_box_element = document.getElementById(delete_box_element_id);
                delete_anamnesis_box_elements[element["creation_timestamp"]] = delete_box_element;
                delete_box_element.addEventListener("click", async (event) => {
                    event.stopPropagation()
                    var confirm = window.confirm(delete_confirm_text);
                    if (confirm) {
                        await delete_anamnesis(element["creation_timestamp"]);
                        active_anamnesis_timestamp = null
                        selected_anamnesis = false;
                        await set_navigation_box_content();
                        await set_anamnesis_dialog_content()
                    }
                });
            });
        }
        else {
            navigation_anamnesis_box.classList.remove("selected_anamnesis")
            navigation_anamnesis_box.innerHTML = '\
            <div class="no_navitator_content">\
                <p id="no_navigator_content_icon">'
                + no_navigation_icon_text +
                '</p>\
                <p id="no_navigator_content_text">'
                + no_navigation_main_text +
                '</p>\
            </div>';
        }
    }

    async function set_anamnesis_dialog_content() {
        dialogs = await get_dialogs()
        anamnesis_dialog_data = await get_anamnesis_data()
        await set_anamnesis_summary_content()
        content_box_main_conversation.innerHTML = "";
        let dialog_html_content = "";
        if (dialogs.length > 0) {
            for (dialog_num in dialogs) {
                let query_text = dialogs[dialog_num]["query_text"];
                let user_text = query_text
                let query_interpreted_text = dialogs[dialog_num]["query_interpreted_text"];
                if ((query_text.length == 0) && (query_interpreted_text.length > 0)) {
                    user_text = query_interpreted_text;
                    query_text = user_text;
                }
                response_text = dialogs[dialog_num]["response_text"];
                if ((query_text.length > 0) || (query_interpreted_text > 0)) {
                    dialog_html_content = dialog_html_content +
                        '<div class="dialog_frame_user_dialog">\
                            <div class="dialog_frame_content_user_dialog">\
                                <div class="dialog_frame_content_icon_user_dialog">\
                                    <img class="system_icon" src="/anamnesis/mini_user">\
                                </div>\
                                <div class="dialog_frame_content_text_user_dialog">\
                                    <p class="dialot_text">'
                        + user_text +
                        '</p>\
                                </div>\
                            </div>\
                        </div>'
                }
                if (response_text.length > 0) {
                    dialog_html_content = dialog_html_content +
                        '<div class="dialog_frame_server_dialog">\
                            <div class="dialog_frame_content_server_dialog">\
                                <div class="dialog_frame_content_icon_server_dialog">\
                                    <img class="system_icon" src="/anamnesis/mini_system">\
                                </div>\
                                <div class="dialog_frame_content_text_server_dialog">\
                                    <p class="dialot_text">'
                        + response_text +
                        '</p>\
                                </div>\
                            </div>\
                        </div>'
                }
                content_box_main_conversation.innerHTML = dialog_html_content;
                content_box_main_conversation.scrollTop = content_box_main_conversation.scrollHeight;

            }
            if (anamnesis_dialog_data
                && (anamnesis_dialog_data.status == "completed" || anamnesis_dialog_data.status == "error")) {
                disable_dialog_input()
            }
            else{
                enable_dialog_input()
            }
            anamnesis_title.classList.remove("disabled");
        }
        else {
            error_text = no_dialog_main_text;
            if (!selected_anamnesis) {
                disable_dialog_input()
                anamnesis_title.classList.add("disabled");
                anamnesis_title.value = "";
                error_text = no_anamnesis_main_text;
                dialog_html_content = dialog_html_content + '\
                <div class="no_anamnesis_content">\
                    <p id="no_anamnesis_content_icon">'
                    + no_anamnesis_icon_text +
                    '</p>\
                    <p id="no_anamnesis_content_text">'
                    + error_text +
                    '</p>\
                </div>';
                content_box_main_conversation.innerHTML = dialog_html_content;
            }
            else {
                disable_dialog_input()
                anamnesis_title.classList.add("disabled");
                anamnesis_title.value = "";
                dialog_html_content = dialog_html_content + '\
            <div class="no_active_anamnesis">\
                <p id="start_anamnesis_content_text">\
                    <p class="start_anamnesis_text"><b>[⚠]&nbsp'+ start_anamnesis_text_1 + '</b></p>\
                    <p class="start_anamnesis_text"></p>\
                    <p class="start_anamnesis_text"></p>\
                    <p class="start_anamnesis_text">'+ start_anamnesis_text_2 + '</p>\
                    <p class="start_anamnesis_text">&nbsp-&nbsp'+ start_anamnesis_text_3_1 + '&nbsp <b>' + start_anamnesis_text_3_2 + '</b></p>\
                    <p class="start_anamnesis_text">&nbsp-&nbsp'+ start_anamnesis_text_4 + '</p>\
                    <p class="start_anamnesis_text">&nbsp-&nbsp'+ start_anamnesis_text_5_1 + '&nbsp<b>' + start_anamnesis_text_5_2 + '</b></p>\
                    <p class="start_anamnesis_text">&nbsp-&nbsp'+ start_anamnesis_text_6 + '</p>\
                    <p class="start_anamnesis_text">&nbsp-&nbsp'+ start_anamnesis_text_7 + '</p>\
                    <p class="start_anamnesis_text">&nbsp-&nbsp'+ start_anamnesis_text_8 + '</p>\
                    <p class="start_anamnesis_text"></p>\
                    <p class="start_anamnesis_text"></p>\
                    <p class="start_anamnesis_text"></p>\
                    <p class="start_anamnesis_text"><b>'+ start_anamnesis_text_9 + '</b></p>\
                </p>\
                <p id="start_anamnesis_content_button">\
                    <button class="primary_button" id="anamnesis_activation_button"><b>'
                    + " [ ▸ ] &nbsp&nbsp Iniciar Anamnesis" +
                    '</b></button>\
                </p>\
            </div>';
                content_box_main_conversation.innerHTML = dialog_html_content;
                const anamnesis_activation_button = document.getElementById("anamnesis_activation_button");
                anamnesis_activation_button.addEventListener("click", async function () {
                    await start_anamnesis();
                    main_message_input.value = "$__intro";
                    dialog_html_content = '<img src="/anamnesis/loading_icon" alt="loading_icon">';
                    content_box_main_conversation.innerHTML = dialog_html_content;
                    send_text_button.click();
                    await set_navigation_box_content()
                });
            }
        }
    }

    async function set_anamnesis_summary_content() {
        if(anamnesis_dialog_data.status != "completed"){
            download_report_button.classList.add("disabled"); 
        }
        else{
            download_report_button.classList.remove("disabled"); 
        }
        let symptoms = anamnesis_dialog_data.symptoms;
        let symptom_titles = [];
        let symptom_regions = [];
        let summary_html_content =
        '<div class="anamnesis_summary_box" id="human_body_zone">\
            <div class="anamnesis_summary_box_text_title">\
                <p id="summary_text_title">'
                    +summary_title_text_1+
                '</p>\
            </div>\
            <div id="body_icon_ima_box">\
                <img src="/anamnesis/body_icon" id="body_ima">\
            </div>\
        </div>\
        <div class="anamnesis_summary_box" id="symptom_zone">\
            <div class="anamnesis_summary_box_text_title">\
                <p id="summary_text_title">'
                    +summary_title_text_2+
                '</p>\
            </div>\
            <div class="symptoms_zone">'
        if (symptoms && symptoms.length>0){
            for (var i=0; i<symptoms.length; i++) {
                let symptom_name = Object.keys(symptoms[i])
                let symptom_title = symptoms[i][symptom_name]["title"];
                let symptom_region = symptoms[i][symptom_name]["region"];
                if(!symptom_titles.includes(symptom_title)){
                    symptom_titles.push(symptom_title)
                }
                if(!symptom_regions.includes(symptom_region)){
                    symptom_regions.push(symptom_region)
                  }
                }
                for(symptom_num in symptom_titles){
                    summary_html_content += 
                '<div class="symptom_text_box">\
                    <p class="symptom_text">'
                        +symptom_titles[symptom_num]+
                    '</p>\
                </div>'
            }
        }
        else{
                summary_html_content += 
                '<p id="no_symptom_content_text">'
                    + "Ningún síntoma" + 
                '</p>'
        }        
        summary_html_content += '\
            </div>\
        </div>\
        <div class="anamnesis_summary_box" id="anamnesis_data_zone">\
            <div class="anamnesis_summary_box_text_title">\
                <p id="summary_text_title">'
                    +summary_title_text_3+
                '</p>\
            </div>\
            <div class="anamnesis_data_zone">'
        if (anamnesis_dialog_data.status && anamnesis_dialog_data.status != "created"){
            summary_html_content += 
            '<div class="anamnesis_data_box">\
                    <p class="anamnesis_data_text">'
                        +"<b>- "+summary_data_type_text+"</b>"+":\
                         "+anamnesis_dialog_data.anamnesis_mode+
                    '</p>\
                    <p class="anamnesis_data_text">'
                        +"<b>- "+summary_data_state_text+"</b>"+":\
                         "+anamnesis_dialog_data.status+
                    '</p>\
                    <p class="anamnesis_data_text">'
                        +"<b>- "+summary_data__duration_text+"</b>"+":\
                         "+anamnesis_dialog_data.duration_seconds+
                    '</p>\
                    <p class="anamnesis_data_text">'
                        +"<b>- "+summary_data_creation_datetime_text+"</b>"+":\
                         "+anamnesis_dialog_data.creation_datetime+
                    '</p>\
                    <p class="anamnesis_data_text">'
                        +"<b>- "+summary_data_last_interaction_datetime_text+"</b>"+":\
                         "+anamnesis_dialog_data.last_interaction_datetime+
                    '</p>\
                    <p class="anamnesis_data_text">'
                        +"<b>- "+summary_data_num_interactions_text+"</b>"+":\
                         "+anamnesis_dialog_data.number_interactions+
                    '</p>\
            </div>'
        }
        else{
            summary_html_content += 
                '<p id="no_summary_data_content_text">'
                    + "Datos no disponibles" + 
                '</p>'
        }
            summary_html_content += '\
            </div>\
        </div>';
        content_box_main_summary.innerHTML = summary_html_content;
        if(symptom_regions.length >0){
            const image = document.getElementById("body_ima");
            console.log(symptom_regions)
            marker_zones={"general":[25,0,150,245],
                          "abdominal":[71,79,110,115],
                          "torácica":[68,41,112,77],
                          "craneal":[78,3,101,32],
                          "cervical":[82,34,99,39],
                          "eess":[[49,41,66,150],[114,41,132,150]],
                          "eeii":[[67,117,88,242],[92,117,113,242]],
                         }
            symptom_regions.forEach(function(region, index){
                if(region == "general"){
                    add_body_marker_general(marker_zones[region][0],
                                            marker_zones[region][1],
                                            marker_zones[region][2],
                                            marker_zones[region][3]);
                }
                else if(region == "eess" || region == "eeii"){
                    add_body_marker_local(marker_zones[region][0][0],
                                            marker_zones[region][0][1],
                                            marker_zones[region][0][2],
                                            marker_zones[region][0][3]);
                    add_body_marker_local(marker_zones[region][1][0],
                                            marker_zones[region][1][1],
                                            marker_zones[region][1][2],
                                            marker_zones[region][1][3]);
                }
                else{
                    add_body_marker_local(marker_zones[region][0],
                                          marker_zones[region][1],
                                          marker_zones[region][2],
                                          marker_zones[region][3]);
                }
            });
        }
    }

    async function add_body_marker_general(start_x, start_y, end_x, end_y){
        let anatomical_zone = document.createElement("div");
        anatomical_zone.className = "anatomical_zone_general";
        anatomical_zone.style.left = (start_x) + "px";
        anatomical_zone.style.top = (start_y) + "px";
        anatomical_zone.style.width = (end_x - start_x) + "px";
        anatomical_zone.style.height = (end_y - start_y) + "px";
        anatomical_zone.style.position = "absolute"
        document.getElementById("body_icon_ima_box").appendChild(anatomical_zone)
    }
    async function add_body_marker_local(start_x, start_y, end_x, end_y){
        let anatomical_zone = document.createElement("div");
        anatomical_zone.className = "anatomical_zone_local";
        anatomical_zone.style.left = (start_x) + "px";
        anatomical_zone.style.top = (start_y) + "px";
        anatomical_zone.style.width = (end_x - start_x) + "px";
        anatomical_zone.style.height = (end_y - start_y) + "px";
        anatomical_zone.style.position = "absolute"
        document.getElementById("body_icon_ima_box").appendChild(anatomical_zone)
    }


    for (const mode in mode_elements) {
        mode_elements[mode].addEventListener("click", async function (event) {
            const result = await new_anamnesis(mode);
            await set_navigation_box_content(new_content = true);
            await set_anamnesis_dialog_content();
        });
    }
    
    anamnesis_title.addEventListener("input", async function () {
        await set_navigation_box_content()
    });

    const observerConfig = { attributes: true, attributeFilter: ["class"] };
    const observe_active_anamnesis = new MutationObserver(function (mutations) {
        mutations.forEach(async function (mutation) {
            if (mutation.target.classList.contains("selected_anamnesis")) {
                active_anamnesis_timestamp = await get_active_anamnesis()
                anamnesis_dialog_data = get_anamnesis_data()
            }
            else if (!mutation.target.classList.contains("selected_anamnesis")) {
            }
        });
    });
    observe_active_anamnesis.observe(navigation_anamnesis_box, observerConfig);

    async function get_active_anamnesis() {
        try {
            const response = await fetch("/anamnesis/get_active_anamnesis");
            const response_data = await response.json();
            active_anamnesis_timestamp = response_data["active_anamnesis"]
            return active_anamnesis_timestamp;
        }
        catch (error) {
            console.error(error);
        }
    }

    async function get_anamnesis_data() {
        try {
            const response = await fetch("/anamnesis/get_anamnesis_data");
            const response_data = await response.json();
            anamnesis_dialog_data = response_data["anamnesis_dialog_data"]
            return anamnesis_dialog_data;
        }
        catch (error) {
            console.error(error);
        }
    }
    async function start_anamnesis() {
        const request_log_in = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                anamnesis_timestamp: active_anamnesis_timestamp,
            })
        }
        try {
            const response = await fetch("/anamnesis/start_anamnesis", request_log_in);
            const response_data = await response.json()
            return response_data
        }
        catch (error) {
            console.error(error)
        }
    }
    async function complete_anamnesis() {
        const request_log_in = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                anamnesis_timestamp: active_anamnesis_timestamp,
            })
        }
        try {
            const response = await fetch("/anamnesis/complete_anamnesis", request_log_in);
            const response_data = await response.json()
            return response_data
        }
        catch (error) {
            console.error(error)
        }
    }

    async function set_anamnesis_title(title) {
        const request_log_in = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                anamnesis_timestamp: active_anamnesis_timestamp,
                anamnesis_title: title
            })
        }
        try {
            const response = await fetch("/anamnesis/update_anamnesis_title", request_log_in);
            const response_data = await response.json()
            return response_data
        }
        catch (error) {
            console.error(error)
        }
    }

    async function send_dialog_text(text) {
        const request_log_in = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                anamnesis_timestamp: active_anamnesis_timestamp,
                text: text
            })
        }
        try {
            const response = await fetch("/anamnesis/send_dialog_text", request_log_in);
            const response_data = await response.json()
            return response_data
        }
        catch (error) {
            console.error(error)
        }
    }

    async function send_dialog_audio(audio_blob) {
        const audio_array_buffer = await audio_blob.arrayBuffer();
        const audio_data = new Uint8Array(audio_array_buffer);
        const request_dialog_audio = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                anamnesis_timestamp: active_anamnesis_timestamp,
                audio: audio_data
            })
        }
        try {
            const response = await fetch("/anamnesis/send_dialog_audio", request_dialog_audio);
            const response_data = await response.json()
            return response_data
        }
        catch (error) {
            console.error(error)
        }
    }
    async function get_dialogs() {
        const request_dialogs = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                anamnesis_timestamp: active_anamnesis_timestamp,
            })
        }
        try {
            const response = await fetch("/anamnesis/get_dialog_texts", request_dialogs);
            const response_data = await response.json()
            return response_data["anamnesis_texts"]
        }
        catch (error) {
            console.error(error)
        }
    }

    async function download_report() {
        const request_report = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                anamnesis_timestamp: active_anamnesis_timestamp,
            })
        }
        try {
            const response = await fetch("/anamnesis/download_report", request_report);
            const response_blob = await response.blob();
            window.open(window.URL.createObjectURL(response_blob), '_blank');
        }
        catch (error) {
            console.error(error)
        }
    }

    audio_off_button.addEventListener("click", async function () {
        audio_off_button.classList.add("active_audio_mode");
        audio_on_button.classList.remove("active_audio_mode");
        audio_on = false;
    });

    audio_on_button.addEventListener("click", async function () {
        audio_on_button.classList.add("active_audio_mode");
        audio_off_button.classList.remove("active_audio_mode");
        audio_on = true;
    });

    anamnesis_title.addEventListener("input", async function () {
        anamnesis_title_to_change = false;
        await set_anamnesis_title(anamnesis_title.value);
        await set_navigation_box_content();
    });

    main_message_input.addEventListener("keydown", async function (event) {
        if (main_message_input.classList.contains("disabled")) {
            event.preventDefault()
        }
        else if (event.key == "Enter") {
            send_text_button.click();
        }
    });

    function disable_dialog_input() {
        send_text_button.classList.add("disabled");
        send_audio_button.classList.add("disabled");
        main_message_input.value = "";
        main_message_input.classList.add("disabled");
    }
    function enable_dialog_input() {
        send_text_button.classList.remove("disabled");
        send_audio_button.classList.remove("disabled");
        main_message_input.classList.remove("disabled");
    }

    send_text_button.addEventListener("click", async function () {
        let text = main_message_input.value;
        disable_dialog_input()
        if (text.length > 0) {
            main_message_input.value = "";
            disable_dialog_input()
            let response = await send_dialog_text(text);
            await set_anamnesis_dialog_content()
            var audio = new Audio("/anamnesis/last_audio_response/" + response["interaction_id"]);
            if (audio_on) {
                await audio.play();
            }
            await get_anamnesis_data();
            if (anamnesis_dialog_data &&
                anamnesis_dialog_data.status == "recording"
                && anamnesis_dialog_data.dialog.complete_intent == true) {
                if (anamnesis_dialog_data.dialog.interaction_meaning == "symptom") {
                    while (!audio.paused) {
                        await delay(1)
                    }
                    main_message_input.value = "$__continue";
                    send_text_button.click();
                }
                else if (anamnesis_dialog_data.dialog.interaction_meaning == "review") {
                    while (!audio.paused) {
                        await delay(1)
                    }
                    main_message_input.value = "$__end";
                    send_text_button.click();
                    await complete_anamnesis()
                    await set_navigation_box_content()
                }
                await get_anamnesis_data();
            }
            if (anamnesis_dialog_data &&
                anamnesis_dialog_data.status == "recording"
                && anamnesis_dialog_data.dialog.new_intent == true
                && anamnesis_dialog_data.dialog.interaction_meaning == "review") {
                while (!audio.paused) {
                    await delay(50)
                }
                main_message_input.value = "$__yes";
                send_text_button.click();
                await get_anamnesis_data();
            }
            if (anamnesis_dialog_data.status == "completed"
                && anamnesis_dialog_data.status == "error") {
                disable_dialog_input()
                await get_anamnesis_data();
                return
            }
            while (!audio.paused) {
                await delay(50)
            }
            if (anamnesis_dialog_data.status != "completed"){
                enable_dialog_input()
            }
        }

    });

    send_audio_button.addEventListener("click", async function () {
        disable_dialog_input()
        if (recording_audio == false) {
            console.log("click1")
            send_audio_button.classList.add("active_micro")
            main_message_input.setAttribute("placeholder", "[⏺] Grabando... Termina pulsando nuevamente el microfono");
            send_text_button.classList.add("disabled");
            main_message_input.classList.add("disabled");
            recording_audio = true;
            navigator.mediaDevices
                .getUserMedia({ audio: true })
                .then((stream) => {
                    media_recorder = new MediaRecorder(stream);
                    media_recorder.ondataavailable = (event) => {
                        if (event.data.size > 0) {
                            recorded_audio_data.push(event.data)
                        }
                    };
                    media_recorder.start()
                });
        }
        else {
            console.log("click2")
            await delay(200);
            let time = 0;
            const time_out = 50;
            send_audio_button.classList.remove("active_micro")
            send_text_button.classList.remove("disabled");
            main_message_input.classList.remove("disabled");
            main_message_input.setAttribute("placeholder", "Escribe aquí tu mensaje");
            recording_audio = false;
            await media_recorder.stop();
            while (recorded_audio_data_blob.size < 1 && time < time_out) {
                await delay(1);
                recorded_audio_data_blob = new Blob(recorded_audio_data, { type: 'audio/wav' });
                time++;
            }
            if ((time < time_out) && (recorded_audio_data_blob.size > 0)) {
                let response = await send_dialog_audio(recorded_audio_data_blob)
                await set_anamnesis_dialog_content()
                var audio = new Audio("/anamnesis/last_audio_response/" + response["interaction_id"]);
                if (audio_on) {
                    audio.play();
                }
            }
            recorded_audio_data = [];
            recorded_audio_data_blob = new Blob();
        }
        await get_anamnesis_data();
        if (anamnesis_dialog_data &&
            anamnesis_dialog_data.status == "recording"
            && anamnesis_dialog_data.dialog.complete_intent == true) {
            if (anamnesis_dialog_data.dialog.interaction_meaning == "symptom") {
                while (!audio.paused) {
                    await delay(1)
                }
                main_message_input.value = "$__continue";
                send_text_button.click();
            }
            else if (anamnesis_dialog_data.dialog.interaction_meaning == "review") {
                while (!audio.paused) {
                    await delay(1)
                }
                main_message_input.value = "$__end";
                send_text_button.click();
                await complete_anamnesis()
                await set_navigation_box_content()
            }
            await get_anamnesis_data();
        }
        if (anamnesis_dialog_data &&
            anamnesis_dialog_data.status == "recording"
            && anamnesis_dialog_data.dialog.new_intent == true
            && anamnesis_dialog_data.dialog.interaction_meaning == "review") {
            while (!audio.paused) {
                await delay(50)
            }
            main_message_input.value = "$__yes";
            send_text_button.click();
            await get_anamnesis_data();
        }
        if (anamnesis_dialog_data.status == "completed"
            && anamnesis_dialog_data.status == "error") {
            disable_dialog_input()
            await get_anamnesis_data();
            return
        }
        if (anamnesis_dialog_data.status != "completed"){
            enable_dialog_input()
        }
    });

    async function delay(ms) {
        await new Promise(function (wait) {
            setTimeout(wait, ms)
        });
    }

    download_report_button.addEventListener("click", async function(){
        return download_report()
    })
});

