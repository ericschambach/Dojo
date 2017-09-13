using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
 
namespace YourNamespace.Controllers
{
    public class HelloController : Controller
    {
        // [HttpGetAttribute]
        [HttpGet]
        [Route("index")]
        public string Index()
        {
            return "Hello World!";
        }

        [HttpGet]
        [Route("displayint")]
        public JsonResult DisplayInt()
        {
            return Json(34);
            //     var AnonObject = new {
            //              FirstName = "Raz",
            //              LastName = "Aquato",
            //              Age = 10
            //          };
            // return Json(AnonObject);
        }
    }
}