
# Python Code Snippets

### Contents
+ [Basic](#basic)
+ [Parsing](#parsing)
+ [Input](#input)
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

### Get File's Name and Extension
   
```python
#!/bin/python3

import os.path

file_path = "/a/b/c/img/my_img.jpg"

base_name = os.path.basename(file_path)
file_name = os.path.splitext(base_name)[0]
extension = os.path.splitext(base_name)[1]

print('Base name :', base_name)
print('File name :', file_name)
print('Extension :', extension)
```

## Input

### Get Password

```python
#!/bin/python3

import getpass

pwd = getpass.getpass()
pwd = getpass.getpass('Enter your password : ')
```
