---
title: "Any way to get 2019 exchange server to not do SSL or TLS and just provide unencrypted email over owa and/or outlook client"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1370241/any-way-to-get-2019-exchange-server-to-not-do-ssl
question_id: 1370241
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Any way to get 2019 exchange server to not do SSL or TLS and just provide unencrypted email over owa and/or outlook client

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1370241/any-way-to-get-2019-exchange-server-to-not-do-ssl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I run a lab for students that look at packet data is there any way to get the 2019 exchange server to not do SSL or TLS and just provide unencrypted email over OWA and/or Outlook client?

I have tried disabling SSL in the ISS default website and unbinding 443 both loop back and external, I have updated the virtual directories more specifically I have updated the OWA and the ec virtual directories.

Any help would be much appreciated for me and the students.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-09-18*

Hi @DRM,

If you mean the raw message, it is possible to view the message header and message contents directly in Outlook.

message header:

double-click to open a message and select File>Properties

message contents:

double-click to open a message and right-click on the blank area to select "View Source"

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
