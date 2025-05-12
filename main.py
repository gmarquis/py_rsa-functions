import sys ; sys.set_int_max_str_digits(640)
from sympy import mod_inverse
p = 797; q = 977 ; n = p * q
phi_n = (p - 1) * (q - 1)
e = 65537 ; d = mod_inverse(e, phi_n)
print('private',p,q, 'public', e,n, 'decrypt',n,d)

# Encrypt,  # public-key e,n
m = 66      # 'plain-text' message letter B', print(66 == (ord('B')))
print(f'plain_text: {m}')
_ = pow(m,e) ; c = _ % n ; print(f'cipher_text: {c}')
with open('cipher.txt', 'w') as f:
    f.writelines(str(c))

# Decrypt,  # private-exp d,n   #   d mod of n of p.q
m = 0 ; c = 0 ; _ = 0
with open('cipher.txt', 'r') as f:
    c = f.readlines()
    c = int(c[0])
    m = pow(c, d) % n;
    print(f'decrypted : {m}')
with open('cipher.txt', 'w') as f:
    f.writelines(str(m))

exit()

def rsa():
    from Crypto.PublicKey import RSA  # provided by pycryptodome
    key = RSA.generate(3096)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    print('private key:', private_key.decode())
    print('public key:', public_key.decode())
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def generate_keypair(p, q):
    import random
    n = p * q
    phi = (p - 1) * (q - 1)             # Phi is the totient of n
    e = random.randrange(1, phi)        # Choose an integer e such that e and phi(n) are coprime
    g = gcd(e, phi)                     # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = mul_inv(e, phi)  # Use Extended Euclid's Algorithm to generate the private key

    if e %2 != 0 and e < 3:
        return generate_keypair(p, q)

    return e, n ;''', (d, n)'''
def mul_inv(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi / e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    if temp_phi == 1:
        return d + phi
print(generate_keypair(2,7))    # 08bit prime: 163, 223

