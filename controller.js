// bola hua  text siri wave pe display hoon sake
$(document).ready(function () {
    eel.expose(displayMessage)
function displayMessage(message){
    console.log("[Siri Message]", message);
    $(".siri-message li:first").text(message);
    $(".siri-message").textillate('start');
}


 // siri wave se wapas input box waale frontend aane ke liye 
 eel.expose(ShowHood)
function ShowHood (){
    $("#oval").attr("hidden",false)
     $("#siri-message").attr("hidden",true)
     return null;

}
eel.expose(senderText)
    function senderText(message) {
        var chatBox = document.getElementById("chat-canvas-body"); // chat canvas ki body ko access kr rahe hai 
        if (message.trim() !== "") { 
            // eska mtlb hai ki agar  message empty nhi hoga toh hum chatbox mein jo pehle se html se thi uske saath yeah jo mention kri hai html usse add krdenge 
            chatBox.innerHTML += `<div class="row justify-content-end mb-4"> 
            <div class = "width-size">
            <div class="sender_message">${message}</div>
        </div>`; // hum jo bolenge wooh text mein display hoon jayega 
    
            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;
        }
        return null;
    }

    eel.expose(receiverText) // yeah wooh hai jo response hmra jarvis dega 
    function receiverText(message) {

        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `<div class="row justify-content-start mb-4">
            <div class = "width-size">
            <div class="receiver_message">${message}</div>
            </div>
        </div>`; 
    
            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight; 
        }
        return null;
        
    }
    // face authenication animation 
   // Hide Loader and display Face Auth animation
    eel.expose(hideLoader)
    function hideLoader() {

        $("#Loader").attr("hidden", true); //  hide loader ka kaam yeah animation ko hide krega
        $("#FaceAuth").attr("hidden", false); // face auth hide nhi hoga  aur yeha hum backend se call krenge (main.py) se

    }
    // Hide Face auth and display Face Auth success animation
    eel.expose(hideFaceAuth)
    function hideFaceAuth() {

        $("#FaceAuth").attr("hidden", true); // jab face authenication hoon jayega toh success wala dekhega
        $("#FaceAuthSuccess").attr("hidden", false);

    }
    // Hide success and display 
    eel.expose(hideFaceAuthSuccess)
    function hideFaceAuthSuccess() {

        $("#FaceAuthSuccess").attr("hidden", true);
        $("#HelloGreet").attr("hidden", false);

    }


    // Hide Start Page and display blob
    eel.expose(hideStart)
    function hideStart() {

        $("#Start").attr("hidden", true);

        setTimeout(function () {
            $("#oval").addClass("animate__animated animate__zoomIn");

        }, 1000)
        setTimeout(function () {
            $("#oval").attr("hidden", false);
        }, 1000)
    }
 


 });






