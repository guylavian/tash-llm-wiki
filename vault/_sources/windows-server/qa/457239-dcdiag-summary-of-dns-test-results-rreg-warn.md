---
title: "Dcdiag Summary of DNS test Results RReg warn"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/457239/dcdiag-summary-of-dns-test-results-rreg-warn
question_id: 457239
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Dcdiag Summary of DNS test Results RReg warn

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/457239/dcdiag-summary-of-dns-test-results-rreg-warn (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Summary of DNS test results:  

```
Auth Basc Forw Del  Dyn  RReg Ext
        _________________________________________________________________
        Domain: domain

           DC1               PASS PASS PASS PASS PASS PASS n/a  
           DC3               PASS PASS PASS PASS PASS WARN n/a  
           DC2               PASS PASS PASS PASS PASS PASS n/a
```

What is causing the WARN?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-30*

I am back to the statement made for LDAP error 81 (Server Down) Win32 Err 58  

The problem with dcdiag is that it is cluttered with mostly  

No suitable default server credential exists on this system. This will prevent server applications that expect to make use of the system default credentials from accepting SSL connections. An example of such an application is the directory server. Applications that manage their own credentials, such as the internet information server, are not affected by this.  

-  A warning event occurred. EventID: 0x00009016

I think I need to clear the above nuisance first.  

Repadmin /showrepl >C:\repl.txt only shows success  

Repadmin /syncall /APeD shows no errors.

I posted a How to get domain controller certificate? question.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-30*

Hi,  

To understand the issue more clearly, please run the following command to get more information:  

Dcdiag /v >c:\dcdiag1.log      

Repadmin /showrepl >C:\repl.txt   

Repadmin /showreps  

ipconfig /all > C:\dc1.txt  

If there are errors, please share a screenshot here! (Please hide the private information)  

Best Regards,
