from PIL import Image
 #-*- coding: utf-8 -*

def zoom_picture(path,width,height):
    pic=Image.open(path)
    pic=pic.resize((width,height))
    pic.save(path)

def rotate(path):
    pic=Image.open(path)
    pic=pic.rotate(90)
    pic.save(path)
    
'''
if  __name__ == "__main__":
    path='C:\study\chengnuoshi.jpg'
    #zoom_picture(path,1200,840)
    rotate(path)
'''