$(document).ready(() => {
    $("#add_item").click(() => {
        let myList = $(".my_list");
        myList.append("<li>Item</li>");
    })
})