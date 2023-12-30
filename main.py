def convert_to_snake_case(camel_case):
    new_list   = []
    new_string = ""
    counter = 0
    
    
    for i in camel_case:
        if counter == 0:
            new_list.append(i.lower())
            counter += 1
        elif  i == i.upper() and i.isalpha() == True:
            new_list.append("_")
            new_list.append(i.lower())
            counter += 1
        else:
            new_list.append(i)
            counter += 1
    
    new_string = "".join(new_list)
    return new_string
    

print(convert_to_snake_case("CamelCase!"))