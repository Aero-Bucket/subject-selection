switch={
    "a":'print("hello")',
    "b":'print("hey")',
    "c":'print("hi")'
}
              
try:
    exec(switch.get(input("> ")))
except:
    print("Value Not Found")