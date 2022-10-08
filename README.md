# Description

Calculates MD5 and SHA256 hashes for a given file

# Installation

`pip install hash_calc`

# Usage

**From command line:**

`python -m hash_calc [-h] --path PATH`


| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | - | Path of the file to be hashed |

**Programmatically:**

```python
from hash_calc.HashCalc import HashCalc

# 1.) Hash a file
pathToFile = "/path/to/file/test.txt

hashCalc = HashCalc(pathToFile)

print(hashCalc.md5)
print(hashCalc.sha256)

# 2.) Hash bytes
h = HashCalc.fromBytes(b"\x01\x02\x03")

print(h.sha256)
print(h.md5)

```

# Example

`python -m hash_calc -p test.txt`

Creates the follwing result:

```
##############################################################################################

Hash Calc by 5f0
Calculates MD5 and SHA256 hashes for a given file

Current working directory: /path/to/hash_calc
        Investigated file: test.txt

                 MD5 Hash: 265e08df10ed62d756e5e0bb6fadd69c
              SHA256 Hash: 1675aa3766017a42980e686132eff094ba789bc3dc44de3e53f2fb05a7a513ff

                 Datetime: 01/01/1970 10:20:30

##############################################################################################

Execution Time: 0.003022 sec
```

# License

MIT