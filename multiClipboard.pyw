#!
import shelve, pyperclip, sys
from types import SimpleNamespace

mcbShelf = shelve.open('mcb')

#Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf.keys():
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()

