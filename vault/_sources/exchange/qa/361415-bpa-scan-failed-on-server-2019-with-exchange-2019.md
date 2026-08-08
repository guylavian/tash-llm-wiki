---
title: "BPA scan failed on Server 2019 with Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/361415/bpa-scan-failed-on-server-2019-with-exchange-2019
question_id: 361415
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# BPA scan failed on Server 2019 with Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/361415/bpa-scan-failed-on-server-2019-with-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear All,    

I have an issue with BPA scan, only with one Windows Server 2019 datacenter. It's a dedicated server with Exchange 2019.    

I made many researches with no avail. See below the error message.    

    

Can you please help me to find out what's wrong?    

Thank you in advance.    

Best Regards,    

William

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-19*

Hi

Unfortunately not, it's worst in my case from Server manager.

With powershell it seem working but with error messages

]2

Regards,  

William

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-19*

Hi Lou,    

Thank you  but I still have the error message. See my result below.    

    

Thanks and regards,    

William

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-18*

Hi,    

Thanks for your quick reply.    

-  I already tried as an Administrator with no success    

-  I also tried with PowerShell[ but got an error, see the log attached.    

-  GPO are only applied from DC. There is no difference with another server where it works    

-  Nothing relevant in the event viewer    

Thanks,    

William

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-18*

Hi,

This looks like a generic error. Could you please try the below,

1.Run BPA as an administrator  

2.Try using powershell and check if that makes any difference (https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh831400(v=ws.11)?redirectedfrom=MSDN#scanning-roles-by-using-windows-powershell-cmdlets)  

3.Check if there are any GPO or local policy blocking this  

https://learn.microsoft.com/en-US/troubleshoot/windows-server/application-management/error-best-practices-analyzer-scan-has-failed  

4.Check for any relevant events in the event viewer

If the above suggestion helps, please click on "Accept Answer" and upvote it
