fw = open('sample.txt', 'a', encoding='utf-8')
fw.write('writing some stuff in y text file\n')
fw.write('I like coding你好, How are you\n')
fw.close()

fr = open('sample.txt')
text = fr.read()
print(text)
fr.close()
