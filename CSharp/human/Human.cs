using System;

namespace human
{

    public class Human
    {
        public string name = "";
        public int strength = 3;
        public int intelligence = 3;
        public int dexterity = 3;
        public int health = 100;
        public Human(string Myname = "")
        {
            name = Myname;

        }

        public Human(string Myname = "", int str = 0, int intel = 0, int dext = 0, int hlth = 0)
        {
            name = Myname;
            strength = str;
            intelligence = intel;
            dexterity = dext;
            health = hlth;
        }

        public void Attack(Human attacked){

            attacked.health -= this.strength * 5;
            Console.WriteLine($"{attacked.name} was viciously attacked by {this.name}! {attacked.name}'s health now is {attacked.health}");

        }

        public void yourStatus(){

            Console.WriteLine($"{this.name}, your current status are: Strength = {this.strength}, Intelligence = {this.intelligence}, Dexterity = {this.dexterity} and Health = {this.health}");

        }
    }
}