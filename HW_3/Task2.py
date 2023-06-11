'''В большой текстовой строке подсчитать количество встречаемых слов и 
вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. 
За основу возьмите любую статью из википедии или из документации к языку.'''

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod\
    tempor incididunt ut labore et dolore magna aliqua. Lorem dolor sed viverra\
    ipsum nunc aliquet bibendum enim. Eget arcu dictum varius duis at consectetur.\
    Mauris ultrices eros in cursus turpis massa. Viverra maecenas accumsan lacus\
    vel facilisis volutpat est. In fermentum et sollicitudin ac orci phasellus\
    egestas tellus rutrum. Malesuada fames ac turpis egestas sed. Vitae sapien\
    pellentesque habitant morbi tristique senectus et netus. Mi quis hendrerit dolor\
    magna. Lorem mollis aliquam ut porttitor leo a. A iaculis at erat pellentesque\
    adipiscing. Et netus et malesuada fames ac turpis. Nunc sed blandit libero volutpat\
    sed. Tortor posuere ac ut consequat semper viverra nam libero justo.'

TOP = 10
edited_text = text.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '')
words_count = {}
sort_dict_words = {}
words_list = edited_text.split()
for word in words_list:
    counter = words_list.count(word)
    words_count[word] = counter
sorted_values = sorted(words_count.values())[::-1]
for i in sorted_values:
        for k in words_count.keys():
            if words_count[k] == i:
                sort_dict_words[k] = words_count[k]

print(text, list(sort_dict_words.items())[0: TOP],\
    f'Количество слов в тексте = {len(edited_text.split())}', sep='\n')