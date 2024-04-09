// // document.addEventListener('DOMContentLoaded', function () {
// //     // Replace 'scraped_data.csv' with the path to your CSV file containing scraped data
// //     const csvFilePath = 'scraped_data.csv';

// //     // Function to fetch and display CSV data
// //     function displayCSVData() {
// //         fetch(csvFilePath)
// //             .then(response => response.text())
// //             .then(data => {
// //                 const rows = data.split('\n');
// //                 const headers = rows[0].split(',');

// //                 // Populate table headers
// //                 const headerRow = document.querySelector('#data-table tr');
// //                 headers.forEach(header => {
// //                     const th = document.createElement('th');
// //                     th.textContent = header.trim();
// //                     headerRow.appendChild(th);
// //                 });

// //                 // Populate table rows
// //                 const tbody = document.querySelector('#data-table tbody');
// //                 for (let i = 1; i < rows.length; i++) {
// //                     const values = rows[i].split(',');
// //                     const tr = document.createElement('tr');

// //                     values.forEach(value => {
// //                         const td = document.createElement('td');
// //                         td.textContent = value.trim();
// //                         tr.appendChild(td);
// //                     });

// //                     tbody.appendChild(tr);
// //                 }
// //             })
// //             .catch(error => {
// //                 console.error('Error fetching CSV data:', error);
// //             });
// //     }

// //     // Call the function to display CSV data
// //     displayCSVData();
// // });

// document.addEventListener('', function () {
//     // Replace 'scraped_data.csv' with the path to your CSV file containing scraped data
//     // const csvFilePath = 'http://localhost:8000/pra1.csv';
//     const csvFilePath = '/home/lenovo/Desktop/pra1.csv';

//     function displayCSVData() {
//         fetch(csvFilePath)
//             .then(response => response.text())
//             .then(data => {
//                 const rows = data.split('\n');
//                 const headers = rows[0].split(',');

//                 const headerRow = document.querySelector('table thead tr');
//                 headers.forEach(header => {
//                     const th = document.createElement('th');
//                     th.textContent = header.trim();
//                     headerRow.appendChild(th);
//                 });

//                 const tbody = document.querySelector('table tbody');
//                 for (let i = 1; i < rows.length; i++) {
//                     const values = rows[i].split('0.0,100.0');
//                     const tr = document.createElement('tr');

//                     values.forEach(value => {
//                         const td = document.createElement('td');
//                         td.textContent = value.trim();
//                         tr.appendChild(td);
//                     });

//                     tbody.appendChild(tr);
//                 }
//             })
//             .catch(error => {
//                 console.error('Error fetching CSV data:', error);
//             });
//     }

//     displayCSVData();
// });


// document.addEventListener('DOMContentLoaded', function () {
//     const csvFilePath = 'pra1.csv'; // Replace with the correct path to your CSV file

//     function displayCSVData() {
//         fetch(csvFilePath)
//             .then(response => response.text())
//             .then(data => {
//                 const rows = data.split('\n');
//                 const headers = rows[0].split(',');

//                 const tableContainer = document.getElementById('table-container');

//                 // Create the table dynamically
//                 const table = document.createElement('table');
//                 const thead = document.createElement('thead');
//                 const tbody = document.createElement('tbody');

//                 // Populate table headers
//                 const headerRow = document.createElement('tr');
//                 headers.forEach(header => {
//                     const th = document.createElement('th');
//                     th.textContent = header.trim();
//                     headerRow.appendChild(th);
//                 });
//                 thead.appendChild(headerRow);

//                 // Populate table rows
//                 for (let i = 1; i < rows.length; i++) {
//                     const values = rows[i].split(',');
//                     const tr = document.createElement('tr');

//                     values.forEach(value => {
//                         const td = document.createElement('td');
//                         td.textContent = value.trim();
//                         tr.appendChild(td);
//                     });

//                     tbody.appendChild(tr);
//                 }

//                 // Append the table to the container
//                 table.appendChild(thead);
//                 table.appendChild(tbody);
//                 tableContainer.appendChild(table);
//             })
//             .catch(error => {
//                 console.error('Error fetching CSV data:', error);
//             });
//     }

//     // Call the function to display CSV data
//     displayCSVData();
// });


document.addEventListener('DOMContentLoaded', function () {
    const csvFilePath = 'pra1.csv'; // Replace with the correct path to your CSV file

    function displayCSVData() {
        fetch(csvFilePath)
            .then(response => response.text())
            .then(data => {
                const rows = data.split('\n');
                const headers = rows[0].split(',');

                const tableContainer = document.getElementById('table-container');

                // Create the table dynamically
                const table = document.createElement('table');
                const thead = document.createElement('thead');
                const tbody = document.createElement('tbody');

                // Populate table headers
                const headerRow = document.createElement('tr');
                headers.forEach(header => {
                    const th = document.createElement('th');
                    th.textContent = header.trim();
                    headerRow.appendChild(th);
                });
                thead.appendChild(headerRow);

                // Populate table rows
                for (let i = 0; i < rows.length; i++) {
                    const values = rows[i].split(',');
                    const tr = document.createElement('tr');

                    values.forEach((value, index) => {
                        const td = document.createElement('td');

                        // Check if the column is 'images' and add an image tag
                        if (index === headers.indexOf('images')) {
                            const img = document.createElement('img');
                            img.src = value.trim();
                            img.alt = 'Product Image';
                            img.style.maxWidth = '100px'; // Set max width for the image
                            td.appendChild(img);
                        } else {
                            // For other columns, use the actual value from the CSV
                            td.textContent = value.trim();
                        }

                        tr.appendChild(td);
                    });

                    tbody.appendChild(tr);
                }

                // Append the table to the container
                table.appendChild(thead);
                table.appendChild(tbody);
                tableContainer.appendChild(table);
            })
            .catch(error => {
                console.error('Error fetching CSV data:', error);
            });
    }

    // Call the function to display CSV data
    displayCSVData();
});
