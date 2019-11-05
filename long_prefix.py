def find_common_prefix(string1, string2):
    result = ""
    lenght1, lenght2 = len(string1), len(string2)
    index1, index2 = 0, 0

    while index1 <= lenght1 - 1 and index2 <= lenght2 - 1:
        if string1[index1] != string2[index2]:
            break
        result += string1[index1]
        index1 += 1
        index2 += 1

    return result


def common_prefix(array, fist, last):
    if fist == last:
        print("Primeiro e ultimo index são iguais !!")
        return array[fist]

    if last > fist:
        print("Primeiro e ultimo index são diferentes !!")
        half = fist + (last - fist) // 2
        print("Str1: {}\t Str2: {}\t Half: {}".format(array[fist],
                                                      array[last],
                                                      array[half]))
        string1 = common_prefix(array, fist, half)
        string2 = common_prefix(array, half + 1, last)
        result = find_common_prefix(string1, string2)
        print("Result: {}".format(result))
        return result


if __name__ == "__main__":
    array = str(input())
    array = array.split(" ")
    lenght = len(array)
    result = common_prefix(array, 0, lenght - 1)

    if len(result):
        print("Prefix: {}.".format(result))

    else:
        print("Doesn't have prefix !!")
