class SmithWatermanAligner:
    """Smith-Waterman optimal local sequence alignment."""
    def __init__(self, match_score: int = 2, mismatch_penalty: int = -1, gap_penalty: int = -2):
        self.match = match_score
        self.mismatch = mismatch_penalty
        self.gap = gap_penalty

    def align(self, seq1: str, seq2: str) -> dict:
        n, m = len(seq1), len(seq2)
        score = [[0] * (m + 1) for _ in range(n + 1)]
        max_score = 0
        best_pos = (0, 0)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                diag = score[i - 1][j - 1] + (self.match if seq1[i - 1] == seq2[j - 1] else self.mismatch)
                up = score[i - 1][j] + self.gap
                left = score[i][j - 1] + self.gap
                val = max(0, diag, up, left)
                score[i][j] = val
                if val > max_score:
                    max_score = val
                    best_pos = (i, j)

        # Backtrack from best_pos until 0 is hit
        aligned1, aligned2 = [], []
        i, j = best_pos
        while i > 0 and j > 0 and score[i][j] > 0:
            current = score[i][j]
            diag = score[i - 1][j - 1]
            up = score[i - 1][j]
            left = score[i][j - 1]

            if current == diag + (self.match if seq1[i - 1] == seq2[j - 1] else self.mismatch):
                aligned1.append(seq1[i - 1])
                aligned2.append(seq2[j - 1])
                i -= 1
                j -= 1
            elif current == up + self.gap:
                aligned1.append(seq1[i - 1])
                aligned2.append("-")
                i -= 1
            else:
                aligned1.append("-")
                aligned2.append(seq2[j - 1])
                j -= 1

        return {
            "max_score": max_score,
            "motif_seq1": "".join(reversed(aligned1)),
            "motif_seq2": "".join(reversed(aligned2)),
            "end_position": best_pos
        }
