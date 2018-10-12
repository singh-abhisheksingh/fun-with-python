import os, ghostscript, sys, locale

command = os.popen('unoconv -f pdf Test1.pptx')
command.close()

args = ["gs", "-q", "-o", "image%d.png", "-sDEVICE=pngalpha", "Test1.pdf"]
encoding = locale.getpreferredencoding()

args = [a.encode(encoding) for a in args]
ghostscript.Ghostscript(*args)