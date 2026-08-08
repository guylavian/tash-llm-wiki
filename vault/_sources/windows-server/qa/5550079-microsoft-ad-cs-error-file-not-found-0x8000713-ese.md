---
title: "Microsoft AD CS error file not found 0x8000713 (ESE:-1811 JET_errFileNotFound)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5550079/microsoft-ad-cs-error-file-not-found-0x8000713-ese
question_id: 5550079
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-directory-services-certificates-pki"]
answer_author_roles: ["Independent Advisor"]
---
# Microsoft AD CS error file not found 0x8000713 (ESE:-1811 JET_errFileNotFound)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5550079/microsoft-ad-cs-error-file-not-found-0x8000713-ese (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we have a 2016 windows server on a HP G9 server. the Microsoft AD CS service is activated on the server and is integrated with a luna G5 HSM. recently we back up the complete OS and restore is on another HP G9 server. the restoration has done sucessfully and it seems that the second server is exactly the same as first one. every thing is restored including any issued certificates, registery info and so on. but when we attach the HSM to the second server and try to start Microsoft AD CS on the second server, there is an error says: "file not found 0x8000713 (ESE:-1811 JET_errFileNotFound)". what is the reason and how we could fix it?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-09-10*

Dear mahsa_rkh,

 Based on your description, the error 0x8000713 (ESE:-1811 JET_errFileNotFound) typically indicates that the AD CS service cannot locate its database files, which are essential for startup. While the OS restoration appears successful, this error suggests that the AD CS database path or associated files may not have been correctly restored or are inaccessible on the second server.

Please verify that the AD CS database files (usually `.edb`) exist in the expected location and that the file permissions are intact. Additionally, ensure that the Luna G5 HSM is properly initialized and recognized by the second server, as AD CS relies on the HSM for cryptographic operations. A mismatch in HSM configuration or missing key containers can also prevent the service from starting.

We recommend checking the AD CS configuration using `certutil -getreg` to confirm the database path and reviewing the Event Viewer logs for more specific details. If needed, restoring the AD CS database from a known good backup or reconfiguring the HSM integration may resolve the issue.

I hope this helps. Just kindly tick Accept Answer that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated. 

Best regards, 

Domic Vo
