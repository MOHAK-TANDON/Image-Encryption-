#take decimal in input and convert it to binary and put it in array
def dec_to_bin_array(num):
    # Convert decimal to binary string
    binary_str = bin(num)[2:]
    
    # Pad with leading zeros if necessary
    while len(binary_str) < 8:
        binary_str = '0' + binary_str
    
    # Create array of binary digits
    bin_arr = [int(bit) for bit in binary_str]
    
    return bin_arr
#xor on first 4 values of array and NOT operation on rest 4 elements
def update_array(arr):
    for i in range(4):
        arr[i] = arr[i] ^ arr[i+1]
    for i in range(4, len(arr)):
        arr[i] = ~arr[i] & 1
    return arr
#take array as input and return the decimal value
def binary_to_decimal(binary_array):
    binary_str = ''.join(str(digit) for digit in binary_array)
    decimal_value = int(binary_str, 2)
    return decimal_value


#read every element of the matrix
def read_matrix(matrix):

    for row in matrix:
        for element in row:
            return element


def cellular_automat_FUNCTION(element):
    arr=dec_to_bin_array(element)
    for i in range (4):
        arr=update_array(arr)
        #print (arr,i)
    return binary_to_decimal(arr)

#funstion to iterate over matrix and update value
def final_function(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            x[i][j] = cellular_automat_FUNCTION(x[i][j])


import cv2
import numpy as np
input_img = cv2.imread(r"C:\Users\mohak\Desktop\New folder\CA ke baad img.png")
cv2.imshow('input', input_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
b, g, r = cv2.split(input_img)
final_function(b)
final_function(g)
final_function(r)
d_c_a_img=cv2.merge((b,g,r))
cv2.imshow('decrypt CA img',d_c_a_img)
file_name='Decrypt CA IMG.png'
#path='D:\FINAL PROJECT COMPILED\output images\Decrypted'
cv2.imwrite(file_name,d_c_a_img)
cv2.waitKey(0)
cv2.destroyAllWindows
