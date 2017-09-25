using System.ComponentModel.DataAnnotations;
using System;

namespace beltexam.Models
{
    public class Bidding : BaseEntity {

        public int BiddingId {get; set;}
        public int UserId {get; set;}
        public User User {get; set;}
        public int AuctionId {get; set;}
        public Auction Auction {get; set;}
        public DateTime Created_at {get; set;}
        public DateTime Updated_at {get; set;}
        
    }
}