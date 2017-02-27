
def write_list_to_file(filename , input):
    file = open(filename,'w')
    for item in input :
        file.write(item+"\n")
    file.close()

def write_string_to_file(filename , input):
    file = open(filename,'w')
    file.write(input)
    file.close()

def append_string_to_file(filename , input):
    file = open(filename,'a')
    file.write(input)
    file.close()

def append_string_to_file_using_with (filename , input):
    with open(filename , 'a') as file :
        file.write(input)
    #no need to use file.close()

def main():
    #write_string_to_file("example.txt","welcome to files tutorials in python \n Hello Guys !!!")
    '''
    input_list = ["line 1" , "line 2" , "line 3"]
    write_list_to_file("example.txt",input_list)
    '''
    #append_string_to_file("example.txt","line 4")
    append_string_to_file_using_with("example.txt","line 5")
if __name__ == '__main__':
    main()
