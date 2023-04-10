import cv2
import time
import os
import argparse

def main():
    """Capture video from the Raspberry Pi camera module and optionally create a timelapse of photos.

    Args:
        --width (int): Width of the video capture in pixels (default: 640).
        --height (int): Height of the video capture in pixels (default: 480).
        --duration (int): Duration of the video in seconds (default: 86400).
        --interval (int): Interval for taking photos in seconds. Set to 0 to disable photo capture (default: 60).
        --photo_dir (str): Directory for storing photos (default: /home/pi/photos).
        --photo_prefix (str): Prefix for the photo filenames (default: timelapse_).
    """

    parser = argparse.ArgumentParser(description="Capture video from the Raspberry Pi camera module and optionally create a timelapse of photos.")
    parser.add_argument("--width", type=int, default=640, help="Width of the video capture in pixels")
    parser.add_argument("--height", type=int, default=480, help="Height of the video capture in pixels")
    parser.add_argument("--duration", type=int, default=86400, help="Duration of the video in seconds")
    parser.add_argument("--interval", type=int, default=60, help="Interval for taking photos in seconds. Set to 0 to disable photo capture.")
    parser.add_argument("--photo_dir", type=str, default="/home/pi/photos", help="Directory for storing photos")
    parser.add_argument("--photo_prefix", type=str, default="timelapse_", help="Prefix for the photo filenames")
    args = parser.parse_args()

    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)

    if not cap.isOpened():
        print("Unable to open the camera")
        return

    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    video_out = cv2.VideoWriter("video.avi", fourcc, 30.0, (args.width, args.height))

    if args.interval != 0 and not os.path.exists(args.photo_dir):
        os.makedirs(args.photo_dir)

    photo_interval = args.interval

    video_duration = args.duration

    start_time = time.time()

    photo_ext = ".jpg"

    while True:

        ret, frame = cap.read()

        if not ret:
            print("Unable to capture frame, retrying in 1 minute")
            time.sleep(60)
            continue

        video_out.write(frame)

        if photo_interval != 0 and time.time() - start_time >= photo_interval:
            photo_filename = os.path.join(args.photo_dir, f"{args.photo_prefix}{int(time.time())}{photo_ext}")
            cv2.imwrite(photo_filename, frame)

            # Check if the device is out of memory
            free_bytes = os.statvfs(args.photo_dir).f_frsize * os.statvfs(args.photo_dir).f_bavail
            if free_bytes < 0:
                # If out of memory, delete the oldest photo
                oldest_photo = min(os.listdir(args.photo_dir), key=lambda f: os.path.getctime(os.path.join(args.photo_dir, f)))
                os.remove(os.path.join(args.photo_dir, oldest_photo))

            start_time = time.time()

        if time.time() - start_time >= video_duration:
            break

    cap.release()
    video_out.release()

if __name__ == "__main__":
    main()
