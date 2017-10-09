var express = require("express");
var path = require("path");

var app = express();
var bodyParser = require('body-parser');

// Add mongoose, change DB name
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/mongoosedb');

var MongooseSchema = new mongoose.Schema({
    name: { type: String, required: true, minlength: 3},
    age: { type: Number, required: true},
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
    Mongoose.find(function(error, mongoose) {
        if(error) {
            console.log("ERRORS");
            console.log(error);
        } else {
            console.log("mongoose");
            console.log(mongoose);
        }
        res.render("index", {mongoose: mongoose});
    })
});
app.get('/mongoose/new', function (req, res) {
    res.render("newmango");

});

app.post('/mongooses', function (req, res) {
    console.log("POST DATA", req.body.name);

    var mongoose = new Mongoose();
    mongoose.name = req.body.name;
    mongoose.age = req.body.age;
    // responses inside of callback
    // JS WONT WAIT FOR YOU!!!
    mongoose.save(function(error) {
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

app.get('/mongooses/:id', function (req, res) {

    Mongoose.findOne({_id:req.params.id},function(error, onemongo) {
        if(error) {
            console.log("ERRORS");
            console.log(error);
        } else {
            console.log("mongoose");
            console.log(mongoose);
        }
        res.render("mongoprofile", {mongoose: onemongo});
    })
});
app.get('/mongooses/edit/:id', function (req, res) {
    
    Mongoose.findOne({_id:req.params.id},function(error, mongoupd) {
        if(error) {
            console.log("ERRORS");
            console.log(error);
        } else {
            console.log("mongoose");
            console.log(mongoose);
        }
        res.render("mongoedit", {mongoose: mongoupd});
    })
});

app.post('/mongooses', function (req, res) {
    console.log("POST DATA", req.body.name);

    var mongoose = new Mongoose();
    mongoose.name = req.body.name;
    mongoose.age = req.body.age;
    // responses inside of callback
    // JS WONT WAIT FOR YOU!!!
    mongoose.save(function(error) {
        if(error) {
            console.log(error)
            res.redirect('/');
        } else {
            console.log("no errors")
            res.redirect('/');
        }
    })
    console.log("outside save");
})
app.post('/mongooses/edit/:id', function (req, res) {
    Mongoose.findOne({_id:req.params.id},function(error,mongoose) {
        if(error) {
            console.log("ERRORS");
            console.log(error);
            res.redirect('/')
        } else {
            mongoose.name = req.body.name;
            mongoose.age = req.body.age;
            mongoose.save(function(error,mongoose) {
                if(error) {
                    console.log(error)
                    res.redirect('/');
                } else {
                    console.log("no errors")
                    res.redirect('/mongooses/'+req.params.id);
                }
            })  
        }
        console.log("outside save");
    })

})
app.post('/mongooses/destroy/:id', function (req, res) {
    Mongoose.remove({_id:req.params.id}, function(error){
        // This code will run when the DB has attempted to remove one matching record to {_id: 'insert record unique id here'}
        if(error) {
            console.log("ERRORS");
            console.log(error);
            res.redirect('/')
        } else {
            console.log("no errors")
            res.redirect('/');          
        }
    })
    console.log("outside save");
})

app.listen(8000, function () {
    console.log("listening on port 8000");
});