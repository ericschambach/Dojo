using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;

namespace dojosurvey.Controllers
{
    public class dojosurveyController : Controller
    {
        // A GET method
		[HttpGet]
		[Route("/")]
		public IActionResult Survey()
		{
            ViewBag.Errors = new List<string>();
			return View("Survey");
		}

                // A POST method
        [HttpPost]
        [Route("process")]
        public IActionResult Results(string userName,string userLocation, string userLanguage, string userComment)
        {
            ViewBag.Errors = new List<string>();

            if(userName == null)
            {
                ViewBag.Errors.Add("Name cannot be empty");
            }

            if(userLocation == "Choose here")
            {
                ViewBag.Errors.Add("Please select a valid location");
            }

            if(userLanguage == "Choose here")
            {
                ViewBag.Errors.Add("Please select a valid language");
            }

            if(userComment == null)
            {
                userComment = "";
            }

            if(ViewBag.Errors.Count>0)
            {
                return View("survey");

            } else {

                ViewBag.name = userName;
                ViewBag.location = userLocation;
                ViewBag.language = userLanguage;
                ViewBag.comment = userComment;
                return View("results");
            }
        }
    }
}