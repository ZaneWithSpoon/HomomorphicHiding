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
ans=24543


random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange

encrypted_x = publickey.encrypt(x, 32)
encrypted_y = publickey.encrypt(y, 32)

encrypted_ans = publickey.encrypt(ans, 32)
#message to encrypt is in the above line 'encrypt this message'


x_and_y = encrypted_x[0] * encrypted_y[0]
print x_and_y

decrypted_xy = key.decrypt(x_and_y)
print decrypted_xy

decrypted_ans = key.decrypt(encrypted_ans)
print decrypted_ans



n=47
g= 3

E1= g**( (x+y) % (n-1)) % n

E2= (g**x * g**y) % n

E3 = g**(ans) % n

print '======Agreed parameters============'
print 'P=',n,'\t(Prime number)'
print 'G=',g,'\t(Generator)'
print 'x=',x,'\t(Value 1 - Alice first value)'
print 'y=',y,'\t(value 2 - Alice second value)'
print 'ans=',ans,'\t(Answer = x+y?)'

print '======Encrypted values============'
print 'g^x=',(g**x) % n
print 'g^y=',(g**y) % n

print '======zkSnark===================='
print 'E1=',E1
print 'E2=',E2
print 'E3=',E3
if (E2==E3):
	print 'Alice has proven she knows the sum is ',ans
else:
	print 'Alice has proven she does not know the sum is ',ans