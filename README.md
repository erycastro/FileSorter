# FileSorter: Organize Images Based on Color Detection

File Sorter is a Python program that automatically organizes images into specific folders based on the predominant color detected in the images. The project uses the OpenCV library to analyze the images and classify them as red or blue.

## How to Use

### Step 1: Prepare Your Image Folder

Place all the images you want to classify in the input folder. The program will scan this folder and move the images to the specific folders based on the predominant color.

### Step 2: Adjust Folder Paths

In the code, adjust the paths for the input and destination folders. Open the Python script (`fsorter.py`) and modify the following lines with the correct paths for your system:

```python
input_folder = r"C:\Path\To\Images"
red_folder = r"C:\Path\To\AlgebraFolder"
blue_folder = r"C:\Path\To\PAAFolder"
```
### Step 3: Run the Code

After adjusting the folder paths, run the Python script to start the color detection and sorting process. Open a terminal or command prompt and run:

```bash
python fsorter.py
```
