---
title: "Best Practices Domain Controller use self DNS Registration or use static host entry?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2186573/best-practices-domain-controller-use-self-dns-regi
question_id: 2186573
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-networking-network-connectivity-file-sharing"]
---
# Best Practices Domain Controller use self DNS Registration or use static host entry?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2186573/best-practices-domain-controller-use-self-dns-regi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

On a Domain Controller, there are two thoughts on DNS entry in the domain forward lookup group. One line of thought is to create a static host (A) entry for the Domain Controller(s) in the domain Forward lookup. This is in addition to the default entries that automatically create for NS etc. The other line of thought is to check mark "Register this connection's address in DNS" in the DNS Tab in advanced settings for TCP/IP in adapter settings and let the controller maintain its own entry.  I have configuring DNS both ways over time, and in each instance got different BPA (Best Practices) or other errors as a result. I'd like some thoughts on how other admins think about this. It is on a local private domain where the computers do not need to be reached from the outside Internet. Thanks in advance.

## Answer (community) — community member

*upvotes: 1 · updated: 2023-11-02*

Thank you. I believe you indicated that on a domain where controllers and member servers don't ever change IP addresses, using static host entries in DNS is acceptable, which would also imply it is therefore safe to ignore the DNS BPA entry that the host DC isn't set up to register itself each time it boots.

## Answer (community) — community member

*upvotes: 1 · updated: 2023-11-02*

Hello!

While dynamic DNS registration can be convenient for end-user devices with dynamic IP addresses, for infrastructure components like DC which IP addresses are static and unlikely to change, static DNS entries may be appropriate. Static entries help maintain network reliability. Stability is crucial. We won't have to deal with unexpected changes in IP addresses.

Thanks,

Karlie
