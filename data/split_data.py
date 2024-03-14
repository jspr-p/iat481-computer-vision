#splitting images into an 80/20 ratio
#total images 9000  = 9000 -> 80%: 7200 ; 20%: 1800 


classes = ['A','B','C']
import os
import glob
import shutil
import random

src = '/Users/jaspe/Documents/School/IAT481/asl_alphabet_a_to_c/src'
train = '/Users/jaspe/Documents/School/IAT481/asl_alphabet_a_to_c/train'
test = '/Users/jaspe/Documents/School/IAT481/asl_alphabet_a_to_c/test'

# MOVE 600/3000 IMAGES TO TEST FOLDERS
def splitimg_80_20():
    for letter in classes:
        src_folder = os.path.join(src, letter)
        src_imgs = glob.glob(src_folder+'/*.jpg')
        count=1

        #RANDOMLY TAKE 600/3000 
        random.shuffle(src_imgs)
        while count <= 600:
            src_path = src_imgs[count]
            dst_path = test + '/' + letter +'/' + letter + str(count) + '.jpg'
            shutil.move(src_path, dst_path)
            count = count+1

        #TAKE EVERY 5th 
        # for src_path in train_imgs:
        #     img_num = os.path.splitext(os.path.basename(src_path))[0][1:]
        #     if (int(img_num) % 5)==0:
        #         dst_path = dst + '/' + letter +'/' + letter + str(count) + '.jpg'
        #         # print(dst_path)
        #         # shutil.move(src_path, dst_path)
        #         count = count+1

# FOR FIXING LABELS AND MOVING REMAINING IMAGES TO TRAIN FOLDERS
def renumber_imgs():
    for letter in classes:
        src_folder = os.path.join(src, letter)
        src_imgs = glob.glob(src_folder+'/*.jpg')
        iterator = 1;
        for img in src_imgs:
            # print(train+'/'+letter+'/'+letter+str(iterator)+'.jpg')
            os.rename(img, train+'/'+letter+'/'+letter+str(iterator)+'.jpg')
            iterator = iterator+1

def split_test_val():
    for letter in classes:
        src_folder = '/Users/jaspe/Documents/GitHub/iat481-computer-vision/data/test/'+letter
        src_imgs = glob.glob(src_folder+'/*.jpg')
        for src_path in src_imgs:
            img_num = int(os.path.splitext(os.path.basename(src_path))[0][1:])
            if (img_num > 300):
                dst_path = '/Users/jaspe/Documents/GitHub/iat481-computer-vision/data/val/' + letter +'/' + letter + str(img_num-300) + '.jpg'
                shutil.move(src_path, dst_path)      

split_test_val()