filename = '/Users/manhhaucao/alice.txt'
try:
    with open(filename) as f_obj:
         contents = f_obj.read()
except FileNotFoundError:
     msg = "File " + filename + " không tồn tại."
     print(msg)
else:
     msg = "File " + filename + " tồn tại."
     print(msg)

