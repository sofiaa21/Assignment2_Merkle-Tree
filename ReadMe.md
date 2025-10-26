## Merkle tree implementation

<p> The following code is an implementation of the Merkle Tree definition from Cryptography Homework 2 - exercise 2.1.3 </p>

### How to run the code:

**Dependencies:**  
- Python 3.8 or higher  
- No external packages required (only standard library: `hashlib`, `math`, `os`)

How to run the files with printable outputs:
```bash
python main.py
```

For running test run the same but change main.py -> test.py
```bash
python test.py
```
Note: if this is problematic try running it with its updated version of python -> python3
```bash
python3 main.py
```
### How to interpret the printouts:
For `main.py` the output should look like this:

```
Original message (m0): Once when I was six years old I saw a magnificent picture in a book, called True Stories from Nature, about the primeval forest. It was a picture of a boa constrictor in the act of swallowing an animal. Here is a copy of the drawing.
Message length: 233 bytes
Salt that will be used in the Merkle tree (HEX): [a randomly chosen 32 byte string to be used as salt]
------------------------------------------------
Final Merkle Root: [a 32 byte hash]
Hash length: 32 bytes
----------------------------------------------------------------
```
The output should include the original message, its hash and also the hexadecimal value of the salt that was used for hashing. Even if there is ahcnage in the original message, the resulting hash should be always **32 bytes**.

For `test.py` the output should look like this:
```
This is hashed value of message m with salt A: [hashed 32-byte string a] with length: 32
This is hashed value of message m with salt B: [a different 32-byte string b] with length: 32
```