text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

text = text.split()
final_txt = []

for txt in text:
    if txt.endswith((',', '.')):
        txt = txt[:-1] + 'ing' + txt[-1]
        final_txt.append(txt)
    else:
        txt = txt + 'ing'
        final_txt.append(txt)
print(' '.join(text))
print(' '.join(final_txt))
