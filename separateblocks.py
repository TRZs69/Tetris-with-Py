from PIL import Image
import os

# Load the image
image_path = "assets/sprites/blocks.png"  # Replace with your image path
image = Image.open(image_path)

# Get image dimensions
width, height = image.size
print(f"Image dimensions: {width}x{height}")  # For debugging

# Define block size and margins (adjust these based on your image)
block_size = 100  # Each block is approximately 100x100 pixels
margin_x = 50  # Horizontal margin between blocks and edges
margin_y = 50  # Vertical margin between blocks and edges

# Define the positions of each block in the 2x3 grid
block_positions = [
    (margin_x, margin_y, margin_x + block_size, margin_y + block_size),  # Top-left (red)
    (margin_x * 2 + block_size, margin_y, margin_x * 2 + 2 * block_size, margin_y + block_size),  # Top-middle (blue)
    (margin_x * 3 + 2 * block_size, margin_y, margin_x * 3 + 3 * block_size, margin_y + block_size),  # Top-right (green)
    (margin_x, margin_y * 2 + block_size, margin_x + block_size, margin_y * 2 + 2 * block_size),  # Bottom-left (yellow)
    (margin_x * 2 + block_size, margin_y * 2 + block_size, margin_x * 2 + 2 * block_size, margin_y * 2 + 2 * block_size),  # Bottom-middle (orange)
    (margin_x * 3 + 2 * block_size, margin_y * 2 + block_size, margin_x * 3 + 3 * block_size, margin_y * 2 + 2 * block_size)  # Bottom-right (purple)
]

# Create a directory to save the separated blocks
output_dir = "block_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Crop and save each block
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
for i, (left, top, right, bottom) in enumerate(block_positions):
    print(f"Cropping block {colors[i]} at: ({left}, {top}, {right}, {bottom})")  # For debugging
    block = image.crop((left, top, right, bottom))
    block.save(os.path.join(output_dir, f"block_{colors[i]}.png"))
    print(f"Saved block_{colors[i]}.png")

print("All blocks have been separated and saved!")