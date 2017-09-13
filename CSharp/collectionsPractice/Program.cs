using System;
using System.Collections.Generic;

namespace collectionsPractice
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] numArray = new int[10];

            string[] strArray = {"Tim", "Martin", "Nikki", "Sara"};

            bool[] booArray = {true,false,true,false,true,false,true,false,true,false};

            int [,] array2D = new int[10,10];

            for(int i = 1; i <= 10; i++){

                Console.Write('(');

                for(int x = 1; x <= 10; x++){
                    array2D[i-1,x-1] = i * x;
                    Console.Write(i * x);

                    if(x<10){

                    Console.Write(',');

                    }
                }

                Console.WriteLine(')');
            }
            Console.Write(array2D);
            List<string> flavors = new List<string>();
            flavors.Add("Chocolate");
            flavors.Add("Vanilla");
            flavors.Add("Coffee");
            flavors.Add("Butter Pecan");
            flavors.Add("Strawberry");
            Console.WriteLine(flavors.Count);
            Console.WriteLine(flavors[2]);
            flavors.RemoveAt(2);
            Console.WriteLine(flavors.Count);

            Dictionary<string,string> pnames = new Dictionary<string,string>();
            foreach(string item in strArray){
                pnames.Add(item,null);          
            }

            Random rand = new Random();
            foreach(string item in new List<string>(pnames.Keys)){
                string x = flavors[rand.Next(0,flavors.Count)];
                while(pnames.ContainsValue(x)){
                    x = flavors[rand.Next(0,flavors.Count)];                    
                }
                Console.WriteLine(x);
                pnames[item] = x;  
            }    
        }
    }
}   