var express = require("express");
var path = require("path");

var app = express();
var bodyParser = require('body-parser');

// Add mongoose, change DB name
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/quotingdojodb');

var MongooseSchema = new mongoose.Schema({
    name: { type: String, required: true, minlength: 3},
    age: { type: Number, required: true},
    height: { type: String, required: true},
}, {timestamps: true})

// model creation
mongoose.model('Mongoose', MongooseSchema); 

// saving the model to use later
var Mongoose = mongoose.model('Mongoose')


app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));

app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

// ** If communicationg with DB, responses should be in the callback
app.get('/', function (req, res) {

        res.render("index");
});
app.get('/quotes', function (req, res) {
    Quote.find(function(error, quotes) {
        if(error) {
            console.log("ERRORS");
            console.log(error);
        } else {
            console.log("QUOTES");
            console.log(quotes);
        }
        res.render("quotes", {quotes: quotes});
    })
});

app.post('/quotes', function (req, res) {
    console.log("POST DATA", req.body.name);

    var quote = new Quote();
    quote.name = req.body.name;
    quote.quote = req.body.quote;
    // responses inside of callback
    // JS WONT WAIT FOR YOU!!!
    quote.save(function(error) {
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