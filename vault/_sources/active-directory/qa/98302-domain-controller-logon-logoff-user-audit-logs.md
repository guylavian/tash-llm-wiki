---
title: "domain controller logon / logoff user audit logs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/98302/domain-controller-logon-logoff-user-audit-logs
question_id: 98302
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# domain controller logon / logoff user audit logs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/98302/domain-controller-logon-logoff-user-audit-logs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

we have 20 domain controllers and need to forward audit logs (user logon / logoff ) to syslog server.   

Below are the query.  

-  whether the audit log will get sync between all the domain controller ?  

-  what is best practice to send audit logs to sys log, all event logs from domain controller need to send separately or is there any other method.   

Regards,  

Mani

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 2 · updated: 2020-09-18*

Hi,  

1, Based on my research, Audit logs will not get sync between all the DCs. DCs just log the events for themself.  

2, For send audit logs to system log, you can refer to the following link: https://social.technet.microsoft.com/Forums/ie/en-US/66587a55-2883-4365-be7d-ab5baed50dc0/need-to-collect-security-logs-from-all-domain-controller-to-central-location?forum=winserverDS  

Best Regards,

## Answer (community) — community member

*upvotes: 1 · updated: 2020-09-23*

Hello Smanif,  

Aside from what's mentioned already, the Windows Event Trap Translator will also do the trick if you have SNMP. Simply locate the EVENT ID(s) you want to trap and it will send an SNMP alert every time the EVENT ID is triggered.  

https://www.falconitservices.com/support/KB/Lists/Posts/Post.aspx?ID=275  

Cheers,  

Miguel Fra  

www.falconitservices.com
