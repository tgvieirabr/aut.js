const fs = require('fs');
const path = require('path');

const dir = fs.readdirSync('.');

const files = dir.filter(file => file.endsWith('png'));

const ordered_files = {};

for (let file of files) {
  const folder = file.replace(/\d+\.png/, '');
  const number = file.match(/(\d+)\.png/);
  if (!number) continue; // ignorar arquivos sem número
  const num = number[1];
  ordered_files[folder] = ordered_files[folder] || [];
  ordered_files[folder][num] = file;
}

const pairs = [];

for (let folder in ordered_files) {
  const files = ordered_files[folder];
  const num_files = Object.keys(files).length;
  for (let i = 0; i < num_files; i += 2) {
    const file1 = files[i];
    const file2 = files[i + 1];

    
    const pair_folder = path.join('.', file1.replace(/\.png/, '') + '_' + file2.replace(/\.png/, ''));
    fs.mkdirSync(pair_folder);
    fs.renameSync(file1, path.join(pair_folder, file1));
    fs.renameSync(file2, path.join(pair_folder, file2));
    pairs.push(pair_folder);
  }
}

console.log(pairs);
