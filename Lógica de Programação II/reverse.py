import sys

def reverse(*args):
    rs = list(args[1:])
    rs.reverse()
    return rs

if __name__ == "__main__":
    print(reverse(*sys.argv))