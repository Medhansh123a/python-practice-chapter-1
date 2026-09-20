import pandas as pd
students={
    "Name":["Medhansh"],
    "Age":[17],
    "Marks":["50"]
}
df=pd.DataFrame(students)
print(df)
print(df["Name"])