def reverse(input_str):
    if input_str == "":
        return ""
    
    reversed_str = ""
    array_length = len(input_str) - 1
    
    for index in range(array_length, -1, -1):
        reversed_str += input_str[index]
    return reversed_str

print(reverse("Olá mundo"))