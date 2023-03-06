const fs = require('fs');
const path = require('path');

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
    for (let i = 0; i < num_files; i += 1) {
        let file1 = files[i];
        let file2 = files[i + 1];
        if (!grouped_files[folder]) grouped_files[folder] = [];
        if (!file2 && file1.match(/\d+$/)) {
            // If file1 has a number at the end but file2 doesn't exist,
            // look for the next file with number 1 at the end
            let j = 0 + 1;
            while (j < num_files && !files[j].match(/1\.png$/)) {
                j++;
            }
            if (j < num_files) {
                file2 = files[j];
            }
        }
        if (file1 && file2) {
            const pair_folder = path.join('.', file1.replace(/\.png/, '') + '_' + file2.replace(/\.png/, ''));
            if (!fs.existsSync(pair_folder)) fs.mkdirSync(pair_folder);
            fs.copyFileSync(file1, path.join(pair_folder, file1));
            fs.copyFileSync(file2, path.join(pair_folder, file2));
            grouped_files[folder].push([file1, file2]);
        }
    }
}

console.log(grouped_files);
