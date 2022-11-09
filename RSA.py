import math
def gcd(a, h):
	temp = 0
	while(1):
		temp = a % h
		if (temp == 0):
			return h
		a = h
		h = temp


p = 5
q = 7
n = p*q
e = 3
phi = (p-1)*(q-1)
while (e < phi):
	if(gcd(e, phi) == 1):
		break
	else:
		e = e+1
k = 1
d = (1 + (k*phi))/e
# print(d)
msg = 12.0
print("Original message:", msg)
c = pow(msg, e)
c = math.fmod(c, n)
print("Encrypted message:", c)
P = pow(c, d)
P = math.fmod(P, n)
print("Plain text:", P)