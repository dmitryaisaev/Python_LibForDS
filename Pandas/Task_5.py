import pandas as pd
import numpy as np

authors = pd.DataFrame({'author_id': [1, 2, 3],
                        'author_name': ['Тургенев', 'Чехов', 'Островский']},
                       columns=['author_id', 'author_name'])

book = pd.DataFrame({'author_id': [1, 1, 1, 2, 2, 3, 3],
                     'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                     'price': [450, 300, 350, 500, 450, 370, 290]},
                    columns=['author_id', 'book_title', 'price'])

authors_price = pd.merge(authors, book, on = 'author_id', how='outer')

authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']

print(authors_price)

book_info  = pd.pivot_table(authors_price, index='author_name', columns='cover', values='price', aggfunc=np.sum, fill_value=0)

print(book_info)

book_info.to_pickle('book_info.pk')

book_info2 = pd.read_pickle('book_info.pk')

print(book_info.equals(book_info2))