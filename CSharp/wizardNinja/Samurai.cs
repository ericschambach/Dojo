using System;

namespace wizardNinja
{
    public class Samurai
    {
        public string name;

        //The { get; set; } format creates accessor methods for the field specified
        //This is done to allow flexibility
        public int health { get; set; }
        public int strength { get; set; }
        public int intelligence { get; set; }
        public int dexterity { get; set; }

        public Samurai(string person)
        {
            name = person;
            strength = 3;
            intelligence = 3;
            dexterity = 3;
            health = 200;
        }
        public Samurai(string person, int str, int intel, int dex, int hp)
        {
            name = person;
            strength = str;
            intelligence = intel;
            dexterity = dex;
            health = hp;
        }
        public void death_blow(object obj)
        {
            if (obj is Wizard)
            {
                Wizard enemy = obj as Wizard;
                if(enemy.health<50)
                {
                    enemy.health = 0;
                    Console.WriteLine($"{enemy.name}, you have been killed by the death blow!");
                }
            } else if(obj is Ninja)
            {
                Ninja enemy = obj as Ninja;
                if(enemy.health<50)
                {
                    enemy.health = 0;
                    Console.WriteLine($"{enemy.name}, you have been killed by the death blow!");
                }

            } else if(obj is Samurai)
            {
                Samurai enemy = obj as Samurai;
                if(enemy.health<50)
                {
                    enemy.health = 0;
                    Console.WriteLine($"{enemy.name}, you have been killed by the death blow!");
                }
            } else if (obj == null)
            {
                Console.WriteLine("Failed Steal");
            }
        }
        public void meditate()
        {
            this.health = 200;
        }
    }
}