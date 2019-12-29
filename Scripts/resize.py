import os 
from PIL import Image

from resizeimage import resizeimage

def getExtension(filename):
   fileName, fileExtension = os.path.splitext(filename)
   return fileExtension

def inArray(array, to_look):
    for x in array:
	    if(to_look[1:] == x):
		    return True

def isImage(filename):
   # Extensions to search
   extensions = ['jpeg', 'jpg', 'jpe'];
   extension = getExtension(filename)
   if (inArray(extensions, extension)):
       return True
   return False

arquivos = os.listdir(os.path.expanduser(
        "/Users/guilhermeviveiros/Desktop/Scraping_Images/images"
    ))

for arquivo in arquivos:
    if(isImage(arquivo) == True):
            print(arquivo)
            img = Image.open('/Users/guilhermeviveiros/Desktop/Scraping_Images/images/'+arquivo)            
            img = img.resize((800, 800), Image.ANTIALIAS)
            img.save('/Users/guilhermeviveiros/Desktop/Scraping_Images/images/'+arquivo)
