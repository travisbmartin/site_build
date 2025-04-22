import os
import shutil
from static_import import pub_copy
import generate_page
from generate_page import generate_pages_recursive

def main():
    # Define source and destination paths
    stat_path = os.path.join(os.getcwd(), 'static')
    pub_path = os.path.join(os.getcwd(), 'public')

    if os.path.exists(pub_path):
        shutil.rmtree(pub_path)

    os.makedirs(pub_path, exist_ok=True)

    # Call the recursive copy function
    pub_copy(stat_path, pub_path)

    print("Public directory successfully built!")

# Process all markdown files in the content directory
    for root, dirs, files in os.walk('content'):
        for file in files:
            if file.endswith('.md'):
                # Construct paths
                content_path = os.path.join(root, file)

                # Determine destination path - preserve the directory structure
                # Replace 'content' with 'public' and keep the rest of the path
                dest_path = content_path.replace('content', 'public', 1)
                dest_path = os.path.splitext(dest_path)[0] + '.html'
                
                # Create the destination directory if it doesn't exist
                dest_dir = os.path.dirname(dest_path)
                os.makedirs(dest_dir, exist_ok=True)
                
                # Generate the page
                generate_pages_recursive(content_path, 'template.html', dest_path)
                print(f"Generated page: {content_path} -> {dest_path}")

if __name__ == "__main__":
    main()
