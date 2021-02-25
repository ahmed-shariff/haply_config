import click
import wget
from pathlib import Path
import os
import csv


@click.command()
def cli():
    """
    Convenience script to setup a directory of processing sketches. 
    Has two parts: 
    
    ##### Downloading files:

    Downloads the files listed in the "files_list.csv" file. The csv file is expected to have the following format:
    
    <file-name>, <url>

    Where the `file-name` is the destination of the file downloaded from `url`.
    
    ##### Setting up symlinks:

    Creates a symlink to the `code` directory in the root directory of the project.
    Also creates symlink to any java files in the root directory.
    
    Example project: https://github.com/ahmed-shariff/CanHap501_Lab_2.git

    """
    root_dir = Path().parent.absolute()

    files_list_f = Path("files_list.csv")
    if files_list_f.exists():
        with open(files_list_f) as f:
            files_list = csv.DictReader(f, ["file_name", "link"])
            for file_entry in files_list:
                file_entry_path = Path(file_entry["file_name"])
                if file_entry_path.exists():
                    print(f"File exists: {file_entry['file_name']}")
                else:
                    file_entry_path.parent.mkdir(parents=True, exist_ok=True)
                    print(f"Getting file: {file_entry['file_name']} from {file_entry['link']}")
                    wget.download(file_entry["link"], out=file_entry["file_name"])
                    print()
            

    java_files = root_dir.glob("*.java")
                    
    for pde_file in root_dir.glob("*/*.pde"):
        sketch_root = pde_file.parent
        print("Found pde file: {}".format(pde_file.relative_to(root_dir)))
        
        if (sketch_root / "code").exists():
            print("  `code` exists")
        else:
            print("  Symlink to `code`")
            os.symlink(root_dir / "code", sketch_root / "code")

        for java_file in java_files:
            if (sketch_root / java_file).exists():
                print(f"  `{java_file}` exists")
            else:
                print(f"  Symlink to `{java_file}`")
                os.symlink(root_dir / java_file, sketch_root / java_file)



if __name__ == "__main__":
    main()
