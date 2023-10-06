const fs = require('fs');
const path = require('path');

const folderPath = './Code Forces/001. Level A'; // Change this to the path of the directory you want to read folder names from
const outputFile = 'Code Forces/001. Level A/names.txt';

// Read the folder names in the specified directory
fs.readdir(folderPath, (err, files) => {
  if (err) {
    console.error('Error reading directory:', err);
    return;
  }

  // Filter out only directories (folders)
  const folderNames = files.filter((file) => {
    return fs.statSync(path.join(folderPath, file)).isDirectory();
  });

  // Join folder names with newline separator
  const outputText = folderNames.join('\n');

  // Write the folder names to the output file
  fs.writeFile(outputFile, outputText, (writeErr) => {
    if (writeErr) {
      console.error('Error writing to file:', writeErr);
    } else {
      console.log(`Folder names written to ${outputFile}`);
    }
  });
});
