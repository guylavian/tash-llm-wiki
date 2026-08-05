---
title: "Exchange 2019 AddressBookPolicy cannot be matched to a name in the address list"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1161221/exchange-2019-addressbookpolicy-cannot-be-matched
question_id: 1161221
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# Exchange 2019 AddressBookPolicy cannot be matched to a name in the address list

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1161221/exchange-2019-addressbookpolicy-cannot-be-matched (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi;

I host multiple domains on exchange 2019. I want each domain to see only users from its own domain in the address book. I tried to do this with address book policies. I used the article here as a reference. [https://practical365.com/separating-users-in-office-365-using-address-book-policies/

After this process, users started to see their user addresses in their own domain names in their address books via OWA.

However, when I try to define the mail address in outlook, I get the "the name cannot be matched to a name in the address list" error.

My autodiscover records are opened as SRV on DNS for each domain. 

In addition, when I do not make an address list policy, I can define mailboxes of domain names in Outlook without any problems.

Is there any way to fix this problem ?

Or can we not use outlook when address book policies are made?

Thank You

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-17*

I am having this problem while defining a new account in outlook.
