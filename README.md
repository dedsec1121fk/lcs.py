### Setup

1. **Installation**:
   - First, ensure that you have Python installed on your system.
   - Copy the provided code into a Python script file (e.g., `cloud_storage.py`).

2. **Running the Program**:
   - Open your terminal or command prompt.
   - Navigate to the directory where you saved the script.
   - Run the script by typing:
     ```sh
     python cloud_storage.py
     ```

   The script will automatically install Flask if it’s not already installed and set up the necessary directory for storing files.

### Accessing the Web Interface

3. **Opening the Web Application**:
   - Once the script is running, open a web browser on your computer or any device connected to the same network.
   - Go to the following URL:
     ```
     http://0.0.0.0:8080
     ```
   - This will take you to the homepage of the local cloud storage system.

### Using the Web Interface

4. **Uploading Files**:
   - On the homepage, you'll see a section titled "Upload New File".
   - Click on the "Choose File" button to select a file from your device.
   - After selecting the file, click the "Upload" button.
   - The file will be uploaded to the local storage, and the page will refresh, showing the newly uploaded file in the list.

5. **Viewing and Downloading Files**:
   - The homepage lists all the files stored in the system, organized by file extension.
   - To download a file, simply click on the file name link. The file will be downloaded to your device.

6. **Deleting Files**:
   - Next to each file, there's a "Delete" link.
   - Click the "Delete" link to remove the file from the storage.
   - The page will refresh, and the file will no longer be listed.

### File Organization

7. **File Grouping**:
   - Files are grouped by their extensions (e.g., all `.txt` files together, all `.jpg` files together).
   - Each group is displayed in a sorted list for easy navigation.

### Important Notes

- **Storage Location**:
  - All files are stored in the directory `/storage/emulated/0/Cloud`. Make sure this path is accessible and writable.
  - If this directory doesn’t exist, the program will create it automatically.

- **Running the Server**:
  - The server runs on `0.0.0.0:8080`, making it accessible from other devices on the same network. Ensure that your firewall settings allow access to this port if you encounter connectivity issues.

### Example Usage Scenario

Imagine you have multiple devices at home, like a laptop, a smartphone, and a tablet. You can run this script on your laptop, which acts as the server. Then, from your smartphone or tablet, you can open the browser, navigate to the provided URL, and upload, download, or delete files as needed. This setup is particularly useful for quickly sharing files between devices without needing an external cloud service.

By following these steps, you can effectively use this local cloud storage system to manage and access your files conveniently from any device within your local network.
