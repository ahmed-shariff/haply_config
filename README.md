Convenience script to setup a directory of processing sketches. 
Has two parts: 

##### Downloading files:
Downloads the files listed in the "files_list.csv" file. The csv file is expected to have the following format:

```csv
<file-name>, <url>
```
Where the `file-name` is the destination of the file downloaded from `url`.

##### Setting up symlinks:
Creates a symlink to the `code` directory in the root directory of the project.
Also creates symlink to any java files in the root directory.

Example project: https://github.com/ahmed-shariff/CanHap501_Lab_2.git

### Usage:

Install by running:
```bash
pip install git+https://github.com/ahmed-shariff/processing_config.git
```

From the root directory with the sketches, run:
```bash
processing-config
```
