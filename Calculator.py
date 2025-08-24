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
def add(*args):return sum(args)
def subtract(*args):
    result=args[0]
    for i in args[1:]:
        result-=i
    return result
def multiply(*args):
    if not args:
        return "No numbers are given"
    result=args[0]
    for i in args[1:]:
        result*=i
    return result
def division(*args):
    if not args:
        return "No numbers are given"
    result=args[0]
    for i in args[1:]:
        result/=i
    return result
def exponentiation(a,b):return a**b
def squareroot(args):
    return math.sqrt(args)
def lcma(a,b):
    if a>b:
        l=a 
    else:
        l=b
    while(l<=a*b):
        if l%a==0 and l%b==0:
            return l
        l+=1
def lcm(*args):
    if len(args)<2:
        return "Required amount of numbers are not given for this operation"
    result=args[0]
    for i in args[1::]:
        result=lcma(result,i)
    return result
def hcfa(a,b):
    h= a if a<b else b
    while h>=1:
        if a%h==0 and b%h==0:
            return h
        h-=1
def hcf(*args):
    if len(args)<2:
        return "Required amount of numbers are not given for this operation"
    result=args[0]
    for i in args[1::]:
        result=hcfa(result,i)
    return result
def factorial(a):
    if a==0 or a==1:
        return 1
    n=1
    while a!=1:
        n=n*a
        a-=1
    return n
def parse(text):
    tokens = text.upper().split()
    result, current_op = None, None

    for token in tokens:
        # If token is a number
        try:
            num = float(token)
            if result is None:
                result = num
            else:
                # Apply the current operation
                if current_op is None:
                    raise ValueError("No operator before number")
                result = current_op(result, num)
        except ValueError:
            # If token is an operation word or symbol
            if token in operations3:
                current_op = operations3[token]

    return result


def sorry():
    print("Sorry I couldn't understand what you wrote please check your prompt and try again.")
def end():
    print("Thank-You for using Smart-Calculator")
    input("Press any key to Exit.")
    exit()

operations1={'END':end,'TERMINATE':end,'EXIT':end}
operations2={'FACTORS':factorial,'FACTORIAL':factorial,'SQUAREROOT':squareroot}
operations3={'ADD':add,'PLUS':add,'SUM':add,'SUBTRACT':subtract,'MINUS':subtract,'MULTIPLY':multiply,'INTO':multiply,'DIVIDE':division,'POWER':exponentiation,'EXPONENTIAL':exponentiation,'LCM':lcm,'HCF':hcf}

def main():
    print("WelCome to the Smart-Calculator")
    while True:
        text=input("Enter your problem:\n")
        if True:
            for word in text.split(" "):
                if word.upper() in operations3.keys():
                    try:
                        print(parse(text))
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
                        print("Sorry you cannot operate this operation for different operations at same time.")
                    finally:
                        break
                elif word.upper() in operations1.keys():
                        l=extract_numbers_from_prompt(text)
                        r=operations1[word.upper()]()
            else:
                sorry()
                           
                
                
    
            
if __name__=="__main__":
    main()