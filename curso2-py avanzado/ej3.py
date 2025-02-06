
""" Print an array of size NxM with its main diagonal elements as 1s and 0s everywhere else. """
import numpy

v_input = input().split()
vars = [int(x) for x in v_input if v_input]
print(numpy.eye(vars[0], vars[1], k=0))