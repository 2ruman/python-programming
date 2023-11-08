
# Python Code Snippets

### Contents
+ [Basic](#basic)
<br>

## Basic

### Get Argc, Argv and Command
   
```python
#!/bin/python3

import sys

if __name__ == '__main__':
    argc = len(sys.argv)
    argv = sys.argv 
    print('Argc :', argc)
    print('Argv :', argv)
    print('Comm :', argv[0])
```
