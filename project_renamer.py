import re
import os
import shutil
import sys

# regex (?<=E\d\d)(.*)
# (?<=E\d\d)(.*) group 1 excess
# ((s|S)\d\d(e|E)\d\d)
# (.*)((s|S)\d\d(e|E)\d\d) group 1 name of file group 2 s00e00


def main():
    #print("Paste in folder directory:")
    # path : str = input()
    # rename_folder(path)
    print(
    """
    POWER RENAMER
    CERTAIN FORMAT (name_S00E00.mkv)
    TYPE exit TO EXIT
    """)
    dirFound: bool = False
    while not dirFound:
        print(u"\u001b[37;1mPaste in folder directory:")
        path: str = input()
        if os.path.isdir(path):
            create_rename_folder(path)
        elif path =="exit":
            sys.exit(0)
        else:
            print(u"\t\u001b[0mCOULD NOT FIND DIRECTORY \n\tTYPE \u001b[31;1mexit \u001b[0mTO EXIT\n")


def rename_folder(path: str):
    files = os.listdir(path)
    for fname in files:
        file_path = os.path.join(path, fname)
        if not os.path.isdir(file_path):
            _match_group = re.search(
                pattern='(?<=(e|E)\d\d)(.*)', string=fname)
            _match_name = re.search(
                pattern='(.*)((s|S)\d\d(e|E)\d\d)', string=fname)
            if not _match_group == None:
                _removeable_group = _match_group.group(0)
            if not _match_name == None:
                _removeable_name = _match_name.group(0)

            # NEW PATHS
            _old_path: str = (path + "\\")
            _new_path: str = (path + "\\")

            # NEW NAMES
            _old_name: str = fname
            _new_name: str = fname.replace(_removeable_group, '').replace(
                ".", " ").replace("(", '').replace(")", '') + ".mkv"

            os.rename(_old_path + _old_name, _new_path + _new_name)
            print("Renamed " + _old_name + " to " + _new_name + ".mkv")


def create_rename_folder(path: str):

    # Rename
    rename_folder(path)

    files = os.listdir(path)
    folder_names: list[str] = []

    # Create folders
    for fname in files:
        file_path = os.path.join(path, fname)
        if not os.path.isdir(file_path):
            # Establish renames
            _match_name = re.search(
                pattern='(.*)((s|S)\d\d(e|E)\d\d)', string=fname)
            _new_folder_name: str = _match_name.group(1).upper().strip()

            # Establish paths
            _old_path = path+"\\"
            _new_path = ""

            # Checks if folder is already present
            _already_contains: bool = False
            for folder_name in folder_names:
                if _new_folder_name in folder_name:
                    _already_contains = True
                    _new_path = _old_path + folder_name
                pass
            if not (_already_contains):
                folder_names.append(_new_folder_name)
                try:
                    os.mkdir(_old_path+_new_folder_name)
                except OSError:
                    print("Creation of the directory %s failed" %
                          _old_path+_new_folder_name)
                _new_path = _old_path + _new_folder_name
                pass

            # Move and rename
            shutil.move(_old_path+fname, _new_path+"\\"+fname)
            print("Moved " + _old_path+fname + " to " + _new_path+"\\"+fname)
            pass
        else:
            print("Skipping " + file_path + " because it is a directory.")


# Defines the main function for the file.
if __name__ == "__main__":
    main()
