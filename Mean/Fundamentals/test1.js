// num = 6;

// function fact(x=num){
//     x--;
//     if(x<=0){
//         return num;
//     }
//     num *= x;
//     console.log(num)
//     fact(x)
// }
// var n = 2

// function fiberN (n,iter = 2, fib = []){
//     if(fib.length == 0){
//         fib = [0,1];
//     }
//     if(iter >= n){
//         console.log(fib[n-1]);
//         return true;
//     }
//
//     fib[iter] = fib[iter-1] + fib[iter-2];
//     iter ++;
//     return fiberN(n,iter,fib);
// }
//
// console.log(fiberN(6))

// var arr = [1,2,2,3,4,4,5,5,5,6,6,7,8,9,9];

// function removedupli(arr){
//     var x = arr.length;
//     arr[x] = arr[0];
//     for(var i = 1;i < x;i++){
//         if(arr[i]!=arr[i-1]) {
//             arr[arr.length] = arr[i];
//         }
//     }
//     console.log(arr);
//     var n = arr.length - x;
//     for(var y = 0; y < x; y++){
//         if(y<n){
//             arr[y] = arr[y+x];
//         }
//     }
//     console.log(arr);
//     var z = arr.length;
//     while(z>n){
//         arr.pop();
//         z--;
//     }
//     return arr;
// }
// console.log(removedupli(arr));

// function magic_multiply(x, y){
//     // --- your code here ---
//     return x;
// }
var arr = [1,5,3,6,9,7,8,2,11,43,13,99,23,44,22,43]
// console.log(typeof(5));

function sortarr(arr){

    var isvalid = false;
    while(isvalid == false){
        isvalid = true;
        for(var i = 0; i < arr.length-1; i++){
            if(arr[i]>arr[i+1]){
                var temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
                isvalid = false;
            }
        }
        console.log(arr)
    }
    return arr;
}

sortarr(arr);