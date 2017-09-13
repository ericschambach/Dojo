using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
 
namespace portfolio.Controllers
{
    public class portfolioController : Controller
    {
        // A GET method
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            //OR
            return View("Index");
            //Both of these returns will render the same view (You only need one!)
        }

        [HttpGet]
        [Route("/projects")]
        public IActionResult projects()
        {
            //OR
            return View("projects");
            //Both of these returns will render the same view (You only need one!)
        }
        [HttpGet]
        [Route("/contact")]
        public IActionResult contact()
        {
            //OR
            return View("contact");
            //Both of these returns will render the same view (You only need one!)
        }
    }
}