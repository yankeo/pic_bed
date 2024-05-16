import os
import json

def scan_images(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            img_path = os.path.join(folder, filename)
            img_size = os.path.getsize(img_path)
            img_url = f"https://github.com/{os.environ['GITHUB_REPOSITORY']}/blob/main/{img_path}"
            images.append({"name": filename, "size": img_size, "url": img_url})
    return images

if __name__ == "__main__":
    folder = "pic"
    images_info = scan_images(folder)
    with open("pic.json", "w") as f:
        json.dump(images_info, f, indent=4)
