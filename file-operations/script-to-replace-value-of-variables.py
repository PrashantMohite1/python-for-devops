file_name = 'server.conf'
key = 'MAX_CONNECTION'
value = '50'


file = open(file_name, 'r')

all_lines = file.readlines()

# print()

def update_conf(file_name , key, value):
    with open (file_name,'w') as file:
        for line in all_lines:
            if key in line:
                print('before editing '+line)
                file.write(key + '='+ value + "\n")
            else:
                file.write(line)


def grep_string(file_name, key):
        with open (file_name,'r') as file:
            edited_line = file.readlines()

        for i in edited_line:
            if key in i:
                print('after editing '+i)





update_conf(file_name, key , value)

grep_string(file_name , key)