a = input()
operator  = ["+" , "-" , "*" , "/" , "^","(",")"]
# oprnd = []
# oprtr = []

def pstfx(x):
    oprnd = []
# oprtr = []
    for i in x:
        if i not in operator:
            oprnd.append(i)
        else:
            f = float(oprnd.pop())
            s = float(oprnd.pop())
            if i == "+":
                r = f+s

            if i == "*":
                r = f*s

            if i == "/":
                r = s/f

            if i == "-":
                r = s-f

            if i == "^":
                r = s**f

            
            oprnd.append(r)
    return oprnd.pop()


def infx(x):
    oprnd = []
    oprtr = []
    prec = {}
    prec["*"] = 4
    prec["/"] = 4
    prec["+"] = 3
    prec["-"] = 3
    prec["^"] = 2
    prec["("] = 1
    for i in x:
        if i not in operator:
            oprnd.append(i)
        elif i == "(":
            oprtr.append(i)
        elif i == ")":
            topToken = oprtr.pop()
            while topToken != '(':
                oprnd.append(topToken)
                topToken = oprtr.pop()
        else:
            while (oprtr != []) and \
               (prec[oprtr[-1]] >= prec[i]):
                  oprnd.append(oprtr.pop())
            oprtr.append(i)



    while oprtr != []:
        oprnd.append(oprtr.pop())
    return "".join(oprnd)





if a[-1] in operator and a[-1] != ")":
    print (pstfx(a))
else:
    print (infx(a))
