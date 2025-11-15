def solve(string) :
    vowels = "AaOoUuEeIi"
    result = ""
    for char in string :
        if char not in vowels :
             result += char
    return result

if __name__ == "__main__" :
    text =input("Write string : ")
    result = solve(text)
    print(f"{result}")

