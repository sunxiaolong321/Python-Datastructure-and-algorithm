# -*- coding:utf-8 -*

import turtle


def drawTriangle(t, points, color): # 绘制三角形
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()


def getMid(p1, p2): # 获取边长中点
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)


def sierpinski(t, degree, points):  # 绘制谢尔宾斯基三角
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'orange']    # 颜色地图
    drawTriangle(t, points, colormap[degree])
    if degree > 0:  # 绘制递归函数，degree 设置深度
        sierpinski(t, degree-1,
                   {
                       'left': points['left'],
                       'top': getMid(points['left'], points['top']),
                       'right': getMid(points['left'], points['right'])
                   })
        sierpinski(t, degree-1,
                   {
                       'left': getMid(points['left'], points['top']),
                       'top': points['top'],
                       'right': getMid(points['top'], points['right'])
                   })
        sierpinski(t, degree-1,
                   {
                       'left': getMid(points['left'], points['right']),
                       'top': getMid(points['top'], points['right']),
                       'right': points['right']
                   })


if __name__ == "__main__":
    t = turtle.Turtle()
    points = {'left': (-200, -100),
              'top': (0, 200),
              'right': (200, -100)}
    sierpinski(t, 5, points)
    turtle.done()
