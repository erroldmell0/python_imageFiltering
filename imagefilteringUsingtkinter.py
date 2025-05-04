
#user input
import cv2
import numpy as np
import os
from tkinter import filedialog, Tk

def apply_red_filter(image):
    filtered = image.copy()
    filtered[:, :, 1] = 0  
    filtered[:, :, 0] = 0  
    return filtered

def apply_green_filter(image):
    filtered = image.copy()
    filtered[:, :, 2] = 0  
    filtered[:, :, 0] = 0  
    return filtered

def apply_blue_filter(image):
    filtered = image.copy()
    filtered[:, :, 2] = 0  
    filtered[:, :, 1] = 0  
    return filtered

def apply_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def display_and_optionally_save(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    save = input("Do you want to save this image? (y/n): ").strip().lower()
    if save == 'y':
        filename = input("Enter filename (without extension): ").strip()
        cv2.imwrite(f"{filename}.png", image)
        print("Image saved as", filename + ".png")
 
def main():
    Tk().withdraw()

    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )

    image = cv2.imread(file_path)
    #image = cv2.resize(image , (500,500))
    display_and_optionally_save("Original Image", image)

    filter_options = {
        0: ("Original Image", lambda img: img),
        1: ("Grayscale", apply_grayscale),
        2: ("Red Filter", apply_red_filter),
        3: ("Green Filter", apply_green_filter),
        4: ("Blue Filter", apply_blue_filter)
    }

    while True:
        try:
            choice = int(input(
                "\nChoose a filter:\n"
                "0. View Original Image\n"
                "1. Grayscale\n"
                "2. Red Filter\n"
                "3. Green Filter\n"
                "4. Blue Filter\n"
                "5. Exit\n"
                "Enter your choice: "
            ))

            if choice == 5:
                print("Exiting...")
                break

            if choice in filter_options:
                name, func = filter_options[choice]
                filtered_image = func(image)
                display_and_optionally_save(name, filtered_image)
            else:
                print("Invalid choice. Enter a number between 0-5.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()