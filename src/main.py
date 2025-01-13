import os, shutil

from generate_page import copy_content, generate_page, generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists("./public"):
        shutil.rmtree("./public")

    print("Copying static files to public directory...")
    copy_content(dir_path_static, dir_path_public)
    print("Done!")

    generate_pages_recursive("./content", "./template.html", "./public")

if __name__ == "__main__":
    main()
