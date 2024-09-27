import cv2

import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument("--webcam-resolution", default=[1280, 720], nargs=2, type=int)
    parser.add_argument(
        "--camera-index", type=int, default=0, help="Camera index to use"
    )
    args = parser.parse_args()
    return args


def list_available_cameras():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr


def main():
    args = parse_arguments()

    print("Checking available cameras...")
    available_cameras = list_available_cameras()
    print(f"Available camera indices: {available_cameras}")

    if not available_cameras:
        print("No cameras found. Please check your webcam connection.")
        return

    if args.camera_index not in available_cameras:
        print(f"Specified camera index {args.camera_index} is not available.")
        print(f"Using the first available camera: {available_cameras[0]}")
        args.camera_index = available_cameras[0]

    print(f"Attempting to open camera {args.camera_index}")
    cap = cv2.VideoCapture(args.camera_index)
    cap = cv2.VideoCapture(0)

    # Set the resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.webcam_resolution[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.webcam_resolution[1])

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()

        if not ret or frame is None:
            print("Error: Failed to capture frame.")
            break

        if frame.size == 0:
            print("Error: Captured frame is empty.")
            continue

        cv2.imshow("yolov8", frame)
        print(frame.shape)

        # if (cv2.waitKey(30)==27):
        #     break

if __name__ == "__main__":
    main()
