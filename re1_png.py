import numpy as np
import matplotlib.pyplot as plt

n=100

def ft(x,a,n):
	sum=0
	for i in range(n):
		sum+=(1/(i+1))*(np.cos((i+1)*a)-1)*np.sin((i+1)*x)
	return 2*sum/np.pi
fig = plt.figure()
fig.patch.set_facecolor('xkcd:black')
plt.clf()
th=np.linspace(0,2*np.pi,n)
x=np.cos(th)
y=np.sin(th)
y1=np.cos(np.pi/4)
plt.hlines(y1,-y1,y1,color='r',linewidth=3)
plt.hlines(-y1,-y1,y1,color='r',linewidth=3)
plt.vlines(-y1,-y1,y1,color='r',linewidth=3)
plt.vlines(y1,-y1,y1,color='r',linewidth=3)
x1=np.linspace(-0.9*y1,0.9*y1,n)
p=1
r=3
nl=10
e=2
th1=np.linspace(-np.pi/nl,np.pi/nl,100)
x2=(p+r*np.cos(nl*th1/2)**e)*np.cos(th1+np.pi/3)
y2=(p+r*np.cos(nl*th1/2)**e)*np.sin(th1+np.pi/3)
x3=(p+r*np.cos(nl*th1/2)**e)*np.cos(th1+2*np.pi/3)
y3=(p+r*np.cos(nl*th1/2)**e)*np.sin(th1+2*np.pi/3)
plt.plot(x,y,'r',x1,0.5*ft(x1,0.9*y1,50),'r',x2,y2,'r',x3,y3,'r',linewidth=3)
plt.xlim([-2.5,2.5])
plt.ylim([-1.1,4])
ax=plt.gca()
ax.set_aspect(1)
ax.set_facecolor('xkcd:black')

plt.savefig("ISS_RabbitEars.png", dpi=300)
plt.show()

