import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default= 1.0,
                       help='What is the first no.?')
    parser.add_argument('--y', type=float, default= 1.0,
                       help='What is the second no.?')
    parser.add_argument('--operation', type=str, default= 'add',
                       help='What is the operation?(add, sub, mul,div)')
    args= parser.parse_args()
    sys.stdout.write(str(calc(args)))
    
def calc(args):
    if args.operation=='add':
        return args.x + args.y
    elif args.operation=='sub':
        return args.x -args.y
    elif args.operation=='mul':
        return args.x *args.y
    elif args.operation=='div':
        return args.x /args.y
    
if __name__ == '__main__':
    main()
