import math

def get_angle(coords):
    '''
    The function gets the angle based on a pair of coordinates x and y
    using basic trigonometry to calculate the angle of the triangle
    this angle will be used to sort coordinates of an array
    '''
    # Compute hypothenuse
    hypothenuse = math.sqrt(coords[0] ** 2 + coords[1] ** 2) 
    # the opposite side is y so we used the second value in coords list
    angle = math.degrees(math.asin(coords[1]/hypothenuse))
    # print("Hypothenuse: " + str(hypothenuse))
    # print("Angle: " + str(angle))
    if angle < 0:
        angle = 360 + (-angle)
    
    return angle
    

def sort_points(points):
    '''
    this functions sorts points from smaller to bigger angles to be able
    to draw points from left to right and draw proper polygons
    '''
    reference = 1
    def sort_item(pointer):
        '''
        It sorts the last element in a list starting from a reference pointer
        iterating backwards, if previous value is bigger, then the last element
        moves one index down
        '''
        while pointer > 0:
            curr = get_angle(points[pointer])
            prev = get_angle(points[pointer - 1])
            if curr < prev:
                old_curr = points[pointer]
                points[pointer] = points[pointer-1]
                points[pointer-1] = old_curr
                pointer -= 1
            else:
                break

    
    while reference < len(points):
        sort_item(reference)
        reference += 1

    
    return points

def get_next_pt(points):
    '''
    This function defines the next point to be drawn
    '''
    next = []
    for point in points:
        if (next == []):
            next = point
        elif(next[0] < point[0]):
            next = point
    
    return next

# print(get_next_pt([[10,20],[100,20],[-10,40]]))


# print(get_angle([300,-150]))
# sort_points([[10,20], [-90,80], [-100,90],[50,60]])