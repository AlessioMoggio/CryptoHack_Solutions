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

To find the requested u and v it use a function that if one of the value is 0 the others is surely 1.
In other cases the function use the recursion of the extended gcd algorithm to find the result.

The demonstration is explained here:

    32321 = 1*26513 + 5808 => 5808 = 32321 + (-1)*26513

    26513 = 4*5808 + 3281 => 3281 = 26513 + (-4)*808

    5808 = 1*3281 + 2527 => 2527 = 5808 + (-1)*3281

    3281 = 1*2527 + 754 => 754 = 3281 + (-1)*2527

    2527 = 3*754 + 265 => 265 = 2527 + (-3)*754

    754 = 2*265 + 224 => 224 = 754 + (-2)*265

    265 = 1*224 + 41 => 41 = 265 + (-1)*224

    224 = 5*41 + 19 => 19 = 224 + (-5)*41

    41 = 2*19 + 3 => 3 = 41 + (-2)*19

    19 = 6*3 + 1 => 1 = 19 + (-6)*3

Substituting the values found in the previously equation:
    1 = 19 + (-6)*(41 + (-2)*19) =
        = (-6)*41 + (13)*19 = (-6)*41 + (13)*(224 + (-5)*41) =
        = (13)*224 + (-71)*41 = (13)*224 + (-71)*(265 + (-1)*224) =
        = (-71)*265 + 84*224 = (-71)*265 + (84)*(754 + (-2)*265) =
        = (84)*754 + (-239)*265 = (84)*754 + (-239)*(2527 + (-3)*754) =
        = (-239)*2527 + (801)*754 = (-239)*2527 + (801)*(3281 + (-1)*2527) =
        = (801)*3281 + (-1040)*2527 = (801)*3281 + (-1040)*(5808 + (-1)*3281) = 
        = (-1040)*5808 + (1841)*3281 = (-1040)*5808 + (1841)*(26513 + (-4)*5808) =
        = (1841)*26513 + (-8404)*5808 = (1841)*26513 + (-8404)*(32321 + (-1)*26513) =
        = (-8404)*32321 + (10245)*26513
