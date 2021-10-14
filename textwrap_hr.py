import textwrap

def wrap(string, max_width):
    a = textwrap.TextWrapper(width=max_width)
    word_list = a.fill(text=string)
    return textwrap.fill(string,max_width)

if __name__=='__main__':
    n = input()
    p = int(input())
    print(wrap(n,p))