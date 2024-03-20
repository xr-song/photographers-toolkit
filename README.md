# Photographer's Toolkit

## 🔧 Photo cleanup script for managing RAW files
`photo_cleanup.py` is designed to help you clean up your photo library by identifying and optionally deleting `.ARW` files (for Sony cameras) that do not have a corresponding `.JPG` file in the same directory or its subdirectories. This is to facilitate the clean-up of your unwanted images that take up a large amount of storage. 

### Prerequisites

- Python 3.x installed
- Basic familiarity with command line operations
- Place the `photo_cleanup.py` script in a chosen directory.

#### Usage

💡 For Sony users: 
```shell
python /path/to/photo_cleanup.py "path\to\your\photo\folder"
```

💡 For Canon users: to clean up .CR2 files, run:
```shell
python /path/to/photo_cleanup.py "path\to\your\photo\folder" --extension CR2
```

💡 For Nikon users: to clean up .NEF files, run:
```shell
python /path/to/photo_cleanup.py "path\to\your\photo\folder" --extension NEF
```

### Default mode
By default, the script will first list all RAW files that would be deleted without actually removing any files. This allows you to review the files before deletion.

### Deleting files
If you are sure you want to delete the listed `.ARW` files directly and permanently, rerun the script with the `--delete` flag:

```shell
python photo_cleanup.py "path\to\your\photo\folder" --delete
```

🌟 Caution: use the `--delete` flag with caution, as it will permanently remove the raw files. 

🎨 Enjoy!
