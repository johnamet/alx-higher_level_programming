#!/usr/bin/node
const fs = require('fs');

// Get the file path from the command line
const filePath = process.argv[2];

// Check if the file path is provided
if (!filePath) {
  console.error('Please provide the file as path argument');
  process.exit(1);
}

// Read the file content
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
