function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

var check = getCookie('drf_token');

// get 기반 token 주인의 pk 획득

axios({
    method: 'get',
    url: '/accounts/',

})

if (check !== undefined) {
    document.getElementById('signup_button').innerHTML =
        "<a href=\"/accounts/retrieve_template/\">\n" +
        "                MyPage\n" +
        "            </a>";
    document.getElementById('login_button').innerHTML =
        "<a href=\"/accounts/logout_template/\">\n" +
        "                Logout\n" +
        "            </a>";
}