from PIL import Image, ImageEnhance, ImageFilter
import os
from pathlib import Path


path = "./photoeditor/imgs" 
pathOut = "./photoeditor/editedImgs" 

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

  
    edit = img.filter(ImageFilter.SHARPEN).convert('L')

 
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

   

    clean_name = os.path.splitext(filename)[0]

    edit.save(os.path.join(pathOut, f"{clean_name}_edited.jpg"))
   





