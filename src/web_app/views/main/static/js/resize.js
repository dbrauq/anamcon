window.addEventListener("load", function(){
    const anamnesisContentZoneRight = document.getElementById("anamnesis_content_zone_right");
    if (window.innerWidth < 1250){
        anamnesisContentZoneRight.classList.add("hide_right");
    }
});
window.addEventListener("resize", function(){
    const anamnesisContentZoneRight = document.getElementById("anamnesis_content_zone_right");
    if (window.innerWidth < 1250){
        anamnesisContentZoneRight.classList.add("hide_right");
    } else{
        anamnesisContentZoneRight.classList.remove("hide_right");
    }
});
