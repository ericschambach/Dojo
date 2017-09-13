using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System;
 
namespace randpass.Controllers
{
    public class randpass : Controller
    {
        // A GET method
		[HttpGet]
		[Route("")]
		public IActionResult main()
		{
			int? passcount = HttpContext.Session.GetInt32("passcount");
            if(passcount != null)
            {
                HttpContext.Session.Clear();
            }
            return View("main");
		}

        [HttpPost]
        [Route("")]
        public IActionResult Other()
        {
            int? passcount = HttpContext.Session.GetInt32("passcount");
            if(passcount == null)
            {
                passcount = 0;
            }
            passcount++;
            const string passSource = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
            Random rand = new Random();
            string passcode = "";
            for(int i = 0; i < 14;i++)
            {
                passcode = passcode + passSource[rand.Next(0,passSource.Length)];
            }
            ViewBag.passcount = passcount;
            ViewBag.passcode = passcode;
            HttpContext.Session.SetInt32("passcount",(int)passcount);
            return View("main");
        }

        // [HttpGet]
        // [Route("template/{Name}")]
        // public IActionResult Method(string Name)
        // {
        //     // Method body
        // }

        // [HttpGet]
        // [Route("")]
        // public JsonResult Example()
        // {
        //     // The Json method convert the object passed to it into JSON
        //     return Json(SomeC#Object);
        // }

        // [HttpGet]
        // [Route("displayint")]
        // public JsonResult DisplayInt()
        // {
        //     return Json(34);
        // }
        
        // // Suppose we're working with the Human class we wrote in the previous chapter
        // [HttpGet]
        // [Route("displayhuman")]
        // public JsonResult DisplayHuman()
        // {
        //     return Json(new Human());
        // }
        // '------------------------'
        // // Other code
        // [HttpGet]
        // [Route("displayint")]
        // public JsonResult DisplayInt()
        // {
        //     var AnonObject = new {
        //                         FirstName = "Raz",
        //                         LastName = "Aquato",
        //                         Age = 10
        //                     };
        //     return Json(AnonObject);
        // }
    }
}