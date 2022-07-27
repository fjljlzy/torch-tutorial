from ast import arg
import sys
import argparse


if __name__ == '__main__':
    print(1)
    print(sys.argv)
    print(sys.argv[-1])
    print(type(sys.argv[-1]))

    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true') # once --debug appear, begin debug mode
    parser.add_argument('--usr', type=str, default='tom')
    parser.add_argument('--age', type=int, default=18)
    args = parser.parse_args()
    if args.debug:
        print(args.usr, args.age)