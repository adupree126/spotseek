var request = require('request'); // "Request" library

var client_id = 'e2c4afe635734040aa2ea466c44f75cd'; // Your client id
var client_secret = 'c1bed0d278484eb2b7b0f6238ac32186'; // Your secret
var playlist_id = '3AXF5oXQAu9mb4abpAxyPR'


// your application requests authorization
var authOptions = {
  url: 'https://api.spotify.com/authorize?',
  headers: {
    'Authorization': 'Basic ' + (new Buffer(client_id + ':' + client_secret).toString('base64'))
  },
  form: {
    grant_type: 'client_credentials'
  },
  json: true
};

console.log();("got here")

request.post(authOptions, function(error, response, body) {
  if (!error && response.statusCode === 200) {

    // use the access token to access the Spotify Web API
    var token = body.access_token;
    var options = {
      url: 'https://api.spotify.com/v1/playlist/' + playlist_id,
      headers: {
        'Authorization': 'Bearer ' + token
      },
      json: true
    };
    request.get(options, function(error, response, body) {
      console.log(body);
    });
  }
});
