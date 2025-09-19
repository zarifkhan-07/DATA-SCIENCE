import numpy as np

data_type=[('name','S20'),('class',int),('height',float)]
student_info=[("James", 12, 8.3),("Tom", 10, 7.9), ("Tashdid", 8, 5.7), ("Zarif", 12, 9.8)]

student=np.array(student_info, dtype=data_type)
print("Original array:")
print(student)
print("Sort by height:")
print(np.sort(student, order='name'))