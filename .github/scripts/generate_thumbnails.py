from PIL import Image
import os

def generate_thumbnail(input_folder, output_folder, size=(128, 128)):
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            img.thumbnail(size)
            img.save(os.path.join(output_folder, filename))

if __name__ == "__main__":
    input_folder = "pic"
    output_folder = "minipic"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    generate_thumbnail(input_folder, output_folder)
