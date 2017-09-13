using System;

namespace human
{
    class Program
    {
        static void Main(string[] args)
        {
            Human myHuman = new Human("Eric");
            Human otherHuman = new Human("Jeff");
            Console.WriteLine(myHuman.intelligence);
            Console.WriteLine(myHuman.name);
            Console.WriteLine(otherHuman.intelligence);
            Console.WriteLine(otherHuman.name);
            myHuman.Attack(otherHuman);
            Console.WriteLine(otherHuman.health);            
            Console.WriteLine(myHuman.health);
            myHuman.yourStatus();           
            Human anotherHuman = new Human("Carolyn",20);  
            anotherHuman.yourStatus();                                
        }
    }
}
