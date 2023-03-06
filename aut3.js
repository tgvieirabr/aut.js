const fs = require('fs');

const dir = fs.readdirSync('.');

const files = dir.filter(file => file.endsWith('png'));

const ordered_files = {};

for (let file of files) {
  const folder = file.replace(/\d+\.png/, '');
  const number = file.match(/(\d+)\.png/)[1];
  if (!ordered_files[folder]) ordered_files[folder] = []
  ordered_files[folder][number] = file;
}

const grouped_files = {};

for (let folder in ordered_files) {
  const files = ordered_files[folder];
  const num_files = Object.keys(files).length;
  for (let i = 0; i < num_files; i += 2) {
    const file1 = files[i];
    const file2 = files[i + 1];
    if (!grouped_files[folder]) grouped_files[folder] = [];
    grouped_files[folder].push([file1, file2]);
  }
}

console.log(grouped_files);
