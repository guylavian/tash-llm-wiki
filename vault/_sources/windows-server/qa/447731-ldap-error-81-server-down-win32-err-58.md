---
title: "LDAP error 81 (Server Down) Win32 Err 58"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/447731/ldap-error-81-server-down-win32-err-58
question_id: 447731
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# LDAP error 81 (Server Down) Win32 Err 58

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/447731/ldap-error-81-server-down-win32-err-58 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Repadmin /showreps *   

Gives LDAP error 81 (Server Down) Win32 Err 58  

This is probably referencing an old Windows Server 2008.   

-  How do I determine which server Repadmin is complaining about?   

-  If it is the old Windows Server 2008, how do I remove Windows Server 2008?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-30*

The problem with dcdiag is that it is cluttered with mostly   

No suitable default server credential exists on this system. This will prevent server applications that expect to make use of the system default credentials from accepting SSL connections. An example of such an application is the directory server. Applications that manage their own credentials, such as the internet information server, are not affected by this.  

```
A warning event occurred.  EventID: 0x00009016
```

I think I need to clear the above nuisance first.   

Repadmin /showrepl >C:\repl.txt only shows success  

Repadmin /syncall /APeD shows no errors.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-28*

3 DCs   

Yes, same exact message on all 3 DCs

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-25*

The Gives LDAP error 81 (Server Down) Win32 Err 58 is the only information that appears. It does not matter which DC is used. I am using Administrator: Command Prompt. I do not see any inbound neighbors for each DC.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-23*

Hi,    

Welcome to ask here!    

The command: "repadmin /showreps *" will display the replication situation for all the DCs.    

You will see all the inbound neighbors for each DCs.    

Check the error happened for which DC.(Destination DC or Source DC)     

If possible, you can share a screenshot here which includes the information. (Please hide the private information)    

To remove the old DC which already demoted, we need to do this on other DC, for more details you can refer to the following link:    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

Best Regards,
