import gzip


def compressed_length(a: str):
    return len(gzip.compress(a.encode()))


def gzip_similarity(a: str, b: str):
    a_len = compressed_length(a)
    b_len = compressed_length(b)
    ab_len = compressed_length(a + " " + b)
    normalized = (ab_len - min(a_len, b_len)) / max(a_len, b_len)
    return normalized
