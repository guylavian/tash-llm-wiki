---
title: "In place Exchange Application upgrade"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2224255/in-place-exchange-application-upgrade
question_id: 2224255
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# In place Exchange Application upgrade

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2224255/in-place-exchange-application-upgrade (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have exchange server running on Operating System 2016 and on exchange version 2016. With all upcoming changes coming, I need to update it to the Exchange version 2019 and then to Exchange SE when it becomes available later this year. Quick overview of my setup:

-  We are in Hybrid mode with almost everything migrated to M365.

-  We have less than 10 mailboxes that are still on prem due to mass external they sent out to external users.

-  Currently using on prem SMTP as well as uses on prem for Scan to Email

-  On-Boarding currently includes created account on On Prem and then being migrated to M365.

Question:

-  Can I do in place upgrade from Exchange 2016 to Exchange 2019 on existing OS 2016? Any issues with that? Is it supported by Microsoft?

Anything particular I need to be concern about. Any insight on this will be appreciated.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-26*

Based on your scenario, here are the key points regarding an in-place upgrade from Exchange 2016 to 2019:

Microsoft's Official Stance

No, in-place upgrades between Exchange versions are not supported by Microsoft. You cannot install Exchange 2019 on a server running Exchange 2016 - you must deploy new Exchange 2019 servers and migrate services.

Recommended Approach

-  Deploy new Windows Server 2019/2022 systems (recommended OS for Exchange 2019)

-  Install fresh Exchange 2019 servers alongside your existing 2016 servers

-  Migrate services gradually (SMTP, scan-to-email, remaining mailboxes)

-  Decommission Exchange 2016 servers after migration is complete

Special Considerations for Your Hybrid Environment

-  You'll need to maintain at least one Exchange server on-premises for hybrid management

-  The 10 remaining mailboxes will need to be moved to the new 2019 servers

-  SMTP relay and scan-to-email configurations will need to be recreated on the new servers

-  Your hybrid configuration will need to be updated to point to the new servers

Future Planning for Exchange SE

When Exchange Server Subscription Edition (SE) becomes available, you'll need to go through a similar process - new server deployment rather than in-place upgrade.

Key Risks with Attempting In-Place Upgrade

-  Unsupported configuration that Microsoft won't assist with

-  Potential for complete Exchange organization failure

-  Data loss possibilities

-  Broken hybrid functionality

The process is well-documented by Microsoft and while it requires new hardware/VMs, it's the only supported path for your version upgrade.
If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-20*

Hi @Mohsauga  , I agree with Andy, an in-place upgrade from Exchange 2016 to Exchange 2019 on Windows Server 2016 is not supported. The proper approach is to first install Exchange 2019 on a new server (not an in-place upgrade) and then migrate your mailboxes and configurations to the new server.   

Once Exchange 2019 is successfully set up and running, you can then proceed with an in-place upgrade to Exchange SE when it becomes available later this year. This two-step process ensures compatibility and a smoother transition.  

You can refer this link.  

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-13*

Hi @Mohsauga,

Thank you for posting your question in the Microsoft Q&A forum.

Based on your description, your question is whether you can directly upgrade Exchange 2016 to 2019 in-place on an existing Windows Server 2016.

-  you cannot directly update Exchange 2016 to Exchange 2019. you need to create a new Exchange 2019 to coexist with Exchange 2016 and then migrate mailboxes to Exchange 2019 and then uninstall Exchange 2016.

-  the minimum operating system supported by Exchange Server 2019 is Windows Server 2019. additionally, since the lifecycle of Windows Server 2019 ends in January 2029, it is recommended that you on Windows Server 2022 install new deployments of Exchange Server 2019 CU15 and Exchange Server SE RTM, if available.

-  the Exchange Deployment Assistant is a web-based tool that asks you a few questions about your current environment and then generates a customized step-by-step checklist to help you deploy Exchange Server in your local organization. you can follow the steps it prompts you to take. Exchange Deployment Assistant | Microsoft Learn

If the answer is helpful, please click on “Accept answer” as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.
