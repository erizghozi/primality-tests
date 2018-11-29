
# coding: utf-8

# In[1]:

from random import randrange
import time


# In[2]:

def solovay_strassen(n, k):
    if n == 2 or n==3:
        return True
    if not n & 1: #kalau bukan bilangan ganjil hasilnya False
        return False

    def legendre(a, p):
        if p < 2:
            raise ValueError('p tidak boleh < 2')
        if (a == 0) or (a == 1):
            return a
        #proses penyederhanaan legendre , karena (ab/p)=(a/p)(b/p)
        #PERTAMA pakai teorema If p is an odd prime, then (2/p)= (- l ) ^( p^2 -l)/8.
        if a % 2 == 0:
            r = legendre(a // 2, p)
            if (p * p - 1) & 8 != 0: #(p^2-1) & 8 ==0 jika dan hanya jika (p^2-1) / 8 hasilnya genap 
                r *= -1
        else:
            #kedua pakai teorema law of quadratic reciprocity
            #Let p and q be distinct odd primes. Then
            #( p/q ) ( q/p )= ( - 1)^((p-1) /2)((q-1)/2)
            r = legendre(p % a, a)
            if (a - 1) * (p - 1) & 4 != 0:
                r *= -1
        return r

    for i in range(k):
        a = randrange(2, n - 1) #bilangan random antara 2 dan (n-1)
        x = legendre(a, n)
        y = pow(a, (n - 1) // 2, n) #a^((n-1)/2) mod n
        if (x == 0) or (y != x % n):
            return False
    return True


# In[4]:

n = int(input("Masukkan bilangan yang ingin diuji: "))
k = int(input("Masukkan jumlah pengulangan: "))
start_time = time.time()
print("Hasil Uji Solovay Strassen (True artinya bilangan prima atau prima semu):")
print(solovay_strassen(n,k))
print("--- %s detik ---" % (time.time() - start_time))


# In[ ]:




# In[ ]:



