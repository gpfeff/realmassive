data = [55, 99, 54, -38, -97, 92, -77, 17, -18, -35, 78, 27, 47, 48, -27, 85, 19, -55, -84, 16,]
#Sets variable, 'data', equal to an array of numbers#

sum_data = sum(data)
#Sets variable, 'sum_data', which is the sum of all the numbers in data#

data_length = len(data)
#Sets variable, 'data_length', equal to the length of the array(how many numbers are in there)#

data_mean = float(sum_data)/data_length
#Computes the mean by dividing the sum of all numbers in 'data' by the length of the array & converts to float#

print "The mean of the array is: ", data_mean



data.sort()
first_value = data[9]
second_value = data[10]
#Given data_length = 20, in order to find the median of data I'll need to find the mean of the two middle numbers#

data_median = (first_value + second_value) / 2

print "The median of the array is: ", data_median



from collections import Counter
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



import numpy
standard_deviation = numpy.std(data)
#Uses the numpy library to calculate#
print "The standard deviation of the array is :", standard_deviation



