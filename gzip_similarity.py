import gzip
from typing import Callable


def ncd(a: bytes, b: bytes, compressor: Callable[[bytes], bytes]) -> float:
    """ncd normalized compression distance

    Args:
        a: string 1
        b: string 2
        compressor: compress bytes into less bytes

    Returns:
        distance:s similarity from a to b from 0.0 to 1.0
    """
    a_compressed_size = len(compressor(a))
    b_compressed_size = len(compressor(b))
    ab_compressed_size = len(compressor(a + b" " + b))
    return (ab_compressed_size - min(a_compressed_size, b_compressed_size)) / max(
        a_compressed_size, b_compressed_size
    )


def gzip_similarity(a: str, b: str):
    return ncd(a.encode(), b.encode(), gzip.compress)
