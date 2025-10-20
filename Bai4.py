def count_words(filename):
    try:
        with open(filename) as f_obj:
             contents = f_obj.read()
    except FileNotFoundError:
        msg = "File " + filename + " không tồn tại."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("File " + filename + " có " + str(num_words) + " từ.")
filenames = ['/Users/manhhaucao/alice.txt', '/Users/manhhaucao/alice1.txt', '/Users/manhhaucao/alice2.txt']
for filename in filenames:
     count_words(filename)

