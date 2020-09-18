def inside(x,y,x1,y1,x2,y2):
    if(x >= x1 and x <= x2 and y>=y1 and y<=y2):
        return True
    return False

# print(inside(-1,-3,-1,-2,1,2))
if(inside(1,1,0.3,0.5,1.1,0.7) and inside(1,1,0.5,0.2,1.1,2)):
    print("The point (1,1) lies inside  both the rectangles")
else:
    print("(1,1) lies outside the rectangle")