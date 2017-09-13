using System;

namespace wizardNinja
{
    public class Ninja
    {
        public string name;

        //The { get; set; } format creates accessor methods for the field specified
        //This is done to allow flexibility
        public int health { get; set; }
        public int strength { get; set; }
        public int intelligence { get; set; }
        public int dexterity { get; set; }

        public Ninja(string person)
        {
            name = person;
            strength = 3;
            intelligence = 3;
            dexterity = 175;
            health = 100;
        }
        public Ninja(string person, int str, int intel, int dex, int hp)
        {
            name = person;
            strength = str;
            intelligence = intel;
            dexterity = dex;
            health = hp;
        }
        public void steal(object obj)
        {
            int damage = 10;
            this.health += damage;
            if (obj is Wizard)
            {
                Wizard enemy = obj as Wizard;
                enemy.health -= damage;

            } else if(obj is Ninja)
            {
                Ninja enemy = obj as Ninja;
                enemy.health -= damage;

            } else if(obj is Samurai)
            {
                Samurai enemy = obj as Samurai;
                enemy.health -= damage;

            } else if (obj == null)
            {
                Console.WriteLine("Failed Steal");
            }
        }
        public void get_away()
        {
            this.health -= 15;
        }
    }
}