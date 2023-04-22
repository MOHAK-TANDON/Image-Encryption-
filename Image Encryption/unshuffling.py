import numpy as np
import cv2

#---FUNCTIONS....------
def reverse_nth_column(matrix, n):

    matrix[:, n] = matrix[::-1, n]
    return matrix

def interchange_nth_column(arr1, arr2, n):
    # Get the number of columns in the matrices
    num_cols = arr1.shape[1]
    
    # Iterate over every nth column and interchange them
    for i in range(n-1, num_cols, n):
        arr1[:, i], arr2[:, i] = arr2[:, i], arr1[:, i].copy()
def reverse_row(matrix):
    reversed_matrix = matrix[::-1]
    return reversed_matrix


def reverse_elements(matrix):
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
    return matrix
def circular_shift_row(matrix, n, shift_amt):
    row = matrix[n]
    shifted_row = np.roll(row, shift_amt)
    matrix[n] = shifted_row
    return matrix


#---reading image and spliting it
img = cv2.imread(r"C:\Users\mohak\Desktop\New folder\unxored_shuffled_image.png")

# Split the image into channels
b, g, r = cv2.split(img)

print(b)
print(g)
print(r)


#decryption starts------
#--undoing the circular shift-----

for i in range(0, len(b), 1):

    circular_shift_row(r, i, i)

for i in range(0, len(b), 3):
    circular_shift_row(b, i, -i)

for i in range(0, -len(b), -5):
    circular_shift_row(g, i, i)
#---undoing rev elem and rev row
r=reverse_elements(r)
b=reverse_elements(b)
g=reverse_elements(g)

g1=g
#b=reverse_row(b)
#r=reverse_row(r)
g=reverse_row(r)
r=reverse_row(g1)



#-----undoing the interchange------
for i in range(1,len(b[0]),5):
    interchange_nth_column(g,b,i+2)

for i in range(1,len(b[0]),3):

    interchange_nth_column(r,b,i+1)

for i in range(1,len(b[0]),1):

    interchange_nth_column(r,g,i)



#--undoing the reverse nth col
for i in range(1, len(b[0]), 2):

    reverse_nth_column(g, i)

for i in range(1, len(b[0]), 1):
    reverse_nth_column(r, -i)

for i in range(1, len(b[0]), 3):
    reverse_nth_column(r, -i)


unshuffled_img = cv2.merge(( b , g , r ))
#path='D:\FINAL PROJECT COMPILED\output images\Decrypted'
file_name='unshuffled_image.png'
cv2.imwrite(file_name,unshuffled_img)

# Display the shuffled image
cv2.imshow('unShuffled Image', unshuffled_img)
cv2.waitKey(0)
cv2.destroyAllWindows()