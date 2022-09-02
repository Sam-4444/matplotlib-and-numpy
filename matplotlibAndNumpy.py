import matplotlib.pyplot as plt
import numpy as np


plt.Figure(figsize=(8,6))
plt.title("this is the title : omg",fontsize=20)
plt.xlabel("monitore ")
plt.ylabel("monsters ")
plt.grid(True)
plt.xlim(0,5)
plt.ylim(0,100)
plt.xticks([i*5 for i in range(12)],fontsize=4)
plt.yticks(fontsize=6)

plt.show()

plt.scatter(x=np.arange(0,20),y=np.arange(0,20),c="orange",)
plt.text(x=15,y=3,s="master !")
plt.vlines(x=0,ymax=20,ymin=0,colors="green")
plt.hlines(y=0,xmax=20,xmin=0,colors="blue")
plt.show()

print(" Hello matplot lib  ! ")

