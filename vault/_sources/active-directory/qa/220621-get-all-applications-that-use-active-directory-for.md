---
title: "Get All applications that use active directory  for authentication  (ldap binding)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/220621/get-all-applications-that-use-active-directory-for
question_id: 220621
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Get All applications that use active directory  for authentication  (ldap binding)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/220621/get-all-applications-that-use-active-directory-for (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Microsoft community ,  

I am in the process of migrating my domain controllers to new IPs and since we have several applications that use LDAP for authentication, I must change the DC ip in the settings of those applications (JIRA , vmware , ...).  

my question is: is there a solution to identify all the applications which use LDAP using a (script/tool/other)?  

Thanks a lot

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-11*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-08*

You may enable logging for LDAP queries or run AD Data Collector set and the result will have details about source IP Address or hostname that utilizes the domain controller from authentication. This should be done against each DCs or you may think of any automated solutions like Splunk or scripts.  

https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/how-to-find-expensive-inefficient-and-long-running-ldap-queries/ba-p/257859  

https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/domain-and-dc-migrations-how-to-monitor-ldap-kerberos-and-ntlm/ba-p/256796  

Regards,  

Deepak

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-07*

Thanks a lot  for your answer,   

Not necessary to use a script but also i already posted in the script's forum.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-07*

Hi,  

Thank you for posting in our forum.  

If you want to use a script to solve this problem, you can go to the script's forum and post.  

reference:https://social.technet.microsoft.com/Forums/Windows/en-US/home?forum=winserverpowershell  

Hope this information can help you  

Best wishes  

Vicky
