import numpy
from collections import Counter
from scipy import stats

data = [55, 99, 54, -38, -97, 92, -77, 17, -18, -35, 78, 27, 47, 48, -27, 85, 19, -55, -84, 16,]

data_length = len(data)
#Sets variable equal to size of the array#


def mean(value):
  sum_data = sum(data)
  data_mean = float(sum_data)/data_length
  return data_mean
#Sets variable, 'sum_data', which is the sum of all the numbers in data#
#Sets variable, 'data_length', equal to the length of the array(how many numbers are in there)#
#Computes the mean by dividing the sum of all numbers in 'data' by the length of the array & converts to float#

print "The mean of the array is: ", mean(data)


def median(value):
  data.sort()
  first_value = data[9]
  second_value = data[10]
  data_median = (first_value + second_value) / 2
  return data_median

#Given data_length = 20, in order to find the median of data I'll need to find the mean of the two middle numbers#
print "The median of the array is: ", median(data)



def mode(values):
  count = Counter(values)
  winner = max(count.values())
  return [k for k,v in count.items() if v == winner]

 
mode_of_data = mode(data)
mode_length = len(mode_of_data)
#Given that the sample data set contains all non-repeating integers, I needed to build an if/else to catch this#


if mode_length == data_length:
  print "Sorry, this data contains no mode"
  #Data_length is previously defined as the length of the array#
else:
   print "The mode(s) of the array:", mode(data)



standard_deviation = numpy.std(data)
#Uses the numpy library to calculate standard_deviation#
print "The standard deviation of the array is :", standard_deviation

variance = numpy.var(data)
#Uses the numpy library to calculate variance#
print "The variance of the array is :", variance

# z_score = stats.zscore(55)
# print "The Z-Score of 55 is: ", z_score

# bins = numpy.histogram(data, bins=10)
# This will return the arrays of each in a variable called 'bins', unsure of where to go from here?#

bins = 2
print "The number of values in each bin is: ", bins



