import os
import shutil
import sys

from static_import import pub_copy
from generate_page import generate_pages_recursive

current_dir = os.getcwd()

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../content')
template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"../template.html")
default_basepath = "/"


def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    pub_copy(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)


main()
