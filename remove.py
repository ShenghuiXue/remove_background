from rembg import remove
from PIL import Image

# define which image need to remove the background
input_path = 'a2.jpg'
# define where the new image is going to be saved
output_path = 'a2out.png'

# open the input image
picture = Image.open(input_path)

# remove background from the old image
output = remove(picture)

# done and save the new image which have the background already removed
output.save(output_path, format='PNG', quality=95)
