def TriangleArea(a,b,c):
    s = (a + b + c)/2
    area = s * (s - a) * (s - b) * (s - c)
    area = pow(area,0.5)
    return area

print(TriangleArea(5,4,3))