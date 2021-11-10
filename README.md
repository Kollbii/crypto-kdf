# Key Derivation Function
Cryptography project [AGH UST]

### Content
1. Wstęp teoretyczny. Czym jest KDF?
1. Od podstawy do czegoś skomplikowanego.
    1. UNIX-Crypt (krótko) --> MD5. Bez soli!
    1. Dobra funkcja KDF? Co powinna zapewniać (Memory-Hardness, Resistant to Cache Attacks, [...])
    1. Prosty przykład w rozwiązaniu sieciowym - LM Hash
    1. Scrypt wchodzący w yescrypta! <--- yesscrypt jest zbudowany na scrypt info: https://www.openwall.com/yescrypt/
1. Ciekawostka Balloon Hashing. 

### Directory layout
    .
    ├── src
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

1. https://qvault.io/cryptography/key-derivation-functions/
1. https://cryptobook.nakov.com/mac-and-key-derivation/hmac-and-key-derivation
1. https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/
1. https://en.wikipedia.org/wiki/Block_cipher
1. https://en.wikipedia.org/wiki/Key_stretching
1.

### Annotations

1. Annotations