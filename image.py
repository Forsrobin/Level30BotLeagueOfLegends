import numpy as np
import PIL

image = PIL.Image.open("cVuXE.png")

image_data = np.asarray(image)
image_data_blue = image_data[:,:,2]

median_blue = np.median(image_data_blue)

non_empty_columns = np.where(image_data_blue.max(axis=0)>median_blue)[0]
non_empty_rows = np.where(image_data_blue.max(axis=1)>median_blue)[0]

boundingBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))

print(boundingBox)