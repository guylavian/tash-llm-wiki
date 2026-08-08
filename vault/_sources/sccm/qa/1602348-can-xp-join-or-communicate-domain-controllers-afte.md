---
title: "Can XP join or communicate Domain Controllers after June 2023"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1602348/can-xp-join-or-communicate-domain-controllers-afte
question_id: 1602348
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-updates"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Can XP join or communicate Domain Controllers after June 2023

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1602348/can-xp-join-or-communicate-domain-controllers-afte (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a couple XP machines in the mix and are trying to understand if they will still be able to connect back to the domain after running windows updates on the domain controller.    there had been some articles stating after updates in June / July 2023 they would not work but I can't find any information.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-02-29*

Hi,

Thank you for posting in Microsoft Q&A forum.

What operating system is your domain controller? You should be able to join Win XP to a domain with a domain controller running Windows Server 2016. Under some circumstances you should be able to join Win XP to a domain with a DC2019. However, you can find many discussions describing issues with joining it to a domain with a DC2019. Some people fixed it by installing specific KBs on the Win XP machine (for instance KB969442, KB968389, etc.), some people claim it's due to the RC4 cipher. 

You can try to install these KBs and see but you'll be very lucky if you ever get it working. Similar thread for your reference.
Windows XP and Active Directory 2019

However, Windows XP is long out of support, and because there is no longer support there also is no patching or testing for XP scenarios. So while it may work today there's really no guarantee for tomorrow.

Thanks for your time. Have a nice day!

Best regards,

Simon

If the response is helpful, please click "Accept Answer" and upvote it.
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
