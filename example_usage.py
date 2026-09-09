from client import SmithWatermanAligner

def main():
    print("=== Smith-Waterman Local Sequence Aligner ===")
    aligner = SmithWatermanAligner(match_score=2, mismatch_penalty=-1, gap_penalty=-2)
    res = aligner.align("TGTTACGG", "GGTTGACTA")

    print("Local Alignment Result:", res)
    assert res["max_score"] > 0
    assert len(res["motif_seq1"]) > 0
    print("Smith-Waterman Aligner verified successfully!")

if __name__ == "__main__":
    main()
