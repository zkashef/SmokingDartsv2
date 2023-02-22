import math

def get_score(x, y):
    #find the angle
    angle = 1 # in degrees
    theta = 0 # in radians

    #find the radius
    radius = math.sqrt((x**2)+(y**2))

    # solve for the angle
    theta = math.atan(y/x)          # in radians
    angle = theta * (180/3.1415)    # convert to degrees

    ## What if angle is in Q3 or Q4 ##
    # makes sure that the arctan angle is accurate for scoring
    if y < 0:
        angle = angle + 180

    # use slice.py to figure out what base number

    # Quadrant 1
    if 0 < angle <= 18:
        slice = 13
    elif 18 < angle <= 36:
        slice = 4
    elif 36 < angle <= 54:
        slice = 18
    elif 54 < angle <= 72:
        slice = 1
    elif 72 < angle <= 90:
        slice = 20
    # Quadrant 2
    if 90 < angle <= 108:
        slice = 5
    elif 108 < angle <= 126:
        slice = 12
    elif 126 < angle <= 144:
        slice = 9
    elif 144 < angle <= 162:
        slice = 14
    elif 162 < angle <= 180:
        slice = 11
    # Quadrant 3
    if 180 < angle <= 198:
        slice = 8
    elif 198 < angle <= 216:
        slice = 16
    elif 216 < angle <= 234:
        slice = 7
    elif 234 < angle <= 252:
        slice = 19
    elif 252 < angle <= 270:
        slice = 3
    # Quadrant 4
    if 270 < angle <= 288:
        slice = 17
    elif 288 < angle <= 306:
        slice = 2
    elif 306 < angle <= 324:
        slice = 15
    elif 324 < angle <= 342:
        slice = 10
    elif 342 < angle <= 360:
        slice = 6
    elif angle == 0:
        slice = 6
    # make sure that the score is acurrate and fits into the scoring above
    else:
        while angle > 360:
            angle = angle - 360

    # use multiplyer.py to figure out the multiplyer
    if radius <= 0.5:
        score = 50
        print("Bullseye!!!")
    elif radius > 0.5 and radius <= 2:
        score = 25
        print("Bull!!!")
    elif radius >= 9.5 and radius <= 10.5:
        score = 3
        print("Triple Score!!!")
        Total = slice * score
    elif radius >= 16 and radius <=17:
        score = 2
        print("Double Score!!!")
        Total = slice * score
    elif radius > 17:
        score = 0
        print("Missed. Try Again.")
        Total = slice * score
    else:
        score = 1
        print("Nice hit!!!")
        Total = slice * score

    ## What if angle is in Q3 or Q4 ##
    if y < 0:
        angle = angle + 180

    return Total