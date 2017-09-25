using System;
using System.Collections.Generic;

namespace beltexam.Models
{
    public class Auction : BaseEntity 
    {
        public int AuctionId {get; set;}
        
        public string CreatedUser {get; set;}
        public string ProductName {get; set;}
        public string Description {get; set;}
        public DateTime EndDate {get; set;}
        public int Bid {get; set;}
        public int MinimumBid {get; set;}
        public string HighestBidder {get; set;}
        public DateTime Created_at {get; set;}
        public DateTime Updated_at {get; set;}
    }
}