const fs = require('fs');
const path = require('path');

const dir = fs.readdirSync('.');
const files = dir.filter(file => file.endWith('png'));

const ordered_files = {};

// agrupa os arquivos por pasta e número
for (let file of files) {
  const folder = file.replace(/\d+\.png/, '');
  const number = file.match(/(\d+)\.png/)[1];
  if (!ordered_files[folder]) ordered_files[folder] = []
  ordered_files[folder][number] = file;
}

// agrupa os arquivos em pares e move para pastas correspondentes
for (let folder in ordered_files) {
  const files = ordered_files[folder];
  const num_files = Object.keys(files).length;
  for (let i = 0; i < num_files; i += 2) {
    let file1 = files[i];
    let file2 = files[i + 1];
    if (!file2 && file1.endsWith('.png')) {
      // se o arquivo final não tiver um número, encontre o próximo arquivo com um número e agrupe
      const next_file_number = Number(file1.match(/(\d+)\.png/)[1]) + 1;
      const next_file_name = folder + next_file_number.toString().padStart(2, '0') + '.png';
      if (fs.existsSync(next_file_name)) {
        file2 = next_file_name;
      }
    }
    if (file1.endsWith('.png') && file2.endsWith('.png')) {
      const pair_folder = path.join('.', folder + file1.replace(/\.png/, '') + '_' + file2.replace(/\.png/, ''));
      if (!fs.existsSync(pair_folder)) {
        fs.mkdirSync(pair_folder);
      }
      fs.renameSync(file1, path.join(pair_folder, file1));
      fs.renameSync(file2, path.join(pair_folder, file2));
    }
  }
}
