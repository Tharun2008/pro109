import pandas as pd
import statistics
import csv

df=pd.read_csv('StudentsPerformance.csv')
maths_list=df['math score'].to_list()


maths_mean=statistics.mean(maths_list)

maths_median=statistics.median(maths_list)


maths_mode=statistics.mode(maths_list)


print('mean of this data is {}'.format(maths_mean))
print('median of this data is {}'.format(maths_median))
print('mode of this data is {}'.format(maths_mode))

maths_std_deviation=statistics.stdev(maths_list)


maths_first_std_deviation_start, maths_first_std_deviation_end = maths_mean-maths_std_deviation, maths_mean+maths_std_deviation
maths_second_std_deviation_start, maths_second_std_deviation_end = maths_mean-(2*maths_std_deviation), maths_mean+(2*maths_std_deviation)
maths_third_std_deviation_start, maths_third_std_deviation_end = maths_mean-(3*maths_std_deviation), maths_mean+(3*maths_std_deviation)



maths_list_of_data_within_1_std_deviation = [result for result in maths_list if result > maths_first_std_deviation_start and result < maths_first_std_deviation_end]
maths_list_of_data_within_2_std_deviation = [result for result in maths_list if result > maths_second_std_deviation_start and result < maths_second_std_deviation_end]
maths_list_of_data_within_3_std_deviation = [result for result in maths_list if result > maths_third_std_deviation_start and result < maths_third_std_deviation_end]

print('standard of this data is {}'.format(maths_std_deviation))

print("{}% of data lies within 1 standard deviation".format(len(maths_list_of_data_within_1_std_deviation)*100.0/len(maths_list)))
print("{}% of data lies within 2 standard deviation".format(len(maths_list_of_data_within_2_std_deviation)*100.0/len(maths_list)))
print("{}% of data lies within 3 standard deviation".format(len(maths_list_of_data_within_3_std_deviation)*100.0/len(maths_list)))

