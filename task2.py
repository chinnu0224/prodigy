from PIL import Image
import numpy as np

def manipulate_pixels(pixels):
    """
    Manipulates pixels by flipping their values.
    
    Parameters:
    pixels (ndarray): The array of pixels.
    
    Returns:
    ndarray: The manipulated array of pixels.
    """
    # Flip the pixel values, can be replaced with other operations
    manipulated_pixels = np.flip(pixels, axis=1)
    
    return manipulated_pixels

def process_image(image_path, operation):
    """
    Encrypts or decrypts an image by manipulating its pixels.
    
    Parameters:
    image_path (str): The path to the image to be processed.
    operation (str): 'encrypt' or 'decrypt', the operation to perform.
    
    Returns:
    Image: The processed image.
    """
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to a numpy array
    pixels = np.array(img)
    
    # Check the operation type and call manipulate_pixels function
    if operation == 'encrypt' or operation == 'decrypt':
        processed_pixels = manipulate_pixels(pixels)
    else:
        raise ValueError("Invalid operation. Please choose 'encrypt' or 'decrypt'.")
    
    # Convert the manipulated pixels back to an image
    processed_img = Image.fromarray(processed_pixels)
    
    return processed_img

# Example usage:
# Encrypt an image
# encrypted_img = process_image('/Users/sunilvechalapu/Documents/UCD/prodigy intern/linux.jpeg', 'encrypt')
# encrypted_img.save('encrypted_image.png')

# Decrypt an image
# decrypted_img = process_image('/Users/sunilvechalapu/Documents/UCD/prodigy intern/encrypted_image.png', 'decrypt')
# decrypted_img.save('decrypted_image.png')
