text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel."
        " Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
text_s = text.split()
fin_text = []
for element in text_s:
    if ',' in element:
        element = element.replace(',', 'ing,')
    elif '.' in element:
        element = element.replace('.', 'ing.')
    else:
        element = element + 'ing'
    fin_text.append(element)
print(' '.join(fin_text))
