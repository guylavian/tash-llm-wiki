---
title: "An error occurs when I configure the second ADFs client, and the first one can be connected"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/763044/an-error-occurs-when-i-configure-the-second-adfs-c
question_id: 763044
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# An error occurs when I configure the second ADFs client, and the first one can be connected

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/763044/an-error-occurs-when-i-configure-the-second-adfs-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Activity ID: f675174b-65a5-4fba-2300-00800b0000ff  

Relying party: DOTCOMLAB ADFS - Web API  

Error details: MSIS9224: Received invalid OAuth authorization request. The received 'redirect_uri' parameter is not a valid registered redirect URI for the client identifier: '195ba9f1-c0fc-4ed3-a943-4e2d0faf5bfe'. Received redirect_uri: 'https://dmzvc.dotcomlab.net/ui/login/oauth2/authcode'.  

Node name: 57366fec-6f5d-4c69-8d3f-6519f07acb40  

Error time: Tue, 08 Mar 2022 05:14:37 GMT  

Cookie: enabled  

User agent string: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-08*

The first client can only be referenced once?    identifier: '195ba9f1-c0fc-4ed3-a943-4e2d0faf5bfe
