import urllib.request
import cv2
import numpy as np
import os
from socket import timeout

class create_haar_classifiers(object):
    def store_raw_images(self):
        if not os.path.exists('D:\\Final year project\\Pictures\\neg'):
            os.makedirs('D:\\Final year project\\Pictures\\neg')
        
        if not os.path.exists('D:\\Final year project\\Pictures\\pos'):
            os.makedirs('D:\\Final year project\\Pictures\\pos')


        pic_num = 1
        new_pic_num = self.neg_offline_pictures(pic_num)
        final_pic_num = (self.neg_online_pictures(new_pic_num)) - 1
        print("Finished, "+str(final_pic_num)+" pictures converted")

    def pos_offline_pictures(self, pic_num):
        pos_images = 'D:\\Final year project\\Pictures\\positives.txt'
        with open(pos_images) as pi:
            for line in pi:
                try:
                    img = cv2.imread(line.strip(), cv2.IMREAD_GRAYSCALE)
                    resized_image = cv2.resize(img, (50,50))
                    cv2.imwrite("D:\\Final year project\\Pictures\\pos\\"+str(pic_num)+".jpg",resized_image) 
                    print("saved: "+str(pic_num)+") "+ line)
                    pic_num += 1
                except Exception as e:
                    print(str(e))

    def neg_offline_pictures(self,pic_num):
        neg_images = 'D:\\Final year project\\Pictures\\negatives.txt'
        with open(neg_images) as ni:
            for line in ni:
                try:
                    img = cv2.imread(line.strip(), cv2.IMREAD_GRAYSCALE)
                    resized_image = cv2.resize(img, (100,100))
                    cv2.imwrite("D:\\Final year project\\Pictures\\neg\\"+str(pic_num)+".jpg",resized_image) 
                    print("saved: "+str(pic_num)+") "+ line)
                    pic_num += 1
                except Exception as e:
                    print(str(e))
        return pic_num    

    def neg_online_pictures(self,pic_num):
        neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
        neg_images_urls = urllib.request.urlopen(neg_images_link).read().decode()
        for i in neg_images_urls.split('\n'):
            try:
                urllib.request.urlretrieve(i, "D:\\Final year project\\Pictures\\neg\\"+str(pic_num)+'.jpg')
                img = cv2.imread("D:\\Final year project\\Pictures\\neg\\"+str(pic_num)+'.jpg', cv2.IMREAD_GRAYSCALE)
                resized_image = cv2.resize(img, (100,100))
                cv2.imwrite("D:\\Final year project\\Pictures\\neg\\"+str(pic_num)+".jpg",resized_image) 
                print("saved: "+str(pic_num)+") "+i)
                pic_num += 1
            except Exception as e:
                print(str(e))
        return pic_num


    def create_pos_and_neg(self):
        for file_type in ['D:\\Final year project\\Pictures\\neg']:
            for img in os.listdir(file_type):
                if file_type == 'D:\\Final year project\\Pictures\\neg':
                    line = file_type+'/'+img+'/n'
                    with open('D:\\Final year project\\Pictures\\neg.txt', 'a') as f:
                        f.write(line)


ch = create_haar_classifiers()
ch.create_pos_and_neg()