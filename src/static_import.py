import os
import shutil

pub_path = '/home/trav/site_build/public'
stat_path = '/home/trav/site_build/static'

if os.path.exists(pub_path):
    shutil.rmtree(pub_path)

os.makedirs(pub_path)

if not os.path.exists(stat_path):
    print(f"Source path '{stat_path}' does not exist!")
    exit(1)

def pub_copy(src_path, dest_path):
    items = os.listdir(src_path)
    for item in items:
        full_item_path = os.path.join(src_path, item)  # Full path in source
        full_dest_path = os.path.join(dest_path, item)  # Full path in destination

        try:
            # Handle files
            if os.path.isfile(full_item_path):
                shutil.copy(full_item_path, full_dest_path)
                print(f"Copied file: {full_item_path} -> {full_dest_path}")

        # Handle directories
            elif os.path.isdir(full_item_path):
                if not os.path.exists(full_dest_path):  # Check if destination exists
                    os.makedirs(full_dest_path)  # Create subdirectory if needed
                pub_copy(full_item_path, full_dest_path)  # Recurse for contents

        except OSError as e:
            print(f'Error creating directory {full_dest_path}: {e}')

pub_copy(stat_path, pub_path)

