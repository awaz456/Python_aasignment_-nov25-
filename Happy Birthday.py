def happy(name, style_char='-'):
    nam = 'Happy Birthday to you\n'
    last = 'Dear'
    print(style_char*25)
    print("{0}{0}{0}{1} {2} {0}".format(nam, last, name))
    print(style_char*25)


happy("Sagar Dai \n")
