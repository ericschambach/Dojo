// Basic 1
var x = [];
x.push('coding');
x.push('dojo');
x.push('rocks');
x.pop();
console.log(x);
console.log('-----------------------------');
//Basic 2
const y = [];
y.push(88);
console.log(y)
console.log('-----------------------------');
//Basic 3
var z = [9, 10, 6, 5, -1, 20, 13, 2];
for(i in z){
    console.log(i,);
}
for(var i = 0;i<z.length-1;i++){
    console.log(i,);
}
console.log('-----------------------------');
//Basic 4
var m = ['Kadie', 'Joe', 'Fritz', 'Pierre', 'Alphonso'];
for(i in m){
    console.log(m[i].length);
}
for(i in m){
    if(m[i].length == 5){
        console.log(m[i]);
    }
}
console.log('-----------------------------');
//Basic 5
function yell(string){
    string = string.toUpperCase();
    return string;
}
console.log(yell('Hello World!'))
