import cv2
import numpy as np
import chaotic
xored_shuffled_input_img = cv2.imread(r"C:\Users\mohak\Desktop\New folder\Decrypt CA IMG.png")
cv2.imshow('xored Shuffled Image', xored_shuffled_input_img)

#chaotic keys banai   
m=xored_shuffled_input_img.shape[0]#no. of row
n=xored_shuffled_input_img.shape[1]#no. of col

key_for_xor=chaotic.key_gen_td(0.9,-0.6013,2.0,0.50,2.75,0.2,.006,.003,(m*n))

xor_undo_ki_image=np.zeros(shape=[m,n,3],dtype=np.uint8)
z=0
for i in range(m):
    for j in range(n):
        xor_undo_ki_image[i,j]=xored_shuffled_input_img[i,j]^key_for_xor[z]
        z+=1
cv2.imshow('unxored Shuffled Image', xor_undo_ki_image)
file_name='unxored_shuffled_image.png'
#path='D:\FINAL PROJECT COMPILED\output images\Decrypted'
cv2.imwrite(file_name,xor_undo_ki_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
