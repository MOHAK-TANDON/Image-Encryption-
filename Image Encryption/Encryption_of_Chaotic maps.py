import cv2
import numpy as np
import chaotic

shuffled_input_img = cv2.imread(r"C:\Users\mohak\Desktop\New folder\shuffled_image_LATEST.png")
cv2.imshow('Shuffled Image', shuffled_input_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#chaotic keys banai
m=shuffled_input_img.shape[0]#no. of row
n=shuffled_input_img.shape[1]#no. of col

key_for_xor=chaotic.key_gen_td(0.9,-0.6013,2.0,0.50,2.75,0.2,.006,.003,(m*n))
print(key_for_xor)
#xor krenge ab
xor_ke_baad_img=np.zeros(shape=[m,n,3],dtype=np.uint8)
z=0
for i in range(m):
    for j in range(n):
        xor_ke_baad_img[i,j]=shuffled_input_img[i,j]^key_for_xor[z]
        z+=1
#path='D:\FINAL PROJECT COMPILED\output images'
cv2.imshow('xored Image', xor_ke_baad_img)
#xor ke baad img file
file_name='xored_image_fresh_test.png'
cv2.imwrite(file_name,xor_ke_baad_img)
cv2.waitKey(0)
cv2.destroyAllWindows()