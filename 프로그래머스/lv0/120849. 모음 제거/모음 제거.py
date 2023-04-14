def solution(my_string):
    lst = ['a','e','i','o','u']
    for i in lst:
        if i in my_string: 
            my_string = my_string.replace(i,'')
    return my_string