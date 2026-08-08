---
title: "The Exchange 2010 HCW says my time differs by more than five minutes from the federated servers, but the time is correct. How to solve?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1488766/the-exchange-2010-hcw-says-my-time-differs-by-more
question_id: 1488766
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# The Exchange 2010 HCW says my time differs by more than five minutes from the federated servers, but the time is correct. How to solve?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1488766/the-exchange-2010-hcw-says-my-time-differs-by-more (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

As title. I'm running Exchange 2010 SP3 and don't want to be. I ran the Hybrid Configuration Wizard and have got as far as validating the fact the domain is mine by verifying a TXT in the DNS but it tells me;
"Failed - Unable to federate your domain. Your system time appears to be more than five minutes out of sync with the time on our federation servers. Ensure your system time is correct and retry the Hybrid Configuration Wizard."
Trouble is, the time is correct on my Exchange server! How do I check what the time is on "our federation servers"?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-12*

Hello @Stuart Hawkins  

Have you checked this article: "Ensure your system time is correct" error when you run Hybrid Configuration wizard.”
It looks like you need to configure an authoritative time server in Windows Server.

Kind Regards
