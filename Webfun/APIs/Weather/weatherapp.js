$(document).ready(function() {
    $('form').submit(function() {
        var apiKey = "434cecfaafe48ebba5822ef71471a9c5/"
        var url = "api.openweathermap.org/data/2.5/weather?q="
        $.get()
        var fahrenheit = (x*(9/5))-459.67
        
        // your code here (build up your url)
        $.get(url, function(res) {
            // your code here
        }, 'json');
        // don't forget to return false so the page doesn't refresh
        return false;
    });

    $(form)

    $("button").click(function(){

        var myID = $(this).attr("id");
        $.get("http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID="+apiKey, function(res) {
            $("#wrapper").html(<h1>res.</h1>)
            
            // ("<img id="+myID+"  src=http://pokeapi.co/media/img/"+myID+".png/>");
            // $("#pokebio h2").html(res.name);
            // $(".weight").html(res.weight);
            // $(".height").html(res.height);
            // $(".types").html("")
            // for(var i = 0;i<res.types.length;i++){
            //     $(".types").append("<li>"+res.types[i].name+"</li>"); 
            }
        })
    })


});


