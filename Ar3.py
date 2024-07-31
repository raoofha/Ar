''''; xterm-send "echo -ne \"\\033c\"; systemd-run --scope -p MemoryMax=2G --user python3 $0" ; exit 1 ; 
'''
''''; xterm-send "echo -ne \"\\033c\"; python3 $0" ; exit 1 ; 
'''

def i(e,l):
  if l < 1: return 
  operators = ["h","sub","div"]
  variables = ["x(" + str(i) + ")" for i in range(0,l)]
  new_exprs = exprs = variables.copy()
  while True:
    if e in new_exprs: return exprs.index(e)
    new_exprs = []
    for op in operators:
      for exp1 in exprs:
        for exp2 in exprs:
          if op=="h":
            for exp3 in exprs:
              new_exprs.append(f"{op}({exp1},{exp2},{exp3})")
          else:
            new_exprs.append(f"{op}({exp1},{exp2})")
    exprs.extend(new_exprs)

def u(*xs):
  k = len(xs)
  if k==0: return 0
  e = xs[0]
  if k==1: return e+1
  ns = xs[1:]
  l = len(ns)
  h = lambda n,a,b: (b+1 if n==0 else (a if n==1 and b==0 else (0 if n==2 and b==0 else (a*b if n==2 else (a**b if n==3 else (1 if n>=3 and b==0 else h(n-1,a,h(n,a,b-1))))))))
  sub = lambda a,b: a-b
  div = lambda a,b: a if b==0 else (int(a//b) if a*b>=0 else -int(-a//b))
  ops = {"h": h,"sub":sub ,"div":div}
  operators = ops.keys()
  variables = [str(ns[i]) for i in range(0,l)]
  exprs = variables.copy()
  if e < 0: e = -e
  while len(exprs) < e+1:
    new_exprs = []
    for op in operators:
      for exp1 in exprs:
        for exp2 in exprs:
          if op=="h":
            for exp3 in exprs:
              new_exprs.append(f"{op}({exp1},{exp2},{exp3})")
          else:
            new_exprs.append(f"{op}({exp1},{exp2})")
    exprs.extend(new_exprs)
  return eval(exprs[e],ops)

zero = lambda a: u()
inc = lambda a: u(a)
mul = lambda a,b: u(8,2,a,b)
sub = lambda a,b: u(11,a,b)
div = lambda a,b: u(15,a,b)
pow = lambda a,b: u(8,3,a,b)
dec = lambda a: sub(a,1)
negate = lambda a: sub(0,a)
add = lambda a,b: sub(a,negate(b))
rem = lambda a,b: sub(a,mul(b,div(a,b)))
square = lambda a: mul(a,a)
isNonZero = lambda a: div(square(sub(square(a),1)),square(add(square(a),1)))
isZero = lambda a: isNonZero(isNonZero(a))
Not = lambda a: isNonZero(a)
And = lambda a,b: isZero(add(isZero(a),isZero(b)))
Or = lambda a,b: isZero(mul(a,b))
eq = lambda a,b: isZero(sub(a,b))
notEq = lambda a,b: Not(eq(a,b))
If = lambda a,b,c: add(mul(isNonZero(a),b),mul(isZero(a),c))
isNegative = lambda a: If(isZero(a),1,isNonZero(div(sub(1,a),a)))
isPositive = lambda a: Not(isNegative(a))
lt = lambda a,b: If(eq(a,b),1,If(And(isNegative(a),isPositive(b)),0,If(And(isPositive(a),isNegative(b)),1,If(And(isNegative(a),isNegative(b)),isZero(div(b,a)),isZero(div(a,b))))))
gt = lambda a,b: And(Not(lt(a,b)),Not(eq(a,b)))
lte = lambda a,b: Or(eq(a,b),lt(a,b))
gte = lambda a,b: Or(eq(a,b),gt(a,b))
sign = lambda a: If(isNegative(a),sub(0,1),If(eq(a,0),0,1))
tsub = lambda a,b: If(lt(a,b),0,sub(a,b))
min = lambda a,b: If(lt(a,b),a,b)
max = lambda a,b: If(lt(a,b),b,a)
absolutevalue = lambda a: mul(sign(a),a)
absolutedifference = lambda a,b: absolutevalue(sub(a,b))
isDivisible = lambda a,b: isZero(rem(a,b))
isEven = lambda a: isDivisible(a,2)
isOdd = lambda a: Not(isEven(a))
sum = lambda a,b: div(mul(add(a,b),add(sub(b,a),1)),2)
cantorPair = lambda a,b: div(add(add(add(add(mul(a,a),a),mul(2,mul(a,b))),mul(3,b)),mul(b,b)),2)
ack = lambda a,b: If(lt(a,1),inc(b),sub(u(8,a,2,add(b,3)),3))

####################################################################################################
test = lambda a,b: [(print(f'\x1b[31m{a}\x1b[0m', "==" ,x, f'\x1b[31m{b}\x1b[0m') if str(x)!=str(b) else 0) if b!=None else print(a,"==",x) for x in [eval(a)]]

TRUE = 0
FALSE = 1

test("i(\"h(x(0),x(1),x(2))\",3)",8)
test("i(\"sub(x(0),x(1))\",2)",11)
test("i(\"div(x(0),x(1))\",2)",15)
test("zero(0)",0)
test("zero(1)",0)
test("inc(0)",1)
test("inc(1)",2)
test("inc(-1)",0)
test("sub(42,20)",22)
test("mul(21,2)",42)
test("div(22,2)",11)
test("inc(negate(1))",0)
test("negate(1)",-1)
test("add(2,2)",4)
test("add(10,10)",20)
test("add(33,11)",44)
test("mul(2,4)",8)
test("mul(10,10)",100)
test("mul(negate(10),0)",0)
test("div(10,0)",10)
test("div(10,0)",10)
test("rem(10,0)",10)
test("negate(42)",-42)
test("isZero(42)",FALSE)
test("isZero(0)",TRUE)
test("isZero(negate(42))",FALSE)
test("eq(0,0)",TRUE)
test("eq(0,4)",FALSE)
test("isDivisible(42,2)",TRUE)
test("isDivisible(42,4)",FALSE)
test("isEven(42)",TRUE)
test("isEven(43)",FALSE)
test("isOdd(43)",TRUE)
test("isEven(-42)",TRUE)
test("isEven(-43)",FALSE)
test("div(-42,2)",-21)
test("rem(-42,2)",0)
test("rem(42,2)",0)
test("isOdd(-43)",TRUE)
test("absolutevalue(negate(43))",43)
test("absolutedifference(negate(43),43)",86)
test("sign(42)",1)
test("sign(0)","0")
test("sign(negate(42))",-1)
test("min(42,negate(42))",-42)
test("max(42,negate(42))",42)
test("sum(0,100)",int(100*101/2))
test("sum(negate(100),100)","0")
test("sum(0,2)",int(2*3/2))
test("div(3,2)",int(3/2))
test("cantorPair(2,3)",18)
test("add(42,42)",84)
test("isZero(42)",FALSE)
test("isZero(negate(42))",FALSE)
test("isZero(0)",TRUE)
test("eq(0,0)",TRUE)
test("eq(0,4)",FALSE)
test("notEq(0,0)",FALSE)
test("notEq(0,4)",TRUE)
test("If(TRUE,42,20)",42)
test("If(FALSE,42,20)",20)
test("isNegative(42)",1)
test("isNegative(0)",FALSE)
test("isPositive(0)",TRUE)
test("add(div(2,0),div(1,0))",3)
test("add(div(1,0),div(2,0))",3)
test("ack(3,1)",13)
test("ack(3,3)",61)
test("ack(4,1)",65533)
