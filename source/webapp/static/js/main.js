async function addFriends(event) {
    event.preventDefault();
    let addtofriendBtn = event.target.parentElement;
    let url = addtofriendBtn.href;

    try {
        let response = await makeRequest(url, 'POST');
        let data = await response.text();
        console.log(data);
    }
    catch (error) {
        console.log(error);
    }

}


window.addEventListener('load', function() {
    const btns = document.getElementsByClassName('btn btn-primary')
    for (let btn of btns) {btn.onclick = addFriends}

});