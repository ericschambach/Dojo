using System;
using System.Collections.Generic;

namespace basicThirteen
{
    class Program
    {
        public static void printNums()
        {
            for(int i = 1; i <= 255; i++){
                Console.WriteLine(i);
            } 
        }

        public static void printOdd()
        {
            for(int i = 1; i <= 255; i++){
                if(i % 2 != 0){
                    Console.WriteLine(i);
                }
            } 
        }

        public static void printSum()
        {
            int sumNum = 0;
            for(int i = 0; i <= 255; i++){
                sumNum += i;
                Console.WriteLine("New number: {0} Sum: {1}", i,sumNum);
            } 
        }

        public static void itiArr(int[] arr)
        {
            for(int i = 0; i < arr.Length; i++){

                Console.WriteLine(arr[i]);
            } 
        }

        public static void arrMax(int[] arr)
        {   
            int max = arr[0];
            for(int i = 0; i < arr.Length; i++){
                if(arr[i]>max){
                    max = arr[i];
                }
            }

            Console.WriteLine(max);
        }

        public static void getAvg(int[] arr)
        {   
            float sumNum = 0;
            for(int i = 0; i < arr.Length; i++){
                sumNum += arr[i];
            }

            Console.WriteLine(sumNum/arr.Length);
        }

        public static List<int> oddArr()
        {   
            List<int> oddNums = new List<int>();
            for(int i = 1; i <= 255; i++){
                if(i % 2 != 0){
                    oddNums.Add(i);
                }
            }
            return oddNums;
        }

        public static void greaterThan(int[] arr, int y)
        {   
            List<int> oddNums = new List<int>();
            for(int i = 1; i <= 255; i++){
                if(i % 2 != 0){
                    oddNums.Add(i);
                }
            }
            return oddNums;
        }

        static void Main(string[] args)
        {
            int[] arr = {1,3,5,7,9,13};
            // printNums();
            // printOdd();
            // printSum();
            // itiArr(arr);
            // arrMax(arr);
            // getAvg(arr);
            oddArr();
        }
    }
}
