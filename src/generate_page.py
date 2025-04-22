import htmlnode
import textnode
import inline_markdown
import static_import
import os
import shutil


from pathlib import Path

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        if ":Zone.Identifier" in filename:
            continue

        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        
        if os.path.isfile(from_path):
            # Check if it's a binary file
            if from_path.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                # Make sure the destination directory exists
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                # Copy binary files directly
                shutil.copy2(from_path, dest_path)
                print(f"Copied binary file: {from_path} -> {dest_path}")
            else:
                # Process text files with generate_page
                dest_path = Path(dest_path).with_suffix(".html")
                generate_page(from_path, template_path, dest_path, basepath)
        else:
            # Handle directories recursively
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(from_path, template_path, dest_path, basepath)


def generate_page(from_path, template_path, dest_path, basepath):
    static_import.pub_copy(static_import.stat_path, static_import.pub_path)

    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    if not os.path.exists(template_path):
        print('no template path')

    

    if not os.path.exists(from_path):
        raise FileNotFoundError(f'{from_path} One or more required files are missing!')

    with open(from_path, 'r') as file:
        initial_file = file.read()

    with open(template_path, 'r') as t_file:
        template_content = t_file.read()


    html_string = inline_markdown.markdown_to_html_node(initial_file)
    html_string = html_string.to_html()

    title = inline_markdown.extract_title(initial_file)
    
    work_file = template_content.replace('{{ Title }}', title)
    work_file = work_file.replace('{{ Content }}', html_string)
    work_file = work_file.replace('href="/', 'href="' + basepath)
    work_file = work_file.replace('src="/', 'src="' + basepath)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as dest:
        dest.write(work_file)

