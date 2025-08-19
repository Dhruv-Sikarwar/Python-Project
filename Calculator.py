import math
def extract_numbers_from_prompt(text):
    l=[]
    for i in text.split(' '):
        for j in i.split(','):
            try:
                l.append(float(j))
            except ValueError:
                pass
    return l
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def exponentiation(a,b):
    return a**b
def squareroot(a):
    return math.sqrt(a)
def lcm(a,b):
    if a>b:
        l=a 
    else:
        l=b
    while(l<=a*b):
        if l%a==0 and l%b==0:
            return l
        l+=1
def hcf(a,b):
    h= a if a<b else b
    while h>=1:
        if a%h==0 and b%h==0:
            return h
        h-=1
def factorial(a):
    n=1
    while a!=1:
        n=n*a
        a-=1
    return n
def sorry():
    print("Sorry I couldn't understand what you wrote please check your prompt and try again.")
def end():
    print("Thank-You for using Smart-Calculator")
    print("Press any key to Exit.")
    input()
    exit()

operations1={'END':end,'TERMINATE':end,'EXIT':end}
operations2={'FACTORS':factorial,'FACTORIAL':factorial,'SQUAREROOT':squareroot}

operations3={'ADD':add,'PLUS':add,'SUM':add,'SUBTRACT':subtract,'MINUS':subtract,'MULTIPLY':multiply,'INTO':multiply,'DIVIDE':division,'POWER':exponentiation,'EXPONENTIAL':exponentiation,'LCM':lcm,'HCF':hcf}

def main():
    print("WelCome to the Smart-Calculator")
    while True:
        text=input("Enter your problem:\n")
        for word in text.split():
            if word.upper() in operations3.keys():
                try:
                    l=extract_numbers_from_prompt(text)
                    r=operations3[word.upper()](l[0],l[1])
                    print(r)
                except:
                    print("Something is Wrong")
                finally:
                    break
            elif word.upper() in operations2.keys():
                try:
                    l=extract_numbers_from_prompt(text)
                    r=operations2[word.upper()](l[0])
                    print(r)
                except:
                    print("something is wrong")
                finally:
                    break
            elif word.upper() in operations1.keys():
                    l=extract_numbers_from_prompt(text)
                    r=operations1[word.upper()]()
        else:
            sorry()
            break
if __name__=="__main__":
    main()