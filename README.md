
**Why this project File Organizer**: 

I chose this project because I have hobbies like video editing/content creation 
that require me to download pictures, videos, music etc. from the internet and I hated 
sorting through the default download path and moving the files from one place to another.
So I figured I would make something that does it for me! 


**Overview**:

Python script is designed to automatically organize your downloaded files based on their types. 
The script monitors a designated downloads folder and moves files to specific directories according 
to their extensions (e.g., `.png`, `.jpg`, `.mp4`, `.mp3`).

Python 3.11

**Features**:

Automatic File Organization: Files are moved to pre-defined directories based on their extensions.
Supports Multiple File Types: The script handles `.png`, `.jpeg`, `.jpg`, `.mp4`, and `.mp3` files.
Error Handling: The script includes robust error handling, retry logic, and ensures files are fully written before attempting to move them.

**Usage**: 

Install the required dependencies using "pip install watchdog". Modify the DIRECTORIES dictionary and DOWNLOADS_FOLDER path to your desired file paths and default downloads folder. After editing, run the script using "python file_organizer.py", and it will automatically organize files based on their extensions. You can add more file types by updating the DIRECTORIES dictionary. To test download something from the internet and you should see a message in your terminal saying where the file got moved to in your IDE. 


