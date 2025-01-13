import os
import shutil
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str):
    print(dir_path_content)
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            generate_page(from_path, template_path, dest_path.replace(".md", ".html"))
        else:
            generate_pages_recursive(from_path, template_path, dest_path)

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file: str = ""
    template_file: str = ""
    with open(from_path, "r") as f:
        markdown_file = f.read()
    with open(template_path, "r") as f:
        template_file = f.read()

    html = markdown_to_html_node(markdown_file).to_html()
    title = extract_title(markdown_file)
    template_file = template_file.replace("{{ Title }}", title)
    template_file = template_file.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template_file)

def extract_title(markdown: str):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line[1:].strip()
    raise Exception("No header!")

def copy_content(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_content(from_path, dest_path)
