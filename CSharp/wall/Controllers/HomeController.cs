using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using System.Text.RegularExpressions;
using System.Linq;
using wall.Connectors;

namespace wall.Controllers
{
    public class HomeController : Controller
    {
        // GET: /Home/
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
        public IActionResult addUser(string firstName,string lastName, string email,string password,string pw_confirm)
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
                    string query = $"INSERT INTO users (firstName,lastName,email,password,created_at,updated_at) VALUES ('{firstName}','{lastName}','{email}','{password}',{rightNow},{rightNow})";
                    MySqlConnector.Execute(query);
                    HttpContext.Session.SetString("userpass",(string)email);
                    return RedirectToAction("Main");                    
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
                        return RedirectToAction("Main");
                    }
                }
            }
        }
        [HttpGet]
        [Route("/main")]
        public IActionResult Main()
        {
            ViewBag.LogErrors = new List<string>();
            string email = HttpContext.Session.GetString("userpass");
            if(email == null)
            {
                ViewBag.LogErrors.Add("You need to log in first");
                TempData["LogErrors"] = ViewBag.LogErrors;
                return RedirectToAction("Index");
            }
            else
            {
                ViewBag.MessageErrors = TempData["MessageErrors"];
                ViewBag.CommentErrors = TempData["CommentErrors"];
                if(ViewBag.MessageErrors == null)
                {
                    ViewBag.MessageErrors = new List<string>();
                }
                if(ViewBag.CommentErrors == null)
                {
                    ViewBag.CommentErrors = new List<string>();
                }
                string selectQuery = $"SELECT id FROM users WHERE email = '{email}'";
                var younow = MySqlConnector.Query(selectQuery);
                string selectMessages = $"SELECT users.firstName AS firstName,users.LastName AS lastName,messages.id AS id,messages.message AS message, messages.user_id AS message_user_id, messages.created_at AS created_at,messages.updated_at AS updated_at FROM users JOIN messages ON users.id = messages.user_id";
                string selectComments = $"SELECT users.firstName AS user_firstName,users.LastName AS user_lastName,messages.id AS message_id,messages.message AS message, messages.user_id AS message_user_id,messages.created_at AS message_created_at,messages.updated_at AS message_updated_at,comments.id AS comment_id,comments.comment AS comment, comments.message_id AS comment_message_id,comments.user_id AS comment_user_id, comments.created_at AS comment_created_at,comments.updated_at AS comment_updated_at FROM users JOIN comments ON users.id = comments.user_id JOIN messages ON comments.message_id = messages.id";
                var messages = MySqlConnector.Query(selectMessages);
                var comments = MySqlConnector.Query(selectComments);
                ViewBag.userid = (int)younow[0]["id"];
                ViewBag.MessageList = messages;
                ViewBag.CommentList = comments;
                return View("Main");
            }
        }
        [HttpPost]
        [Route("/addMessage")]
        public IActionResult addMessage(string message)
        {
            ViewBag.MessageErrors = new List<string>();
            if(message == null || message.Length<4)
            {
                ViewBag.MessageErrors.Add("The message has to have at least 4 characters.");
                TempData["messageErrors"] = ViewBag.MessageErrors;
                return RedirectToAction("Main");
            }
            else
            {
                message = message.Replace("'",@"\'");
                string email = HttpContext.Session.GetString("userpass");
                string selectQuery = $"SELECT * FROM users WHERE email = '{email}'";
                var younow = MySqlConnector.Query(selectQuery);
                int? yourid = (int)younow[0]["id"];
                string rightNow = DateTime.Now.ToString("yyyyMMddHHmmss");
                string messageQuery = $"INSERT INTO messages (message,user_id,created_at,updated_at) VALUES ('{message}',{yourid},{rightNow},{rightNow})";
                MySqlConnector.Execute(messageQuery);
                return RedirectToAction("Main");
            }
        }

        [HttpPost]
        [Route("/addComment")]
        public IActionResult addComment(string comment,int? messageid)
        {
            ViewBag.CommentErrors = new List<string>();
            if(comment == null || comment.Length<4)
            {
                ViewBag.commentErrors.Add("The comment has to have at least 4 characters.");
                TempData["CommentErrors"] = ViewBag.commentErrors;
                return RedirectToAction("Main");
            }
            else
            {
                comment = comment.Replace("'",@"\'");
                string email = HttpContext.Session.GetString("userpass");
                string selectQuery = $"SELECT * FROM users WHERE email = '{email}'";
                var younow = MySqlConnector.Query(selectQuery);
                int? yourid = (int)younow[0]["id"];
                string rightNow = DateTime.Now.ToString("yyyyMMddHHmmss");
                string commentQuery = $"INSERT INTO comments (comment,user_id,message_id,created_at,updated_at) VALUES ('{comment}',{yourid},{messageid},{rightNow},{rightNow})";
                MySqlConnector.Execute(commentQuery);
                return RedirectToAction("Main");
            }
        }
        [HttpPost]
        [Route("/deleteMessage")]
        public IActionResult deleteMessage(int? messageid)
        {
            // string email = HttpContext.Session.GetString("userpass");
            // string selectQuery = $"SELECT * FROM users WHERE email = '{email}'";
            // var younow = MySqlConnector.Query(selectQuery);
            // int? yourid = (int)younow[0]["id"];
            string delComments = $"DELETE FROM comments WHERE message_id = {messageid}";
            string delMessage = $"DELETE FROM messages WHERE id = {messageid}";
            MySqlConnector.Execute(delComments);
            MySqlConnector.Execute(delMessage);
            return RedirectToAction("Main");
        }
        [HttpGet]
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
