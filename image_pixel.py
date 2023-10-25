from PIL import Image
import numpy as np
image1 = Image.open('d:/pythondata/sample_image.bmp')
array1 = np.array(image1)
print(array1)