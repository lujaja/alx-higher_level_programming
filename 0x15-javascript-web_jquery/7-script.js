$(document).ready(() => {
    $.getJSON("https://swapi-api.alx-tools.com/api/people/5/?format=json",
        (data) => {
            const name = data.name;
            const character = $("#character");
            character.text(name)            
        }
    );
});