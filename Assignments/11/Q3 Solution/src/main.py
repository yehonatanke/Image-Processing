from error_diffusion import process_image


def main():
    image_path_01 = 'input/lena.gif'
    image_path_02 = 'input/cameraman.jpg'
    image_path_03 = 'input/tungsten_original.JPG'

    for m in range(2, 6):
        process_image(image_path_01, m)
        process_image(image_path_02, m)
        process_image(image_path_03, m)


if __name__ == "__main__":
    main()
