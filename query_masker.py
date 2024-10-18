import itertools
from typing import List, Set

class QueryMasker:
    """
    Generates masked patterns for a given query.
    """

    def __init__(self, mask_bits: int):
        self.mask_bits = mask_bits

    def generate(self, query: str) -> Set[str]:
        """
        Generate all masked patterns by masking `mask_bits` of the query.
        """
        masked_positions = list(range(len(query) - self.mask_bits, len(query)))
        masked_patterns = set()

        for bits in itertools.product('01', repeat=self.mask_bits):
            pattern = list(query)
            for pos, bit in zip(masked_positions, bits):
                pattern[pos] = bit
            masked_patterns.add(''.join(pattern))

        return masked_patterns
