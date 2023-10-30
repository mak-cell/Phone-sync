import os
from ftplib import FTP
from tqdm import tqdm  # Import tqdm for progress tracking

ftp_server = "192.168.101.2"
ftp_port = 2221
ftp_username = "android"
ftp_password = "android"

def copy(local_folder, remote_folders):
    # Initialize the overall progress bar
    overall_progress = None
    total_files = 0

    for remote_folder in remote_folders:
        ftp = FTP()
        ftp.connect(ftp_server, ftp_port)
        ftp.login(ftp_username, ftp_password)
        try:
            ftp.cwd(remote_folder)
            file_list = []
            ftp.retrlines("LIST", file_list.append)
            total_files += sum(1 for item in file_list if (item.split()[-1]).endswith((".jpg", ".png")))
        except Exception as e:
            print(f"Error while accessing '{remote_folder}': {str(e)}")
        finally:
            ftp.quit()

    overall_progress = tqdm(total=total_files, unit="B", unit_scale=True, unit_divisor=1024, desc="Copying")

    for remote_folder in remote_folders:
        try:
            # Connect to the FTP server
            ftp = FTP()
            ftp.connect(ftp_server, ftp_port)
            ftp.login(ftp_username, ftp_password)

            # Attempt to change to the remote folder
            ftp.cwd(remote_folder)

            # Create the local folder if it doesn't exist
            local_folder_path = local_folder
            if not os.path.exists(local_folder_path):
                os.makedirs(local_folder_path)

            # List the files in the remote folder
            file_list = []
            ftp.retrlines("LIST", file_list.append)

            # Get a list of filenames already in the local folder
            local_files = os.listdir(local_folder_path)

            # Iterate over the remote files and download each one if it doesn't already exist locally
            for item in file_list:
                parts = item.split()
                filename = parts[-1]
                if filename.endswith(".jpg") or filename.endswith(".png"):
                    local_file_path = os.path.join(local_folder_path, filename)
                    if filename not in local_files:
                        with open(local_file_path, 'wb') as local_file:
                            ftp.retrbinary("RETR " + filename, local_file.write)
                    overall_progress.update(1)  # Increment overall progress

        except Exception as e:
            print(f"Error while copying from '{remote_folder}': {str(e)}")

        finally:
            ftp.quit()

    overall_progress.close()  # Close the overall progress bar

