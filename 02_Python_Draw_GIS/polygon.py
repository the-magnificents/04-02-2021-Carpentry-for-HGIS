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
    # Compute hypothenuse
    hypothenuse = math.sqrt(coords[0] ** 2 + coords[1] ** 2) 
    
    # the opposite side is y so we used the second value in coords list
    angle = math.degrees(math.asin(coords[1]/hypothenuse))
    
    if(coords[0] < 0):
        angle = angle * 3

    if angle < 0:
        angle = 360 + (-angle)
    
    return angle

def sort_item(ref,points):
        '''
        It sorts the last element in a list starting from a reference ref
        iterating backwards, if previous value is bigger, then the last element
        moves one index down
        '''
        while ref >= 0:
            curr = get_angle(points[ref])
            prev = get_angle(points[ref - 1])
            if curr < prev:
                old_curr = points[ref]
                points[ref] = points[ref-1]
                points[ref-1] = old_curr
                ref -= 1
            else:
                break
        
        return points

def sort_points(points):
    '''
    this function sorts points from smaller to bigger angles to be able
    to draw points from left to right and draw proper polygons
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


print(get_angle([-142.5,115]))
print(get_angle([7.5,135.0]))

# Example
points = [[-142.5, 115.0], [7.5, 135.0], [-72.5, -35.0], [207.5, -215.0]]
print(points)
print(sort_points(points)) 
