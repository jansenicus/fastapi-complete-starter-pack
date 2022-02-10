const form = document.querySelector("form");

      function serializeJSON(form) {
        const formData = new FormData(form);
        const pairs = {};
        for (const [name, value] of formData) {
          pairs[name] = value;
        }
        return JSON.stringify(pairs, null, 2);
      }

      function handleSubmit(event) {
        event.preventDefault();
        const data = serializeJSON(this)
        console.log(data);
        var xhr = new XMLHttpRequest();
        xhr.open("POST", form.action, true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(data);
      }

      form.addEventListener("submit", handleSubmit);