import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    letters = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        letters.append((s[::-1] + s[1:]).center(4*size-3, "-"))
    print("\n".join(letters[::-1] + letters[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
