data=['1','2','apple','carrot','mango']
fruits=['apple','orange','mango']
vegies=['carrot','brinjal']
for i in data:
    if i  not in fruits and i in vegies:

        print(i)