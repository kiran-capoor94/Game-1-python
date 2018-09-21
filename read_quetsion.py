"""Read and printing lines"""


with open("gametest.txt", encoding= "utf-8") as file:
    x =[l.strip() for l in file]

print(x)
