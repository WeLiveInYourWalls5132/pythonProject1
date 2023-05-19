list_for_slice  =[5,48,3,76,389,1000,872,1,0]

#[5,48,3]
print(list_for_slice[0:3])


#[48,3,76]
print(list_for_slice[1:4])


#[1000,872,1,0]
print(list_for_slice[5:9])

#[1,0]
print(list_for_slice[7:9])
print(len(list_for_slice))
print(list_for_slice[len(list_for_slice)-2:len(list_for_slice)])

#[5,48,3,76,389,1000,872,1]
print(list_for_slice[0:len(list_for_slice)-1])

#[48,3,76,389,1000,872,1]
print(list_for_slice[1:len(list_for_slice)-1])