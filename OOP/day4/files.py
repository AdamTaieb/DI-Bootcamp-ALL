# file_text = ''
# file_text_lines = []

# def read_file(file, input_str):
#     file_txt = ""
#     with open('./sample.txt', mode='r') as f:
#          print(f.tell())
#          file_text += f.read()
#          f.seek(0)
#          file_text_lines = f.readlines()


# def write_to_fime(input_str):
#     with open('./sample.txt', mode='r') as f:
#          print(f.tell())
#          file_text += f.read()
#          f.seek(0)
#          file_text_lines = f.readlines()

# print(file_text_lines)

# with open('./sample.txt', mode='w') as f:
#     f.write(file_text + '\n')
#     f.writelines(sentence2)
# text = ''
# text_lines = []
# with open('star_wars.txt', 'r') as f:
#     text += f.read()
#     f.seek(0)
#     text_lines = f.readlines()
#1
# for line in enumerate(text_lines):
#     print(line)

#2
#print(text_string[:5])

#3
# print(text_lines[4])

# #5
# stript_new_line = lambda s: s.strip('\n')
# text_lines = list(map(stript_new_line, text_lines))
# names_unique = list(set(text_lines))

# count_names = {name: 0 for name in names_unique}
# print(count_names)

# for name in text_lines:
#     count_names[name] += 1
# print(count_names)

# #5.2

# from collections import Counter
# count_names = Counter(text_lines)
# print(type(count_names))