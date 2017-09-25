using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Session;
// These three using statements are necessary
using beltexam.Models; // <-- Needed for context object
using Microsoft.EntityFrameworkCore; // <-- needed to include sub models
using System.Linq; // <-- for .ToList & other filtering LINQ functions


namespace beltexam.Controllers
{
    public class HomeController : Controller
    {
        beltexamContext _context;

        public HomeController(beltexamContext context)
        {
            _context = context;
        }
        // GET: /Home/
        // GET: /Home/
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            return View("Index");
        }
        [HttpPost]
        [Route("")]
        public IActionResult Index(UserModelView model)
        {
            if(ModelState.IsValid)
            {
                User loginuser = _context.Users.SingleOrDefault(user => user.Username == model.Username);
                if (loginuser != null)
                {
                    ViewBag.RegDup = "This e-mail already belongs to a registered user";
                    return View("Index");
                }
                else
                {
                    User newUser = new User 
                    {
                        FirstName = model.FirstName,
                        LastName = model.LastName,
                        Wallet = 1000,
                        Username = model.Username,
                        Created_at = DateTime.Now,
                        Updated_at = DateTime.Now,
                    };
                    PasswordHasher<User> hasher = new PasswordHasher<User>();
                    newUser.Password = hasher.HashPassword(newUser, model.Password);
                    _context.Add(newUser);
                    _context.SaveChanges();
                    HttpContext.Session.SetInt32("currentUserId", newUser.UserId);
                    HttpContext.Session.SetString("currentUserName", newUser.FirstName);
                    return RedirectToAction("Home");
                    }
            }
            else
            {
                return View("Index");
            }
        }
        [HttpPost]
        [Route("/login")]
        public IActionResult Login(string username, string password)
        {
            User loginuser = _context.Users.SingleOrDefault(user => user.Username == username);
            if(loginuser == null)
            {
                TempData["UsernameError"] = "Incorrect username";
                // TempData["UsernameError"] = ViewBag.UsernameError;
                return RedirectToAction("Index");
            }
            else
            {
                PasswordHasher<User> hasher = new PasswordHasher<User>();
                if(hasher.VerifyHashedPassword(loginuser, loginuser.Password, password) != 0)
                {
                    HttpContext.Session.SetInt32("currentUserId", loginuser.UserId);
                    HttpContext.Session.SetString("currentUserName", loginuser.FirstName);
                    return RedirectToAction("Home");
                } 
                else 
                {
                    TempData["PasswordError"] = "Incorrect password";
                    // TempData["PasswordError"] = ViewBag.PasswordError;
                    return RedirectToAction("Index");
                }
            }
        }

        [HttpGet]
        [Route("/home")]
        public IActionResult Home()
        {
            int? userId = HttpContext.Session.GetInt32("currentUserId");
            if(userId == null)
            {
                TempData["LogErrors"] = "You need to log in first";
                return RedirectToAction("Index");
            }
            else
            {
                User currentUser = _context.Users.SingleOrDefault(u => u.UserId == (int)userId);
                DateTime now = DateTime.Now;
                List<Auction> allAuctions = _context.Auctions.OrderBy(a => a.EndDate).Where(auc => auc.EndDate > now).ToList();
                List<Auction> expiredAuctions = _context.Auctions.Where(a => a.EndDate <= now).ToList();
                foreach(var auction in expiredAuctions)
                {
                    User highestBidder = _context.Users.SingleOrDefault(u => u.FirstName == auction.HighestBidder);
                    User createdUser = _context.Users.SingleOrDefault(u => u.FirstName + " " + u.LastName == auction.CreatedUser);
                    highestBidder.Wallet -= auction.Bid;
                    createdUser.Wallet += auction.Bid;
                }
                _context.SaveChanges();

                Dictionary<int, int> remainingTime = new Dictionary<int, int>();
                foreach(var auction in allAuctions)
                {
                    remainingTime[auction.AuctionId] = (auction.EndDate - now).Days;
                }
                
                ViewBag.User = currentUser;
                ViewBag.Auctions = allAuctions;
                ViewBag.Reamining = remainingTime;
                return View();         
            }
        }

        [HttpGet]
        [Route("/createauction")]
        public IActionResult CreateAuction()
        {
            int? userId = HttpContext.Session.GetInt32("currentUserId");
            if(userId == null)
            {
                TempData["LogErrors"] = "currentUserId";
                return RedirectToAction("Index");
            }
            else
            {
                User currentUser = _context.Users.SingleOrDefault(u => u.UserId == (int)userId);
                ViewBag.User = currentUser;
                return View();
            }
        }
        [HttpPost]
        [Route("/createauction")]
        public IActionResult CreateAuction(AuctionViewModel model)
        {                        
            int? userId = HttpContext.Session.GetInt32("currentUserId");
            if(userId == null)
            {
                TempData["LogErrors"] = "You need to log in first";
                return RedirectToAction("Index");
            }
            else
            {
                User currentUser = _context.Users.SingleOrDefault(u => u.UserId == (int)userId);
                if(ModelState.IsValid)
                {
                    if(model.EndDate.Date<DateTime.Today)
                    {
                        TempData["InvalidTime"] = "Your end date has to be after today";
                        return View();
                    }
                    else
                    {
                        Auction newAuction = new Auction 
                        {
                            ProductName = model.ProductName,
                            CreatedUser = currentUser.FirstName + " " + currentUser.LastName,
                            Description = model.Description,
                            MinimumBid = model.MinimumBid,
                            EndDate = model.EndDate,
                            Created_at = DateTime.Now,
                            Updated_at = DateTime.Now
                        };
                        _context.Add(newAuction);
                        _context.SaveChanges();
                        return RedirectToAction("Home");
                    }
                }
                TempData["InvalidTime"] = "Your end date has to be after today";
                return View();
            }
        }

        [HttpGet]
        [Route("/auction/{id}")]
        public IActionResult ShowAuction(string id)
        {
            int? userId = HttpContext.Session.GetInt32("currentUserId");
            if(userId == null)
            {
                TempData["LogErrors"] = "You need to log in first";
                return RedirectToAction("Index");
            }
            else
            {
                User currentUser = _context.Users.SingleOrDefault(u => u.UserId == (int)userId);
                int auctionId = Int32.Parse(id);
                Auction showingAuction = _context.Auctions.SingleOrDefault(a => a.AuctionId == auctionId);
                ViewBag.Auction = showingAuction;
                ViewBag.User = currentUser;
                return View();
            }
        }
        [HttpPost]
        [Route("/auction/{id}")]
        public IActionResult ShowAuction(string id, string bid)
        {
            int? userId = HttpContext.Session.GetInt32("currentUserId");
            if(userId == null)
            {
                TempData["LogErrors"] = "You need to log in first";
                return RedirectToAction("Index");
            }
            else
            {
                List<string> errors = new List<string>();
                int auctionId = Int32.Parse(id);
                Auction showingAuction = _context.Auctions.SingleOrDefault(a => a.AuctionId == auctionId);
                if(bid != null){             
                    int bidAmount = Int32.Parse(bid);
                    User currentUser = _context.Users.SingleOrDefault(u => u.UserId == (int)userId);

                    if(bidAmount <= showingAuction.Bid)
                    {
                        errors.Add("You have to top the current bid");
                        ViewBag.AmountErrors = errors;
                        ViewBag.Auction = showingAuction;
                        return View();
                    } 
                    else if(bidAmount > currentUser.Wallet)
                    {
                        errors.Add("You currently do not have enough funds");
                        ViewBag.AmountErrors = errors;
                        ViewBag.Auction = showingAuction;
                        return View();
                    } 
                    else
                    {
                        showingAuction.Bid = bidAmount;
                        showingAuction.HighestBidder = currentUser.FirstName;
                        currentUser.Wallet -= bidAmount;
                        _context.SaveChanges();
                        return RedirectToAction("ShowAuction");
                    }
                } 
                else
                {
                    errors.Add("Did you forget?");
                    ViewBag.AmountErrors = errors;
                    ViewBag.Auction = showingAuction;
                    return View();
                }
            }
        }
        [HttpGet]
        [Route("logout")]
        public IActionResult Logout()
        {
            int? userId = HttpContext.Session.GetInt32("currentUserId");
            if(userId == null)
            {
                TempData["LogErrors"] = "You need to log in first";
                HttpContext.Session.Clear();
                return RedirectToAction("Index");
            }
            else
            {
                HttpContext.Session.Clear();
                return RedirectToAction("Index");
            }
        }
        [HttpGet]
        [Route("/auction/delete/{id}")]
        public IActionResult DeleteAuction(string id)
        {
            int? userId = HttpContext.Session.GetInt32("currentUserId");
            if(userId == null)
            {
                TempData["LogErrors"] = "You need to log in first";
                return RedirectToAction("Index");
            }
            else
            {
                int auctionId = Int32.Parse(id);
                Auction deletedAuction = _context.Auctions.SingleOrDefault(a => a.AuctionId == auctionId);
                _context.Auctions.Remove(deletedAuction);
                _context.SaveChanges();
                return RedirectToAction("Home");
            }
        }
    }
}
