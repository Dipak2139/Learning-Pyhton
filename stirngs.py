# Learning Strings today

name = 'Dipak'
name2= "Dipak"
name3= '''Dipak'''

print(name)
print(name2)
print(name3)

# String can be define using three format mentioned above

#String Indexing

name4 = "rahul"
#index   01234    

#to just print 'ahu'
updated_name4 = name4[1:4]
print(updated_name4)
updated1_name = name[:4]
print(updated1_name)
updated2_name = name[1:]
print(updated2_name)



#Negative Slicing
name5 = "rajesh"
updated_name5 = name5[-4: -1]
print(updated_name5)
# print(name5)