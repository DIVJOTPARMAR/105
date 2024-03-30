import os
import cv2


path = "Images/"


images = []


for file in os.listdir(path):
    
    name, ext = os.path.splitext("PRO-C105-Project-Images-main/Images/111.jpg")
    name, ext = os.path.splitext("PRO-C105-Project-Images-main/Images/112.jpg")
    name, ext = os.path.splitext("PRO-C105-Project-Images-main/Images/113.jpg")
    name, ext = os.path.splitext("PRO-C105-Project-Images-main/Images/114.jpg")
    name, ext = os.path.splitext("PRO-C105-Project-Images-main/Images/115.jpg")
    name, ext = os.path.splitext("PRO-C105-Project-Images-main/Images/116.jpg")
    name, ext = os.path.splitext("PRO-C105-Project-Images-main/Images/117.jpg")
    name, ext = os.path.splitext("PRO-C105-Project-Images-main/Images/118.jpg")
    name, ext = os.path.splitext("PRO-C105-Project-Images-main/Images/119.jpg")
    name, ext = os.path.splitext("PRO-C105-Project-Images-main/Images/120.jpg")
    
    if ext.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
        
        file_name = os.path.join(path, file)
       
        print(file_name)
        
        images.append(file_name)


count = len(images)


frame = cv2.imread(images[0])


height, width, channels = frame.shape

size = (width, height)

print(size)


out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)


for i in range(0, count):
    
    img = cv2.imread(images[i])
    
    out.write(img)


print("Done")


out.release()
