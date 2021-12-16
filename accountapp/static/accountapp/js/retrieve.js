function initialize(pk) {
    axios.get('/profiles/' + pk )
        .then(function (response) {
            // handle success
            console.log(response);
            document.getElementById('image').src = response.data['profile']['image'];
            document.getElementById('nickname').innerHTML = response.data['profile']['nickname'];
            document.getElementById('message').innerHTML = response.data['profile']['message'];
        })
        .catch(function (error) {
            // handle error
            console.log(error);
        })
        .then(function () {
            // always executed
        });
}