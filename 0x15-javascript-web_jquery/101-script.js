$(document).ready(() => {
    let myList = $(".my_list");
    $("#add_item").click(() => {        
        myList.append("<li>Item</li>");
    })
    $("#remove_item").click(() => {
        $(myList + "li:last-child").remove();
    })
    $("#clear_list").click(() => {        
        myList.empty();
    })
})