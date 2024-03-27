#!/usr/bin/node
const fs = require('fs');

// Get the file path from the command line
const filePath = process.argv[2];
const content = process.argv[3];
// Check if the file path is provided
if (!filePath) {
  console.error('Please provide the file as path argument');
  process.exit(1);
}

// write to the file content
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
