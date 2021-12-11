import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

n=100
f=60
fig, a=plt.subplots()

def ft(x,a,n):
	sum=0
	for i in range(n):
		sum+=(1/(i+1))*(np.cos((i+1)*a)-1)*np.sin((i+1)*x)
	return 2*sum/np.pi

def run(frame):
	if frame<=f:
		plt.clf()
		th=np.linspace(0,2*np.pi*(frame)/f,n)
		x=np.cos(th)
		y=np.sin(th)
		plt.plot(x,y,'r')
		plt.xlim([-1.2,1.2])
		plt.ylim([-1.2,1.2])
		ax=plt.gca()
		ax.set_aspect(1)
		ax.set_facecolor('xkcd:black')
	if frame>f and frame<=2*f:
		plt.clf()
		th=np.linspace(0,2*np.pi,n)
		x=np.cos(th)
		y=np.sin(th)
		y1=np.cos(np.pi/4)
		plt.plot(x,y,'r')
		plt.hlines(y1,-y1,-y1+(2*y1/f)*(frame-f),color='r')
		plt.hlines(-y1,y1-(2*y1/f)*(frame-f),y1,color='r')
		plt.xlim([-1.2,1.2])
		plt.ylim([-1.2,1.2])
		ax=plt.gca()
		ax.set_aspect(1)
		ax.set_facecolor('xkcd:black')
	if frame>2*f and frame<=3*f:
		plt.clf()
		th=np.linspace(0,2*np.pi,n)
		x=np.cos(th)
		y=np.sin(th)
		y1=np.cos(np.pi/4)
		plt.plot(x,y,'r')
		plt.hlines(y1,-y1,y1,color='r')
		plt.hlines(-y1,-y1,y1,color='r')
		plt.vlines(-y1,-y1,-y1+(2*y1/f)*(frame-2*f),color='r')
		plt.vlines(y1,y1-(2*y1/f)*(frame-2*f),y1,color='r')
		plt.xlim([-1.2,1.2])
		plt.ylim([-1.2,1.2])
		ax=plt.gca()
		ax.set_aspect(1)
		ax.set_facecolor('xkcd:black')
	if frame>3*f and frame<=4*f:
		plt.clf()
		th=np.linspace(0,2*np.pi,n)
		x=np.cos(th)
		y=np.sin(th)
		y1=np.cos(np.pi/4)
		plt.hlines(y1,-y1,y1,color='r')
		plt.hlines(-y1,-y1,y1,color='r')
		plt.vlines(-y1,-y1,y1,color='r')
		plt.vlines(y1,-y1,y1,color='r')
		x1=np.linspace(-0.9*y1,-0.9*y1+(0.9*2*y1/f)*(frame-3*f),n)
		plt.plot(x,y,'r',x1,0.5*ft(x1,0.9*y1,50),'r')
		plt.xlim([-1.2,1.2])
		plt.ylim([-1.2,1.2])
		ax=plt.gca()
		ax.set_aspect(1)
		ax.set_facecolor('xkcd:black')
	if frame>4*f and frame<=5*f:
		plt.clf()
		th=np.linspace(0,2*np.pi,n)
		x=np.cos(th)
		y=np.sin(th)
		y1=np.cos(np.pi/4)
		plt.hlines(y1,-y1,y1,color='r')
		plt.hlines(-y1,-y1,y1,color='r')
		plt.vlines(-y1,-y1,y1,color='r')
		plt.vlines(y1,-y1,y1,color='r')
		x1=np.linspace(-0.9*y1,0.9*y1,n)
		plt.plot(x,y,'r',x1,0.5*ft(x1,0.9*y1,50),'r')
		q1=(1/f)*(frame-4*f)
		q2=(2.5/f)*(frame-4*f)
		plt.xlim([-1.2-q1,1.2+q1])
		plt.ylim([-1.2,1.2+q2])
		ax=plt.gca()
		ax.set_aspect(1)
		ax.set_facecolor('xkcd:black')
	if frame>5*f and frame<=6*f:
		plt.clf()
		th=np.linspace(0,2*np.pi,n)
		x=np.cos(th)
		y=np.sin(th)
		y1=np.cos(np.pi/4)
		plt.hlines(y1,-y1,y1,color='r')
		plt.hlines(-y1,-y1,y1,color='r')
		plt.vlines(-y1,-y1,y1,color='r')
		plt.vlines(y1,-y1,y1,color='r')
		x1=np.linspace(-0.9*y1,0.9*y1,n)
		p=1
		r=3
		nl=10
		e=2
		th1=np.linspace(-np.pi/nl,(-np.pi/nl)+2*np.pi/(f*nl)*(frame-5*f),100)
		x2=(p+r*np.cos(nl*th1/2)**e)*np.cos(th1+np.pi/3)
		y2=(p+r*np.cos(nl*th1/2)**e)*np.sin(th1+np.pi/3)
		x3=(p+r*np.cos(nl*th1/2)**e)*np.cos(th1+2*np.pi/3)
		y3=(p+r*np.cos(nl*th1/2)**e)*np.sin(th1+2*np.pi/3)
		plt.plot(x,y,'r',x1,0.5*ft(x1,0.9*y1,50),'r',x2,y2,'r',x3,y3,'r')
		plt.xlim([-2.2,2.2])
		plt.ylim([-1.2,3.7])
		ax=plt.gca()
		ax.set_aspect(1)
		ax.set_facecolor('xkcd:black')
	if frame>6*f and frame<=7*f:
		plt.clf()
		th=np.linspace(0,2*np.pi,n)
		x=np.cos(th)
		y=np.sin(th)
		y1=np.cos(np.pi/4)
		plt.hlines(y1,-y1,y1,color='r')
		plt.hlines(-y1,-y1,y1,color='r')
		plt.vlines(-y1,-y1,y1,color='r')
		plt.vlines(y1,-y1,y1,color='r')
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
		plt.plot(x,y,'r',x1,0.5*ft(x1,0.9*y1,50),'r',x2,y2,'r',x3,y3,'r')
		plt.xlim([-2.2,2.2])
		plt.ylim([-1.2,3.7])
		ax=plt.gca()
		ax.set_aspect(1)
		ax.set_facecolor('xkcd:black')

ani=animation.FuncAnimation(fig,run,frames=7*f)
writervideo = animation.FFMpegWriter(fps=24)
ani.save('re.mp4', writer=writervideo)
plt.show()

