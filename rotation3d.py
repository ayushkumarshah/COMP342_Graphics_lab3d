#reflection 3D
# -*- coding: utf-8 -*-
from tkinter import *
from math import sqrt
from math import sin, cos, radians, pi
points=[]
def conv3Dto2D(x,y,z):
	z=z/sqrt(2)
	x=ox+(x-z)
	y=oy-(y-z)
	return x,y

def drawcube(points3d,outline='black'):
	for i in range (len(points3d)):	
		points.insert(i,conv3Dto2D(points3d[i][0],points3d[i][1],points3d[i][2]))
		win.create_text(points[i],text=str(i),font="Times 10 bold")
	win.create_polygon(points[0],points[1],points[2],points[3],outline=outline,fill='')	
	win.create_polygon(points[4],points[5],points[6],points[7],outline=outline,fill='')	
	win.create_line(points[0],points[4],fill=outline)
	win.create_line(points[1],points[5],fill=outline)
	win.create_line(points[2],points[6],fill=outline)
	win.create_line(points[3],points[7],fill=outline)	

def rotation(x,y,z):
	Rotz = 	[[cos(theta), -sin(theta), 0,	0],
      		[sin(theta), cos(theta),  0,	0],
      		[0,              0,        1,	0],
		[0,		0,	0,	1]]

	P =     [[x],
		[y],
		[z],
		[1]]

	result= [[0],
	  	 [0],
	   	 [0],
		 [0]]

#Matrix multiplication resultx=Refx.P
	# iterate through rows of Refx
	for i in range(len(Rotz)):
		# iterate through columns of P
		for j in range(len(P[0])):
			# iterate through rows of P
			for k in range(len(P)):
				result[i][j] += Rotz[i][k] * P[k][j]
	return result[0][0],result[1][0],result[2][0]
print("Enter the width,height and depth of cube")
w,h,d=map(int,input().split())
print ("enter the center coordinates xc yc")
xc,yc=map(int,input().split())
zc=0
print("Enter value of rotation andle theta in degrees")
theta=float(input())
theta=radians(theta)
master=Tk()
canvas_width=master.winfo_screenwidth()
canvas_height=master.winfo_screenheight()
win=Canvas(master,width=canvas_width,height=canvas_height)
win.pack()
#origin
ox,oy=canvas_width/2,canvas_height/2
#axes
win.create_line(ox,0,ox,oy)
win.create_line(ox,oy,ox*2,oy)
win.create_line(ox,oy,0,oy*2)
#cube points
points3d=[(0,0,0),(w,0,0),(w,h,0),(0,h,0),(0,0,d),(w,0,d),(w,h,d),(0,h,d)]
#displacing cubes by xc,yc
points3dnew=[]
for i in range(len(points3d)):
	points3dnew.insert(i,(points3d[i][0]+xc,points3d[i][1]+yc,points3d[i][2]+zc))
drawcube(points3dnew)
win.create_text(points[0],text="Original cube",font="Times 10 bold")
#calculating points after rotation about z axis
pointsx=[]
for i in range(len(points)):
	pointsx.insert(i,rotation(points3dnew[i][0],points3dnew[i][1],points3dnew[i][2]))
print (pointsx)
drawcube(pointsx,'blue')
win.create_text(points[0],text="cube after rotation about z axis",font="Times 10 bold")
mainloop()




     
