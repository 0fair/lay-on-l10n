import csv
import json
import pandas as pd

KEY_DELETED = 'f_deleted'
TARGET_FIELDS = set([
    'id',
    'author_fullName',
    'title_orig'
])

def get_book_info(pos, line):
    # delete start and end brackets
    if pos == 0:
        line = line[1:]
    line = line[:-2] # delete comma/last bracket at the end
    data = json.loads(line)
    if data[KEY_DELETED]: # this rule doesn't work with the current dataset
        return None
    data_cleaned = {}
    for key, value in data.items():
        if key in TARGET_FIELDS:
            data_cleaned[key] = value
    return data_cleaned

json_lines = []
for pos, line in enumerate(open('../datasets_raw/books_full.jsn')):
    book_info = get_book_info(pos, line)
    if book_info:
        json_lines.append(book_info)
    if pos % 100000 == 0:
        print(f'Processed {pos} lines')

books = pd.DataFrame(json_lines)

del json_lines

for c in books.columns:
    column_type = books[c].dtype
    if column_type in (int, float):
        books[c].fillna(0, inplace=True)
    if column_type == object:
        books[c].fillna("", inplace=True)
    print(f'Processed: {c}')

id_matchings = pd.read_csv('../datasets_raw/books_collapsed.csv')
books = pd.merge(books, id_matchings, how='left', left_on='id', right_on='id')

books.rename(
    columns={'author_fullName': 'author_fullname', 'title_orig': 'title_original', 'main_id': 'collapse_parent_id',
             'parentId': 'parent_id', 'publicationType': 'publication_type', 'NORM_part': 'norm_part'}, inplace=True)

books.to_csv("../datasets_prepared/books_prepared.csv", index = False, quoting=csv.QUOTE_NONNUMERIC)