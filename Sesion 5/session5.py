#SEx 1+2:

def remove_dollar_sign(string):
    i = 0
    
    while i <= len(string)-1: #Duyet
        if string[i] == '$':
            string = string.replace(string[i],'') # Neu gap ky tu $ thi xoa
        else:
            i +=1 # Khong thi tang con chay
            
    return string

string_with_no_dollars = remove_dollar_sign('$80% percent of $life is to show $up')

if string_with_no_dollars == '80% percent of life is to show up':
    print('Your function is correct')
else:
    print('Oops, there\'s a bug')

print()

#SEx 2+3: 

def get_even_list(lis):
    i = 0
    while i <= len(lis)-1: #Duyet
        if lis[i] % 2 != 0:
            del lis[i]  # Not even number == del
        else:
            i +=1 # Khong thi tang 1 vao con chay
    return lis

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")





