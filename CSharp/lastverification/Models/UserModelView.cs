
using System.ComponentModel.DataAnnotations;
namespace beltexam.Models
{
    public class UserModelView : BaseEntity {
        [Key]
        public int UserId {get; set;}

        [Required(ErrorMessage="Please include a Username")]
        [MinLength(3, ErrorMessage="Username has to be at least 3 characters long")]
        [MaxLength(20, ErrorMessage="Username cannot be more than 20 characters long")]
        public string Username {get; set;}

        [Required(ErrorMessage="Please include a password")]
        [MinLength(8, ErrorMessage="The password has to be at least 8 characters long")]
        [DataType(DataType.Password)]
        public string Password {get; set;}

        [Required(ErrorMessage="Please confirm the password entered")]
        [Compare("Password", ErrorMessage="Password confirmation does not match")]
        public string Confirm {get; set;}

        [Required(ErrorMessage="Please include a first name")]
        [MinLength(3, ErrorMessage="First name has to be at least 3 characters long")]
        public string FirstName {get; set;}

        [Required(ErrorMessage="Please include a last name")]
        [MinLength(3, ErrorMessage="Last name has to be at least 3 characters long")]
        public string LastName {get; set;}
    }
}