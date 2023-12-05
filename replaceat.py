# !/usr/bin/env python3
import argparse

if __name__ == '__main__':
  # Create the parser
  parser = argparse.ArgumentParser( description="A simple argparse example" )

  # Add arguments
  parser.add_argument( 'number1', type=int, help='Number 1' )
  parser.add_argument( 'number2', type=int, help='Number 2' )
  parser.add_argument( 'op', type=str, help='Operation')

  # Parse the arguments
  args = parser.parse_args()

  if args.op=='add':
    print(args.number1+args.number2)
  elif args.op=='substract':
    print(args.number1-args.nuber2)
  elif args.op=='multiply':
    print(args.number1*args.nuber2)
  elif args.op=='divide':
    print(args.number1/args.nuber2)