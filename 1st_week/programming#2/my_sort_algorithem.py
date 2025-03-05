def my_sort(in_target:list)->list:
    target = in_target[:]
    list_len = len(target)

    for i in range(list_len):
        small_idx = i
        for j in range(i, list_len):
            if target[small_idx]>target[j]:
                small_idx = j
        
        temp = target[small_idx]
        target[small_idx]=target[i]
        target[i]=temp

    return target
    
row_list = list(map(int, input('정수를 띄어쓰기로 구분해 입력\n').split()))
print('sorted list:', my_sort(row_list))
