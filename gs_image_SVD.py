import numpy as np
from PIL import Image

img = Image.open("Yosemite.jpg").convert('L')

def la_suma(n):
    matriz = np.array(img)
    U, Sigma, V = np.linalg.svd(matriz)
    sumita = np.zeros((len(matriz), len(matriz[0]))) 
    for i in xrange(0,n):                            
        mvs = Sigma[i] * U[:,i:i+1] * V[i:i+1,:] 
        sumita = sumita + mvs                        
    matriz_final = np.array(sumita, dtype='uint8')   
    return matriz_final
    
def la_imagen(n):                                    
    matriz = la_suma(n)                              
    imagen = Image.fromarray(matriz)                 
    print 'r = ', n
    return imagen 
