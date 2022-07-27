import sys
import argparse

from traitlets import default

if __name__ == '__main__':
    print(1)
    print(sys.argv)
    print(sys.argv[-1])
    print(type(sys.argv[-1]))

    parser = argparse.ArgumentParser()
    parser.add_argument('--usr', type=str, default='tom')
    parser.add_argument('--age', type=int, default=18)
    args = parser.parse_args()

    print(args.usr, args.age)