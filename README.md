# Photographer's Toolkit

🔧 **Ever-evolving toolbox**: You may expect spontaneous updates in the following years (no guarantee, but feel to leave your ideas about useful functions!)

## Photo Cleanup Script for Managing RAW files
The `photo_cleanup.py` script is designed to help you clean up your photo library by identifying and optionally deleting `.ARW` files (for Sony cameras) that do not have a corresponding `.JPG` file in the same directory or its subdirectories. This is to facilitate the clean-up of your unwanted images that take up a large amount of storage. 

### Prerequisites

- Python 3.x installed on your system.
- Basic familiarity with command line operations.

### Setup

1. Ensure Python is installed and accessible from your terminal.
2. Place the `photo_cleanup.py` script in a chosen directory.

#### Usage

Open a command prompt and navigate to the directory containing the `photo_cleanup.py` script. 

💡 For Sony users: run the script using the following command:
```shell
python photo_cleanup.py "path\to\your\photo\folder"
```

💡 For Canon users: to clean up .CR2 files, run:
```shell
python photo_cleanup.py "path\to\your\photo\folder" --extension CR2
```

💡 For Nikon users: to clean up .NEF files, run:
```shell
python photo_cleanup.py "path\to\your\photo\folder" --extension NEF
```

### Default Mode

By default, the script will first list all RAW files that would be deleted without actually removing any files. This allows you to review the files before making any changes.

### Deleting Files

If you are sure you want to delete the listed `.ARW` files directly and permanently, rerun the script with the `--delete` flag:

```shell
python photo_cleanup.py "path\to\your\photo\folder" --delete
```

🌟 Caution: use the `--delete` flag with caution, as it will permanently remove `.ARW` files that do not have a corresponding `.JPG` file from your system. 

🎨 Enjoy!
