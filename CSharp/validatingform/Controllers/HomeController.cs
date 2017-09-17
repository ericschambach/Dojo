using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using System.Text.RegularExpressions;
using validatingform.Connectors;


namespace validatingform.Controllers
{
    public class HomeController : Controller
    {
        private static bool isValidEmail(string inputEmail)
        {
        string strRegex = @"^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}" +
                @"\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\" + 
                @".)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$";
        Regex re = new Regex(strRegex);
        if (re.IsMatch(inputEmail))
            return (true);
        else
            return (false);
        }

        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            ViewBag.Errors = TempData["Errors"];
            if(ViewBag.Errors == null)
            {
                ViewBag.Errors = new List<string>();
            }
            ViewBag.LogErrors = TempData["LogErrors"];
            if(ViewBag.LogErrors == null)
            {
                ViewBag.LogErrors = new List<string>();
            }
            return View();
        }

        [HttpPost]
        [Route("/addUser")]
        public IActionResult addUser(string firstName,string lastName, int? age,string email,string password,string pw_confirm)
        {
            ViewBag.Errors = new List<string>();
            if(firstName == null || firstName.Length<4)
            {
                ViewBag.Errors.Add("First name field has to have at least 4 characters.");
            }
            if(lastName == null || lastName.Length<4)
            {
                ViewBag.Errors.Add("Last name field has to have at least 4 characters.");                
            }
            if(age == null)
            {
                ViewBag.Errors.Add("You have to provide your age.");                                
            }
            if(email == null)
            {
                ViewBag.Errors.Add("You have to provide an e-mail address");                                                
            }
            else
            {
                if(isValidEmail(email)==false)
                {
                    ViewBag.Errors.Add("The email format provided is not correct");
                }
            }
            if(password == null || password.Length<8)
            {
                ViewBag.Errors.Add("You have to provide a password");                                                
            }
            if(pw_confirm == null || pw_confirm!=password)
            {
                ViewBag.Errors.Add("Password and password confirmation do not match");                                                
            }
            if(ViewBag.Errors.Count>0)
            {
                TempData["Errors"] = ViewBag.Errors;
                return RedirectToAction("Index");
            } 
            else
            {
                string selectQuery = $"SELECT * FROM users WHERE email = '{email}'";
                var emailVal = MySqlConnector.Query(selectQuery);
                if (emailVal.Count > 0)
                {
                    ViewBag.Errors.Add("This e-mail already belongs to a registered user");
                    TempData["Errors"] = ViewBag.Errors;
                    return RedirectToAction("Index");
                }
                else
                {
                    string rightNow = DateTime.Now.ToString("yyyyMMddHHmmss");
                    string query = $"INSERT INTO users (firstName,lastName,age,email,password,created_at,updated_at) VALUES ('{firstName}','{lastName}','{age}','{email}','{password}',{rightNow},{rightNow})";
                    MySqlConnector.Execute(query);
                    HttpContext.Session.SetString("userpass",(string)email);
                    return RedirectToAction("Index");                    
                }
            }
        }

        [HttpPost]
        [Route("/login")]
        public IActionResult login(string email,string password)
        {
            ViewBag.LogErrors = new List<string>();
            if(email == null)
            {
                ViewBag.LogErrors.Add("You have to provide an username");                                                
            }
            if(password == null)
            {
                ViewBag.LogErrors.Add("You have to provide a password");                                                
            }
            if(ViewBag.LogErrors.Count>0)
            {
                TempData["LogErrors"] = ViewBag.LogErrors;
                return RedirectToAction("Index");
            } 
            else
            {
                string selectQuery = $"SELECT * FROM users WHERE email = '{email}'";
                var emailVal = MySqlConnector.Query(selectQuery);
                if (emailVal.Count < 1)
                {
                    ViewBag.LogErrors.Add("We cannot find your username in our records");
                    TempData["LogErrors"] = ViewBag.LogErrors;
                    return RedirectToAction("Index");
                }
                else
                {
                    if((string)emailVal[0]["password"] != password)
                    {
                        ViewBag.LogErrors.Add("Wrong password");
                        TempData["LogErrors"] = ViewBag.LogErrors;
                        return RedirectToAction("Index");
                    }
                    else
                    {
                        HttpContext.Session.SetString("userpass",(string)email);
                        return RedirectToAction("Success");
                    }
                }
            }
        }
        [HttpGet]
        [Route("/success")]
        public IActionResult Success()
        {
            if(HttpContext.Session.GetString("userpass") == null)
            {
                ViewBag.LogErrors.Add("You need to log in first");
                TempData["LogErrors"] = ViewBag.LogErrors;
                return RedirectToAction("Index");
            }
            else
            {
                return RedirectToAction("Success");
            }
        }

        [HttpPost]
        [Route("/logout")]
        public IActionResult Logout()
        {
            if(HttpContext.Session.GetString("userpass") == null)
            {
                ViewBag.LogErrors.Add("You need to log in first");
                TempData["LogErrors"] = ViewBag.LogErrors;
                HttpContext.Session.Clear();
                return RedirectToAction("Index");
            }
            else
            {
                HttpContext.Session.Clear();
                return RedirectToAction("Index");
            }
        }
    }
}
