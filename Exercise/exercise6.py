import glob
import datetime

#main function
def main():
    files = glob.glob(pathname="Sample-Files/*.txt")
    with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%s-%f")+".txt" , 'w') as write_file :
        for file in files :
            with open(file , 'r') as readfile:
                write_file.write(readfile.read()+"\n")

if __name__ == '__main__':
    main()
