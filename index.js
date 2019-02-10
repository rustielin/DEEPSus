const express = require('express');
const path = require('path');

const app = express();

// Imports the Google Cloud client library
const {Storage} = require('@google-cloud/storage');

// -------------------GCS----------------
 
const projectId = 'HackDavis';
 
const storage = new Storage({
  projectId: projectId,
});
 
const bucketName = 'hack-davis-osi-bucket';

var bucket = storage.bucket(bucketName);

// -------------------EXPRESS----------------

// Serve the static files from the React app
app.use(express.static(path.join(__dirname, 'client/build')));

// helper to stream data
var stream_helper = (bucket_path, res) => {
    var remoteFile = bucket.file(bucket_path);
    var fileContents = new Buffer('');
    remoteFile.createReadStream()
    .on('error', function(err) {
        console.log(err);
    })
    .on('response', function(response) {
        // Server connected and responded with the specified status and headers.
        console.log(response);
    })
    .on('data', function(chunk) {
        fileContents = Buffer.concat([fileContents, chunk]);
        // res.write(chunk);
        // console.log(chunk);
    })
    .on('end', function() {
        // The file is fully downloaded.
        res.send(fileContents.toString('utf8'));
        console.log("DOWNLOADED");
    });
}

// fetch object
app.get('/api/getHello', (req,res) => {
    stream_helper('hello.txt', res);
});

app.get('/api/getARC', (req,res) => {
    var ret = 'data/Activities and Recreation Center_' + req.query.type + '_' + req.query.attribute;
    stream_helper(ret, res);
});

// An api endpoint that returns a short list of items
app.get('/api/getList', (req,res) => {
    var list = ["item1", "item2", "item3"];
    res.json(list);
    console.log('Sent list of items');
});

// Handles any requests that don't match the ones above
app.get('*', (req,res) =>{
    res.sendFile(path.join(__dirname+'/client/build/index.html'));
});

const port = process.env.PORT || 8080;
app.listen(port);

console.log('App is listening on port ' + port);
