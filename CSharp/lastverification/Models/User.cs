using System.ComponentModel.DataAnnotations;
using System;

namespace beltexam.Models
{
    public class User : BaseEntity {
        
        public int UserId {get; set;}
        public string FirstName {get; set;}
        public string LastName {get; set;}
        public string Username {get; set;}
        public int Wallet {get; set;}   
        public string Password {get; set;}
        public DateTime Created_at {get; set;}
        public DateTime Updated_at {get; set;}  
    }
}