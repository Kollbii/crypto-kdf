# Key Derivation Function
Cryptography project [AGH UST]
Contains notebook about key derivation functions and simple implementation of KDF.

### Content
1. Wstęp teoretyczny. Czym jest KDF?
1. Od podstaw do czegoś skomplikowanego.
    1. `SHA` oraz `salt`. Funkcje haszujące.
    1. Prosty przykład w rozwiązaniu sieciowym - `LM Hash`. <!-- Do przemyślenia czy wstawiamy gdzieś na początku czy nie 
    1. Dobra funkcja KDF? Co powinna zapewniać (Memory-Hardness).
    1. `Scrypt` omówienie.
    1. Atak kanałem bocznym w `scrypt` (Side Channel Attack) oraz Resistance to Cache Attacks. https://crypto.stanford.edu/cs359c/17sp/projects/MarkAnderson.pdf
    1. `Yescrypt` bazujący na `scrypt`. <!-- yesscrypt jest zbudowany na scrypt info: https://www.openwall.com/yescrypt/ -->
1. Ciekawostka `Balloon Hashing`.

### Directory layout
    .
    ├── src
    │   ├── lbk_cll_kdf
    │   │   └── . . .
    │   └── main.py
    ├── tests                           # Tests, scoring system
    │   ├── test_implementation.py
    │   └── README.md
    ├── .gitignore
    ├── kdf.ipynb
    ├── README.md
    └── requirements.txt

### Usage

```bash
    $> cd /directory/with/this/program
    $> jupyter notebook
```

### Credits and used links for inspirations

1. Funkcje wyprowadzania klucza (KDF) wykorzystujące odwzorowanie logistyczne - Grzegorz Frejek
1. https://qvault.io/cryptography/key-derivation-functions/
1. https://cryptobook.nakov.com/mac-and-key-derivation/hmac-and-key-derivation
1. https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/
1. https://en.wikipedia.org/wiki/Block_cipher
1. https://en.wikipedia.org/wiki/Key_stretching
1. https://docs.python.org/3/library/hmac.html
1. https://en.wikipedia.org/wiki/Avalanche_effect
1. https://crypto.stanford.edu/cs359c/17sp/projects/MarkAnderson.pdf
1. https://www.openwall.com/yescrypt/
1. https://www.tarsnap.com/scrypt.html
1. https://datatracker.ietf.org/doc/html/rfc7914
1. https://qvault.io/cryptography/very-basic-intro-to-the-scrypt-hash/
1. https://courses.csail.mit.edu/6.857/2016/files/salsa20.py
1. https://github.com/Daeinar/salsa20

### Annotations

1. Annotations