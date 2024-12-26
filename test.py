import os

def rename_photos(folder_path):
    try:
        # Get a list of files in the folder
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        
        # Filter for image files (you can add more extensions if needed)
        image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')
        photos = [f for f in files if f.lower().endswith(image_extensions)]

        # Rename each photo
        for index, photo in enumerate(photos, start=1):
            old_path = os.path.join(folder_path, photo)
            new_name = f"{index+20}{os.path.splitext(photo)[1]}"  # Keep the original file extension
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)

        print(f"Renamed {len(photos)} photos successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_folder_path' with the actual folder path
folder_path = "photos"
rename_photos(folder_path)
