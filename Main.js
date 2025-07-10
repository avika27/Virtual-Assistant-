// input box mein ke jo upar message hai ( ask me anything) usmein animate laane ke liye 
$(function () {
  eel.init()() // yeah init  func backend se aa rha hai esliye ()  doo baar lage hai 
  $('.text').textillate({
    loop: true,
    minDisplayTime: 2000, // Time before out effect starts
    in: {
      effect: 'bounceIn',
      delayScale: 1.5,
      delay: 50,
      sync: true
    },
    out: {
      effect: 'bounceOut',
      delayScale: 1.5,
      delay: 50,
      sync: true
    }
  });
});

// siri configuration
var siriWave = new SiriWave({
  container: document.getElementById("siri-container"),
  width: 1000,
  height: 750,
  style: "ios9",
  amplitude: "1",
  speed: "0.30",
  autostart: true
});

// for siri message mein animate laane ke liye
$(function () {
  $('.siri-message').textillate({
    loop: true,
    minDisplayTime: 2000, // Time before out effect starts
    in: {
      effect: 'fadeInUp',
      delayScale: 1.5,
      delay: 50,
      sync: true
    },
    out: {
      effect: 'fadeOutUp',
      delayScale: 1.5,
      delay: 50,
      sync: true
    }
  });
});

// jab mic button dabayenge jabhi  hi siri wave show hoon uske liye  event 
$("#micBtn").click(function () { 
  eel.playAssistantSound();
  $("#oval").attr("hidden", true);
  $("#SiriWave").attr("hidden", false);
  eel.allCommands();
});

// shortuct key banane ke liye taki shortcut key se v.a  open hoon jaaye 
function doc_keyUp(e) {
  if (e.key === 'd' && e.metaKey) { // Windows + D shortcut
    eel.playAssistantSound();
    $("#oval").attr("hidden", true); // hide main
    $(".siri-message").attr("hidden", false); //  class selector
    $("#SiriWave").attr("hidden", false);     // show wave
    eel.allCommands(); // trigger assistant
  }
}

$(document).ready(function () {
  document.addEventListener('keyup', doc_keyUp, false);

// jab hotword appear hoon toh siri wave open hoon 
// ✅ This function will show Siri wave and trigger assistant

// ✅ Expose this function to Python
eel.expose(showSiriWaveFromHotword);
function showSiriWaveFromHotword() {
    alert("Siri wave function triggered"); // Add this
    document.getElementById("SiriWave").removeAttribute("hidden");
    document.getElementById("oval").setAttribute("hidden", true);
}
 // chat feature ke liye hum  function banayenge 
function PlayAssistant(message){
  if (message!=""){
    $("#oval").attr("hidden",true);
    $("#SiriWave").attr("hidden",false);
    eel.allCommands(message);
    $("#chatbox").val("");
    $("#micBtn").attr("hidden",false);
    $("#SendBtn").attr("hidden",true);
  }
}
// send button display kab  krwana hai kab nhi 
function ShowHideButton(message) {
        if (message.length == 0) {
            $("#micBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
        else {
            $("#micBtn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);
        }
    }
  

  $("#chatbox").keyup(function () {

        let message = $("#chatbox").val();
        ShowHideButton(message)
    
    });
  $("#SendBtn").click(function () {
    
        let message = $("#chatbox").val()
        PlayAssistant(message)
    
    });
    // taaki enter daba ke bhi hmra input box hmri query lele
     $("#chatbox").keypress(function (e) {
        key = e.which;
        if (key == 13) { // 13 key is enter
            let message = $("#chatbox").val()
            PlayAssistant(message)
        }
    });


});
    