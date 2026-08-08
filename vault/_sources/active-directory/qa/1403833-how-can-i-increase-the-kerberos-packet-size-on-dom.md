---
title: "How can I increase the kerberos packet size on Domain Controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1403833/how-can-i-increase-the-kerberos-packet-size-on-dom
question_id: 1403833
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# How can I increase the kerberos packet size on Domain Controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1403833/how-can-i-increase-the-kerberos-packet-size-on-dom (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have CIFS server where we have created shared folders. When users access it, some times it works fine and some times give error "Access Denied". I found below events in my DC. Please may I know what is the issue? How can I increase the kerberos packet size in Domain Controllers 2019??

A ticket to the service cifs/CIFS-Server01 is issued for account ******@xyz.com. The size of the encrypted part of this ticket is 14583 bytes, which is close or greater than the configured ticket size threshold (12000 bytes). This ticket or any additional tickets issued from this ticket might result in authentication failures if the client or server application allocates SSPI token buffers bounded by a value that is close to the threshold value.

The size of ticket is largely determined by the size of authorization data it carries. The size of authorization data is determined by the groups the account is member of, the claims data the account is setup for, and the resource groups resolved in the resource domain.

Events id 31

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-11-26*

Enabled SMB signing on storage side and all works well now.
