#1 function to return a median of given list

def calculate_median(num_list):
    num_list.sort()
    length=len(num_list)
    if length%2==0:
        m=length/2
        m=round(m)
        med=(num_list[m-1]+num_list[(m)])/2
        #med=num_list[position]
    else:
        posi=(length+1)/2
        posi=round(posi)
        med=num_list[posi-1]
    return med

#num_list=[13,21,21,40,48,55,72]
#num_list=[1,3,5,7,9,11,13]
#num_list=[1,3,5,7,9,11]
num_list=[-11,5.5,-3.4,7.1,-9,22]
k=calculate_median(num_list)
print("The meian is",k)
