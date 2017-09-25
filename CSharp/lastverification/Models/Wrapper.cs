using System.ComponentModel.DataAnnotations;
using System.Collections.Generic;

namespace beltexam.Models
{
    public class Wrapper : BaseEntity
    {
        // public List<Player> Players {get; set;}
        // public List<Team> Teams {get; set;}
        public List<User> Users {get; set;}
        public List<Auction> Auctions {get; set;}
        // public List<Group> Groups {get; set;}
        // public List<Membership> Memberships {get; set;}
        // public Player newPlayer { get; set; }

        // public Wrapper(List<Player> p, List<Team> t, List<User> u, List<Group> g, List<Membership> m)
        public Wrapper(List<User> u,List<Auction> a)
        {
            // Players = p;
            // Teams = t;
            Users = u;
            Auctions = a;
            // Groups = g;
            // Memberships = m;
            // newPlayer = new Player();
        }
    }
}