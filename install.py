#!/usr/bin/env python3
import glob
import shutil
import os
import subprocess

PSEUDO_TYPE = "SR"  # or "FR"
ACCURACY = "standard"  # or "stringent"

PSEUDO_SUFFIX = {"standard": "_std", "stringent": "_str"}
PSEUDO_DIRS = {"SR": "ONCVPSP-PBE-SR/", "FR": "ONCVPSP-PBE-FR/"}
PSEUDO_DIR = "./pseudos/" + PSEUDO_DIRS[PSEUDO_TYPE]
PSEUDO_PATH = PSEUDO_DIR + "*/*" + PSEUDO_SUFFIX[ACCURACY] + ".upf"


def copy_pseudos():
    local_pseudo_path = "./pseudos/local/"
    for file_path in glob.glob(PSEUDO_PATH):
        file_name = os.path.split(file_path)[1]
        short_file_name = file_name.replace(PSEUDO_SUFFIX[ACCURACY], "")
        shutil.copyfile(file_path, local_pseudo_path + short_file_name)


def install_qeinput():
    subprocess.run("cd qeinput; pip install .", shell=True)


def main():
    copy_pseudos()
    install_qeinput()


if __name__ == "__main__":
    main()
