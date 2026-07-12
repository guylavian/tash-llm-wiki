Bank v4 grading note:

Class A fails deterministically when the answer contains a denial-of-existence / denial-of-documentation phrase from `denial_tokens` and the expected slug's supporting fact is actually present in corpus; the check is report-only here and should not be treated as a pass just because the answer cites a source.

Class B is pending `answer_source`: if the answer is labeled as filed/cached/previously answered (or mentions `questions/`), it satisfies the cache-hit label check; otherwise, the grader should only consider it after `answer_source` lands, because the unlabeled cache-hit case must stay UNGRADED until the provenance tag exists.
