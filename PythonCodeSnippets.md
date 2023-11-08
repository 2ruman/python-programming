
# Python Code Snippets

### Contents
+ [Basic](#basic)
+ [Parsing](#parsing)
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

## Parsing

### Get File Extension
   
```python
#!/bin/python3

import os.path

file_name = "my_img.jpg"

name_only = os.path.splitext(file_name)[0]
extension = os.path.splitext(file_name)[1]

print('name only :', name_only)
print('extension :', extension)
```
