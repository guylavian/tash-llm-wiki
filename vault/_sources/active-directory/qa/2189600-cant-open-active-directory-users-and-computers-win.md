---
title: "Can't open Active Directory Users and Computers - Windows 11 Pro 23H2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2189600/cant-open-active-directory-users-and-computers-win
question_id: 2189600
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 8
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Can't open Active Directory Users and Computers - Windows 11 Pro 23H2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2189600/cant-open-active-directory-users-and-computers-win (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am unable to open AD Users and Computers anymore. It asks for an admin login, however it doesn't load after entering my credentials. It shows the loading symbol briefly by the cursor but nothing happens after that. It was working fine in the past. No changes have been made to the computer.   

Have tried restarting and running windows updates. 

***moved from Windows / Windows 11 / Accessibility***

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-13*

Hello  

Greetings!  

Please check if this machine is connected to domain network.  

Please try to restart this machine and check if you can uninstall RSAT tool.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-12*

Yes I did.   

It works on other client machines and on the domain controller. 

When I try to uninstall the RSAT tool I get this error:

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-12*

Hello Angus Long,

Thank you for posting in Microsoft Community forum.

Did you install RSAT tool on one domain Windows 11 Pro 23H2 client machine and open the AD Users and Computers?

Please check if you can open AD users and computers on domain controller? If so, please uninstall RSAT tool and reinstall it and check if it helps.

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
