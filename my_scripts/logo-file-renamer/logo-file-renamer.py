import os

base = os.getcwd()

finword = ['-logo', '_logo', 'logo']
repword = 'logo-'

for file in os.listdir(base):
    filname = str(file)
    for fword in finword:
        if fword in filname:
            newname = filname.replace(fword, '')
            newname = newname.replace('-.', '.')
            newname = newname.replace('_.', '.')
            newname = newname.strip('-')
            newname = repword + newname
    try:
        os.rename(file, f"{base}/{newname}")
        print(f"{file} renamed to: {newname}.")
    except Exception as e:
        print(e)
