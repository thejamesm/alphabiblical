import re
from textwrap import TextWrapper


def to_upper(match):
    return match.group(0).upper()


symbol_pattern = re.compile(r"[A-Za-z'-]+"      # Words
                            r"|[^A-Za-z'-]+"   # Everything else
                           )
nonword_pattern = re.compile(r"[^A-Za-z'-]")

in_file = open('bible.txt', 'r')
text = in_file.read()
in_file.close()

print('Symbols...')
symbol_list = symbol_pattern.findall(text)

print('Word indexes...')
word_index_list = [i for i, x in enumerate(symbol_list)
              if not(nonword_pattern.search(x))]

print('Words...')
word_list = [x for x in symbol_list if not(nonword_pattern.search(x))]

print('Sorting words...')
word_list = sorted(word_list)
word_list = sorted(word_list, key=lambda w: w.casefold())

print('Filling words...')
for new_i, orig_i in enumerate(word_index_list):
    symbol_list[orig_i] = word_list[new_i]

print('Joining...')
text = ''.join(symbol_list)

print('Wrapping...')
wrapper = TextWrapper()
lines = text.split('\n\n')
new_lines = []

for line in lines:
    new_lines.append('\n'.join(wrapper.wrap(line.strip())))

text = '\n\n'.join(new_lines)

print('Capitalizing titles...')
text = re.sub(r'_[^\n]+', to_upper, text)

print('Removing title indicators...')
text = text.replace('_', '')

print('Writing...')
out_file = open('alphabiblical_a.txt', 'w')
out_file.write(text)
out_file.close()
print('Done')
