# Raspberry Pi Camera Timelapse Script

This Python script captures video from the Raspberry Pi camera module and optionally creates a timelapse of photos. The script can be run with various command-line options to customize the video and photo capture settings.

## Usage
python3 timelapse.py [--width WIDTH] [--height HEIGHT] [--duration DURATION] [--interval INTERVAL] [--photo_dir PHOTO_DIR] [--photo_prefix PHOTO_PREFIX]


The following command-line options are available:

* `--width WIDTH`: Width of the video capture in pixels (default: 640)
* `--height HEIGHT`: Height of the video capture in pixels (default: 480)
* `--duration DURATION`: Duration of the video in seconds (default: 86400)
* `--interval INTERVAL`: Interval for taking photos in seconds. Set to 0 to disable photo capture (default: 60)
* `--photo_dir PHOTO_DIR`: Directory for storing photos (default: /home/pi/photos)
* `--photo_prefix PHOTO_PREFIX`: Prefix for the photo filenames (default: timelapse_)

## Author

This script and README file were created by ChatGPT, a large language model trained by OpenAI.
