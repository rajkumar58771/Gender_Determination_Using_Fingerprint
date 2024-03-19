const express = require('express');
const fs = require('fs');

const app = express();
const port = 3000;

app.get('/api/result', (req, res) => {
  // Read the content of the text file
  fs.readFile('my_file (1).txt', 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return res.status(500).send('Error reading the file');
    }

    // Split the content into an array of lines
    const dataArray = data.split('\n');

    // Send the data as JSON to the client
    res.json({ data: dataArray });
  });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
