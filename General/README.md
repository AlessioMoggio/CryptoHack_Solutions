# General

## Encoding

### ASCII

Using the function `chr()` the integers in the list can be converted to ASCII characters.

### Hex

Using the function `bytes.fromhex()` the string can be converted from hex to bytes.

### Base64

Importing the library base64 the string can be enconded in base64 with the functions `base64.b64encode()` after the conversion from hex to bytes.

### Bytes and Big Integers

Importing the library Crypto the long value can be converted using the function `long_to_bytes()`.

## XOR

### XOR Starter

Importing the library pwntools the function `xor()` can XOR the string 'label' and the number 13 to get the flag.

### XOR Properties

Using the XOR properties:
>>>
    Commutative: A ⊕ B = B ⊕ A
    Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
    Identity: A ⊕ 0 = A
    Self-Inverse: A ⊕ A = 0
>>>
I can get the flag computing XOR among the variables `FLAG ^ KEY1 ^ KEY3 ^ KEY2`, `KEY2 ^ KEY1` and `KEY1` after the conversion in bytes.

### Favourite byte

Doing a loop we can look for the right combination computing XOR between the string and each byte value.

### You either know, XOR you don't

Knowing the flag format we can compute XOR between the raw flag and the known part of the flag encoded.

## Mathematics

### Greatest Common Divisor

The python library Math has the function `gcd()` to compute it.

### Extended GCD

