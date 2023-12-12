document.addEventListener('DOMContentLoaded', function() {
//     // Logic to start the crawl
//     document.getElementById('start-crawl').addEventListener('click', function() {
//         fetch('/start_crawling', { method: 'POST' })
//             .then(response => response.json())
//             .then(data => console.log(data))
//             .catch((error) => {
//                 console.error('Error:', error);
//             });
//     });

    // Logic to stop the crawl
    document.getElementById('stop-crawl').addEventListener('click', function() {
        fetch('/stop_crawling', { method: 'POST' })
            .then(response => response.json())
            .then(data => console.log(data))
            .catch((error) => {
                console.error('Error:', error);
            });
    });

    // Logic to enqueue URL
    document.getElementById('enqueue-form').addEventListener('submit', function(e) {
        e.preventDefault();

        var url = document.getElementById('url').value;

        var data = { url: url };

        fetch('/enqueue', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
            console.error('Error:', error);
        });
    });

    document.getElementById('download-data').addEventListener('click', function() {
        fetch('/download-my-data')  // Adjust this URL to your Flask route
            .then(response => {
                if (response.ok) return response.blob();
                throw new Error('Network response was not ok.');
            })
            .then(blob => {
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.style.display = 'none';
                a.href = url;
                // Give the file a name:
                a.download = 'user_data.docx';
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
    });
});
