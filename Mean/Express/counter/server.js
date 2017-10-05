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
    if(!req.session.counter){
        req.session.counter = 1;
    }
    else{
        req.session.counter += 1;
    }
    var viewcounter = req.session.counter;
    res.render("index",{counter: viewcounter});
})
app.post('/', function(req, res) {
    req.session.counter += 1;
    res.redirect('/');
})
app.post('/endsession', function(req, res) {
    req.session.destroy();
    console.log("I am here")
    res.redirect("/");
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