#!/usr/bin/env python3
"""
Create button icons for the YouTube Downloader
Generates PNG icons for stop, resume, and network test buttons
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(text, filename, bg_color="#ffffff", text_color="#000000", size=(32, 32)):
    """Create a simple icon with text"""
    # Create image with background
    img = Image.new('RGBA', size, bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a system font, fallback to default
    try:
        # Try different font options
        font_options = [
            ("arial.ttf", 20),
            ("segoeui.ttf", 18),
            ("calibri.ttf", 18),
            ("tahoma.ttf", 18),
        ]
        
        font = None
        for font_name, font_size in font_options:
            try:
                font = ImageFont.truetype(font_name, font_size)
                break
            except:
                continue
        
        if font is None:
            font = ImageFont.load_default()
    except:
        font = ImageFont.load_default()
    
    # Calculate text position to center it
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    
    # Draw text
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Save icon
    img.save(filename, 'PNG')
    print(f"Created icon: {filename}")

def create_stop_icon():
    """Create stop icon (red square)"""
    size = (32, 32)
    img = Image.new('RGBA', size, (220, 53, 69, 255))  # Red background
    draw = ImageDraw.Draw(img)
    
    # Draw white square in center
    margin = 6
    draw.rectangle([margin, margin, size[0]-margin, size[1]-margin], fill='white')
    
    img.save('stop_icon.png', 'PNG')
    print("Created stop icon: stop_icon.png")

def create_resume_icon():
    """Create resume icon (green play button)"""
    size = (32, 32)
    img = Image.new('RGBA', size, (40, 167, 69, 255))  # Green background
    draw = ImageDraw.Draw(img)
    
    # Draw white play triangle
    margin = 8
    points = [
        (margin, margin),
        (margin, size[1] - margin),
        (size[0] - margin, size[1] // 2)
    ]
    draw.polygon(points, fill='white')
    
    img.save('resume_icon.png', 'PNG')
    print("Created resume icon: resume_icon.png")

def create_network_icon():
    """Create network test icon (globe)"""
    size = (32, 32)
    img = Image.new('RGBA', size, (0, 123, 255, 255))  # Blue background
    draw = ImageDraw.Draw(img)
    
    # Draw simple globe (circle with lines)
    center = (size[0] // 2, size[1] // 2)
    radius = 12
    
    # Draw circle
    draw.ellipse([center[0]-radius, center[1]-radius, 
                  center[0]+radius, center[1]+radius], 
                 outline='white', width=2)
    
    # Draw horizontal lines
    for i in range(-2, 3):
        y = center[1] + i * 3
        if y > center[1] - radius and y < center[1] + radius:
            x1 = center[0] - int((radius**2 - (y - center[1])**2)**0.5)
            x2 = center[0] + int((radius**2 - (y - center[1])**2)**0.5)
            draw.line([(x1, y), (x2, y)], fill='white', width=1)
    
    img.save('network_icon.png', 'PNG')
    print("Created network icon: network_icon.png")

def create_download_icon():
    """Create download icon (blue arrow down)"""
    size = (32, 32)
    img = Image.new('RGBA', size, (25, 118, 210, 255))  # Blue background
    draw = ImageDraw.Draw(img)
    
    # Draw white arrow down
    margin = 8
    center = (size[0] // 2, size[1] // 2)
    
    # Arrow shaft
    draw.rectangle([center[0]-2, margin, center[0]+2, size[1]-margin-6], fill='white')
    # Arrow head
    points = [
        (center[0], size[1] - margin),
        (center[0] - 6, size[1] - margin - 6),
        (center[0] + 6, size[1] - margin - 6)
    ]
    draw.polygon(points, fill='white')
    
    img.save('download_icon.png', 'PNG')
    print("Created download icon: download_icon.png")

def main():
    """Create all icons"""
    print("Creating button icons for YouDownload...")
    
    # Create directory for icons if it doesn't exist
    icons_dir = "icons"
    if not os.path.exists(icons_dir):
        os.makedirs(icons_dir)
    
    # Change to icons directory
    os.chdir(icons_dir)
    
    # Create icons
    create_stop_icon()
    create_resume_icon()
    create_network_icon()
    
    # Create simple text icons as fallback
    create_icon("⏹", "stop_text.png", "#dc3545", "white")
    create_icon("⏯", "resume_text.png", "#28a745", "white")
    create_icon("🌐", "network_text.png", "#007bff", "white")
    create_icon("▶", "download_text.png", "#1976d2", "white")
    
    print("\nAll icons created successfully!")
    print("Icons are saved in the 'icons' directory.")
    print("\nYou can use these icons in your application or")
    print("continue using the Unicode symbols in the button text.")

if __name__ == "__main__":
    main() 