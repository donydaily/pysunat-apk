import os
import shutil

def load_whitelist_from_file(file_path):
    """
    Load the whitelist from a text file.

    Args:
        file_path (str): The path to the text file containing folder names.

    Returns:
        list: A list of folder names.
    """
    try:
        with open(file_path, 'r') as file:
            # Membaca semua baris dan menghapus spasi di sekitar
            whitelist = [line.strip() for line in file if line.strip()]
        return whitelist
    except FileNotFoundError:
        print(f"File '{file_path}' tidak ditemukan.")
        return []

def delete_non_whitelisted_folders(whitelist, path):
    """
    Delete folders not in the whitelist from the specified path.

    Args:
        whitelist (list): List of folder names to keep.
        path (str): The directory path to check for folders.
    """
    try:
        all_folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    except FileNotFoundError:
        print(f"Path '{path}' tidak ditemukan.")
        return

    print("Folder yang ditemukan:")
    for folder in all_folders:
        print(f"- {folder}")

    confirmation = input("Apakah Anda yakin ingin menghapus folder yang tidak ada dalam whitelist? (y/n): ")
    if confirmation.lower() != 'y':
        print("Penghapusan dibatalkan.")
        return

    deleted_count = 0
    for folder in all_folders:
        if folder.lower() not in [name.lower() for name in whitelist]:  # Case insensitive comparison
            shutil.rmtree(os.path.join(path, folder))
            print(f"Folder '{folder}' telah dihapus.")
            deleted_count += 1
        else:
            print(f"Folder '{folder}' ada dalam whitelist, tidak dihapus.")

    print(f"Total folder dihapus: {deleted_count}")

# Meminta pengguna untuk memasukkan path file whitelist
whitelist_file = input("Masukkan path file whitelist (txt): ")
whitelist = load_whitelist_from_file(whitelist_file)

# Meminta pengguna untuk memasukkan path folder
path = input("Masukkan path folder yang ingin diproses: ")

# Panggil fungsi untuk menghapus folder yang tidak ada dalam whitelist
delete_non_whitelisted_folders(whitelist, path)