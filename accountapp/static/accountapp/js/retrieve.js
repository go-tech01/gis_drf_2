function initialize(pk) {
    axios.get('/profiles/' + pk )
        .then(function (response) {
            // handle success
            console.log(response);
            document.getElementById('image').src = response.data['image'];
            document.getElementById('nickname').innerHTML = response.data['nickname'];
            document.getElementById('message').innerHTML = response.data['message'];
        })
        .catch(function (error) {
            // handle error
            console.log(error);
        })
        .then(function () {
            // always executed
        });
}