---
title: "Deploy Software with GPO for domain joined laptops"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1511178/deploy-software-with-gpo-for-domain-joined-laptops
question_id: 1511178
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Deploy Software with GPO for domain joined laptops

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1511178/deploy-software-with-gpo-for-domain-joined-laptops (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I created a GPO where I deployed a .msi package in the computer configuration - software settings.
The msi file is in a network share folder. Domain users, domain computers and domain admins have Read access to it
I want to apply that GPO to an OU in our AD
I want to apply the GPO based on user accounts (domain users) and not domain computers.
Currently in the security filtering only Authenticated Users are added.
The (TEST) OU only has 1 user currently. 
My question is do i need to add both the domain user account and domain computer to the OU or will only having the domain user account in the OU will install the package on the computer that user is logging into.  

I hope i was able to explain my situation

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-25*

Hi Salvi Ali,

Since you want to apply the GPO based on user accounts, you only need to have the domain user accounts in the OU and set the software installation under User Configuration in the GPO. 

Best Regards,
Ian Xue

If the Answer is helpful, please click "Accept Answer" and upvote it.
