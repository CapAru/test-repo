#Program to output given number in words(Indian System of Numbering)
w1=["one","two","three","four","five","six","seven","eight","nine"]
w10=["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
w2=["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
ws=["hundred","thousand","lakh","crore"]
l=[]
def word1(n):
    if n==0:
        return("zero")
    else:
        return w1[n-1]
def word10(n):
        return w10[n%10-1]
num=int(input("Enter number: "))
#checking the last two digits
def check10(num):
    w=[]
    rem=num%100
    if rem==0:
        return []
    else:
        quo10=rem//10
        rem10=rem%10
        #checking the 1's place
        if rem10 in range(1,10) and quo10>1:
            w.append(w1[rem10-1])
        if quo10==0:
            w.append(word1(rem))
        #checking 10's place
        elif quo10==1 and rem10!=0:
            w.append(word10(rem))
        elif quo10<10:
            w.append(w2[quo10-1])
        return w

def twodig(n):
    w=[]
    rem=n%100
    if n!=0:
        if rem<10:
            w.append(w1[rem-1])
        elif rem%10==0:
            w.append(w2[rem//10-1])
        elif rem>10 and rem<20:
            w.append(w10[rem-11])
        else:
            w+=check10(rem)
    if rem==0:
        w=[]
    return w

l=check10(num)

#checking hundred's place
def check100(num):
    quo100=num//100
    rem=quo100%10
    if quo100!=0:
        w=[w1[rem-1]+" "+ws[0]]
    if rem==0:
        w=[]
    return w

l+=check100(num)

for i in range(3):
    wn=[ws[i+1]]
    quo=num//(1000*(100**i))
    wn+=twodig(quo)
    if wn==[ws[i+1]]:
        l+=[]
    else:
        l+=wn

l.reverse()
first=l[0].capitalize()
l[0]=first
for i in l:
    print(i, end=" ")
