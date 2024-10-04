import numpy as np
import imgaug.augmenters as iaa
import imageio
import os


# Function to load images
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = imageio.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images


# Function to save augmented images
def save_augmented_images(images, output_folder, prefix="aug_"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, img in enumerate(images):
        imageio.imwrite(os.path.join(output_folder, f"{prefix}{i}.png"), img)


# Define the augmentation pipeline
def augment_images(images, num_augmented_images):
    seq = iaa.Sequential(
        [
            iaa.Fliplr(0.5),  # Horizontal flip
            iaa.Flipud(0.5),  # Vertical flip
            iaa.Rotate((-30, 30)),  # Rotate by -30 to +30 degrees
            iaa.Scale(
                {"height": (0.5, 1.5), "width": (0.5, 1.5)}
            ),  # Randomly scale images
            iaa.AdditiveGaussianNoise(scale=(0, 0.1 * 255)),  # Add Gaussian noise
            iaa.Multiply((0.8, 1.2)),  # Change brightness
            iaa.Crop(percent=(0, 0.1)),  # Randomly crop images
        ]
    )

    augmented_images = []
    for img in images:
        for _ in range(
            num_augmented_images // len(images)
        ):  # Generate equal number of images from each input
            augmented_image = seq(image=img)
            augmented_images.append(augmented_image)

    return augmented_images


# Main function
def main(input_folder, output_folder):
    # Load images
    images = load_images_from_folder(input_folder)

    # Augment images
    augmented_images = augment_images(images, 20)  # Request 20 augmented images

    # Save augmented images
    save_augmented_images(augmented_images, output_folder)



if __name__ == "__main__":
    input_folder = "/home/fx/Desktop/akash/Study work/Study_work/face_recogniation/data/ip/"  # Update with your input folder path
    output_folder = "/home/fx/Desktop/akash/Study work/Study_work/face_recogniation/data/op/"  # Update with your output folder path

    main(input_folder, output_folder)
