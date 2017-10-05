// require express
var express = require("express");
// path module -- try to figure out where and why we use this
var path = require("path");
// create the express app
var app = express();
var bodyParser = require('body-parser');
// use it!
// new code:
var session = require('express-session');
// original code:
var app = express();
// more new code:
app.use(session({secret: 'codingdojorocks'}));  // string for encryption
app.use(bodyParser.urlencoded({ extended: true }));
// static content
app.use(express.static(path.join(__dirname, "./static")));
// setting up ejs and our views folder
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
// root route to render the index.ejs view
app.get('/', function(req, res) {

    res.render("index");
})
app.post('/process', function(req, res) {
    req.session.username= req.body.user_username;
    req.session.location= req.body.user_location;
    req.session.language= req.body.user_language;
    req.session.description= req.body.user_description;
    res.redirect("/result");
})
app.get('/result', function(req, res) {
        var results = {
        username: req.session.username,
        location: req.session.location,
        language: req.session.language,
        description: req.session.description,

    }
        res.render("result",{showresults:results});
})
app.get('/goback', function(req, res) {
    req.session.destroy();
    res.redirect('/');
})
// post route for adding a user
// app.post('/users', function(req, res) {
//  console.log("POST DATA", req.body);
//  // This is where we would add the user to the database
//  // Then redirect to the root route
//  res.redirect('/');
// })
// tell the express app to listen on port 8000
app.listen(8000, function() {
 console.log("listening on port 8000");
});