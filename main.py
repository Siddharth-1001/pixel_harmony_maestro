import os

import face_recognition


def identify_person(target_image_path, root_directory):
    # Load the target image (your photo)
    target_image = face_recognition.load_image_file(target_image_path)
    target_face_encoding = face_recognition.face_encodings(target_image)[0]

    # List of supported image formats
    supported_formats = [".jpg", ".jpeg", ".png", ".gif", ".webp"]

    # Recursive function to search for images in a directory
    def search_directory(directory_path):
        for root, dirs, files in os.walk(directory_path):
            for filename in files:
                if any(filename.lower().endswith(ext) for ext in supported_formats):
                    image_path = os.path.join(root, filename)
                    unknown_image = face_recognition.load_image_file(image_path)

                    # Find face locations and encodings in the image
                    face_locations = face_recognition.face_locations(unknown_image)
                    face_encodings = face_recognition.face_encodings(
                        unknown_image, face_locations
                    )

                    for face_encoding in face_encodings:
                        # Compare the face encoding with the target
                        results = face_recognition.compare_faces(
                            [target_face_encoding], face_encoding
                        )

                        if results[0]:
                            print(f"Found a match in {image_path}")
                            # You can return or store the result as needed

    # Search in the root directory
    search_directory(root_directory)


if __name__ == "__main__":
    target_image_path = "snaps/sample.jpg"
    directory_path = "snaps"

    identify_person(target_image_path, directory_path)
