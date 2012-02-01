#Originally written by James Best

import math

def rotateX(X,Y,n,t):
    X=float(X)
    Y=float(Y)
    t=-t
    Angle=(2*math.pi/n)*t
    return round((X*math.cos(Angle))-(Y*math.sin(Angle)),4)
    
def rotateY(X,Y,n,t):
    X=float(X)
    Y=float(Y)
    t=-t
    Angle=(2*math.pi/n)*t
    return round((X*math.sin(Angle))+(Y*math.cos(Angle)),4)

def rotateX1(X,Y,n,t):
    X=float(X)
    Y=float(Y)
    t=-(t+1)
    Angle=(2*math.pi/n)*t
    return round((X*math.cos(Angle))-(Y*math.sin(Angle)),4)
    
def rotateY1(X,Y,n,t):
    X=float(X)
    Y=float(Y)
    t=-(t+1)
    Angle=(2*math.pi/n)*t
    return round((X*math.sin(Angle))+(Y*math.cos(Angle)),4)

def createSprocket(n,h=0):
    """ creates the G-Code for a #25 chain sprocket
        enter n the number of teeth.
    """
    R=(.125/(math.sin(math.pi/n)))
    V=((R**2)-(.125**2))**(.5)
    H=((.1745**2)-(.057**2))**(.5)
    T=H+V

    #print'Right Curve Start'
    RightCurveStartPoints=[]
    OriginalTopOfToothX=0.0
    OriginalTopOfToothY=T
    for x in range(n):
        TopOfToothX=rotateX(OriginalTopOfToothX,OriginalTopOfToothY,n,x)
        TopOfToothY=rotateY(OriginalTopOfToothX,OriginalTopOfToothY,n,x)
        RightCurveStartPoints+=[[TopOfToothX,TopOfToothY]]
        #print(TopOfToothX,TopOfToothY)

    #print'center for right curves'
    CenterForRightCurvePoints=[]
    OriginalRightToothCenterX=-0.057
    OriginalRightToothCenterY=V
    for x in range(n):
        RightToothCenterX=rotateX(OriginalRightToothCenterX,OriginalRightToothCenterY,n,x)
        RightToothCenterY=rotateY(OriginalRightToothCenterX,OriginalRightToothCenterY,n,x)
        CenterForRightCurvePoints+=[[RightToothCenterX,RightToothCenterY]]
        #print(RightToothCenterX,RightToothCenterY)

        
    #print'center for left curves'
    CenterForLeftCurvePoints=[]
    OriginalLeftToothCenterX=0.057
    OriginalLeftToothCenterY=V
    for x in range(n):
        LeftToothCenterX=rotateX1(OriginalLeftToothCenterX,OriginalLeftToothCenterY,n,x)
        LeftToothCenterY=rotateY1(OriginalLeftToothCenterX,OriginalLeftToothCenterY,n,x)
        CenterForLeftCurvePoints+=[[LeftToothCenterX,LeftToothCenterY]]
        #print(LeftToothCenterX,LeftToothCenterY)

    #print'center for bottom curve'
    CenterForBottomCurvePoints=[]
    OriginalBottomOfToothCenterX=.125
    OriginalBottomOfToothCenterY=V
    for x in range(n):
        BottomOfToothCenterX=rotateX(OriginalBottomOfToothCenterX,OriginalBottomOfToothCenterY,n,x)
        BottomOfToothCenterY=rotateY(OriginalBottomOfToothCenterX,OriginalBottomOfToothCenterY,n,x)
        CenterForBottomCurvePoints+=[[BottomOfToothCenterX,BottomOfToothCenterY]]
        #print(BottomOfToothCenterX,BottomOfToothCenterY)

    #print 'bottom curve start'
    BottomCurveStartPoints=[]
    OriginalBottomCurveStartX=.1175
    OriginalBottomCurveStartY=V
    for x in range(n):
        BottomCurveStartX=rotateX(OriginalBottomCurveStartX,OriginalBottomCurveStartY,n,x)
        BottomCurveStartY=rotateY(OriginalBottomCurveStartX,OriginalBottomCurveStartY,n,x)
        BottomCurveStartPoints+=[[BottomCurveStartX,BottomCurveStartY]]
        #print(BottomCurveStartX,BottomCurveStartY)

    #print'left curve start'
    LeftCurveStartPoints=[]
    OriginalLeftCurveStartX=-.1175
    OriginalLeftCurveStartY=V
    for x in range(n):
        LeftCurveStartX=rotateX1(OriginalLeftCurveStartX,OriginalLeftCurveStartY,n,x)
        LeftCurveStartY=rotateY1(OriginalLeftCurveStartX,OriginalLeftCurveStartY,n,x)
        LeftCurveStartPoints+=[[LeftCurveStartX,LeftCurveStartY]]
        #print(LeftCurveStartX,LeftCurveStartY)

    RightCurveIandJPoints=[]
    for x in range(n):
        RightCurveI=CenterForRightCurvePoints[x][0]-RightCurveStartPoints[x][0]
        RightCurveJ=CenterForRightCurvePoints[x][1]-RightCurveStartPoints[x][1]
        RightCurveIandJPoints+=[[RightCurveI,RightCurveJ]]

    BottomCurveIandJPoints=[]
    for x in range(n):
        BottomCurveI=CenterForBottomCurvePoints[x][0]-BottomCurveStartPoints[x][0]
        BottomCurveJ=CenterForBottomCurvePoints[x][1]-BottomCurveStartPoints[x][1]
        BottomCurveIandJPoints+=[[BottomCurveI,BottomCurveJ]]

    LeftCurveIandJPoints=[]
    for x in range(n):
        LeftCurveI=CenterForLeftCurvePoints[x][0]-LeftCurveStartPoints[x][0]
        LeftCurveJ=CenterForLeftCurvePoints[x][1]-LeftCurveStartPoints[x][1]
        LeftCurveIandJPoints+=[[LeftCurveI,LeftCurveJ]]

    #print RightCurveStartPoints
    #print LeftCurveStartPoints
    #print BottomCurveStartPoints
    #print CenterForRightCurvePoints
    #print CenterForLeftCurvePoints
    #print CenterForBottomCurvePoints

    print 'G90'
    print 'E1.0'
    print 'F2.0'
    print 'G01 Z0.1250'
    print 'M03'
    
    if h>.125:
        bitradius=round((h/2)-.0625,4)
        print 'G01 X0.0000 Y'+str(bitradius)
        print 'G01 Z-0.0625'
        print 'G17 G03 J-'+str(bitradius)
        print 'G01 Z-0.1250'
        print 'G17 G03 J-'+str(bitradius)
        print 'G17 G03 J-'+str(bitradius)
        print 'G01 Z0.1250'
    elif h==.125:
        print 'G01 Z-0.1250'
        print 'G01 Z0.1250'
        

    print 'G01 X'+str(RightCurveStartPoints[0][0])+' Y'+str(RightCurveStartPoints[0][1])
    print 'G01 Z-0.0625'
    for x in range(n):     
        print'G17 G02 X'+str(BottomCurveStartPoints[x][0]),
        print'Y'+str(BottomCurveStartPoints[x][1]),
        print'I'+str(RightCurveIandJPoints[x][0]),
        print'J'+str(RightCurveIandJPoints[x][1])

        print'G17 G03 X'+str(LeftCurveStartPoints[x][0]),
        print'Y'+str(LeftCurveStartPoints[x][1]),
        print'I'+str(BottomCurveIandJPoints[x][0]),
        print'J'+str(BottomCurveIandJPoints[x][1])
        if x==n-1:
            g=0
        else:
            g=x+1
        print'G17 G02 X'+str(RightCurveStartPoints[g][0]),
        print'Y'+str(RightCurveStartPoints[g][1]),
        print'I'+str(LeftCurveIandJPoints[x][0]),
        print'J'+str(LeftCurveIandJPoints[x][1])

    print 'G01 Z-0.1250'
    for x in range(n):     
        print'G17 G02 X'+str(BottomCurveStartPoints[x][0]),
        print'Y'+str(BottomCurveStartPoints[x][1]),
        print'I'+str(RightCurveIandJPoints[x][0]),
        print'J'+str(RightCurveIandJPoints[x][1])

        print'G17 G03 X'+str(LeftCurveStartPoints[x][0]),
        print'Y'+str(LeftCurveStartPoints[x][1]),
        print'I'+str(BottomCurveIandJPoints[x][0]),
        print'J'+str(BottomCurveIandJPoints[x][1])
        if x==n-1:
            g=0
        else:
            g=x+1
        print'G17 G02 X'+str(RightCurveStartPoints[g][0]),
        print'Y'+str(RightCurveStartPoints[g][1]),
        print'I'+str(LeftCurveIandJPoints[x][0]),
        print'J'+str(LeftCurveIandJPoints[x][1])

    print 'G01 Z0.1250'

    print 'M05'
    print 'M00'

def counterBore(SH, BH, SD, BD, X, Y, Z, ZC, MD):
    
    """ SH = Small hole diameter, BH = Big hole diameter, SD = Small hole's depth, BD = Big hole's depth
        X = x coordinate center, Y = y coordinate center Z= Top of hole
        ZC= cut depth per pass MD= mill bit diameter
        """
    SD=round(SD,4)
    BD=round(BD,4)
    X=round(X,4)
    Y=round(Y,4)
    Z=round(Z,4)
    ZC=round(ZC,4)
    MD=round(MD,4)
    BDPasses = BD/ZC
    evenDepth=round(BDPasses*ZC,4)
    if BD==evenDepth:
        Extrapass=False
    else:
        Extrapass=True

    for x in range(1,int(BDPasses+1)):
        print 'G01 X' +str(X) +' Y'+str(Y)
        print 'G01 Z' +str(round(Z-(x*ZC),4))
        print 'G01 X' +str(X) +' Y'+str(round(Y-(BH/2)+(MD/2),4))
        print 'G17 G03 J' +str(round((BH/2)-(MD/2),4))
    if Extrapass==True:
        print 'G01 X' +str(X) +' Y'+str(Y)
        print 'G01 Z' +str(Z-BD)
        print 'G01 X' +str(X) +' Y'+str(round(Y-(BH/2)+(MD/2),4))
        print 'G17G03 J' +str(round((BH/2)-(MD/2),4))
        print 'G17G03 J' +str(round((BH/2)-(MD/2),4))
    else:
        print 'G17G03 J' +str(round((BH/2)-(MD/2),4))

    SDPasses = (SD-BD)/ZC
    evenDepth=round(SDPasses*ZC,4)
    if SD==round(evenDepth+BD,4):
        Extrapass=False
    else:
        Extrapass=True

    for x in range(1,int(SDPasses+1)):
        print 'G01 X' +str(X) +' Y'+str(Y)
        print 'G01 Z' +str(round(Z-BD-(x*ZC),4))
        print 'G01 X' +str(X) +' Y'+str(round(Y-(SH/2)+(MD/2),4))
        print 'G17 G03 J' +str(round((SH/2)-(MD/2),4))
    if Extrapass==True:
        print 'G01 X' +str(X) +' Y'+str(Y)
        print 'G01 Z' +str(Z-SD)
        print 'G01 X' +str(X) +' Y'+str(round(Y-(SH/2)+(MD/2),4))
        print 'G17 G03 J' +str(round((SH/2)-(MD/2),4))
        print 'G17 G03 J' +str(round((SH/2)-(MD/2),4))
    else:
        print 'G17 G03 J' +str(round((SH/2)-(MD/2),4))

    print'G01 X'+str(X)+' Y'+str(Y)
    print'G01 Z'+ str(Z+.125)
    
def square(X1,Y1,X2,Y2,D):
    X1=round(X1,4)
    X2=round(X2,4)
    Y1=round(Y1,4)
    Y2=round(Y2,4)
    print 'G01 X'+str(X1)+ ' Y'+str(Y1)
    if D==True:
        print 'G01 X'+str(X2)+ ' Y'+str(Y1)
        print 'G01 X'+str(X2)+ ' Y'+str(Y2)
        print 'G01 X'+str(X1)+ ' Y'+str(Y2)
        print 'G01 X'+str(X1)+ ' Y'+str(Y1)

    else:
        print 'G01 X'+str(X1)+ ' Y'+str(Y2)
        print 'G01 X'+str(X2)+ ' Y'+str(Y2)
        print 'G01 X'+str(X2)+ ' Y'+str(Y1)
        print 'G01 X'+str(X1)+ ' Y'+str(Y1)

def roundedSquare(X1,Y1,XW,YH,R):
    X1=round(X1,4)
    XW=round(XW,4)
    Y1=round(Y1,4)
    YH=round(YH,4)
    R=round(R,4)
    print 'G01 X'+str(X1)+' Y'+str(round((Y1+R),4))
    print 'G01 X'+str(X1)+' Y'+str(round((Y1+YH-R),4))
    print 'G17 G02 I'+str(R)+' X'+str(round((X1+R),4))+' Y'+str(round((Y1+YH),4))
    print 'G01 X'+str(round((X1+XW-R),4))+' Y'+str(round((Y1+YH),4))
    print 'G17 G02 J'+str(-R)+' X'+str(round((X1+XW),4))+' Y'+str(round((Y1+YH-R),4))
    print 'G01 X'+str(round((X1+XW),4))+' Y'+str(round((Y1+R),4))
    print 'G17 G02 I'+str(-R)+' X'+str(round((X1+XW-R),4))+' Y'+str(Y1)
    print 'G01 X'+str(round((X1+R),4))+' Y'+str(Y1)
    print 'G17 G02 J'+str(R)+' X'+str(X1)+' Y'+str(round((Y1+R),4))

def Circle(H,HD,X,Y,Z,ZC,MD):
    H=round(H,4)
    HD=round(HD,4)
    X=round(X,4)
    Y=round(Y,4)
    Z=round(Z,4)
    ZC=round(ZC,4)
    MD=round(MD,4)
    HDPasses = HD/ZC
    evenDepth=round(HDPasses*ZC,4)
    if HD==evenDepth:
        Extrapass=False
    else:
        Extrapass=True

    for x in range(1,int(HDPasses+1)):
        print 'G01 X' +str(X) +' Y'+str(Y)
        print 'G01 Z' +str(round(Z-(x*ZC),4))
        print 'G01 X' +str(X) +' Y'+str(round(Y-(H/2)+(MD/2),4))
        print 'G17 G03 J' +str(round((H/2)-(MD/2),4))
    if Extrapass==True:
        print 'G01 X' +str(X) +' Y'+str(Y)
        print 'G01 Z' +str(Z-HD)
        print 'G01 X' +str(X) +' Y'+str(round(Y-(H/2)+(MD/2),4))
        print 'G17G03 J' +str(round((H/2)-(MD/2),4))
        print 'G17G03 J' +str(round((H/2)-(MD/2),4))
    else:
        print 'G17 G03 J' +str(round((H/2)-(MD/2),4))
    
    
        
    






        
