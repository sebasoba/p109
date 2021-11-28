import random
import statistics
import plotly.figure_factory as ff

StudentsPerformance_mean = statistics.mean("StudentsPerformance_mean")
StudentsPerformance_median = statistics.median("StudentsPerformance_mean")
StudentsPerformance_mode = statistics.mode("StudentsPerformance_mean")


print("mean of Students Performance",StudentsPerformance_mean)
print("median of Students Performance",StudentsPerformance_median)
print("mode of Students Performance",StudentsPerformance_mode)


first_std_deviation_start, first std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

thin_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
thin_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < first_std_deviation_end]
thin_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < first_std_deviation_end]