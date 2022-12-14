from rembg import remove
from PIL import Image
import os

# get current working directory
cwd = os.getcwd()
# setup input and output directory
inputDir = cwd + "/input/"
outputDir = cwd + "/output/"

files = os.listdir(inputDir)

for fileName in files:
	# setup input file path
	input_path = inputDir + fileName
	# setup output file path
	output_path = outputDir + fileName.split('.')[0] + '.png'

	# open the input image
	picture = Image.open(input_path)
	# remove background from the old image
	output = remove(picture)

	# done and save the new image which have the background already removed
	output.save(output_path, format='PNG', quality=95)