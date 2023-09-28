def insert_element(slist, ID, element):
    slist.insert(ID, element)


def src_element(slist, ID):
    if 0 <= ID < len(slist):
        return slist[ID]
    else:
        return None

def remove_element(slist, ID):
    if 0 <= ID < len(slist):
        return slist.pop(ID)
    else:
        return None

def prev_next(slist, ID):
    previous = slist[ID - 1] if ID > 0 else None
    next = slist[ID + 1] if ID < len(slist) - 1 else None
    return previous, next

def merge_lists(list1, list2):
    return list1 + list2


def merge_sorted_lists(list1, list2, key=None):
    merged = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if key:
            if key(list1[i]) <= key(list2[j]):
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        else:
            if list1[i] <= list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1

    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

list_a = [66, 99, 21]
list_b = [12, 52, 65]

insert_element(list_a, 1, 10)  
print ("Список:")
print(list_a)
print("====") 

element = src_element(list_a, 2) 
print ("Знайдений елемент з індексом 2")
print(element) 
print("====") 

removed_element = remove_element(list_a, 2) 
print ("Видалений елемент:")
print(removed_element) 
print ("Список:")
print(list_a) 
print("====") 

previous, next = prev_next(list_a, 1)
print("Попередній:")
print(previous)  
print ("Наступний")
print(next) 
print("====")  

merged_list = merge_lists(list_a, list_b) 
print ("2 списки разом:")
print(merged_list)  
print("====") 

sorted_list = merge_sorted_lists(list_a, list_b)  
print ("Відсортований список:")
print(sorted_list)  
print("====") 