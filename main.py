
string_1 = "ah#brr11122######acadabbRd###Ra"  #abracadabRa
string_2 = "####abrd#acadabb#Ra"              #abracadabRa

# runs in 0(n)

def do_they_match(str_1, str_2):
    # first string pointer (last character)
    a = len(str_1)-1
    # second string pointer (last character)
    b = len(str_2)-1
    # while there are characters to go through
    while a >= 0 and b >= 0:
        if str_1[a] == '#' or str_2[b] == '#':
            if str_1[a] == '#':
                # two is the number of characters that will be deleted by # (the # and the char before it)
                count = 2
                # check if the next symbol after # is also a #
                while str_1[a-1] == '#':
                    # if so, there are two more symbols to delete (increase the count)
                    count += 2
                    # shift value to check the next character
                    a -= 1
                else:
                    # once we go through all # characters following one another we move the pointer
                    a = a - count

            if str_2[b] == '#':
                count = 2
                while str_2[b-1] == '#':
                    count += 2
                    b -= 1
                else:
                    a = a - count

        else:
            if str_1[a] != str_2[b]:
                return False
            else:
                # move the pointer
                a -= 1
                b -= 1
    return True


print(do_they_match(string_1, string_2))






