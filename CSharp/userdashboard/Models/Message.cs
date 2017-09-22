using System.ComponentModel.DataAnnotations;
using System;
namespace userdashboard.Models
{
    public class Message : BaseEntity
    {

        public int MessageId { get; set; }
        public string message { get; set; }
        public User User { get; set; }
        public int UserID { get; set; }
        public DateTime created_at { get; set; }
        public DateTime updated_at { get; set; }


    }
}