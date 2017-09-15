using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using ajaxnotes.Connectors;


namespace ajaxnotes.Controllers
{
    public class HomeController : Controller
    {
        // GET: /Home/
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            var allNotes = MySqlConnector.Query("SELECT * FROM notes");
            ViewBag.notes = allNotes;
            return View("Index");
        }

        [HttpPost]
        [Route("/addNote")]
        public IActionResult addNote(string yourtitle,string yournote)
        {
            string query = $"INSERT INTO notes (title,note) VALUES ('{yourtitle}','{yournote}')";
            MySqlConnector.Execute(query);
            return RedirectToAction("Index");
        }
        [HttpPost]
        [Route("/removeNote/{id}")]
        public IActionResult removeNote(int id)
        {
            
            string query = $"DELETE FROM notes WHERE (id='{id}')";
            MySqlConnector.Execute(query);
            return RedirectToAction("Index");
        }
    }
}

// using System.Collections.Generic;
// using AjaxNotes.Factories;
// using AjaxNotes.Models;
// using Microsoft.AspNetCore.Mvc;

// namespace AjaxNotes.Controllers
// {
//     public class NotesController : Controller
//     {

//         private readonly NoteFactory _noteFactory;

//         public NotesController(NoteFactory noteFactory)
//         {
//             _noteFactory = noteFactory;
//         }

//         [HttpGet]
//         [Route("")]
//         public IActionResult Index()
//         {
            
//             return View();
//         }

//         [HttpGet]
//         [Route("notes")]
//         public JsonResult AllNotes()
//         {
//             List<Note> AllNotes = _noteFactory.FindAll();
//             return Json(AllNotes);
//         }

//         [HttpPost]
//         [Route("newnote")]
//         public JsonResult CreateNote(Note model)
//         {
//             if(ModelState.IsValid)
//             {
//                 _noteFactory.Add(model);

//                 Note NewNote = _noteFactory.GetLatest();

//                 return Json(NewNote);
//             }
//             return Json(new {Failed = "true"});
//         }

//         [HttpPost]
//         [Route("updatenote")]
//         public void UpdateNote(Note model)
//         {
//             _noteFactory.Update(model);
//         }

//         [HttpPost]
//         [Route("deletenote/{Id}")]
//         public void DeleteNote(int Id)
//         {
//             _noteFactory.Delete(Id);
//         }
//     }
// }
