#Title: Homework 6
#Author: Andrew Ayala

### IMPORT PACKAGES ###
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

### MAIN ###

#Se constant values and initialize array to track brownian motion

T = int(1e5)
L = 101
i = 50
j = 50
motionArray = np.array([[i, j]])
rng = np.random.default_rng()

#For loop to compute random stepping of Brownian motion particle
for t in np.arange(T):
    step = rng.integers(1,4)
#For loop to compute random stepping of Brownian motion particle
    if step==1: #Move particle one step up
        if i==L: 
            continue
        else:
            i+=1
    elif step==2: #Move particle one step down
        if i==0: 
            continue
        else: 
            i-=1
    elif step==3: #Move particle one step right
        if j==L:
            continue
        else:
            j+=1
    elif step==4: #Move particle one step left
        if j==0: 
            continue
        else:
            j-=1
    #Save step to array
    motionArray = np.append(motionArray, [[i,j]], axis=0)


#Create figure to plot motion of Brownian particle
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1)
ax.set_xlim(0, L)
ax.set_ylim(0, L)
particle = plt.Circle((50,50),radius=1,facecolor='red')
line, = ax.plot([50],[50])
ax.add_patch(particle)

#Create animation function
def animate(n):
    i = motionArray[n][0]
    j = motionArray[n][1]
    line.set_data([motionArray[:n,0]], [motionArray[:n,1]])
    particle.center = i,j
    return particle, line,

#Execute animation by creating GIF
anim = animation.FuncAnimation(fig, animate, blit = True)
writergif = animation.PillowWriter(fps=30)
HTML(anim.to_html5_video())
plt.show()

#Option to save animation as GIF
#anim.save('filename.gif',writer=writergif)