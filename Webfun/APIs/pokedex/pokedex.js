// Getting and displaying pokemons

$(document).ready(function(){
    for(var i = 1;i<=151;i++){
    $("#pokemons").append("<img id="+i+" src=http://pokeapi.co/media/img/"+i+".png/>");
    }

    $("img").click(function(){
        var myID = $(this).attr("id");
        $.get("http://pokeapi.co/api/v1/pokemon/"+myID, function(res) {
            $(".pokeimg").html("<img id="+myID+"  src=http://pokeapi.co/media/img/"+myID+".png/>");
            $("#pokebio h2").html(res.name);
            $(".weight").html(res.weight);
            $(".height").html(res.height);
            $(".types").html("")
            for(var i = 0;i<res.types.length;i++){
                $(".types").append("<li>"+res.types[i].name+"</li>"); 
            }
        })
    })
})