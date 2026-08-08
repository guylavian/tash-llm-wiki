---
title: "domain controller DNS server no listening interfaces After instaling OpenVPN"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1380846/domain-controller-dns-server-no-listening-interfac
question_id: 1380846
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# domain controller DNS server no listening interfaces After instaling OpenVPN

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1380846/domain-controller-dns-server-no-listening-interfac (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

domain controller DNS server with no listening interfaces After installing OpenVPN ( For a Few Days Will Work Fine But In a Few Days The DNS Server Will Start  with no listening interfaces And There DNS server can't resolve the Google DNS Also So I have to disable the Apdater of OpenVPN Than it Works Fine

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-10-04*

Multi-homing a domain controller will always cause no end to grief for active directory DNS. Better to install the VPN on a dedicated member server.       

--please don't forget to close up the thread here by marking answer if the reply is helpful--
