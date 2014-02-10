data = [55, 99, 54, -38, -97, 92, -77, 17, -18, -35, 78, 27, 47, 48, -27, 85, 19, -55, -84, 16]
#Sets variable, 'data', equal to an array of numbers#

sum_data = sum(data)
#Sets variable, 'sum_data', which is the sum of all the numbers in data#

data_length = len(data)
#Sets variable, 'data_length', equal to the length of the array(how many numbers are in there)#

data_mean = float(sum_data)/data_length
#Computes the mean by dividing the sum of all numbers in 'data' by the length of the array & converts to float#

data.sort()
first_value = data[9]
second_value = data[10]
#Given data_length = 20, in order to find the median of data I'll need to find the mean of the two middle numbers#

data_median = (first_value + second_value) / 2

from collections import Counter
def mode(values):
  count = Counter(values)
  winner = max(count.values())
  return [k for k,v in count.items() if v == winner]





print "The mean of the array is ", data_mean
print "The median of the array is ", data_median
print "The mode of the array is ", mode(data)



