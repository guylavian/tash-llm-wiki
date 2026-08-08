---
title: "Exchange - protection against backscatter attacks"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1435937/exchange-protection-against-backscatter-attacks
question_id: 1435937
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Exchange - protection against backscatter attacks

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1435937/exchange-protection-against-backscatter-attacks (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The organization has an Exchange server and an external anti-spam server that filters mail

After filtering the mail, the external server sends the mail to the internal Exchange server.

The organization has distribution groups where sender authentication is enabled. Accordingly, unauthorized users (any external sender) receive NDR about the impossibility of delivering the letter:

Your message can't be delivered because delivery to this address is restricted.

#550 5.7.1 RESOLVER.RST.AuthRequired; authentication required ##rfc822

But this NDR is already coming from the internal mail server, which means there is a risk of a Backscatter Attack.

Is it possible to configure Exchange to reject SMTP sessions in such cases, so that the external server itself forms the NDR to receive mail?

We can make additional settings on an external anti-spam server, but this is a double job for the administrator when creating distribution groups.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-23*

Then I think there are only 2 options:

-  Blocking on the external server side

-  Blocking through installation of Exchange transport agents (I don't check how it will be worked, but think, that will be)

It's sad that this isn't supported in other ways.
