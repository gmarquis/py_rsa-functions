import sys
sys.set_int_max_str_digits(640)
from sympy import mod_inverse
p = 797 ; q = 977 ; n = p * q
phi_n = (p - 1) * (q - 1)
e = 65537 ; d = mod_inverse(e, phi_n)
print('private',p,q, 'public', e,n, 'decrypt',n,d)

# Encrypt,  # public-key e,n
m = 66      # 'message-plain-text' letter B', print(66 == (ord('B')))
print(f'plain_text: {m}')
_ = pow(m,e) ; c = _ % n ; print(f'cipher_text: {c}')

# Decrypt,  # private-exp d,n   #   d mod of (p,q)
m = pow(c,d) % n ; print(f'decrypted : {m}')

