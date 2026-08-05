---
title: "Delete mailbox option is not available in Exchange server 2019 admin center"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1359176/delete-mailbox-option-is-not-available-in-exchange
question_id: 1359176
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Delete mailbox option is not available in Exchange server 2019 admin center

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1359176/delete-mailbox-option-is-not-available-in-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have recently deployed two node cluster exchange 2019 all works fine, but to surprise we have noticed delete mailbox option is not available from admin center in mail recipients page.

Just to know how we get it.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-08*

Hi @IT Engineer  

I deleted one of my test mailboxes in my environment through the "delete" button, so I saw the executed commands in the "event viewer". I got the result in the image below through the shell command, which returns the roles and permissions required to use "remove-mailbox".

Find the permissions required to run any Exchange cmdlet

But you mentioned that your user already exists in "Organization Management", so I think that's strange, which is why above you are asked to check "Mail Recipient creation". Or you can ask other administrators to check and see if there is no delete button.

Anyway, feel free to share with us any progress you have made, or if you have solved this problem, you can also share your solution with us.

Regards

Shaofan
