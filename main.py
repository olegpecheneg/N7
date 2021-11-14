import random


def find_minrun(n): 
    MINIMUM = 32
    r = 0
    while n >= MINIMUM: 
        r |= n & 1
        n >>= 1
    return n + r

def loader(lists):
    
    
    first_array = []
    for i in lists:
        for k in i:
            first_array.extend(k)

    return first_array

def get_list(run, array): # эта функция делит массив на подмассивы величиной minrun
    
    list_of_array = []
    for i in range(len(array) // run):
        temp = []
        for j in range(run):
            temp.append(array[i * run + j])
        list_of_array.append(temp)

    return(list_of_array)



def insertion(data): # эта функция сортирует вставками те массивы, которые ты передашь
    
    for i in range(len(data)):
        j = i - 1 
        key = data[i]
        while data[j] > key and j >= 0:
            data[j + 1] = data[j]
            j -= 1
            data[j + 1] = key

    return data

def merge_func(left_array, right_array): # эта функция сортирует два массива слиянием
    
    array = []
    left_array = insertion(left_array)      # сортирует два переданных
    right_array = insertion(right_array)    # массива вставкой
    
    k, y = 0, 0
    
    for i in range(len(left_array) + len(right_array)):
        if k >= len(left_array):
            array.append(right_array[y])
            y += 1
        elif y >= len(right_array):
            array.append(left_array[k])
            k += 1
        else:
            if left_array[k] <= right_array[y]:
                array.append(left_array[k])
                k += 1
            else:
                array.append(right_array[y])
                y += 1
                
    return array

def merge(*lists):
    
    a = loader(lists)
    
    list_of_array = get_list(find_minrun(len(a)), a) # здесь мы получаем
                        #двумерный массив подмассива
                                        

                                        
    while len(list_of_array) != 1:      # этот цикл работает, пока внутри 
        # input()                         # массива нее останется один элемент,
                                        #то есть все подмассивы не сольются
        tt = len(list_of_array)
        save_list = list_of_array[:]    # просто бэкап нашего двумерного массива
        temp_list = []
        for i in range(0, tt - 1, 2):   # шагаем по двумерному массиву через
                                        # одного
                                        
            result = merge_func(list_of_array[i], list_of_array[i + 1])  # сливает  
                                                    # два соседних подмассива
    
            temp_list.append(result)    # сохраняет результат во временное 
                                        #хранилище, нужно чтоб
                                        # не изменять исходный двумерный массив
            
            save_list.pop(0)            # удаляет первый отработанный элемент 
                                        #двумерного массива удаляет второй 
            save_list.pop(0)            # отработанный элемент двумерного массива
            
        if save_list:                   # рофловая тема, это условие значит,
                                        # что если save_list содержит хоть 
                                        # что-то - выполняется блок кода
                                        
            temp_list.append(save_list[0])  # а именно - добавится 1-й элемент
                                            # из хранилища, это условие нужно 
                                            # чтобы, если run'ов в list_of_array
                                            # будет нечентное количество
                                            # последний не потерялся,
                                            # так как в цикле мы шагаем через 2
        list_of_array = temp_list[:]
    print(f'answer = {len(list_of_array[0])}')
    print(list_of_array[0])

if __name__ == "__main__":
    a, b = [[random.randint(1, 100) for _ in range(random.randint(1, 20))] for j in range(40)], [[random.randint(1, 100) for k in range(random.randint(1, 20))] for i in range(40)]
  
    merge(a, b)
