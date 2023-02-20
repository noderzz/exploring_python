from PIL import Image

# Load the character image
character_img = Image.open("character/pose0007.png")

# Loop over the mouth images and superimpose them on the character image
for i in range(1, 23):
    # Load the mouth image
    mouth_img = Image.open(f"mouths/mouth{i}.png")
    
    # Superimpose the mouth image on the character image
    character_img.paste(mouth_img, (310, 435), mask=mouth_img)
    
    # Save the resulting image as a PNG file
    character_img.save(f"frames/frame_{i:02d}.png")

    # Reset the character image for the next iteration
    character_img = Image.open("character/pose0007.png")
