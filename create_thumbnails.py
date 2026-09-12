#!/usr/bin/env python3
"""
Script to create thumbnails for gallery images.
This will be used locally to generate thumbnail versions of the full-size images.
"""
from PIL import Image
import os

# Images to create thumbnails for
images = [
    'assets/forever_fields_poster.png',
    'assets/ff_gardening_1.jpeg',
    'assets/ff_gardening_2.jpeg',
    'assets/ff_gardening_3.jpeg',
    'assets/ff_gardening_4.jpeg',
    'assets/ff_gardening_5.jpeg',
    'assets/ff_gardening_6.jpeg',
]

# Create thumbnails
for image_path in images:
    if os.path.exists(image_path):
        img = Image.open(image_path)
        
        # Get file name and extension
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        ext = os.path.splitext(image_path)[1]
        
        # Create thumbnail (300x300 max, maintaining aspect ratio)
        img.thumbnail((300, 300), Image.Resampling.LANCZOS)
        
        # Save thumbnail
        thumb_name = f'assets/{base_name}-thumb{ext}'
        img.save(thumb_name, quality=85, optimize=True)
        print(f'Created: {thumb_name}')
    else:
        print(f'File not found: {image_path}')

print('Thumbnails created successfully!')
