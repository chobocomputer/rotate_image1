import os, datetime, time

from PIL import Image



################## make direc #########################################
def makedirec():
    global naljja, naldirec
    
    naljja = datetime.datetime.now()
    naldirec = naljja.strftime('%Y%m%d_%H%M%S')
    os.makedirs(naldirec)
#######################################################################



################## rotate_180       ####################################
def rotate_180():
        original_image = Image.open(filename)

        original_image = original_image.rotate(360-180, expand = True)

        file_front_name, file_back_name = os.path.splitext(filename)

        original_image.save(os.path.join(naldirec, file_front_name + '.png'))

        original_image.close()   
#######################################################################



################## exist file #########################################
def exist_file():
    if ((filename.lower().endswith('.png') and (filename != 'logo.png')) or filename.lower().endswith('.jpg') or filename.lower().endswith('.gif') or filename.lower().endswith('.bmp') or filename.lower().endswith('.pcx')):
        return True
    

#######################################################################


################## main       #########################################

naljja = 0
naldirec = 0
makedirec()



for filename in os.listdir('.'):
    if exist_file():    
        rotate_180()

#######################################################################
