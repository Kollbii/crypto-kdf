# Key Derivation Function
Cryptography project [AGH UST]

### Content
1. Intro - Czym jest KDF
1. Prosty przykład w rozwiązaniu sieciowym - LM Hash
1. Od podstawy do czegoś skomplikowanego.
    1. UNIX-Crypt (krótko) --> MD5. Bez soli!
    1. Dobra funkcja KDF? Co powinna zapewniać (Memory-Hardness, Resistant to Cache Attacks, [...])
    1. Scrypt wchodzący w yescrypta! <--- yesscrypt jest zbudowany na scrypt info: https://www.openwall.com/yescrypt/
1. Ciekawostka Balloon Hashing. 

### Directory layout
    .
    ├── src
    │   └── main.py
    ├── tests                           # Tests, scoring system
    ├── .gitignore
    ├── kdf.ipynb
    ├── README.md
    └── requirements.txt

### Usage

```bash
    $> jupyter notebook
```
### Credits and used links for inspirations

1. https://qvault.io/cryptography/key-derivation-functions/
1. Link2

### Annotations

1. Annotations