from hashlib import md5

ex = "abc"
input = "reyedfim"

def part1(input):
    password = ""
    i = 0
    while len(password) < 8:
        check = input + str(i)
        hash = md5(str.encode(check)).digest().hex()
        if hash.startswith("00000"):
            print(hash)
            password += hash[5]

        i += 1
    return password


def part2(input):
    password = ["","","","","","","",""]
    count = 0
    i = 0
    while count < 8:
        check = input + str(i)
        hash = md5(str.encode(check)).digest().hex()
        if hash.startswith("00000"):
            print(hash)
            index = hash[5]
            if index.isdigit():
                index = int(index)
                if index < 8 and len(password[index]) == 0:
                    password[index] = hash[6]
                    count +=1

        i += 1
    return "".join(password)
print(part2(input))