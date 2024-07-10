inc = (a) => (typeof(a.v)==="bigint") ? a : 1n+a
sub = (a,b) => (typeof(a.v)==="bigint") ? a : ((typeof(b.v)==="bigint") ? b : 0n+a-b)
mul = (a,b) => (typeof(a.v)==="bigint") ? a : ((typeof(b.v)==="bigint") ? b : 0n+a*b)
div = (a,b) => (typeof(a.v)==="bigint") ? a : ((typeof(b.v)==="bigint") ? b : ((b!==0n) ? 0n+a/b : {v:a,toString(a){return this.v.toString(a);},valueOf(){return this.v;}}))
/* for correct logging of gap values */ const originalLog = console.log; console.log = (...args) => originalLog(...args.map((a)=>a.valueOf?a.valueOf():a));

zero = (a) => sub(a,a)
one = (a) => inc(zero(a))
two = (a) => inc(one(a))
three = (a) => inc(two(a))
negate = (a) => sub(zero(a),a)
add = (a,b) => sub(a,negate(b))
rem = (a,b) => sub(a,mul(b,div(a,b)))
square = (a) => mul(a,a)
isNonZero = (a) => div(square(sub(square(a),one(a))),square(add(square(a),one(a))))
isZero = (a) => isNonZero(isNonZero(a))
not = (a) => isNonZero(a)
and = (a,b) => isZero(add(isZero(a),isZero(b)))
or = (a,b) => isZero(mul(a,b))
eq = (a,b) => isZero(sub(a,b))
notEq = (a,b) => not(eq(a,b))
divz = (a,b) => div(a,add(b,isNonZero(b)))
If = (a,b,c) => add(mul(isNonZero(a),b),mul(isZero(a),c))
isNegative = (a) => If(isZero(a),one(a),isNonZero(divz(sub(one(a),a),a)))
isPositive = (a) => not(isNegative(a))
lt = (a,b) => If(eq(a,b),one(a),If(and(isNegative(a),isPositive(b)),zero(a),If(and(isPositive(a),isNegative(b)),one(a),If(and(isNegative(a),isNegative(b)),isZero(divz(b,a)),isZero(divz(a,b))))))
gt = (a,b) => and(not(lt(a,b)),not(eq(a,b)))
lte = (a,b) => or(eq(a,b),lt(a,b))
gte = (a,b) => or(eq(a,b),gt(a,b))
sign = (a) => If(isNegative(a),sub(zero(a),one(a)),If(eq(a,zero(a)),zero(a),one(a)))
tsub = (a,b) => If(lt(a,b),zero(a),sub(a,b))
min = (a,b) => If(lt(a,b),a,b)
max = (a,b) => If(lt(a,b),b,a)
absolutevalue = (a) => mul(sign(a),a)
absolutedifference = (a,b) => absolutevalue(sub(a,b))
isDivisible = (a,b) => isZero(rem(a,b))
isEven = (a) => isDivisible(a,two(a))
isOdd = (a) => not(isEven(a))
