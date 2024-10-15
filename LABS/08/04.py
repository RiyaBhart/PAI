import numpy as np

student_dtype = np.dtype([('name', 'U20'),  
                          ('height', 'f8'), 
                          ('class', 'i4')])  

students = np.array([('Ali', 5.5, 10),
                     ('Ayesha', 5.9, 9),
                     ('Rayyan', 5.7, 10),
                     ('Muhammad', 5.8, 9),
                     ('Ukkashah', 5.6, 10)], dtype=student_dtype)

sortedstudents = np.sort(students, order=['class', 'height'])

print(sortedstudents)
