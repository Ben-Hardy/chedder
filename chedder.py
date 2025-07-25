#!/usr/bin/env python3

import os
import sys
import subprocess as sp


def find_valid_files(path='.'):
    valid_files = []
    for path, directories, files in os.walk(path):
        for file in files:
            if file[-4:].lower() in ['.iso', '.cue']:
                valid_files.append(os.path.join(path,file))

    return valid_files


def convert_to_chd(in_file):
    sp.run(['chdman', 'createcd', '-i', in_file, '-o', in_file.split("/")[-1][:-4] + '.chd'])


def print_help():
    print('''Welcome to Chedder, the tool for batch converting disc image files to the CHD (Compressed Hunks of Data) format.

To run Chedder you require the chdman tool as Chedder is a convenience wrapper for it.


Options:

\t\033[1mall\033[0m: convert all ISO and CUE files in the current directory and all subdirectories to CHD

\t\033[1mall-isos\033[0m: convert all ISO images in the current directory and all subdirectories to CHD

\t\033[1mall-cues\033[0m: convert all CUE images in the current directory and all subdirectories to CHD


Example Usage:
\t\033[1mchedder all\033[0m''')


def process_input():
    args = sys.argv

    if len(args) >= 2:
        files = find_valid_files()

        if args[1] in ['help', '--help', '-h', '-help']:
            print_help()
        # iso and cue to chd
        # convert all disc images regardless of type to CHD
        elif args[1] == 'all':
            for file in files:
                convert_to_chd(file)
        # convert all ISOs to CHDs if they are not already CHDs
        elif args[1] == 'all-isos':
            files = [i for i in files if i.lower().endswith(".iso")]
            for file in files:
                convert_to_chd(file)
       # convert all BIN/CUE to CHD if they are not already CHDs
        elif args[1] == 'all-cues':
            files = [i for i in files if i.lower().endswith(".cue")]
            for file in files:
                convert_to_chd(file)
        else:
            print_help()
    else:
        print_help()


def main():
    process_input()


if __name__ == "__main__":
    main()
