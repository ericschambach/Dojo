using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System;
 
namespace dojodachi.Controllers
{
    public class dojodachiController : Controller
    {
        private Random rand = new Random();
        
        // A GET method
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            int? fullness = HttpContext.Session.GetInt32("Fullness");
            if(fullness == null)
            {
                fullness = 20;
            }
            int? happiness = HttpContext.Session.GetInt32("Happiness");
            if(happiness == null)
            {
                happiness = 20;
            }
            int? meals = HttpContext.Session.GetInt32("Meals");
            if(meals == null)
            {
                meals = 3;
            }
            int? energy = HttpContext.Session.GetInt32("Energy");
            if(energy == null)
            {
                energy = 50;
            }
            string status = HttpContext.Session.GetString("Status");
            if(status == null)
            {
                status = "Welcome!";
            }
            string picture = HttpContext.Session.GetString("Picture");
            if(picture == null)
            {
                picture = "~/img/welcome.jpg";
            }

            ViewBag.fullness = fullness;
            ViewBag.happiness = happiness;
            ViewBag.meals = meals;
            ViewBag.energy = energy;
            ViewBag.status = status;
            ViewBag.picture = picture;
            HttpContext.Session.SetInt32("Fullness",(int)fullness);
            HttpContext.Session.SetInt32("Happiness",(int)happiness);
            HttpContext.Session.SetInt32("Meals",(int)meals);
            HttpContext.Session.SetInt32("Energy",(int)energy);
            HttpContext.Session.SetString("Status",(string)status);
            HttpContext.Session.SetString("Picture",(string)picture);
            return View("index");
        }

        [HttpPost]
        [Route("/feed")]
        public IActionResult feed()
        {
            string status = HttpContext.Session.GetString("Status");
            int? meals = HttpContext.Session.GetInt32("Meals");               
            if(meals < 1)
            {
                string picture = "~/img/hungry.jpg";
                HttpContext.Session.SetString("Picture",(string)picture);
                status = "You do not have any meals left to eat!";
                HttpContext.Session.SetString("Status",(string)status);                
                return RedirectToAction("index");
            } 
            else
            {
                int liked = rand.Next(0,4);
                int mealsLoss = -1;
                meals += mealsLoss;
                HttpContext.Session.SetInt32("Meals",(int)meals);
                if(liked < 1)
                {
                    string picture = "~/img/eatingsad.jpg";
                    HttpContext.Session.SetString("Picture",(string)picture);
                    status = $"You have fed your doji however he did not like it: Meals {mealsLoss}";
                    HttpContext.Session.SetString("Status",(string)status);
                    return RedirectToAction("index");
                    
                }
                else
                {
                    string picture = "~/img/eating.jpg";
                    HttpContext.Session.SetString("Picture",(string)picture);
                    int? fullness = HttpContext.Session.GetInt32("Fullness");
                    int fullnessGain = rand.Next(5,11);
                    fullness += fullnessGain;
                    status = $"You have fed your doji however he loved it: Meals {mealsLoss}, Fullness {fullnessGain}";                    
                    HttpContext.Session.SetInt32("Fullness",(int)fullness);
                    HttpContext.Session.SetString("Status",(string)status);
                    return RedirectToAction("index");
                }
            }
        }

        [HttpPost]
        [Route("/play")]
        public IActionResult play()
        {
            string status = HttpContext.Session.GetString("Status");              
            int? energy = HttpContext.Session.GetInt32("Energy");
            int energyLoss = -5;     
            energy += energyLoss;
            HttpContext.Session.SetInt32("Energy",(int)energy);     
            int liked = rand.Next(0,4);
            if(liked < 1)
            {
                string picture = "~/img/playsad.jpg";
                HttpContext.Session.SetString("Picture",(string)picture);
                status = $"You have played with your Dojodoji however he did not like it: Energy {energyLoss}";
                HttpContext.Session.SetString("Status",(string)status);
                return RedirectToAction("index");
                
            }
            else
            {
                string picture = "~/img/play.jpg";
                HttpContext.Session.SetString("Picture",(string)picture);
                int? happiness = HttpContext.Session.GetInt32("Happiness");
                int happinessGain = rand.Next(5,11);
                happiness += happinessGain;
                status = $"You have fed your doji and he very much liked it: Happiness {happinessGain}, Energy {energyLoss}";
                HttpContext.Session.SetInt32("Happiness",(int)happiness);
                HttpContext.Session.SetString("Status",(string)status);
                return RedirectToAction("index");
            }
        }

        [HttpPost]
        [Route("/work")]
        public IActionResult work()
        {
            string picture = "~/img/working.jpg";
            HttpContext.Session.SetString("Picture",(string)picture);
            string status = HttpContext.Session.GetString("Status");              
            int? energy = HttpContext.Session.GetInt32("Energy");
            int? meals = HttpContext.Session.GetInt32("Meals");
            int energyLoss = -5;
            int mealsGain = rand.Next(1,4);  
            energy += energyLoss;
            meals += mealsGain;
            status = $"You have worked hard: Meals {mealsGain}, Energy {energyLoss}";
            HttpContext.Session.SetString("Status",(string)status);            
            HttpContext.Session.SetInt32("Energy",(int)energy);     
            HttpContext.Session.SetInt32("Meals",(int)meals);     
            return RedirectToAction("index");

        }
        [HttpPost]
        [Route("/sleep")]
        public IActionResult sleep()
        {
            string picture = "~/img/sleeping.jpg";
            HttpContext.Session.SetString("Picture",(string)picture);
            string status = HttpContext.Session.GetString("Status");              
            int? energy = HttpContext.Session.GetInt32("Energy");
            int? fullness = HttpContext.Session.GetInt32("Fullness");
            int? happiness = HttpContext.Session.GetInt32("Happiness");
            int energyGain = 15;
            int fullnessLoss = -5;
            int happinessLoss = -5;
            energy += energyGain;
            fullness += fullnessLoss;
            happiness += happinessLoss;
            status = $"You have slept a lot: Energy {energyGain}, Fullness {fullnessLoss}, Happiness {happinessLoss}";
            HttpContext.Session.SetString("Status",(string)status);            
            HttpContext.Session.SetInt32("Energy",(int)energy);     
            HttpContext.Session.SetInt32("Fullness",(int)fullness);     
            HttpContext.Session.SetInt32("Happiness",(int)happiness);     
            return RedirectToAction("index");

        }

        [HttpPost]
        [Route("/clear")]
        public IActionResult clear()
        {
    
            HttpContext.Session.Clear();
            return RedirectToAction("index");

        }

    // A POST method
        // [HttpPost]
        // [Route("process")]
        // public IActionResult process()
        // {
        //     int? fullness = HttpContext.Session.GetInt32("Fullness");
        //     if(fullness == null)
        //     {
        //         fullness = 20;
        //     }
        //     int? happiness = HttpContext.Session.GetInt32("Happiness");
        //     if(happiness == null)
        //     {
        //         happiness = 20;
        //     }
        //     int? meals = HttpContext.Session.GetInt32("Meals");
        //     if(meals == null)
        //     {
        //         meals = 50;
        //     }
        //     int? energy = HttpContext.Session.GetInt32("Energy");
        //     if(energy == null)
        //     {
        //         energy = 3;
        //     }
            
        //     return View("index");
        // }

        // [HttpGet]
        // [Route("template/{Name}")]
        // public IActionResult Method(string Name)
        // {
        //     // Method body
        // }

        // 7 - Json examples
        // - On controller

        // [HttpGet]
        // [Route("")]
        // public JsonResult Example()
        // {
        //     // The Json method convert the object passed to it into JSON
        //     return Json(SomeC#Object);
        // }
        // '-------------------------'
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
