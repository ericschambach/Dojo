
using System;
using System.ComponentModel.DataAnnotations;
namespace beltexam.Models
{
    public class AuctionViewModel : BaseEntity {
        [Key]
        public int AuctionId {get; set;}

        [Required(ErrorMessage="Please include a product name")]
        [MinLength(3, ErrorMessage="The name has to be at least 3 characters long")]
        public string ProductName {get; set;}


        [Required(ErrorMessage="Please include a description")]
        [MinLength(10, ErrorMessage="The description has to be at least 10 characters long")]
        public string Description {get; set;}

        [Required(ErrorMessage="Please include a price value")]
        [Range(1, Int32.MaxValue, ErrorMessage="The value has to be a number")]
        public int MinimumBid {get; set;}

        [Required(ErrorMessage="Please include a expiry date")]
        // [Compare("password", ErrorMessage="Passwords don't match")]
        public DateTime EndDate{get; set;}
    }
}