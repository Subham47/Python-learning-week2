def problem2_7():
    s1=input("Enter length of side one:")
    x1=float(s1)
    s2=input("Enter length of side two:")
    x2=float(s2)
    s3=input("Enter length of side three:")
    x3=float(s3)
    s=.5*(x1+x2+x3)
    x=s*(s-x1)*(s-x2)*(s-x3)
    Area=x**.5
    print("Area of a triangle with sides",x1,x2,x3,"is",Area)