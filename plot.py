from numpy import*
from matplotlib.pyplot import*

t=arange(-50,50,0.0001)

y1=sin(t)
y2=cos(t)
y3=gradient(y1)
y4=gradient(y2)
y5=gradient(y3)
y6=gradient(y4)

rcParams["figure.figsize"]=(10,10)
#title('graphs of sine and cosine family')
fig,axs=subplots(3,2)

axs[0,0].plot(t,y1,label='sine')
axs[0,0].set_title('sine wave')
axs[0,0].grid(True,color="red")
axs[0,0].legend()

axs[0,1].plot(t,y2,label='cos')
axs[0,1].set_title('cose wave')
axs[0,1].grid(True,color="red")
axs[0,1].legend()

axs[1,0].plot(t,y3,label='der of sin')
axs[1,0].set_title('derivative of sine wave')
axs[1,0].grid(True,color="red")
axs[1,0].legend()


axs[1,1].plot(t,y4,label='der of cos')
axs[1,1].set_title('derivative of cos wave')
axs[1,1].grid(True)
axs[1,1].legend()

axs[2,0].plot(t,y5,label='sec der sin')
axs[2,0].set_title('second derivative of sine wave')
axs[2,0].grid(True,color="black")
axs[2,0].legend()

axs[2,1].plot(t,y6,label='sec der of cos')
axs[2,1].set_title('second derivative of cose wave')
axs[2,1].grid(True,color="black")
axs[2,1].legend()

show()
