import os
from PIL import Image

directory = input("Enter the path to the folder containing images: ").strip()
print("Choose the output format:")
print("1: JPG")
print("2: PNG")
print("3: WEBP")

choice = input("Enter the number of your choice: ").strip()
formats = {"1": "jpg", "2": "png", "3": "webp"}

if choice not in formats:
    print("Invalid choice. Exiting.")
    exit()

output_format = formats[choice]

output_folder = os.path.join(directory, "converted")
os.makedirs(output_folder, exist_ok=True)

input_formats = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp", ".tiff")

for filename in os.listdir(directory):
    if filename.lower().endswith(input_formats):
        file_path = os.path.join(directory, filename)
        img = Image.open(file_path)
        base_name = os.path.splitext(filename)[0]
        save_path = os.path.join(output_folder, f"{base_name}.{output_format}")
        if output_format in ["jpg", "jpeg"] and img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(save_path, output_format.upper())
        print(f"Converted {filename} -> {base_name}.{output_format}")

print(f"All images converted to {output_format} in '{output_folder}' folder.")
