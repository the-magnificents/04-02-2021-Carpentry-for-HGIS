import math

def centroid(vertexes):
     _x_list = [vertex [0] for vertex in vertexes]
     _y_list = [vertex [1] for vertex in vertexes]
     _len = len(vertexes)
     _x = sum(_x_list) / _len
     _y = sum(_y_list) / _len
     return [_x, _y]    

def get_angle(coords):
    '''
    The function gets the angle based on a pair of coordinates x and y
    using basic trigonometry to calculate the angle of the triangle
    this angle will be used to sort coordinates of an array
    '''     
    x = coords[0]
    y = coords[1]

    # Compute hypothenuse
    hypothenuse = math.sqrt(x ** 2 + y ** 2) 

    # Gets angle and converts radians in degrees
    angle = math.degrees(math.asin(y/hypothenuse))
    
    # Define angle for second quadrant
    if(x < 0 and y > 0 ):
        angle = 180 - angle

    # Define angle for third quadrant
    elif(x < 0 and y < 0):
        angle = 270 - angle      

    # Define angle for forth quadrant
    elif(x > 0 and y < 0):
        angle = 360 - angle
         
    while angle > 360:
        angle =  360 - angle 
    

    return angle

def sort_item(ref,points):
        '''
        It sorts the last element in a list starting from a reference ref
        iterating backwards, if previous value is bigger, then the last element
        moves one index down
        '''
        while ref > 0:
            curr = get_angle(points[ref])
            prev = get_angle(points[ref - 1])
            if prev > curr:
                new_prev = points[ref]
                new_curr = points[ref-1]
                points[ref-1] = new_prev
                points[ref] = new_curr
                ref -= 1
            else:
                break

        return points
        
def sort_points(points):
    '''
    this function sorts points from smaller to bigger angles to prepare polygon data
    '''
    reference = 1
    
    while reference < len(points):
        points = sort_item(reference, points)
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

def list_ordered_angles(coords):
    angles = []
    coords = sort_points(coords)
    for point in coords:
        angles.append(get_angle(point))
    
    return angles
    

