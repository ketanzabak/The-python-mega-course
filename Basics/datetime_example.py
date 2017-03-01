import datetime
'''
    This is example for datetime in python .
'''

#main function start here
def main():
    now = datetime.datetime.now()
    yesterday = datetime.datetime(2017,2,27,9,45,0)
    delta = now - yesterday
    print (delta)

if __name__ == '__main__':
    main()
