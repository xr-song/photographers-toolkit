import os
import argparse
import fnmatch

def cleanup_photos(folder_path, file_extension='ARW', dry_run=True):
    arw_files_to_delete = []

    for root, _, _ in os.walk(folder_path):
        # Filter files based on the specified extension
        target_files = fnmatch.filter(os.listdir(root), f'*.{file_extension}')

        for target_file in target_files:
            # Generate the corresponding JPEG filename by replacing the extension
            base_name = os.path.splitext(target_file)[0]
            jpeg_files = [
                jpeg_file
                for jpeg_file in os.listdir(root)
                if os.path.splitext(jpeg_file)[0].lower() == base_name.lower()
                and os.path.splitext(jpeg_file)[1].lower() in {'.jpg', '.jpeg'}
            ]

            # If no matching JPEG file exists, add to the list for deletion
            if not jpeg_files:
                file_path = os.path.join(root, target_file)
                arw_files_to_delete.append(file_path)

    # Dry run or delete directly
    if dry_run:
        if arw_files_to_delete:
            print("The following files do not have a matching JPEG and will be deleted:")
            for file_path in arw_files_to_delete:
                print(file_path)
            user_input = input("Do you want to delete these files? (yes/no): ")
            if user_input.lower() == 'yes':
                for file_path in arw_files_to_delete:
                    os.remove(file_path)
                    print(f"Deleted {file_path}")
            else:
                print("No files were deleted.")
        else:
            print("No files without matching JPEGs were found.")
    else:
        for file_path in arw_files_to_delete:
            os.remove(file_path)
            print(f"Deleted {file_path}")

    print("Cleanup complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cleanup files without matching JPEG files in the current or subfolders.")
    parser.add_argument("folder_path", help="Path to the folder containing the target and JPEG files.")
    parser.add_argument("--extension", default="ARW", help="File extension of the files to clean up (default is ARW).")
    parser.add_argument("--delete", action='store_true', help="Actually delete the files instead of just listing them.")
    args = parser.parse_args()
    
    cleanup_photos(args.folder_path, args.extension.upper(), dry_run=not args.delete)
