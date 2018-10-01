import time
import math
def getAngle():
    global finalx, finaly
    oldx=int(input('xold'))
    oldy=int(input('yold')) 
    currentx=int(input('xcurr'))
    currenty=int(input('ycurr'))
    finalx=int(input('xnew'))
    finaly=int(input('ynew'))
    # Vector made by (oldx, oldy) to (currentx, currenty)
    A = [currentx - oldx, currenty - oldy]
    # Vector made by (oldx, oldy) to (finalx, finaly)
    B = [finalx - oldx, finaly - oldy]
    # Vector made by (currentx, currenty) to (finalx, finaly)
    # A + C = B
    # Therefore, C = B - A
    C = [0, 0]
    C[1] = B[1] - A[1]
    C[0] = B[0] - A[0]
    ''' To find the angle between A and C                  '''
    ''' calculate the dot product of A and C/mag(A)*mag(C) '''
    
    costheta_numerator = A[0]*C[0] + A[1]*C[1]
    costheta_denominator = ((A[0]**2 + A[1]**2)**0.5) * ((C[0]**2 + C[1]**2)**0.5)

    if costheta_denominator == 0:
        # Recursively keep trying till you get a valid direction vector
        return getAngle()

    costheta = costheta_numerator/costheta_denominator
    angle = round(math.degrees(math.acos(costheta)),3)
    print('Angle to rotate',angle)

    # Cross Product
    sintheta_numerator = A[0]*C[1] - A[1]*C[0]
    sintheta_denominator = costheta_denominator
    sintheta = sintheta_numerator/sintheta_denominator
    
    sinangle = round(math.degrees(math.asin(sintheta)),3)
    
    if sinangle<0:
        print('Direction to rotate: Clockwise')
    else:
        print('Direction to rotate: Anticlockwise')
    
    return angle

    
