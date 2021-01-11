a, b = 10, 20

# if (a < b):
#     min = a
# else:
#     min = b

min = a if (a < b) else b

print(min)


name = ''
default_name = name if (name != '') else 'Guest'
print(default_name)
