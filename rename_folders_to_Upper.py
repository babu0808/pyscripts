# import os

# def rename_folders_to_uppercase(root_dir):
#     for root, dirs, _ in os.walk(root_dir, topdown=False):
#         for folder in dirs:
#             old_path = os.path.join(root, folder)
#             new_folder = folder.upper()
#             new_path = os.path.join(root, new_folder)
            
#             # Rename only if the folder name is not already uppercase
#             if old_path != new_path:
#                 try:
#                     os.rename(old_path, new_path)
#                     print(f"Renamed: {old_path} -> {new_path}")
#                 except Exception as e:
#                     print(f"Error renaming {old_path}: {e}")

# if __name__ == "__main__":
#     # root_directory = input("Enter the root directory path: ")
#     rename_folders_to_uppercase("D:\Tasks")


# import os

# def rename_folders_to_lowercase(root_dir):
#     for root, dirs, _ in os.walk(root_dir, topdown=False):
#         for folder in dirs:
#             old_path = os.path.join(root, folder)
#             new_folder = folder.lower()
#             new_path = os.path.join(root, new_folder)
            
#             # Rename only if the folder name is not already lowercase
#             if old_path != new_path:
#                 try:
#                     os.rename(old_path, new_path)
#                     print(f"Renamed: {old_path} -> {new_path}")
#                 except Exception as e:
#                     print(f"Error renaming {old_path}: {e}")

# if __name__ == "__main__":
#     # Replace with the directory you want to process
#     # rename_folders_to_lowercase("D:\\Tasks")
#     rename_folders_to_lowercase(r"D:\gaps_filliing")



import os

def rename_folders_replace_spaces(root_dir):
    for root, dirs, _ in os.walk(root_dir, topdown=False):
        for folder in dirs:
            old_path = os.path.join(root, folder)
            new_folder = folder.replace(" ", "_")
            new_path = os.path.join(root, new_folder)

            # Rename only if the folder name contains spaces
            if old_path != new_path:
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")
                except Exception as e:
                    print(f"Error renaming {old_path}: {e}")

if __name__ == "__main__":
    # Replace with the directory you want to process
    rename_folders_replace_spaces(r"D:\My_releases_gen2")

#How to run:
#& C:/Users/Bcits/AppData/Local/Programs/Python/Python312/python.exe d:/Learning/Pyscripts/rename_folders_to_Upper.py