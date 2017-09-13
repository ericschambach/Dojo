using System;

namespace dojodachi
{
    public class dachi
    {
        public string name;

        //The { get; set; } format creates accessor methods for the field specified
        //This is done to allow flexibility
        public int health { get; set; }
        public int strength { get; set; }
        public int intelligence { get; set; }
        public int dexterity { get; set; }

        public dachi(string person)
        {
            name = person;
            strength = 3;
            intelligence = 25;
            dexterity = 3;
            health = 50;
        }
    }
}