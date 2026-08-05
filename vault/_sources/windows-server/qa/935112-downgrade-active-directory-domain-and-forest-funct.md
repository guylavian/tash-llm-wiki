---
title: "Downgrade Active Directory Domain and Forest Functional levels"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/935112/downgrade-active-directory-domain-and-forest-funct
question_id: 935112
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Downgrade Active Directory Domain and Forest Functional levels

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/935112/downgrade-active-directory-domain-and-forest-funct (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,    

I just wanted  to reach out regarding downgrading the domain and forest functional level. I found some instructions that looks like we would be able to downgrade functional levels from 2019 to 2008. I just wanted to confirm if this is indeed a possiblity, and I also want to ask what are the risks assiociated with this? Right now we only have one domain control that supports about 30 computers, and this looks like something we may need to do to get their XP machines to connect back to the domain again. Just looking to get some infomration regarding this process?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-21*

Hello    

Thank you for your question and reaching out. I can understand you are  having query\issues related  to    

When attempting to downgrade (lower) the DFL of a domain, you would first need to downgrade the FFL to the same level as the required DFL to be configured. The FFL can never be higher than the DFL of any domain in the forest.    

Functional levels determine the available AD DS domain or forest capabilities.    

In your case if you have XP Machines then you should be able to join to Windows 2019 DC , Hence there should be no need to downgrade functional level.    

--------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--
