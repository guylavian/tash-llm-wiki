---
title: "Exchange Server 2016 Manage Audit and Security logs requirement poilicy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1194728/exchange-server-2016-manage-audit-and-security-log
question_id: 1194728
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Server 2016 Manage Audit and Security logs requirement poilicy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1194728/exchange-server-2016-manage-audit-and-security-log (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to find some documentation on the requirement for Exchange Servers to have 'Manage Audit and Security Logs' rights on the DC. I know without that setting, you can't enable mailboxes and potentially other issues arise. Our Cyber management wants us to pull this policy, but I can't find supporting documentation; just forums topics regarding it. 

Thanks everyone.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-03-31*

Hi @Scott Studer  ,

Per my research, there's no such a document exclusively for Exchange server 2016. But here are two official links that mention about the 'Manage auditing and security log' permission should not be removed from the Exchange Servers group. They are for Exchange 2007 and 2010 but this requirement should still apply to Exchange 2016:

-  The 'Manage auditing and security log' permission is removed from the Exchange Servers group on one or more domain controllers  

   

-  The Exchange server does not have the Audit Security privilege on a Domain Controller  

   

Below are two more 3rd-party articles for reference:  

(Please Note: Since the web sites below are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.)

-  Exchange Servers need the Manage Auditing and Security Log right

-  Ensure 'Manage auditing and security log' is set to 'Administrators' and (when Exchange is running in the environment) 'Exchange Servers' (DC only)

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
