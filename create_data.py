import random
import sys
import argparse

K_SIZE = 1000

class Generator:
    def __init__(self,low=4,high=10,only_chars=False):
        if not only_chars:
                self.table = {i:chr(i) for i in range(33,127)}
                self.rand_low = 33
                self.rand_high = 126
        else:
                table1 = [chr(i+ord('a')) for i in range(0,26)]
                table2 = [chr(i+ord('A')) for i in range(0,26)]
                self.table = table1+table2
                self.rand_low = 0
                self.rand_high = len(self.table)-1
        self.low = low
        self.high = high


    def create_n_bytes(self,total_bytes):
        bytes_created = 0
        """Hack at the moment, this condition will fail only after more than n bytes are 
        written """
        while bytes_created < total_bytes:
            bytes_to_create = random.randint(self.low,self.high)
            bytes_created = bytes_created+bytes_to_create+1
            word=[""]*bytes_to_create
            for i in range(bytes_to_create):
                word[i] = self.table[random.randint(self.rand_low,self.rand_high)]
            text = "".join(word)
            #print(str(hash(text))+"\t"+text)
            print(text)


def get_file_size_in_bytes(size):
    multiplier = 1
    size_unit = size[-1]

    if size_unit == 'M' or size_unit == 'm':
        multiplier = K_SIZE*K_SIZE
    elif size_unit == 'K' or size_unit == 'k':
        multiplier = K_SIZE
    elif size_unit == 'G' or size_unit == 'g':
        multiplier = K_SIZE*K_SIZE*K_SIZE
    elif size_unit in ('0','1','2','3','4','5','6','7','8','9'):
        multiplier = 1
    else:
        writeStdError("invalid size")
        exit()

    total_bytes = 0
    if multiplier == 1:
        total_bytes = int(size)
    else:
        total_bytes = multiplier*int(size[:len(size)-1])

    return total_bytes


def writeStdError(message):
    sys.stderr.write(message)

def main():
    parser = argparse.ArgumentParser(description='Generate Random Strings of printable ASCII characters')
    parser.add_argument('size',help='The size of the file in bytes you want to generate ex 1G , 10M,5k,100')
    parser.add_argument('--min',dest='min_len',default=4,const=4,action='store',\
              nargs='?',type=int,\
              help='The minimum string length per line')
    parser.add_argument('--max',dest='max_len',default=10,const=10,action='store',\
              nargs='?',type=int,\
              help='The maximum string length per line')
    parser.add_argument('--chars',action='store_true',help='Only generate string with characters [a-z][A-Z]')
    args = parser.parse_args()
    gen = Generator(args.min_len,args.max_len,args.chars)
    file_size = get_file_size_in_bytes(args.size)
    if args.min_len > args.max_len:
	    writeStdError("Invalid Min , Max arguments")
	    exit()
    #print("Size "+args.size)
    #print("Min Len "+str(args.min_len))
    #print("Max Len "+str(args.max_len))
    #print("Only Chars "+str(args.chars))
    gen.create_n_bytes(file_size)

if __name__== "__main__":
    main()
