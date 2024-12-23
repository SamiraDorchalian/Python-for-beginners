my_string = input('Enter string: ')

nums = []

for char in my_string:
    # print(ord(char) , end=' ')
    nums.append(str(ord(char) + 12))

secret_string = ','.join(nums)
print(secret_string)

# secret_string = '101,123,129,44,111,109,122,44,112,123,44,117,128'

string_list = []

for num_str in (secret_string.split(',')):
    string_list.append(chr(int(num_str) - 12))

print(''.join(string_list))