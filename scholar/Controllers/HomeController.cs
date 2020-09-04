using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Data;
using System.Data.SqlClient;
using scholar.Entities;

namespace scholar.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public ActionResult Detail(string user)
        {
            User userModel = new User();
            Paper paperModel = new Paper();
            var userFound = userModel.getUserByUsername(user);
            var papers = paperModel.getPapersByUserid(userFound.id);
            userFound.papers = papers;
            return View(userFound);
        }

        public ActionResult Contact()
        {
            ViewBag.Message = "Your contact page.";
            return View();
        }
    }
}