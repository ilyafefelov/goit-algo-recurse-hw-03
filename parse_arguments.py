import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Recursively copy and sort files by extension"
    )
    parser.add_argument("--src", type=str, help="Source directory path")
    parser.add_argument(
        "--dist", type=str, nargs="?", default="dist", help="Destination directory path"
    )
    return parser.parse_args()


def copy_files_recursively(src, dist):
    """
    Recursively copies files from the source directory to the destination directory.

    Args:
        src (str): The path of the source directory.
        dist (str): The path of the destination directory.

    Returns:
        None
    """
    
    if not os.path.exists(dist):
        print(f"Source directory '{src}' does not exist.")
        print(f"Creating directory '{src}'")
        os.makedirs(dist)

    for item in os.listdir(src):
        item_path = os.path.join(src, item)

        if os.path.isdir(item_path):
            copy_files_recursively(item_path, dist)
        else:
            file_extension = os.path.splitext(item)[1][1:]
            dest_folder = os.path.join(dist, file_extension)
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            try:
                shutil.copy2(item_path, dest_folder)
                print(f"Copied {item} to {dest_folder}")
            except Exception as e:
                print(f"Error copying {item}: {str(e)}")


def main():
    args = parse_arguments()
    copy_files_recursively(args.src, args.dist)


if __name__ == "__main__":
    main()
