age = int(input('What is your Age? '))

if (age >= 18):
    nationality = input('Do you have NID? (Y/N) ')
    if (nationality == 'y'):
        pass
    else:
        print('You are not eligible...')
else:
    print('You are Too Young...')
