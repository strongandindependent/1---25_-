from PIL import Image, ImageFilter


def apply_filter_to_images(filter_function, image_list):
    for image_path in image_list:
        image = Image.open(image_path)
        filtered_image = filter_function(image)
        filtered_image.save(image_path)


def filter_function(image):
    img_gray_smooth = image.filter(ImageFilter.SMOOTH)
    edges_smooth = img_gray_smooth.filter(ImageFilter.FIND_EDGES)
    edges_smooth.show()
    return image


if __name__ == "__main__":
    images_to_process = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']

    apply_filter_to_images(filter_function, images_to_process)