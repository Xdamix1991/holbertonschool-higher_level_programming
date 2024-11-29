const request = new Request("https://swapi-api.hbtn.io/api/people/5/?format=json");
fetch(request)
  .then((response) => {
    if (response.status === 200) {
      return response.json();
    } else {
      throw new Error("Something went wrong on API server!");
    }
  })
  .then((data) => {
    const name = data.name;
    document.getElementById("character").textContent = name;
  })
  .catch((error) => {
    console.error(error);
  });
