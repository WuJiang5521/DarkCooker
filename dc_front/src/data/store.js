class Store {
  send = (method, url, data, callback) => {
    console.log("send");
    fetch('http://127.0.0.1:2019' + url, {
      body: JSON.stringify(data),
      cache: 'no-cache',
      credentials: 'same-origin',
      headers: {
        'user-agent': 'Mozilla/4.0 MDN Example',
        'content-type': 'application/json'
      },
      method: method,
      mode: 'cors',
      redirect: 'follow',
      referrer: 'no-referrer',
    })
      .then(response => {
        console.log(response);
      })
  };

  handleChange = key => params => {
    switch (key) {
      case "TryConnecting":
        this.send("POST", "/connect", {
          type: "msg",
          info: "Hello!",
        });
        break;
      default:
        console.log(`"${key}" is not a valid request key to change.`);
        break;
    }
  }
}

const store = new Store();

export default store;