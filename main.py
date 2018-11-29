""" Made by Eriz Ghozi Al Hakim.
Start: 2 November 2018. End: 14 November 2018.

Program utama untuk melakukan pengetesan bilangan prima menggunakan
metode Solovay-Strassen dan Miller-Rabin. Program akan menerima
masukan berupa angka pada variabel longnum, yang kemudian akan
diuji primalitasnya menggunakan salah satu dari kedua metode yang
diberikan.
"""

from math import gcd
from timeit import default_timer
from random import randrange

EXP_1 = '85053461164796801949539541639542805770666392330682' \
        '67330253081977410514153169870714693030729025353732' \
        '0447270457'
EXP_2 = '20473277403346818321158412934142799491415263365281' \
        '74665805818548988357907512532570321012353452511041' \
        '140892019729857298913933131'
EXP_3 = '20395687835640197740576586692903457728019399331434' \
        '82630947726464532830627227012776329366160631440881' \
        '73312372882677123879538709400158306567338328279154' \
        '49969836607190676644003707421711780569087279284814' \
        '91120222863321448761833763265120835748216479339929' \
        '61249917319836219304274280243803104015000563790127' # Digit terakhir aslinya 3
SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


def main():
    """Program utama dari rangkaian program ini.
    Berfungsi untuk menerima masukan bilangan yang akan diuji
    dan menentukan pilihan mode uji primalitas.
    """
    print("---Program uji primalitas bilangan besar---")

    num_list = {'A': EXP_1, 'B': EXP_2, 'C': EXP_3}
    print("Mau menerima masukan dari mana?"
          "\nA. Contoh 1 (prima)"
          "\nB. Contoh 2 (komposit)"
          "\nC. Contoh 3 (belum diuji)"
          "\nX. Masukkan sendiri.")
    num_cho = input("Pilihan :").upper()
    if num_cho in num_list:
        longnum = int(num_list[num_cho])
        print("Masukan =", longnum)
    else:
        longnum = int(input("Masukkan bilangan yang akan dicek: "))
    print("Banyak digit masukan:", len(str(longnum)))

    iter_max = int(input("Masukkan banyak iterasi program: "))

    print("\nPilihan program yang dapat digunakan: "
          "\nA. Algoritma Solovay-Strassen"
          "\nB. Algoritma Rabin-Miller")

    while True:
        prog_cho = input("\nMasukkan pilihan program (A/B): ")
        if prog_cho.upper() == 'A':
            start_time = default_timer()
            isprime = test_solovay_strassen(longnum, iter_max)
            break
        elif prog_cho.upper() == 'B':
            start_time = default_timer()
            isprime = test_rabin_miller(longnum, iter_max)
            break
        else:
            print("Masukan tidak dimengerti.")

    if isprime:
        print("Masukan prima.")
    elif not isprime:
        print("Masukan komposit.")
    end_time = default_timer()
    print("Waktu eksekusi:", end_time - start_time)


def test_solovay_strassen(n, iter_num):
    """Uji Solovay-Strassen untuk menentukan apakah masukan n
    prima atau bukan. Merupakan metode Monte Carlo dengan peluang
    kesalahan sekitar 1/2.

    :param n: Bilangan yang akan diuji primalitasnya.
    :type n: int
    :param iter_num: Banyak iterasi maksimum untuk pengujian.
    :type iter_num: int
    :return: Pernyataan apakah n prima.
    :rtype: bool
    """
    print("Tes Solovay-Strassen dimulai.")
    if n < 2:
        print("Bilangan terlalu kecil")
        return False
    for p in SMALL_PRIMES:
        if n < p * p:
            print("Bilangan terlalu kecil.")
            return True
        if n % p == 0:
            print("Faktornya adalah", p)
            return False

    for _ in range(iter_num):
        a = randrange(2, n - 1)
        x = legendre(a, n)
        y = pow(a, (n - 1) // 2, n)
        if (x == 0) or (y != x % n):
            return False
    return True


def legendre(a, p):
    """Fungsi pendukung untuk uji Solovay-Strassen

    :param a: Masukan bagian atas pada fungsi Legendre.
    :type a: int
    :param p: Masukan bagian bawah pada fungsi Legendre
    :type p: int
    :return: Hasil fungsi Legendre (0, 1, atau -1)
    :rtype: int
    """
    if p < 2:
        raise ValueError('p harus minimal 2')
    if (a == 0) or (a == 1):
        return a
    if a % 2 == 0:
        r = legendre(a // 2, p)
        if p * p - 1 & 8 != 0:
            r *= -1
    else:
        r = legendre(p % a, a)
        if (a - 1) * (p - 1) & 4 != 0:
            r *= -1
    return r


def test_rabin_miller(n, iter_num):
    """Tes Rabin-Miller untuk menguji apakah bilangan n merupakan
    bilangan prima atau bukan. Merupakan Metode Monte Carlo dengan
    peluang kesalahan 1/4.

    :param n: Bilangan yang akan diuji primalitasnya.
    :type n: int
    :param iter_num: Banyak iterasi maksimum untuk pengujian.
    :type iter_num: int
    :return: Pernyataan apakah n prima.
    :rtype: bool
    """
    print("Tes Rabin-Miller dimulai.")
    if n < 2:
        print("Bilangan terlalu kecil")
        return False
    for p in SMALL_PRIMES:
        if n < p * p:
            print("Bilangan terlalu kecil.")
            return True
        if n % p == 0:
            print("Faktornya adalah", p)
            return False

    exponent_2, factor_odd = 0, n - 1
    while factor_odd % 2 == 0:
        exponent_2 += 1
        factor_odd //= 2

    for _ in range(iter_num):
        a = randrange(2, n - 1)
        x = pow(a, factor_odd, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(exponent_2 - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


if __name__ == '__main__':
    main()
