$(document).ready(() => {
    $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", (data) => {
    const movies = data.results;
    let list = $("#list_movies");    
    $.each(movies, (index, movie) => { 
            list.append("<li>" + movie.title + "</li>")
        });
    }
    );
})