from operator import methodcaller

a = 1
bytes_formatter = methodcaller('to_bytes')

print(bytes_formatter(a))
