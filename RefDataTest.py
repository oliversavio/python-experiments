from ReferenceData import *


r = ReferenceData("M","Male","07/11/2014","07/11/2200")
r.insert_data_list_value("Males from 1 ro 100")
print r.key
print r.value


print "Test Default Date Values"
print
print

r2 = ReferenceData("M","Male")
print r2.start_date
print r2.is_active()

print "Expired Date Values"
r3 = ReferenceData("F","Female", "08/01/2014")
print r3.start_date
print r3.is_active()



