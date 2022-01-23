from datetime import datetime
import os, zipfile

"""Open the file and make it as lists"""


dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

with zipfile.ZipFile('wk2_test2_in.zip', 'r') as zip_ref:
    zip_ref.extractall(dir_path)
    extracted_file = zip_ref.namelist()

with open(extracted_file[0]) as f:
    lines = f.readlines()

"""Time difference between first and last log."""


first_timestamp = lines[0].split(' ')[0][:-1]
last_timestamp = lines[-1].split(' ')[0][:-1]

First_date = datetime.strptime(first_timestamp, "%Y-%m-%dT%H:%M:%S.%f+0000")
Last_date = datetime.strptime(last_timestamp, "%Y-%m-%dT%H:%M:%S.%f+0000")

print(f"The difference between the first and the last log is : {Last_date - First_date}")

""" Total number of Full GCs / Minor GCs """
""" Create 2 new lists in order to separate the GC [Minor GC / Full GC]"""

Minor_GC = []
Full_GC = []
for log in lines:
    if '[Full GC' in log:
        Full_GC.append(log)
    else:
        Minor_GC.append(log)

print(f"The total Minor GCs are : {len(Minor_GC)}")
print(f"The total Full GCs are : {len(Full_GC)}")


""" Find the maximum/average MinorGC - FullGC """

""" Regarding Minor GC """
""" Maximum logs  """
print("The top 3 Minor GC's logs.")

sortedMinor_GC_specific_field = []

topMinor_GC = []
i = 0

for log in Minor_GC:

    specific_field = Minor_GC[i].split(' ')
    sortedMinor_GC_specific_field.append(specific_field[4])
    i += 1

TopMinor_times = sorted(sortedMinor_GC_specific_field, reverse=True)[0:3]


for timestamps in TopMinor_times:
    for logs in Minor_GC:
        if timestamps in logs:
            print(f"{logs.split(' ')[0].replace('+0000:','+0000')}, {logs.split(',')[1].replace(']','')}", end='')

"""Average time"""
float_sorted_timesMinor = []
for items in sortedMinor_GC_specific_field:
    float_sorted_timesMinor.append(float(items))


print(f"The average time of the Minor GCs is : {sum(float_sorted_timesMinor)/len(sortedMinor_GC_specific_field)}")
print()

""" Maximum regarding Full GC """
""" Maximum logs  """

print("The top 3 Full GC's logs.")

sortedFull_GC_specific_field = []

topFull_GC = []
i = 0

for log in Full_GC:

    specific_field = Full_GC[i].split(' ')
    sortedFull_GC_specific_field.append(specific_field[5])
    i += 1

TopFull_times = sorted(sortedFull_GC_specific_field, reverse=True)[0:3]

for timestamps in TopFull_times:
    for logs in Full_GC:
        if timestamps in logs:
            print(f"{logs.split(' ')[0].replace('+0000:','+0000')}, {logs.split(',')[1].replace(']','')}",end='')

"""Average time"""
float_sorted_timesFull = []
for items in sortedFull_GC_specific_field:
    float_sorted_timesFull.append(float(items))

print(f"The average time of the Full GCs is : {sum(float_sorted_timesFull)/len(sortedFull_GC_specific_field)}")














