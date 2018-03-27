"""

[ filter_out.py ]

    This program is to filter out some lines which start with specific keywords.
  
"""

# Adjust keyword list as you want
keywords = [ 'ABC', 'Hello', 'Welcome' ]

f_name = input('Input file name to modify : ')
print('Target file : ' + f_name)

try:
    with open(f_name, 'r') as f:
        lines = f.readlines()

        res_f_name = 'res_' + f_name
        res_f = open(res_f_name, 'w')
        print('Result file : ' + res_f_name)

        for line in lines:
            skip = False

            if not line.isspace():
                for keyword in keywords:
                    if line.startswith(keyword):
                        skip = True
                        break

            if skip:
                continue
            res_f.write(line)

        res_f.close()
        print('Modification successful!')
            
except FileNotFoundError:
    print('Error :: Couldn\'t find file - ' + f_name + '...');
                


