import os

folder_path = "/workspaces/32358244/image_source"
import csv
import numpy as np
from PIL import Image

def main():
    with open("views.csv", "r") as views, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames = reader.fieldnames + ["brightness"])
        writer.writeheader()


        for row in reader:
            row["brightness"]= round(calculate_brightness(f"{row['id']}.jpeg"),2)
            writer.writerow(row)
            # writer.writerow({
            #     "id": row["id"],
            #     "english_title": row["english_title"],
            #     "japanese_title": row["japanese_title"],
            #     "brightness": round(brightness,2)
            # })
            # print(round(brightness, 2))

# calculate_brightness returns a float value on a scale of 0 to 1 as how dark or bright the image is.

def calculate_brightness(filename):
    file_path = os.path.join(folder_path,filename)
    with Image.open(file_path) as image:
        # brightness returns on a scale of 0 to 1 as how bright or dark the image is
        brightness = np.mean(np.array(image.convert("L"))) / 255
        return brightness


if __name__ == "__main__":
    main()
