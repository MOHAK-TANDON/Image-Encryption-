import math
import numpy as np
#chaotic key generation using td map

def key_gen_td(a,b,c,d,e,f,x,y,no_of_keys):
    z=x+y
    key=[]
    for i in range (no_of_keys):
        #x=(x*x)-(y*y)+(a*x)+(b*y)+y
        #y=(2*x*y)+(c*x)+(d*y)+(e*y)-(f*x)-(y*y*y)
       
        x=((a*x)+(b*y)+y)
        y=((c*x)+(d*y)+(e*y)-(f*x))
        x=(x*e)%256
        y=(y*c)%256
        z=(int(x*c+e*y)%256)
        key.append(z)

    return key      

    
print(key_gen_td(0.9,-0.6013,2.0,0.50,2.75,0.2,.006,.003,(10)))