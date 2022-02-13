const form = document.querySelector("form");

      function prepareData(form) {
        const formData = new FormData(form);
        const params = new URLSearchParams(formData).toString()
        return params
      }

      function handleSubmit(event) {
        event.preventDefault();
        const data = prepareData(this)
        console.log(data);
        var xhr = new XMLHttpRequest();
        xhr.open("POST", this.action, true);
        xhr.setRequestHeader('Content-Type', this.enctype);
        xhr.send(data);
      }

      form.addEventListener("submit", handleSubmit);