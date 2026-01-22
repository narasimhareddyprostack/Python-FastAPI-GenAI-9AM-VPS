import csv
fp=open("emp.csv",'r')
emp_csv=csv.reader(fp)
emp_data=list(emp_csv)

#remove csv header using list slicing
for emp in emp_data[1:]:
    print(emp[1])

fp.close()