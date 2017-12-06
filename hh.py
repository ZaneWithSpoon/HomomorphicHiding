# Homomorphic Hidings hh.py
# Zane Witherspoon
# 12/5/2017
# An RSA implementation of the Homomorphic hidings used in zkSNARKS

import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

x = 101
y = 243
mult = x * y
add = x + y

print 'x = ', x
print 'y = ', y
print 'x * y = ', mult
print 'x + y = ', add
print ''

print '==================================='
print 'RSA for Homomorphic Multiplication '
print '==================================='
print ''

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange

encrypted_x = publickey.encrypt(x, 32)
encrypted_y = publickey.encrypt(y, 32)
encrypted_ans = publickey.encrypt(mult, 32)


print '======Encrypted values============'
print 'E(x)=', encrypted_x[0]
print 'E(y)=', encrypted_y[0]
print 'E(x*y)=', encrypted_ans[0]
print ''

x_times_y = encrypted_x[0] * encrypted_y[0]
decrypted_xy = key.decrypt(x_times_y)
decrypted_ans = key.decrypt(encrypted_ans)


print '======zkSnark===================='
print 'E(x) * E(y)=',x_times_y
print 'D(E(x) * E(y))=',decrypted_xy
print 'D(E(x * y))=',decrypted_ans
print ''

if (decrypted_xy==decrypted_ans):
	print 'Alice has proven she knows the product is ',mult
else:
	print 'Alice has proven she does not know the product is ',mult

print ''
print '==================================='
print '  Modulus for Homomorphic Addition '
print '==================================='
print ''


n=47
g= 3

E1= g**( (x+y) % (n-1)) % n
E2= (g**x * g**y) % n
E3 = g**(add) % n

print '======Agreed parameters============'
print 'P=',n,'\t(Prime number)'
print 'G=',g,'\t(Generator)'
print 'x=',x,'\t(Value 1 - Alice first value)'
print 'y=',y,'\t(value 2 - Alice second value)'
print 'ans=',add,'\t(Answer = x+y?)'
print ''

print '======Encrypted values============'
print str(g) + '^x=',(g**x) % n
print str(g) + '^y=',(g**y) % n
print str(g) + '^(x+y)=',(g**add) % n
print ''

print '======zkSnark===================='
print 'g^((x+y)%(n-1)) % n=\t',E1
print '(g^x * g^y) % n=\t',E2
print 'g^(x+y) % n=\t\t',E3
print ''

if (E2==E3):
	print 'Alice has proven she knows the sum is ',add
else:
	print 'Alice has proven she does not know the sum is ',add