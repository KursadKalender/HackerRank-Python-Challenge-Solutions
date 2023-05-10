import textwrap

def wrap(string, max_width):
    filled_string=textwrap.fill(string, max_width)
    return filled_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
