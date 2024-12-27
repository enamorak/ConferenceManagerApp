// Пример JavaScript для взаимодействия с сервером через AJAX
fetch('/api/events')
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => console.error('Error:', error));
