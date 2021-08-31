#Number Line Jumps - from Hackerrank by Juan Cruz

def kangaroo(x1, v1, x2, v2):
    t=float(0)
    t_=0
    try:
        t=(x1-x2)/(v2-v1)
        t_=(t-int(t))
    except ZeroDivisionError:
        t=0
#-----------------------------REST of CODE---------------------------------------

    if t<=0:
        print("NO")
    elif t>0 and t_==0:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)
