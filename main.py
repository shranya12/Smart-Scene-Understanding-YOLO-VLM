import cv2
from detector import detect_objects
from describer import SceneDescriber


def main():
    print("Starting pipeline...")

    # Initialize describer
    describer = SceneDescriber()

    # Open webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Detect objects
        objects = detect_objects(frame)

        # Analyze scene using LLM
        description, risk, level = describer.analyze_scene(objects)

        # Print output
        print("Objects:", objects)
        print("Description:", description)
        print("Risk:", risk)
        print("Level:", level)
        print("-" * 50)

        # Show webcam feed
        cv2.imshow("Smart Scene Understanding", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
