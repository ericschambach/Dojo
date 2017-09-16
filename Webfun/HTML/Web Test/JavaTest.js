// var words = ["fun", "exciting", "about not giving up", "being helpful", "being open", "what I learned at CodingDojo!"];

// for(var i in words[2]){
//     i = i.replace(" ", "ZZZZZZ");
// }

// console.log(words[2]);

var x = "this is a sample";


for(var i in x){
    if(x[i] === " "){
        x[i] = "z";
        // console.log("YES")
    }
}

console.log(x);