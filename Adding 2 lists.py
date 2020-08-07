def list():

    list1 = ["Sunflower","Dandelion","Azalea","Jasmine"]
    list2 = ["Irises","Tulips"]
    for i in list1:
        x=len(i)
        if x>5:
        list1.extend(list2)
    
    return(list1)
a=list()
print(a)
