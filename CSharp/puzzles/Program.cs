using System;
using System.Collections.Generic;
using System.Linq;

namespace puzzles
{
    class Program
    {
        public static void RandomArray()
        {
            Random rand = new Random();
            int[] arrNums = new int[10];
            int x = rand.Next(5,26);
            int sumNums = 0;
            int minNum = arrNums[0];
            int maxNum = arrNums[0];
            for(int i = 0; i <= 9; i++)
            {
                if(arrNums.Length>0)
                {
                    while(arrNums.Contains(x))
                    {
                        x = rand.Next(5,25);                    
                    }
                }

                arrNums[i] = x;
                sumNums += arrNums[i];

                if(arrNums[i]<minNum)
                {
                    minNum = arrNums[i];
                }

                if(arrNums[i]>maxNum)
                {
                    maxNum = arrNums[i];
                }
            }
            Console.WriteLine(minNum);
            Console.WriteLine(maxNum);
            Console.WriteLine(sumNums);
        }

        public static string TossCoin()
        {   
            Random rand = new Random();
            int x = rand.Next(0,2);
            string heads = "Heads";
            string tails = "Tails";
            // Console.WriteLine(x);
            if(x == 0)
            {
                Console.WriteLine(heads);
                return heads;
            } else {
                Console.WriteLine(tails);                
                return tails;
            }
        }

        public static double TossCoinDouble(int num)
        {   
            Random rand = new Random();
            int x = rand.Next(0,2);
            int headToss = 0;
            int tailToss = 0;
            int sumToss = 0;
            // string heads = "Heads";
            // string tails = "Tails";
            // Console.WriteLine(x);
            while(num > 0)
            {
                sumToss ++;

                if(x == 0)
                {
                    Console.WriteLine(heads);
                    headToss += 1;
                } else {
                    Console.WriteLine(tails);                
                    tailToss += 1;
                }  

                num --;   
            }

            return tailToss/sumToss;
        }

        static void Main(string[] args)
        {
            // RandomArray();
            // TossCoin();
            TossCoinDouble();
        }
    }
}
