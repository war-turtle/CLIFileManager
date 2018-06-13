import os
import argparse
from shutil import copyfile

parser = argparse.ArgumentParser(description="cli file manager")


def validate_file(file_name):
    if file_name.endswith('.txt') and os.path.isfile(file_name):
        return True
    else:
        print("Invalid File Name, Can't operate")
        exit()


def validate_dir(dir_name):
    if os.path.isdir(dir_name):
        return True
    else:
        print("Invalid Path Entered. Can't operate")
        exit()


def read(args):
    file_name = args.read[0]

    validate_file(file_name)

    with open(file_name, 'r') as f:
        print(f.read())


def write(args):
    file_name = args.write[0]

    validate_file(file_name)

    with open(file_name, 'w') as f:
        inp = input("Enter What to write ")
        f.write(inp)
        print("'" + inp + "'" + " successfully written in " + file_name)


def list_dir(args):
    dir_name = args.list

    validate_dir(dir_name)

    list_dir_files = os.listdir(dir_name)

    print("Items in current directory are: ")
    for i in list_dir_files:
        print(i)


def copy_file(args):
    from_file = args.copy[0]
    dest_file = args.copy[1]

    validate_file(from_file)
    validate_file(dest_file)

    copyfile(from_file, dest_file)
    print("file copied successfully")


def delete(args):
    file_name = args.delete[0]

    if os.path.isfile(file_name):
        os.remove(file_name)
        print("file removed successfully")
    else:
        print("No such file exists. Can't operate")
        exit()


def rename(args):
    file_name = args.rename[0]
    renamed_name = args.rename[1]

    os.rename(file_name, renamed_name)
    print("file renamed successfully")


parser.add_argument("--read", "-r", help="read a file in the current directory",
                    nargs=1, type=str, metavar="file_name", default=None)

parser.add_argument("--write", "-w", help="write into a file",
                    nargs=1, default=None, metavar="file_name", type=str)

parser.add_argument(
    "--list", "-l", help="list the file in the directory", nargs='?', const=os.getcwd())

parser.add_argument("--copy", "-c", help="copy a file to specified path",
                    nargs=2, type=str, metavar=("file_name", "file_name"))

parser.add_argument("--delete", "-d", help="delete a specified file",
                    nargs=1, type=str, metavar="file_name")

parser.add_argument("--rename", "-re", help="rename a file",
                    nargs=2, metavar="file_name", type=str)

args = parser.parse_args()

if args.read != None:
    read(args)
elif args.write != None:
    write(args)
elif args.list != None:
    list_dir(args)
elif args.copy != None:
    copy_file(args)
elif args.delete != None:
    delete(args)
elif args.rename != None:
    rename(args)
else:
    print("not working")
