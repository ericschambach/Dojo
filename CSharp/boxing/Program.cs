using System;
using System.Collections.Generic;

namespace boxing
{
    class Program
    {
        static void Main(string[] args)
        {
            object num1 = 7;
            object num2 = 28;
            object num3 = -1;
            object option = true;
            object toSit = "Chair";
            List<object> boxItems = new List<object>();
            boxItems.Add(num1);
            boxItems.Add(num2);
            boxItems.Add(num3);
            boxItems.Add(option);
            boxItems.Add(toSit);
            int sumNum = 0;
            foreach (var item in boxItems){
                Console.WriteLine(item);
                if(item is int){
                    // Console.WriteLine(item);
                    
                    sumNum += (int)item;
                }
            }
                Console.WriteLine(sumNum);                        
        }
    }
}
