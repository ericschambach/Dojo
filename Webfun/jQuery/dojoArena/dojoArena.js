var backgroundfix = false;
//HOVER BACKGROUND IMAGES
$(document).ready(function () {

    $(".arena").hover(function () {
        var imURL = $(this).attr("id");
        $("#wrapper").css("background", "url(" + imURL + ".jpg)");
        }, function () {
            if(backgroundfix == false){
            $("#wrapper").css("background", "");
            }
        })
    });

//SET BACKGROUND IMAGES
    $(document).ready(function () {
        $(".arena").click(function() {
            var imURL = $(this).attr("id");
            $("#wrapper").css("background", "url(" + imURL + ".jpg)");
            backgroundfix = true;
            $("#selectArena").css("display","none");
            $("#selectPlayers").css("display","block");
        })
    });

//PLAYER1 IMAGE
    $(document).ready(function () {
        $("#player1").change(function(){
            var p1URL = $("#player1 option:selected").attr("class");
            $("#turtle1").css("background","url(" + p1URL + ".png)");
            $("#turtle1").css("background-repeat","no-repeat")
            $("#turtle1").css("background-position","center")
        })
    });

//PLAYER2 IMAGE
     $(document).ready(function () {
        $("#player2").change(function(){
            var p2URL = $("#player2 option:selected").attr("class");
            $("#turtle2").css("background","url(" + p2URL + ".png)");
            $("#turtle2").css("background-repeat","no-repeat")
            $("#turtle2").css("background-position","center")
        })
    });
    
