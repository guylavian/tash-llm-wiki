---
title: "Deploy Software with GPO for domain joined laptops"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2193436/deploy-software-with-gpo-for-domain-joined-laptops
question_id: 2193436
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Deploy Software with GPO for domain joined laptops

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2193436/deploy-software-with-gpo-for-domain-joined-laptops (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I created a GPO where I deployed a .msi package in the computer configuration - software settings. 

The msi file is in a network share folder. 

Domain users, domain computers and domain admins have Read access to it.

I want to apply that GPO to an OU in our AD. 

I want to apply the GPO based on user accounts (domain users) and not domain computers.

Currently in the security filtering only Authenticated Users are added. The (TEST) OU only has 1 user currently. 

My question is do i need to add both the domain user account and domain computer to the OU or will only having the domain user account in the OU will install the package on the computer that user is logging into.

I hope i was able to explain my situation

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-25*

Hello cescSalv21,

Thank you for posting in Microsoft Community forum.       

You can deploy software via computer configuration - software settings or user configuration - software settings.  

If you want to use user configuration - software settings.

You only need to add the domain account in the OU, and link the GPO to the OU when editing, select the software settings under the user configuration, please be careful not to select the software settings under the computer configuration. When a domain user logs in from a domain member computer, the software will be installed after restarting the machine 2-3 times.

If you want to use computer configuration - software settings.

You only need to add the domain computer in the OU, and link the GPO to the OU when editing, select the software settings under the computer configuration, please be careful not to select the software settings under the user configuration. When a domain user logs in from a domain member computer, the software will be installed after restarting the machine 2-3 times.

For more information about deploy software installation via GPO under user configuration or computer configuration, please refer to link below.  

Use Group Policy to remotely install software - Windows Server | Microsoft Learn

I hope the information above is helpful.           

If you have any question or concern, please feel free to let us know.     

Best Regards,  

Daisy Zhou
