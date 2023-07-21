# Compression Distance

Some tests and common code for distance via compression (thank you Kolmogorov again, I should say this more often)

```python
from compression_distance import normalized_compression_distance as ncd

strings = [
    "I love rap battles",
    "I win rap battles, I'm supa hot",
    "Wrap this up!",
    "John Keats the poet could beat soulja boy",
]

my_string = "rapping is my passion, what can I say, I'm a poet"

similarities = [ncd(my_string.encode(), other.encode()) for other in strings]

print(my_string)
print(list(sorted(zip(similarities, strings), key=lambda x: x[0])))
```

outputs sorted by most similar to my sentence (rapping is my passion, what can I say, I'm a poet) first

```python
[(0.5217391304347826, "I win rap battles, I'm supa hot"),
(0.5217391304347826, 'John Keats the poet could beat soulja boy'),
(0.6376811594202898, 'I love rap battles'),
(0.6811594202898551, 'Wrap this up!')]
```

or go to [`example.ipynb`](example.ipynb) for a real example on 10,000 pieces of text.

## Speed

From tests (in [`performance.ipynb`](performance.ipynb)), could conclude with no confidence that probably for small enough strings takes 50 microseconds per `ncd` call.

Should do more tests before making any decisions though.

## Different Compression

I use [gzip](https://docs.python.org/3/library/gzip.html) by default from the default python library.

If you'd like to switch, all you need to do is pass in a `compressor` in `ncd`.

For example if you wanted to use [bz2](https://docs.python.org/3/library/bz2.html)

```python
import bz2

similarity = ncd("dogs".encode(), "cats".encode(), compressor=bz2.compress)
```

You just need to provide a function (`compressor`) that takes bytes and returns bytes.
