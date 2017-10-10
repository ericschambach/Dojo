var express = require("express");
var path = require("path");

var app = express();
var bodyParser = require('body-parser');

// Add mongoose, change DB name
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/messageboarddb');  

var Schema = mongoose.Schema;
var MessageSchema = new mongoose.Schema({
        name: { type: String, required: true, minlength: 3},
        text: { type: String, required: true},
        comments: [{ type: Schema.Types.ObjectId, ref: 'Comment'}],
}, {timestamps: true})
var CommentSchema = new mongoose.Schema({
        _message: {type: Schema.Types.ObjectId, ref: 'Message'},
        name: { type: String, required: true, minlength: 3},
        text: { type: String, required: true},
}, {timestamps: true})

// model creation
mongoose.model('Message', MessageSchema);
mongoose.model('Comment', CommentSchema);  

// saving the model to use later
var Message = mongoose.model('Message')
var Comment = mongoose.model('Comment')


app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));

app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

// ** If communicationg with DB, responses should be in the callback
app.get('/', function (req, res) {
    Message.find().populate('comments').exec(function(error, message) {
        if(error) {
            console.log("ERRORS");
            console.log(error);
        } else {
        
            console.log("message");
            res.render("index", {messages: message});
        }
        console.log('Outside');
    })
});
app.post('/addmessage', function (req, res) {
        var message = new Message();
        message.name = req.body.name;
        message.text = req.body.text;
        // responses inside of callback
        // JS WONT WAIT FOR YOU!!!
        message.save(function(error) {
            if(error) {
                console.log(error)
                res.redirect('/');
            } else {
                console.log("no errors")
                res.redirect('/');
            }
        })
        console.log("outside save")
});
app.post('/addcomment/:id', function (req, res) {
        Message.findOne({_id: req.params.id}, function(error, message){
                if(error){
                        console.log(error);
                        res.redirect('/');                      
                } else {
                        var comment = new Comment(req.body);
                        comment._message = message._id;
                        comment.name = req.body.name;
                        comment.text = req.body.text;
                        // responses inside of callback
                        // JS WONT WAIT FOR YOU!!!
                        message.comments.push(comment);
                        console.log(message._id);
                        console.log(comment.text);
                        comment.save(function(error) {
                                if(error) {
                                    console.log(error);
                                    res.redirect('/');
                                } else {
                                        message.save(function(error){
                                                if(error){
                                                        console.log(error);
                                                        res.redirect('/');
                                                } else {
                                                        console.log(message.comments[0].text)
                                                        res.redirect('/');
                                                }
                                        })
                                        console.log("outside save");
                                }
                        }
                )}  
        })
});
app.listen(8000, function () {
    console.log("listening on port 8000");
});