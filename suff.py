'''

    Reads a file and retuns the longest repeating substring.
'''
import sys

def main():
    if len(sys.argv) == 1:
        print "Please specify a File Name"

    file_name = sys.argv[1]
    f = open(file_name,'r')
    content = f.read()
    split_value = content.split(' ')
    print split_value








if __name__ == '__main__':
   main()
