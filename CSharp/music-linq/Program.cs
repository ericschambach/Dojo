using System;
using System.Collections.Generic;
using System.Linq;
using JsonData;

namespace ConsoleApplication
{
    public class Program
    {
        public static void Main(string[] args)
        {

            List<Artist> Artists = JsonToFile<Artist>.ReadJson();
            List<Group> Groups = JsonToFile<Group>.ReadJson();


            //========================================================
            //Solve all of the prompts below using various LINQ queries
            //========================================================

            //There is only one artist in this collection from Mount Vernon, what is their name and age?

            var rightArtist = from idol in Artists.Where(str => str.Hometown == "Mount Vernon")
                    select new { idol.RealName, idol.Age, idol.Hometown };
            foreach (var item in rightArtist)
            {
                Console.WriteLine($"The name of the Artist from {item.Hometown} is {item.RealName}, who is {item.Age} years old");
            }
            Console.WriteLine("----------------------------------------------------");
            //Who is the youngest artist in our collection of artists?

            var oldestArtist = from idol in Artists
                    orderby idol.Age
                    select new {idol.RealName,idol.Age};
            oldestArtist = oldestArtist.Take(1);
            foreach (var item in oldestArtist)
            {
                Console.WriteLine($"The youngest artist is {item.RealName}, who is {item.Age}");
            }
            Console.WriteLine("----------------------------------------------------");  

            //Display all artists with 'William' somewhere in their real name

            var williamName = from idol in Artists.Where(str => str.RealName.Contains("William"))
                    orderby idol.Age
                    select new {idol.RealName};
            foreach (var item in williamName)
            {
                Console.WriteLine($"The artist {item.RealName} has William in its name");
            }
            Console.WriteLine("----------------------------------------------------");  

            //Display all groups with names less than 8 characters in length.

            var nameLessEight = from band in Groups.Where(str => str.GroupName.Length < 8)
                    select new {band.GroupName};
            foreach (var item in nameLessEight)
            {
                Console.WriteLine($"The name {item.GroupName} is less than 8 characters long");
            }
            Console.WriteLine("----------------------------------------------------"); 
            
            //Display the 3 oldest artist from Atlanta

            var artistFromAtlanta = from idol in Artists.Where(str => str.Hometown == "Atlanta")
                    orderby idol.Age descending
                    select new {idol.RealName,idol.Age,idol.Hometown};
            artistFromAtlanta = artistFromAtlanta.Take(3);
            foreach (var item in artistFromAtlanta)
            {
                Console.WriteLine($"- {item.RealName} is is {item.Age} years old and from {item.Hometown}");
            }
            Console.WriteLine("----------------------------------------------------"); 

            //(Optional) Display the Group Name of all groups that have members that are not from New York City

            var groupsNotFromNY = from idol in Artists.Where(str => str.Hometown != "New York City")
                    join band in Groups on idol.GroupId equals band.Id
                    group band by band.GroupName into bandGroup
                    select new {
                        bandName = bandGroup.Key
                    };
            foreach (var item in groupsNotFromNY)
            {
                Console.WriteLine($"- The group {item.bandName} has members not from New York");
            }
            Console.WriteLine("----------------------------------------------------"); 

            //(Optional) Display the artist names of all members of the group 'Wu-Tang Clan'

            var WuTangClan = from idol in Artists
                    join band in Groups.Where(str => str.GroupName == "Wu-Tang Clan") on idol.GroupId equals band.Id
                    select new {band.GroupName,idol.ArtistName};
            foreach (var item in WuTangClan)
            {
                Console.WriteLine($"- {item.ArtistName} is from {item.GroupName}");
            }
            Console.WriteLine("----------------------------------------------------"); 
        }
    }
}
