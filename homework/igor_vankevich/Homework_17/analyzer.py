import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("file", help="File name")
parser.add_argument("text", help="Search text")
parser.add_argument("--full", help="Full search row", action="store_true")
args = parser.parse_args()

str_file = args.file
file = str_file.replace('\\', '/')
file_dir = os.listdir(file)

line_num = 0
for file_name in file_dir:
    file_path = os.path.join(args.file, file_name)
    with open(file_path, 'r') as file:
        line_num = 0
        for line in file:
            line_num += 1
            if args.full is True and args.text in line:
                print(f'{args.text} found in {file_name} on line {line_num}\n{line}')
            elif args.text in line:
                str_line = line
                list_line = str_line.split()
                ind_text = list_line.index(args.text)
                word_after = ind_text + 6
                word_before = ind_text - 5
                words = list_line[word_before:word_after]
                print(f'{args.text} found in {file_name} on line {line_num}\n{" ".join(words)}\n')
