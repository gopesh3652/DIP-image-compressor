import cv2

def compress_image(input_path, output_path, quality=95):
    image = cv2.imread(input_path)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    cv2.imwrite(output_path, image, encode_param)
