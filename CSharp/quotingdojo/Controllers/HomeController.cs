using System;
using System.Globalization;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using quotingdojo.Connectors;

namespace quotingdojo.Controllers
{

    public class HomeController : Controller
    {
        private MySqlConnector cnx;

        public HomeController()
        {
            cnx = new MySqlConnector();
        }
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            return View("Index");
        }

        [HttpPost]
        [Route("addQuote")]
        public IActionResult addQuote(string yourname,string yourquote)
        {
            // string name = HttpContext.Session.GetString("yourname");
            // string quote = HttpContext.Session.GetString("yourquote");
            // string rightNow = now.ToString("yyyy-MM-dd HH:mm");
            string rightNow = DateTime.Now.ToString("yyyyMMddHHmmss");
            string query = $"INSERT INTO comments (user,comment,created_at,updated_at) VALUES ('{yourname}','{yourquote}',{rightNow},{rightNow})";
            MySqlConnector.Execute(query);
            return RedirectToAction("quotes");
        }
        [HttpPost]
        [Route("toQuote")]
        public IActionResult toQuote(string yourname,string yourquote)
        {
            // yourname = "";
            // yourquote = "";
            return View("quotes");
        }

        [HttpGet]
        [Route("quotes")]
        public IActionResult quotes()
        {
            var allQuotes = MySqlConnector.Query("SELECT * FROM comments");
            ViewBag.quotes = allQuotes;
            return View("quotes");
        }
    }
}
