# prime_factor
def main():
    pass
    a=int(input())
    l=[]
    list_2=[]
    for num in range (2,a+1):
        if (num>1):
            for i in range(2,num):
                if (num%i==0):
                    break
            else:
                l.append(num)
    for k in l:
        if(a%k==0):
            list_2.append(k)
    print(' '.join(map(str,list_2)))

if __name__ == '__main__':
    main()
