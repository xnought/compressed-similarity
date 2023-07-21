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
