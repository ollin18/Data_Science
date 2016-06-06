import numpy as np
from PIL import Image

img = Image.open("Image_route")

matriz = np.array(img)

def las_matrices(n):

    matriz_r = np.zeros((len(matriz),len(matriz[0])))
    matriz_g = np.zeros((len(matriz),len(matriz[0])))
    matriz_b = np.zeros((len(matriz),len(matriz[0])))
    
    for s in range(0,len(matriz)):
        for t in range(0,len(matriz[0])):
            matriz_r[s,t] = matriz[s,t][0]        
            matriz_g[s,t] = matriz[s,t][1]
            matriz_b[s,t] = matriz[s,t][2]
    
    sumita_r = np.zeros((len(matriz_r), len(matriz_r[0])))
    sumita_g = np.zeros((len(matriz_r), len(matriz_r[0])))
    sumita_b = np.zeros((len(matriz_r), len(matriz_r[0])))
    
    U_r, Sigma_r, V_r = np.linalg.svd(matriz_r)
    U_g, Sigma_g, V_g = np.linalg.svd(matriz_g)
    U_b, Sigma_b, V_b = np.linalg.svd(matriz_b)
    
    for i in xrange(0,n):
        mvs_r = Sigma_r[i] * U_r[:,i:i+1] * V_r[i:i+1,:]
        mvs_g = Sigma_g[i] * U_g[:,i:i+1] * V_g[i:i+1,:]
        mvs_b = Sigma_b[i] * U_b[:,i:i+1] * V_b[i:i+1,:]
        sumita_r = sumita_r + mvs_r
        sumita_g = sumita_g + mvs_g
        sumita_b = sumita_b + mvs_b
    matriz_final_r = np.array(sumita_r, dtype='uint8')
    matriz_final_g = np.array(sumita_g, dtype='uint8')
    matriz_final_b = np.array(sumita_b, dtype='uint8')
    return matriz_final_r, matriz_final_g, matriz_final_b



def la_suma(n):
    R, G, B = las_matrices(n)
    suma = np.copy(matriz)
    for n in range(0,len(R)):
        for m in range(0,len(R[0])):
            suma[n,m] = np.array([R[n,m],G[n,m],B[n,m]])
    return suma



def la_imagen(n):
    matriz = la_suma(n)
    imagen = Image.fromarray(matriz)
    return imagen
