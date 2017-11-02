import numpy as np
import math
import cv2

def get_int_distance(value1, value2):
    ''' Returns the absolute distance from two float objects '''
    return int(math.ceil(abs(value1 - value2)))

class Layer:
    ''' Default GridMap Layer Instance '''

    def __init__(self, name, region_points):
        '''
            Class Constructor
            params:
                name: string Layer name to b referenced
                region_points: list of two points corresponding to layer widith and height
        '''
        self.name = name
        self.set_borders(region_points[0], region_points[1])
        self.grid = self.init_layer()
        self.border_points = set()

    def init_layer(self):
        '''
            Layers have, a resolution of 5 points per meter
        '''
        # basic setup
        grid_widith = get_int_distance(self.border_points[0].x, self.border_points[1].x)
        grid_height = get_int_distance(self.border_points[0].y, self.border_points[1].y)
        # number of points per meter
        resolution = 5
        # get rows and cols
        rows = grid_height * resolution
        cols = grid_widith * resolution
        # create empty numpy instace
        return np.ones([rows, cols], np.float32)/2

    def get_grid(self):
        ''' Return corresponding grid '''
        return self.grid

    def set_grid(self, matrix):
        ''' Assign a new matrix to layers grid '''
        if matrix.shape == self.grid.shape:
            self.grid = matrix
        else:
            print 'Trying to assign grid layer of a different shape'

    def set_borders(self, pt1, pt2):
        ''' Define border points for layer '''
        self.border_points = [pt1, pt2]

    def show_layer(self, windowname):
        ''' Shows an image of the layer '''
        cv2.imshow(windowname, self.get_grid())

    def save_layer(self, filename):
        ''' Saves layer image to a file '''
        cv2.imwrite(filename, self.get_grid())
