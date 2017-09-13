using System;

namespace wizardNinja
{
    public class Wizard
    {
        public string name;

        //The { get; set; } format creates accessor methods for the field specified
        //This is done to allow flexibility
        public int health { get; set; }
        public int strength { get; set; }
        public int intelligence { get; set; }
        public int dexterity { get; set; }

        public Wizard(string person)
        {
            name = person;
            strength = 3;
            intelligence = 25;
            dexterity = 3;
            health = 50;
        }
        public Wizard(string person, int str, int intel, int dex, int hp)
        {
            name = person;
            strength = str;
            intelligence = intel;
            dexterity = dex;
            health = hp;
        }
        public void heal()
        {
            this.health += this.intelligence * 10;
            Console.WriteLine($"{this.name}, your health has been increased by 10 and now is {this.health}");            

        }
        public void fireball(object obj)
        {
            Random rand = new Random();
            int x = rand.Next(20,51);
            if (obj is Wizard)
            {
                Wizard enemy = obj as Wizard;
                enemy.health -= x;

            } else if(obj is Ninja)
            {
                Ninja enemy = obj as Ninja;
                enemy.health -= x;

            } else if(obj is Samurai)
            {
                Samurai enemy = obj as Samurai;
                enemy.health -= x;

            } else if (obj == null)
            {
                Console.WriteLine("Failed Fireball Attack");
            }
        }
    }
}