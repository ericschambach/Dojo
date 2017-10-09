var express = require("express");
var path = require("path");

var app = express();
var bodyParser = require('body-parser');

// Add mongoose, change DB name
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/testOct');

var UserSchema = new mongoose.Schema({
    name: String,
    age: Number,
})

// model creation
mongoose.model('User', UserSchema); 

// saving the model to use later
var User = mongoose.model('User')

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));

app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

// ** If communicationg with DB, responses should be in the callback
app.get('/', function (req, res) {
    User.find(function(error, users) {
        if(error) {
            console.log("ERRORS");
            console.log(error);
        } else {
            console.log("USERS");
            console.log(users);
        }
        res.render("index", {users: users});
    })
});

app.post('/users', function (req, res) {
    console.log("POST DATA", req.body.username);

    var user = new User();
    user.name = req.body.name;
    user.age = req.body.age;
    // responses inside of callback
    // JS WONT WAIT FOR YOU!!!
    user.save(function(error) {
        if(error) {
            console.log(error)
            res.redirect('/');
        } else {
            console.log("no errors")
            res.redirect('/');
        }
    })
    console.log("outside save")
})

app.listen(8000, function () {
    console.log("listening on port 8000");
});