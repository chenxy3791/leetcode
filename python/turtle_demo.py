# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 14:27:20 2021

@author: chenxy

https://blog.csdn.net/qq_45361790/article/details/120558275
思路
1.选定适宜规格画笔
2.选落脚及其初始偏转角度（可不偏转）
3.开始绘制两个三角形
（1）其中第一个三角形绘制完毕需重新选择落脚点
（2）第二个三角落脚点可由第一个推算，详细代码后有图文解释！！！

下面补充一些可方便绘图的turtle库函数
1.turtle.setx( )：将当前x轴移动到指定位置；
2.turtle.sety( )：将当前y轴移动到指定位置；
3.turtle.right(x)：顺时针偏转x°；
4.turtle.left(x)：逆时针偏转x°；
5.turtle.penup()：不需填充数据，仅代表提笔；
6.turtle.pendown():表示落笔，与penup搭配时两者之间需要使用goto移动笔尖位置；

但是以下代码没有生成任何图形，为什么？

"""

import turtle          #导入turtle库

turtle.color("pink")   #画笔颜色
turtle.pensize(5)      #画笔粗细

turtle.seth(30)        #画笔落脚角度，可忽略

turtle.penup()
turtle.goto(-200,50)   #选择合适下笔处
turtle.pendown()
for i in range(3):      #绘制第一个等边三角形
    turtle.forward(200) #等边三角形边长
    turtle.left(120)    

turtle.penup()
turtle.goto(-84.5299461620748,50)  #此处由等边三角形边长计算：200-200/3*（根号3）
turtle.pendown()
for i in range(1):              #绘制第二个等边三角形
    turtle.left(60)
    turtle.forward(200)
for i in range(2):
    turtle.left(120)
    turtle.forward(200)
    
turtle.end_fill()
