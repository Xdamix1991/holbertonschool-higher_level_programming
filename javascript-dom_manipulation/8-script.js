const request = new Request("https://hellosalut.stefanbohacek.dev/?lang=fr");
fetch(request)
  .then((response) => {
    if (response.status === 200){
      return response.json();
    } else {
      throw new Error("Something went wrong on API server!")
    }
  })
  .then((data) => {
    const result = data.hello
    document.querySelector("header").textContent = result;
  })
  .catch((error) => {
    console.error(error);
  })
