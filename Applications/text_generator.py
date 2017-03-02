import random , string

def generator(input_letter):
    output_letter=''
    if input_letter == 'v':
        output_letter = random.choice("aeiou")
    elif input_letter == 'c':
        output_letter = random.choice("bcdfghjklmnpqrstvwxy")
    elif input_letter == 'l':
        output_letter = random.choice(string.ascii_letters)

    return output_letter

def main():
    name = ""
    for i in range(0,3):
        letter = input("Enter a letter (v-vowels , c-consonants , l-other): ")
        name = name + generator(letter)

    print (name)
if __name__ == '__main__':
    main()
