data = [55, 99, 54, -38, -97, 92, -77, 17, -18, -35, 78, 27, 47, 48, -27, 85, 19, -55, -84, 16]
#Sets variable, 'data', equal to an array of numbers#

def mean(data):
  sum_data = sum(data)
  data_length = len(data)
  data_mean = float(sum_data)/data_length
  print data_mean
