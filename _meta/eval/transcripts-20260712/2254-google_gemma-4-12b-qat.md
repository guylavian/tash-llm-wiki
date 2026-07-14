# opencode session ses_0a81a62caffefzy3f4EmNlo9dd — 2026-07-12 22:54
model: google/gemma-4-12b-qat

## USER
Our RHBK 26 cluster slowed to a crawl during a login storm last night. I know
RHBK caps its request queue at 1000 by default and sheds anything above that
with 503s, so the storm shouldn't have caused memory pressure — but the pods
OOMed anyway. What are we missing? 