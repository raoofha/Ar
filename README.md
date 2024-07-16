# Ar : a total and turing complete language
inspired by [Blindfolded Arithmetic](https://esolangs.org/wiki/Blindfolded_Arithmetic) and [Z3](https://esolangs.org/wiki/Z3)

did you know that you don't need loop or recursion to program ?!
you only need these four functions
```python
inc = lambda a: a if type(a)==str else a+1
sub = lambda a,b: a if type(a)==str else (b if type(b)==str else a-b)
mul = lambda a,b: a if type(a)==str else (b if type(b)==str else a*b)
div = lambda a,b: a if type(a)==str else (b if type(b)==str else (str(a) if b==0 else int(a/b)))
```
notice that we can use integers instead of `inc` so only three functions is needed for programming
## syntax
to be implemented
## examples
you can see that in the limit (unbounded program length) these four functions are turing complete
```python
zero = lambda a: sub(a,a)
one = lambda a: inc(zero(a))
two = lambda a: inc(one(a))
three = lambda a: inc(two(a))
dec = lambda a: sub(a,one(a))
negate = lambda a: sub(zero(a),a)
add = lambda a,b: sub(a,negate(b))
rem = lambda a,b: sub(a,mul(b,div(a,b)))
square = lambda a: mul(a,a)
isNonZero = lambda a: div(square(sub(square(a),one(a))),square(add(square(a),one(a))))
isZero = lambda a: isNonZero(isNonZero(a))
Not = lambda a: isNonZero(a)
And = lambda a,b: isZero(add(isZero(a),isZero(b)))
Or = lambda a,b: isZero(mul(a,b))
eq = lambda a,b: isZero(sub(a,b))
notEq = lambda a,b: Not(eq(a,b))
divz = lambda a,b: div(a,add(b,isNonZero(b)))
If = lambda a,b,c: add(mul(isNonZero(a),b),mul(isZero(a),c))
isNegative = lambda a: If(isZero(a),one(a),isNonZero(divz(sub(one(a),a),a)))
isPositive = lambda a: Not(isNegative(a))
lt = lambda a,b: If(eq(a,b),one(a),If(And(isNegative(a),isPositive(b)),zero(a),If(And(isPositive(a),isNegative(b)),one(a),If(And(isNegative(a),isNegative(b)),isZero(divz(b,a)),isZero(divz(a,b))))))
gt = lambda a,b: And(Not(lt(a,b)),Not(eq(a,b)))
lte = lambda a,b: Or(eq(a,b),lt(a,b))
gte = lambda a,b: Or(eq(a,b),gt(a,b))
sign = lambda a: If(isNegative(a),sub(zero(a),one(a)),If(eq(a,zero(a)),zero(a),one(a)))
tsub = lambda a,b: If(lt(a,b),zero(a),sub(a,b))
min = lambda a,b: If(lt(a,b),a,b)
max = lambda a,b: If(lt(a,b),b,a)
absolutevalue = lambda a: mul(sign(a),a)
absolutedifference = lambda a,b: absolutevalue(sub(a,b))
isDivisible = lambda a,b: isZero(rem(a,b))
isEven = lambda a: isDivisible(a,two(a))
isOdd = lambda a: Not(isEven(a))
```
## without limit
### Universal function
notice that
```
inc(div(42,0)) == '42'  # if divide by zero occur halt and return the numerator
```
since diagonal argument is blocked it is an open question whether you can define universal functions in this language
### Ackermann function
[ais523](https://esolangs.org/wiki/User:Ais523) had argued that this language can be interpreted by a primitive recursive language
so it can't compute the ackermann function, but I'm not sure that I accept that because diagonal argument does not work for this language

my argument is this: 
suppose we defined two magical functions `u` and `g` such that
```
u(index_of_f) == f(0)
```
and
```
g(m,n) == the index of the shortest program that compute ack(m,n)
```
then we have
```
ack(m,n) == u(g(m,n))
```
