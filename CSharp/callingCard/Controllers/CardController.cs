using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
 
namespace callingCard.Controllers
{
    public class CardController : Controller
    {
        [HttpGet]
        [Route("/{FirstName}/{LastName}/{Age}/{FavColor}")]
        public JsonResult CallCard(string FirstName, string LastName, int Age, string FavColor)
        {
            return Json(new {FirstName = FirstName, LastName = LastName, Age = Age, FavoriteColor = FavColor});
        }
    }
}