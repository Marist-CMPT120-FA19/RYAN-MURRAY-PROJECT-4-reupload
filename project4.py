#!/usr/bin/env python
# coding: utf-8

# In[1]:


from graphics import *

def main():
    win = GraphWin()
    
    box = Rectangle(Point(100, 170), Point(20, 20))
    box.setOutline("black")
    box.setFill("white")
    box.draw(win)
    
    light = Circle(Point(59,50), 20)
    light.setFill("red")
    light.draw(win)
    
    light = Circle(Point(59,95), 20)
    light.setFill("yellow")
    light.draw(win)
    
    light = Circle(Point(59,140), 20)
    light.setFill("green")
    light.draw(win)
    
        
    win.getMouse()
main()


# In[ ]:




