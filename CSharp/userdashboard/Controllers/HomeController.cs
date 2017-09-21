using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Session;
// These three using statements are necessary
using userdashboard.Models; // <-- Needed for context object
using Microsoft.EntityFrameworkCore; // <-- needed to include sub models
using System.Linq; // <-- for .ToList & other filtering LINQ functions

namespace userdashboard.Controllers
{
    public class HomeController : Controller
    {
        userdashboardContext _context;

        public HomeController(userdashboardContext context)
        {
            _context = context;
        }
        [HttpGet]
        [Route("")]
        public IActionResult Frontpage()
        {
            return RedirectToAction("Register");
        }
        [HttpGet]
        [Route("register")]
        public IActionResult Register()
        {
            return View("Register");
        }
        [HttpPost]
        [Route("register")]
        public IActionResult Register(registerViewModel model)
        {
            List<User> users = _context.Users.ToList();
            string newuser_level = "";
            if (ModelState.IsValid)
            {
                if(users == null)
                {
                    newuser_level = "admin";
                }
                if(users != null)
                {
                    newuser_level = "normal";
                }
                User newUser = new User
                {
                    firstName = model.firstName,
                    lastName = model.lastName,
                    email = model.email,
                    created_at = DateTime.Now,
                    updated_at = DateTime.Now,
                    user_level = newuser_level,
                };
                PasswordHasher<User> hasher = new PasswordHasher<User>();
                newUser.password = hasher.HashPassword(newUser, model.password);
                _context.Add(newUser);
                _context.SaveChanges();
                HttpContext.Session.SetInt32("currentUserId", newUser.id);
                return RedirectToAction("Main");
            }
            else
            {
                return View(model);
            }
        }
        [HttpGet]
        [Route("login")]
        public IActionResult Login()
        {
            return View("Login");
        }

        [HttpPost]
        [Route("login")]
        public IActionResult Login(string Email, string Password)
        {
            User loginuser = _context.Users.SingleOrDefault(user => user.email == Email);
            List<string> errors = new List<string>();
            if (loginuser == null)
            {
                errors.Add("Invalid Email");
                ViewBag.Errors = errors;
                return View("Login");
            }
            else
            {
                PasswordHasher<User> hasher = new PasswordHasher<User>();
                if (hasher.VerifyHashedPassword(loginuser, loginuser.password, Password) != 0)
                {
                    HttpContext.Session.SetInt32("currentUserId", loginuser.id);
                    if(loginuser.user_level == "admin")
                    {
                        return RedirectToAction("dashboard/admin");
                    }
                    else
                    {
                        return RedirectToAction("dashboard");
                    }
                    
                }
                else
                {
                    errors.Add("Invalid Password");
                    ViewBag.Errors = errors;
                    return View("Login");
                }
            }
        }
        [HttpGet]
        [Route("main")]
        public IActionResult Main()
        {
            string email = HttpContext.Session.GetString("currentUserId");
            if(email == null)
            {
                // ViewBag.LogErrors.Add("You need to log in first");
                // TempData["LogErrors"] = ViewBag.LogErrors;
                return RedirectToAction("Login");
            }
            else
            {
                return View("Main");
            }      
        }
        [HttpGet]
        [Route("new")]
        public IActionResult Admin()
        {
            return View("Admin");
        }
        [HttpPost]
        [Route("new")]
        public IActionResult Admin(registerViewModel model)
        {
            if (ModelState.IsValid)
            {
                User newUser = new User
                {
                    firstName = model.firstName,
                    lastName = model.lastName,
                    email = model.email,
                    created_at = DateTime.Now,
                    updated_at = DateTime.Now

                };
                PasswordHasher<User> hasher = new PasswordHasher<User>();
                newUser.password = hasher.HashPassword(newUser, model.password);
                _context.Add(newUser);
                _context.SaveChanges();
                // HttpContext.Session.SetInt32("currentUserId", newUser.id);
                return RedirectToAction("Admin");
            }
            else
            {
                return View(model);
            }
        }
        [HttpGet]
        [Route("dashboard")]
        public IActionResult Dashboard()
        {
            string email = HttpContext.Session.GetString("currentUserId");
            List<User> users = _context.Users.ToList();
            if(email == null)
            {
                // ViewBag.LogErrors.Add("You need to log in first");
                // TempData["LogErrors"] = ViewBag.LogErrors;
                HttpContext.Session.Clear();
                return RedirectToAction("Login");
            }
            else if(users == null)
            {
                HttpContext.Session.Clear();
                return RedirectToAction("Register");               
            }
            else
            {
                // Wrapper model = new Wrapper(players, teams, users, groups, memberships);
                Wrapper model = new Wrapper(users);                
                return View(model);
            }
        }
        
        [HttpGet]
        [Route("/logout")]
        public IActionResult Logout()
        {
            string email = HttpContext.Session.GetString("currentUserId");
            if(email == null)
            {
                // ViewBag.LogErrors.Add("You need to log in first");
                // TempData["LogErrors"] = ViewBag.LogErrors;
                HttpContext.Session.Clear();
                return RedirectToAction("Login");
            }
            else
            {
                HttpContext.Session.Clear();
                return RedirectToAction("Main");
            }
        }
        [HttpGet]
        [Route("delete/{userid}")]
        public IActionResult deleteMessage(int userid)
        {
            string email = HttpContext.Session.GetString("currentUserId");
            if(email == null)
            {
                // ViewBag.LogErrors.Add("You need to log in first");
                // TempData["LogErrors"] = ViewBag.LogErrors;
                HttpContext.Session.Clear();
                return RedirectToAction("Login");
            }
            else
            {
                User RetrievedUser = _context.Users.SingleOrDefault(user => user.id == userid);
                _context.Users.Remove(RetrievedUser);
                _context.SaveChanges();
                return RedirectToAction("Dashboard");
            }
        }
        // [HttpPost]
        // [Route("")]
        // public IActionResult Index(registerViewModel model)
        // {
        //     if (ModelState.IsValid)
        //     {
        //         Person newUser = new Person
        //         {
        //             firstName = model.firstName,
        //             lastName = model.lastName,
        //             email = model.email,
        //             created_at = DateTime.Now,
        //             updated_at = DateTime.Now

        //         };
        //         PasswordHasher<Person> hasher = new PasswordHasher<Person>();
        //         newUser.password = hasher.HashPassword(newUser, model.password);
        //         _context.Add(newUser);
        //         _context.SaveChanges();
        //         HttpContext.Session.SetInt32("currentUserId", newUser.id);
        //         return RedirectToAction("Users");
        //     }
        //     else
        //     {
        //         return View(model);
        //     }
        // }
        
        // // GET: /Home/
        // [HttpGet]
        // [Route("")]
        // public IActionResult Index()
        // {
        //     List<Team> teams = _context.Teams.Include(team => team.Players).ToList();
        //     List<Player> players = _context.Players.Include(player => player.Team).ToList();

        //     List<User> users = _context.Users.Include(u => u.Memberships).ThenInclude(m => m.Group).ToList();
        //     List<Membership> memberships = _context.Memberships.Include(m => m.User).Include(m => m.Group).ToList();
        //     List<Group> groups = _context.Groups.Include(g => g.Members).ToList();

        //     Wrapper model = new Wrapper(players, teams, users, groups, memberships);

            

        //     return View(model);
        // }

        // [HttpGet]
        // [Route("makeMtoNThings")]
        // public IActionResult Make_MtoN_Things()
        // {
        //     // Let's create some objects
        //     User user1 = new User();
        //     User user2 = new User();
        //     Group grp1 = new Group();
        //     Membership mbr1 = new Membership();
        //     Membership mbr2 = new Membership();

        //     grp1.Name = "Coders Group";

        //     user1.Name = "Inspector Mike";
        //     user1.Address = "The Dojo";
        //     user1.City = "Chicago";
        //     user1.Zip = "60640";

        //     user2.Name = "Inspector Gadget";
        //     user2.Address = "Nickelodeon";
        //     user2.City = "Toronto";
        //     user2.Zip = "12345";

        //     mbr1.User = user1;
        //     mbr1.Group = grp1;

        //     mbr2.User = user2;
        //     mbr2.Group = grp1;

        //     _context.Add(user1);
        //     _context.Add(user2);
        //     _context.Add(grp1);
        //     _context.Add(mbr1);
        //     _context.Add(mbr2);

        //     _context.SaveChanges();

        //     return RedirectToAction("Index");
        // }

        // [HttpGet]
        // [Route("make1toMThings")]
        // public IActionResult Make_1toM_Things()
        // {
        //    Player player1 = new Player();
        //    Player player2 = new Player();

        //    Team Cubs = new Team();
        //    Cubs.City = "Chicago";
        //    Cubs.Name ="Cubs";

        //    player1.Name = "Ryne Sandberg";
        //    player1.Team = Cubs;

        //    player2.Name = "Andre Dawson";
        //    player2.Team = Cubs;

        //    _context.Players.Add(player1);
        //    _context.Players.Add(player2);

        //    _context.Teams.Add(Cubs);
           
        //     _context.SaveChanges();

        //     return RedirectToAction("Index");
        // }

        // [HttpPost]
        // [Route("addTeam")]
        // public IActionResult addTeam(Team newTeam)
        // {
        //     _context.Add(newTeam);
        //     _context.SaveChanges();
        //     return RedirectToAction("Index");
        // }   

        // [HttpPost]
        // [Route("addPlayer")]
        // public IActionResult addPlayer(Player newPlayer, int TeamId)
        // {
        //     newPlayer.TeamID = TeamId;
        //     _context.Add(newPlayer);
        //     _context.SaveChanges(); 
        //     return RedirectToAction("Index");
        // }   

        // [HttpGet]
        // [Route("delPlayer/{playerId}")]
        // public IActionResult delPlayer(int playerId)
        // {
        //     Player pl = _context.Players.Where(p => p.PlayerId == playerId).FirstOrDefault();
        //     if(pl != null)
        //     {
        //         _context.Remove(pl);
        //         _context.SaveChanges();
        //     }
            
        //     return RedirectToAction("Index");
        // }
    }
}
