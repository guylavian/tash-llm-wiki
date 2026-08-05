---
title: "Godex printer installation via GPO. Requesting credentials."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/368782/godex-printer-installation-via-gpo-requesting-cred
question_id: 368782
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-print-jobs"]
---
# Godex printer installation via GPO. Requesting credentials.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/368782/godex-printer-installation-via-gpo-requesting-cred (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello.  

I have a Godex printer added to the prints server.  

I'd like it to automatically install via GPO.  

But a plate of credentials about the need for elevation of privilege appears (possibly while installing drivers).  

Drivers are added in GPO as trusted.  

What should I do to prevent the credentials from appearing?  

I know that after some update, Windows blocks untrusted drivers.  

Greetings.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-28*

We have three AD containers:  

-users  

-  desktop computers  

-  laptops  

There is a policy in each container:  

-  computer configuration  

-  user configuration  

Which policy is the most important / overarching?  

Which one should I modify?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-26*

Hello,  

Few GPO you could try to modify.  

User Configuration > Policies > Administrative Templates >Control Panel/Printers > Point and Print Restrictions  

Computer Configuration > Policies > Administrative Templates >Control Panel/Printers > Point and Print Restrictions  

computer config / policies / admin templates / system / driver installation / policy enable the allow non-admins to install drivers  

Please refer to the information below: Hope they could be helpful.  

https://serverfault.com/questions/641579/users-still-get-uac-prompt-after-allowing-printer-install-and-alter-lan-connecti  

https://community.spiceworks.com/topic/645262-how-to-install-new-printers-via-gpo-when-users-don-t-have-permission  

Hope this helps and please help to accept as Answer if the response is useful.  

Best Regards,  

Carl
