import gzip
from typing import Callable


space_byte = " ".encode()


def space_separated_concat(a: bytes, b: bytes):
    return a + space_byte + b


def normalized_compression_distance(
    a: bytes,
    b: bytes,
    compressor: Callable[[bytes], bytes],
    concat_bytes: Callable[[bytes, bytes], bytes] = space_separated_concat,
) -> float:
    """normalized compression distance

    Args:
        a: string 1
        b: string 2
        compressor: compress bytes into less bytes

    Returns:
        distance: similarity from a to b from 0.0 to 1.0
    """
    a_compressed_size = len(compressor(a))
    b_compressed_size = len(compressor(b))
    ab_compressed_size = len(compressor(concat_bytes(a, b)))
    return (ab_compressed_size - min(a_compressed_size, b_compressed_size)) / max(
        a_compressed_size, b_compressed_size
    )


def gzip_similarity(a: str, b: str):
    return normalized_compression_distance(a.encode(), b.encode(), gzip.compress)
