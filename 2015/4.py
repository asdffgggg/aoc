from hashlib import md5

ex = "abcdef"
input = "bgvyzdsv"

def part1(input):
    i = 0
    while True:
        check = input + str(i)
        hash = md5(str.encode(check)).digest().hex()
        if hash.startswith("00000"):
            return i

        i += 1

def part2(input):
    i = 0
    while True:
        check = input + str(i)
        hash = md5(str.encode(check)).digest().hex()
        if hash.startswith("000000"):
            return i

        i += 1
  
print(part2(input))