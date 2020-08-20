const express = require('express');
const dust = require("dustjs-helpers");
const cons = require("consolidate");
const bodyParser = require("body-parser");
var path = require('path');
const app = express();

var main = require("./routes/main.js");

app.engine("dust", cons.dust);
app.set("view engine", "dust");
app.set("views", __dirname + "/views");
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use('/', main);

/*stream = new Stream({
  name: 'name',
  streamUrl: 'rtsp://admin:silucan04@192.168.0.12:554/onvif1',
  wsPort: 9999,
  ffmpegOptions: { // options ffmpeg flags
    '-stats': '', // an option with no neccessary value uses a blank string
    '-r': 30 // options with required values specify the value after the key
  }
});*/

app.listen(80, function(){
    console.log("Server encendido!");
});