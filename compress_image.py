import cv2

def compress_image(input_path, output_path, compression_quality=20, max_width=800, max_height=800):
    image = cv2.imread(input_path)
    
    # Resize image if it's larger than max dimensions
    height, width = image.shape[:2]
    if height > max_height or width > max_width:
        scaling_factor = min(max_width / width, max_height / height)
        image = cv2.resize(image, (int(width * scaling_factor), int(height * scaling_factor)), interpolation=cv2.INTER_AREA)
    
    cv2.imwrite(output_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), compression_quality])
