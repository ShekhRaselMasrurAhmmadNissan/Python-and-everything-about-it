# name = 'Shekh Rasel Masrur Ahmmad'
name = ''

# if (name == ''):
#     default_name = 'Guest'
# else:
#     default_name = name

default_name = name or 'Guest'
print(default_name)

name and print(default_name.upper())
