import pandas as pd
from collections import Counter

# load tmp.csv DataFrame
pd.set_option('display.max_columns', None)
df = pd.read_csv('tmp.csv', sep='\t')

print(df)
'''
# function to count duplicated words in a string
def count_duplicated_words(text):
    words = text.split()
    counter = Counter(words)
    return [(word, count) for word, count in counter.items() if count > 1]

# apply the function to the DataFrame column
df['duplicated_words'] = df['productName'].apply(count_duplicated_words)
print(df)
'''
