---
title: "Duplicating mails in exchange online in junk folder"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2225545/duplicating-mails-in-exchange-online-in-junk-folde
question_id: 2225545
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 2
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Duplicating mails in exchange online in junk folder

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2225545/duplicating-mails-in-exchange-online-in-junk-folde (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey, 

we have a problem with duplicating mails in actually four tenants: 

Exchange online is duplicating spam mails itself, u can see, it was only once delivered to Exchange Online, but it's delivered to junk mail repeatedly! 

At some addresses it's only a few message, at another address there are over 600.000 mails (3 or 4 different mails). All filters for not delivering the email don't take action, because the mails don't arrive new at the Exchange Server. 

Microsoft can't find a solution yet, my first ticket was opened Februar 19th, it's now at the 3rd or 4th escalation, but no solution! My customer is not amused. 

Also tried to empty the junk folder by exo shell, but doesn't help. 

Any suggestions?

Greets from Germany, 

Bjoern

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-17*

Hello, @Bjoern Goetze,

Welcome to the Microsoft Q&A platform!

I understand how critical this issue is for your customer, while I can't provide a direct solution, I can give you some steps that might help you troubleshoot or work around the problem until Microsoft provides a more definitive fix.

1.Create a New Mailbox: As a temporary workaround, you could create a new mailbox for the affected user and set up forwarding from the old mailbox, filtering out junk mail or setting up rules to manage spam differently.

2.Delegate Access: Assign delegate access to another user or admin account to manually monitor and manage the junk folder, which may help keep it under control in the interim.

3.Configure Junk Email Settings: Admins can configure junk email settings in Exchange Online mailboxes through Outlook or Outlook on the web. For reference, please refer to Configure junk email settings on Exchange Online mailboxes - Microsoft Defender for Office 365 | Microsoft Learn.

4.Configure Anti-Spam Policies: Use the Microsoft Defender portal to create and manage anti-spam policies with the help of Configure spam filter policies - Microsoft Defender for Office 365 | Microsoft Learn. This can help prevent spam emails from being duplicated.

It is critical to continue to work closely with Microsoft Support as they can provide advanced troubleshooting and log analysis. While the process is long, persistence and detailed investigation are key to finding a solution. 

If the answer is helpful, please click on “Accept answer” as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.

Best Wishes,

Alex Zhang
