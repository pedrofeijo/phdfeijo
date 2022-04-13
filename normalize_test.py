# Teste e Visualização da normalização

import numpy as np
import cv2
import pptk

# pc = np.loadtxt('pontos_1580317671.txt')
pc = np.loadtxt('arvore1.asc')
np.savetxt('bruta.asc',pc)

print(pc, pc.shape)

resized_4096 = cv2.resize(pc, (3,4096), interpolation = cv2.INTER_NEAREST)
resized_4096 = (resized_4096 - resized_4096.mean(axis=0))
# resized_4096 = (resized_4096 - resized_4096.min())/(resized_4096.max() - resized_4096.min())

print(resized_4096, resized_4096.shape)
print(resized_4096.mean(axis=0))
np.savetxt('resized_cent_4096_arvore1.asc', resized_4096)

dados= np.loadtxt('resized_cent_4096_arvore1.asc', delimiter= ' ') #padronizar o formato txt com ou sem virgula dkdkke
dados= dados[:,:3] # ler até a 3 coluna
v = pptk.viewer(dados, dados[:, 2]) # visualização colorida referencia em Z
v.set(point_size=0.005)

resized_2048 = cv2.resize(pc, (3,2048), interpolation = cv2.INTER_NEAREST)
resized_2048 = (resized_2048 - resized_2048.mean(axis=0))
# resized_2048 = (resized_2048 - resized_2048.min())/(resized_2048.max() - resized_2048.min())

print(resized_2048, resized_2048.shape)
print(resized_2048.mean(axis=0))
np.savetxt('resized_cent_2048_arvore1.asc', resized_2048)

dados= np.loadtxt('resized_cent_2048_arvore1.asc', delimiter= ' ') #padronizar o formato txt com ou sem virgula dkdkke
dados= dados[:,:3] # ler até a 3 coluna
v = pptk.viewer(dados, dados[:, 2]) # visualização colorida referencia em Z
v.set(point_size=0.005)


resized_1024 = cv2.resize(pc, (3,1024), interpolation = cv2.INTER_NEAREST)
resized_1024 = (resized_1024 - resized_1024.mean(axis=0))
# resized_1024 = (resized_1024 - resized_1024.min())/(resized_1024.max() - resized_1024.min())

print(resized_1024, resized_1024.shape)
print(resized_1024.mean(axis=0), resized_1024.mean(axis=0))
np.savetxt('resized_cent_1024_arvore1.asc', resized_1024)
dados= np.loadtxt('resized_cent_1024_arvore1.asc', delimiter= ' ') #padronizar o formato txt com ou sem virgula dkdkke
dados= dados[:,:3] # ler até a 3 coluna
v = pptk.viewer(dados, dados[:, 2]) # visualização colorida referencia em Z
v.set(point_size=0.005)

resized_512 = cv2.resize(pc, (3,512), interpolation = cv2.INTER_NEAREST)
resized_512 = (resized_512 - resized_512.mean(axis=0))
# resized_512 = (resized_512 - resized_512.min())/(resized_512.max() - resized_512.min())

print(resized_512, resized_512.shape)
print(resized_512.mean(axis=0))
np.savetxt('resized_cent_512_arvore1.asc', resized_512)
dados= np.loadtxt('resized_cent_512_arvore1.asc', delimiter= ' ') #padronizar o formato txt com ou sem virgula dkdkke
dados= dados[:,:3] # ler até a 3 coluna
v = pptk.viewer(dados, dados[:, 2]) # visualização colorida referencia em Z
v.set(point_size=0.005)

# v = pptk.viewer(resized_512) # visualizar em tons de cinza
# v = pptk.viewer(resized_512, resized_512[:, 2]) # visualização colorida referencia em Z
# v.set(point_size=0.005)