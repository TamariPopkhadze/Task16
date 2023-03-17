def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    punctuation = "!# $%&'()*+, -./:;<=>?@[\]^_`{|}~"
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    leters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

    if len(s) < 2 or len(s) > 6:
        return False
    if s[0] not in leters or s[1] not in leters:
        return False
    for x in s:
        if x in punctuation:
            return False
    for z in range(0, len(s)):
        if s[z] in numbers and s[z-1] in leters:
            newstr = s[z:]
            if newstr[0] == "0":
                return False
            for i in newstr:
                if i in leters:
                    return False
    return True


main()
