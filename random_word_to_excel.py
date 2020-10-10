import random
import re

import pandas as pd

phrases = "something something"
file_name = "test.csv"

randomized_phrases = []
for p in phrases:
    delimiters = re.split(", |/", p)
    combine = " ".join(delimiters)
    arr = combine.split()
    randomized_phrase = random.sample(arr, len(arr))
    randomized_phrases.append(" ".join(randomized_phrase))

df = pd.DataFrame(randomized_phrases)
df.to_csv(file_name, encoding="utf-8-sig")
