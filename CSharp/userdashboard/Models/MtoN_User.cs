// using System.ComponentModel.DataAnnotations;
// using System.Collections.Generic;

// namespace codeFirst.Models
// {
//     public class User : BaseEntity
//     {
//         public long UserId { get; set; }
//         public string Name {get; set;}
//         public string Address {get; set;}
//         public string City {get; set;}
//         public string Zip {get; set;}
//         public List<Membership> Memberships { get; set; }
 
//         // Example of ONE TO MANY (One User has MANY Groups)
//         public User()
//         {
//             Memberships = new List<Membership>();
//         }
//     }
// }