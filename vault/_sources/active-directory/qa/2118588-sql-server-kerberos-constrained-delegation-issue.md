---
title: "SQL Server Kerberos Constrained Delegation Issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2118588/sql-server-kerberos-constrained-delegation-issue
question_id: 2118588
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["sql-server-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# SQL Server Kerberos Constrained Delegation Issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2118588/sql-server-kerberos-constrained-delegation-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, hoping someone can help. We're in the process of migrating to a new SQL instance and bulk load / insert from SMB share isn't working in SMSS or via SQL agent job

I'm reasonably confident its Kerberos delegation as I see ANONYMOUS in the file server audit log with constrained delegation and when I enable temporarily enable unconstrained delegation it works fine showing my own domain account in the audit log of the file server

We're using a managed service account

```
PS C:\>setspn -L msa$
Registered ServicePrincipalNames for CN=MSA,CN=Managed Service Accounts,DC=Domain,DC=com:
MSSQLSvc/sql02.domain.com:1433
MSSQLSvc/sql02.domain.com
```

Have allowed for constrained delegation

```
Set-ADAccountControl -Identity msa$ -TrustedForDelegation $false -TrustedToAuthForDelegation $false

Set-ADAccountControl -Identity sql02$ -TrustedForDelegation $false -TrustedToAuthForDelegation $false
```

Have set SPN's for CIFS on file servers

```
PS C:\> setspn -L server04
Registered ServicePrincipalNames for CN=server04,OU=Servers,DC=domain,DC=com:
cifs/server04.domain.com
cifs/server04
```

Confirmed delegation is set 

```
PS C:\Get-ADServiceAccount -Identity msa -Properties * | select msds-allowedtodelegateto,hostcomputers

msds-allowedtodelegateto                                                                         hostcomputers
------------------------                                                                         -------------
{cifs/server04.domain.com, cifs/server04} 
{CN=SQL02,OU=Servers,DC=domain,DC=com}
```

I ran sqlcheck from Microsoft and this looks fine, only warning trusted for delegation is false but I believe that is the expected result with constrained delegation. Would like to have shared that but kept getting "file upload failed, please try again"

What am I missing?

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-19*

Edited as accidental duplicate

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-19*

I've managed to resolve this by swapping from "Use Kerberos only" to "Use any authentication protocol". I don't really understand why it didn't work though, query to SQL says its using Kerberos, eventlog on file server shows Kerberos too - something for another day

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-14*

Hi @Chris W

as I see ANONYMOUS in the file server audit log with constrained delegation

Seems like your SQL Server instance and the SQL Server Agent service is unable to impersonate the user to access the SMB share. 

Please make sure the constrained delegation is configured correctly. Review this tech doc: How to configure Kerberos Constrained Delegation for Web Enrollment proxy pages.

Best regards,

Cosmog

If the answer is the right solution, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-11-13*

Use the MS SQL Server Kerberos Configuration Manager to validate and may fix the issue.

Free download at

https://www.microsoft.com/en-us/download/details.aspx?id=39046
