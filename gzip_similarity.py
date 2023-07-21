import gzip


def compressed_size(message: str, compressor=gzip):
    return len(compressor.compress(message.encode()))


def normalized_compression_distance(
    a_compressed_size: int, b_compressed_size: int, ab_compressed_size: int
):
    return (ab_compressed_size - min(a_compressed_size, b_compressed_size)) / max(
        a_compressed_size, b_compressed_size
    )


def gzip_similarity(a: str, b: str):
    a_size = compressed_size(a)
    b_size = compressed_size(b)
    ab_size = compressed_size(a + " " + b)
    return normalized_compression_distance(a_size, b_size, ab_size)
