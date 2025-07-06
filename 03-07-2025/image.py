import os
from PIL import Image

def batch_resize_images(input_folder, output_folder, new_size, output_format=None, quality=85):
    """
    Resize and convert all images in a folder
    
    Parameters:
    - input_folder: Path to folder containing original images
    - output_folder: Path to save resized images
    - new_size: Tuple of (width, height) in pixels for the output size
    - output_format: Optional format to convert to (e.g., 'JPEG', 'PNG'). 
                    If None, keeps original format.
    - quality: Quality for JPEG images (1-100)
    """
    
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Get list of image files in input folder
    image_files = [f for f in os.listdir(input_folder) 
                  if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff'))]
    
    if not image_files:
        print(f"No image files found in {input_folder}")
        return
    
    print(f"Processing {len(image_files)} images...")
    
    for filename in image_files:
        try:
            # Open the image file
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            
            # Resize the image
            resized_img = img.resize(new_size, Image.LANCZOS)
            
            # Determine output format
            name, ext = os.path.splitext(filename)
            if output_format is None:
                output_format = ext[1:].upper()  # Remove dot and convert to uppercase
            
            # Handle format-specific cases
            save_kwargs = {}
            if output_format.upper() == 'JPEG':
                save_kwargs['quality'] = quality
                if img.mode in ('RGBA', 'LA'):
                    # Convert to RGB if image has transparency
                    resized_img = resized_img.convert('RGB')
            
            # Save the resized image
            output_filename = f"{name}.{output_format.lower()}"
            output_path = os.path.join(output_folder, output_filename)
            resized_img.save(output_path, format=output_format, **save_kwargs)
            
            print(f"Processed: {filename} -> {output_filename}")
            
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
    
    print("Batch processing complete!")

if __name__ == "__main__":
    # Example usage
    input_dir = "input_images"  # Folder containing original images
    output_dir = "output_images"  # Folder to save resized images
    target_size = (800, 600)  # Target width and height in pixels
    
    # Optional: convert all images to JPEG
    # output_format = "JPEG"
    output_format = None  # Keep original format
    
    batch_resize_images(input_dir, output_dir, target_size, output_format)