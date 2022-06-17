import pandas as pd

authors = pd.DataFrame({'author_id': [1, 2, 3],
                        'author_name': ['Тургенев', 'Чехов', 'Островский']},
                       columns=['author_id', 'author_name'])

book = pd.DataFrame({'author_id': [1, 1, 1, 2, 2, 3, 3],
                     'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                     'price': [450, 300, 350, 500, 450, 370, 290]},
                    columns=['author_id', 'book_title', 'price'])

authors_price = pd.merge(authors, book, on = 'author_id', how='outer')

authors_stat = authors_price[['author_name', 'price']].copy()

authors_stat = pd.merge(authors_stat, authors_stat.groupby('author_name').agg({'price':'max'}).rename(columns=dict(price='max_price')), on = 'author_name', how='inner')
authors_stat = pd.merge(authors_stat, authors_stat.groupby('author_name').agg({'price':'min'}).rename(columns=dict(price='min_price')), on = 'author_name', how='inner')
authors_stat = pd.merge(authors_stat, authors_stat.groupby('author_name').agg({'price':'mean'}).rename(columns=dict(price='mean_price')), on = 'author_name', how='inner')

print(authors_stat)
