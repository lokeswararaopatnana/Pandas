# pandas are used for creating data frames
# import pandas  #{Here we use terminal window for pandas module installing [pip install pandas]}
# a=pandas.read_csv("C:\\Users\PATNANA LOKESWARARAO\Dropbox\Python Practice Sessions\Pandas\hi.csv")
# print(a)

# import pandas as pd  #{for excel file to open install openpyxl in terminal window}
# b=pd.read_excel("C:\\Users\PATNANA LOKESWARARAO\Dropbox\Python Practice Sessions\Pandas\hello.xlsx")
# print(b) 

#we creating data frame with the help of dictionaries method
# data={"id":[1,2,3,4],
#       "Name":["Lokesh","Darling","Sai","Hari"],
#       "Course":["Python","MySQL","Full_Stack","Tableau"],
#       "DOJ":["NOV","DEC","JAN","FEB"]}
# print(data,type(data))
# import pandas as pd
# c=pd.DataFrame(data)
# print(c)

# we create data frame with the help of tuple method
# import pandas as pd
# bio=[(101,"Lokesh","arun"),(202,"Sasi","karthi"),(303,"ram","krishna"),(404,"sita","koka")]
# d=pd.DataFrame(bio,columns=["id","name","nickname"])
# print(d)