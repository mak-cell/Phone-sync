import os
from ftplib import FTP
from tqdm import tqdm
import logging
from datetime import datetime

# Configure logging
log_folder = "logs"  # Change this to your desired log folder
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

log_filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_logs.log"
log_filepath = os.path.join(log_folder, log_filename)

logging.basicConfig(filename=log_filepath, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

ftp_server = "192.168.101.3"
ftp_port = 2221
ftp_username = "android"
ftp_password = "android"
def copy(local_folder, remote_folders):
    # Initialize the overall progress bar
    overall_progress = None
    total_files = 0

    # Set up FTP connection outside the loop
    ftp = FTP()
    ftp.connect(ftp_server, ftp_port)
    ftp.login(ftp_username, ftp_password)

    try:
        for remote_folder in remote_folders:
            try:
                ftp.cwd(remote_folder)
                file_list = []
                ftp.retrlines("LIST", file_list.append)
                total_files += sum(1 for item in file_list if (item.split()[-1]).endswith((".jpg", ".png", "mp4")))
            except Exception as e:
                logger.error(f"Error while accessing '{remote_folder}': {str(e)}")
                continue  # Skip to the next folder if it does not exist

        # Create the local folder if it doesn't exist
        local_folder_path = local_folder
        if not os.path.exists(local_folder_path):
            os.makedirs(local_folder_path)

        overall_progress = tqdm(total=total_files, unit="B", unit_scale=True, unit_divisor=1024, desc="Copying")

        local_videos_folder = os.path.join(local_folder, "Videos")

        # Create a "Videos" folder if it doesn't exist in the local folder
        if not os.path.exists(local_videos_folder):
            os.makedirs(local_videos_folder)

        for remote_folder in remote_folders:
            try:
                ftp = FTP()
                ftp.connect(ftp_server, ftp_port)
                ftp.login(ftp_username, ftp_password)
                ftp.cwd(remote_folder)
                file_list = []
                ftp.retrlines("LIST", file_list.append)
                # Get a list of filenames already in the local videos folder
                local_video_files = os.listdir(local_videos_folder)

                # Get a list of filenames already in the local folder
                local_files = os.listdir(local_folder_path)

                for item in file_list:
                    parts = item.split()
                    filename = parts[-1]
                    local_file_path = os.path.join(local_folder_path, filename)

                    if filename.endswith((".jpg", ".png")):
                        if filename not in local_files:
                            with open(local_file_path, 'wb') as local_file:
                                ftp.retrbinary("RETR " + filename, local_file.write)
                            logger.info(f"Copied: {filename}")
                            overall_progress.update(1)  # Increment overall progress
                        

                    elif filename.endswith(".mp4"):
                        local_file_path = os.path.join(local_videos_folder, filename)
                        if filename not in local_video_files:
                            with open(local_file_path, 'wb') as local_file:
                                ftp.retrbinary("RETR " + filename, local_file.write)
                            logger.info(f"Copied: {filename}")
                            overall_progress.update(1)  # Increment overall progress
                            

            except Exception as e:
                logger.error(f"Error while copying from '{remote_folder}': {str(e)}")

        overall_progress.close()  # Close the overall progress bar

    finally:
        ftp.quit()