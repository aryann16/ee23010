import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mping


#vertices of triangle
B=np.array([-4,6])
C=np.array([-3,-5])
#direction vector
def dir_vec(C,B):
  return C-B
#square root of multiplication of direction vector and its transpose
sqrt_arr=np.sqrt(np.linalg.norm((dir_vec(C,B).T) @ (dir_vec(C,B))))
#length of BC
print("the length of BC is",sqrt_arr)
#for diagram of line BC
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
x_BC = line_gen(B,C)
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
B = B.reshape(-1,1)
C = C.reshape(-1,1)
tri_coords = np.block([[B,C]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['B','C']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                textcoords="offset points", # how to position the text
                xytext=(0,10), # distance from text to points (x,y)
                ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.savefig("figure")