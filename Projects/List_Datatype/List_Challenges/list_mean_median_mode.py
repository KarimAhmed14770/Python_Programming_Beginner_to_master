from collections import Counter

def get_mean(iterable):
    length=len(iterable)
    sum=0
    mean=0
    for i in iterable:
        sum+=i
    mean=sum/length
    return mean


def get_median(iterable):
    iterable.sort() #sort with list is an inplace method
    length=len(iterable)
    median=0
    if length%2==0:
        median=(iterable[length//2]+iterable[(length//2)-1])/2
    else:
        median=iterable[length//2]

    return median

def get_mode(iterable):# needs solution for no mode and bimodal
    unique_elements=[]
    list_of_counts=[]
    counter=0
    max_count=0
    Modes=[]
    for i in iterable:
        if(i not in unique_elements):
            unique_elements.append(i)
            list_of_counts.append(iterable.count(i))

    while counter<len(unique_elements):
        if list_of_counts[counter]>max_count:
            max_count=list_of_counts[counter]
        counter+=1
    if max_count==1:
        Modes=[]
    else:
        counter=0
        while counter < len(unique_elements):
            if list_of_counts[counter] == max_count:
                Modes.append(unique_elements[counter])
            counter += 1
    return Modes







test_list = [2, 3, 4, 4, 4, 5, 6, 7]

print("Mean: ",get_mean(test_list))
print("Median: ",get_median(test_list))
print("Mode: ",get_mode(test_list))
print()
test_list = [1, 1, 2, 3, 3, 4, 5]
print("Mean: ",get_mean(test_list))
print("Median: ",get_median(test_list))
print("Mode: ",get_mode(test_list))
print()
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Mean: ",get_mean(test_list))
print("Median: ",get_median(test_list))
print("Mode: ",get_mode(test_list))
print()


#efficient functions, above functions are completelyy inefficient


def get_mean_eff(iterable):
    if not iterable:#makes sure its not empty
        return []
    #avoid the use of loops as much as you can and
    #use built in functions whenever u can, they are optimized
    return sum(iterable)/len(iterable)




def get_median_eff(iterable): #if i write iterable.sort i will change the iterable
    if not iterable:#makes sure its not empty
        return []
    sorted_list=sorted(iterable)
    #this returns a sorted copy and doesn't change the iterable
    length = len(sorted_list)
    if length % 2 == 0:
        median = (sorted_list[length // 2] + sorted_list[(length // 2) - 1]) / 2
    else:
        median = sorted_list[length // 2]

    return median

def get_mode_eff(iterable):
    if not iterable:#makes sure its not empty
        return []
    #we will use Counter module, it counts the values efficiently
    count_values=Counter(iterable)
    max_count=max(count_values.values())
    if max_count==1:
        return []
    else:
        return [item for item , count in count_values.items() if count==max_count]



test_list = [2, 3, 4, 4, 4, 5, 6, 7]

print("Mean: ",get_mean_eff(test_list))
print("Median: ",get_median_eff(test_list))
print("Mode: ",get_mode_eff(test_list))
print()
test_list = [1, 1, 2, 3, 3, 4, 5]
print("Mean: ",get_mean_eff(test_list))
print("Median: ",get_median_eff(test_list))
print("Mode: ",get_mode_eff(test_list))
print()
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Mean: ",get_mean_eff(test_list))
print("Median: ",get_median_eff(test_list))
print("Mode: ",get_mode_eff(test_list))
print()
