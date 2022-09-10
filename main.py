
string_1 = "ah#brr11122##a#11######acadabbRd###Ra"  #abracadabRa
string_2 = "####abrd#acadabb#Ra"              #abracadabRa

# runs in 0(n)

def do_they_match(str_1, str_2):
    # first string pointer (last character)
    a = len(str_1)-1
    # second string pointer (last character)
    b = len(str_2)-1
    # while there are characters to go through
    while a >= 0 or b >= 0:
        if str_1[a] == '#':
            # two is the number of characters that will be deleted by # (the # and the char before it)
            skip = 1
            # check if the next symbol after # is also a # or if we have to pass by the character
            while (a >= 0 and str_1[a] == '#') or (a >= 0 and skip > 0):
                if str_1[a-1] == '#':
                # increase the count and move the pointer
                    skip += 1
                    a - = 1
                else:
                    # reduce the count and move the pointer
                    skip -= 1
                    a - = 1

        if str_2[b] == '#':
            skip = 1
            while (b >= 0 and t[b] == '#') or (b >= 0 and skip > 0):
                if str_2[b-1] == '#':
                    skip += 1
                    b - = 1
                else:
                    skip -= 1
                    b - = 1
        
        # in accesing the value of the current character we have to account for delete operation to go beyond the beginning of the string 
        current_a = str_1[a] if a >= 0 else ''
        current_b = str_2[b] if b >= 0 else ''
        
        if current_a != current_b:
            return False
        
        # move the pointer
        a -= 1
        b -= 1
    return True


print(do_they_match(string_1, string_2))






