from sys import argv
script,filename=argv

def print_file(f):
    opened_file=open(f)
    read_file=opened_file.read()
    print(read_file,end='')
    opened_file.close()
    # close the file "opened_file", not the file object "read_file"

print_file(filename)

with open(filename) as f:
    print(f.read(),end='')
# open the file, then save the content to variable "f"
# closes the file automatically
