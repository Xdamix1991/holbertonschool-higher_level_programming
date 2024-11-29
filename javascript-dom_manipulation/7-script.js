const request = new Request("https://swapi-api.hbtn.io/api/films/?format=json");
fetch(request)
  .then((response) => {
    if (response.status === 200){
      return response.json();
    } else {
      throw new Error("Something went wrong on API server!")
    }
  })
  .then((data) => {
    const movieTitles = data.results;
    const movieList = document.getElementById("list_movies");

    movieTitles.forEach(element => {
      const newElement = document.createElement("li"); 
      newElement.textContent = element.title;
      movieList.appendChild(newElement);
    });
  })
  .catch(error => {
    console.error('Erreur:', error);
  })
