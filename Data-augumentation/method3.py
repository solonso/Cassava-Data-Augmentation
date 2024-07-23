import cv2
import sys
import os
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import random
from PIL import Image, ImageEnhance
import colorsys
import scipy as sp
import scipy.ndimage as nd
from skimage import data, io



class ImgAug():
    def __init__(self, root_path, img_name, img_path, append=0):
        self.img_name = img_name
        self.root_path = root_path
        self.img_path = img_path
        self.append = append

    def __call__(self):
        self.APP3()
    
    def APP3(self):

        def X_reflect():
            self.append += 1
            decision = random.choice([True, False])
            img = cv2.imread(self.img_path)
            #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)            
            if decision == True:
                plt.axis("off")
                rows, cols, dim = img.shape
                M = np.float32([[1, 0, 0],
                [0, -1, rows],
                [0,0,1]])
                reflected_img = img.copy()
                reflected_img = cv2.warpPerspective(img, M, (int(cols), int(rows)))
                #plt.imshow(reflected_img)
                #plt.show()
                cv2.imwrite(os.path.join(self.root_path, self.img_name[:-4]+'_'+str(self.append))+'.jpg', reflected_img)
            cv2.imwrite(os.path.join(self.root_path, self.img_name[:-4]+'_'+str(self.append))+'.jpg', img)
        X_reflect()

        def Y_reflect():
            self.append += 1
            decision = random.choice([True, False])
            img = cv2.imread(self.img_path)
            #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            if decision == True:
                plt.axis("off")
                rows, cols, dim = img.shape
                M = np.float32([[-1, 0, cols],
                [0, 1, 0],
                [0,0,1]])
                reflected_img = img.copy()
                reflected_img = cv2.warpPerspective(img, M, (int(cols), int(rows)))
                #plt.imshow(reflected_img)
                #plt.show()
                cv2.imwrite(os.path.join(self.root_path, self.img_name[:-4]+'_'+str(self.append))+'.jpg', reflected_img)
            cv2.imwrite(os.path.join(self.root_path, self.img_name[:-4]+'_'+str(self.append))+'.jpg', img)
        Y_reflect()

        def rand_scale():
            self.append += 1
            scale_factor = random.uniform(1,1.2)
            img = cv2.imread(self.img_path)
            #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            plt.axis("off")
            #plt.imshow(img)
            #plt.show()
            rows, cols, dim = img.shape
            M = np.float32([[scale_factor, 0, 0],
            [0, scale_factor, 0],
            [0,0,1]])
            scaled_img = img.copy()
            scaled_img = cv2.warpPerspective(img, M, (cols*2, rows*2))
            #plt.imshow(scaled_img)
            #plt.show()
            cv2.imwrite(os.path.join(self.root_path, self.img_name[:-4]+'_'+str(self.append))+'.jpg', scaled_img)
        rand_scale()

        def rand_rotation():
            self.append += 1
            deg = (10-(-10))*np.random.random_sample()-10
            img = cv2.imread(self.img_path)
            #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            plt.axis("off")
            rows, cols, dim = img.shape
            angle = np.radians(deg)
            M = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
            [np.sin(angle), np.cos(angle), 0],
            [0,0,1]])
            rotated_img = img.copy()
            rotated_img = cv2.warpPerspective(img, M, (int(cols), int(rows)))
            #plt.imshow(rotated_img)
            #plt.show()
            cv2.imwrite(os.path.join(self.root_path, self.img_name[:-4]+'_'+str(self.append))+'.jpg', rotated_img)
        rand_rotation()

        def rand_translation():
            self.append += 1
            dist = (5-(-5))*np.random.random_sample()-5
            img = cv2.imread(self.img_path)
            #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            plt.axis("off")
            rows, cols, dim = img.shape
            M = np.float32([[1, 0, dist],
            [0, 1, dist],
            [0,0,1]])
            translated_img = img.copy()
            translated_img = cv2.warpPerspective(img, M, (cols, rows))
            #plt.imshow(translated_img)
            #plt.show()
            cv2.imwrite(os.path.join(self.root_path, self.img_name[:-4]+'_'+str(self.append))+'.jpg', translated_img)
        rand_translation()

def run_aug(img_dir=None):
    img_dir = str(input("Enter the image folder directory: "))
    img_dir = Path(img_dir)
    #img_dir = Path(r"C:\Users\Dozie Sixtus\Desktop\birds")
    print('img_path: ', img_dir)
    for root, dirs, files in os.walk(img_dir):
        print('The operation is currently working in this ', root, ' directory')
        file_list = [x for x in files if x[-3:] in ['jpg', 'png', 'JPEG']]
        for file in file_list:
            img_aug = ImgAug(root, file, str(os.path.join(root, file)))
            img_aug()

        #img_paths = [os.path.join(root, x) for x in files if x[-3:] == 'jpg']

#run_aug()


if __name__ == "__main__":
    print('Your code is running ...')
    run_aug()

