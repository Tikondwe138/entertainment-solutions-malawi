# backend/scripts/thumb_generator.py

import os
from PIL import Image

MEDIA_DIR = os.path.join(os.path.dirname(__file__), "../../media")

THUMBNAIL_SIZE = (300, 300)  # px (width, height)

def generate_thumbnails():
    for project in os.listdir(MEDIA_DIR):
        project_path = os.path.join(MEDIA_DIR, project)
        if not os.path.isdir(project_path):
            continue

        thumb_dir = os.path.join(project_path, "thumbnails")
        os.makedirs(thumb_dir, exist_ok=True)

        for file in os.listdir(project_path):
            if file.lower().endswith((".png", ".jpg", ".jpeg")):
                src = os.path.join(project_path, file)
                dst = os.path.join(thumb_dir, f"thumb_{file}")

                try:
                    img = Image.open(src)
                    img.thumbnail(THUMBNAIL_SIZE)
                    img.save(dst, "JPEG")
                    print(f"Generated thumbnail: {dst}")
                except Exception as e:
                    print(f"Failed thumbnail for {src}: {e}")


if __name__ == "__main__":
    generate_thumbnails()
