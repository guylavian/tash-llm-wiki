---
title: "Dependency on a Single Domain Controller - I_NetLogonControl failed: Status = 1062 0x426 ERROR_SERVICE_NOT_ACTIVE"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/552466/dependency-on-a-single-domain-controller-i-netlogo
question_id: 552466
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Dependency on a Single Domain Controller - I_NetLogonControl failed: Status = 1062 0x426 ERROR_SERVICE_NOT_ACTIVE

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/552466/dependency-on-a-single-domain-controller-i-netlogo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We got 3 DCs - 1 of Win 2008 R2 & 2 of Win 2012 R2  

Names of DC  

WIN2008R2 - MDC  

WIN2012R2 - BDC & ADCP  

Problem is if we disconnect the Win2008R2 DC, all the servers cannot logon to domain. All our exchange server fails. Upon connecting the W2008R2 DC back, everything works fine.  

DNS Config on all servers are pointed to  W2012R2 DC Servers  

C:\Users\MYDOMAIN-admin> nltest /SERVER:MEMBERSERVER /SC_RESET:MYDOMAIN\MDC  

Flags: 30 HAS_IP  HAS_TIMESERV  

Trusted DC Name \mdc.MYDOMAIN.in  

Trusted DC Connection Status Status = 0 0x0 NERR_Success  

The command completed successfully  

C:\Users\MYDOMAIN-admin> nltest /SERVER:MEMBERSERVER /SC_RESET:MYDOMAIN\BDC  

I_NetLogonControl failed: Status = 1062 0x426 ERROR_SERVICE_NOT_ACTIVE  

C:\Users\MYDOMAIN-admin> nltest /SERVER:MEMBERSERVER /SC_RESET:MYDOMAIN\ADCP  

I_NetLogonControl failed: Status = 1062 0x426 ERROR_SERVICE_NOT_ACTIVE  

C:\Users\MYDOMAIN-admin> nltest /SERVER:MEMBERSERVER /SC_RESET:MYDOMAIN\MDC  

Flags: 30 HAS_IP  HAS_TIMESERV  

Trusted DC Name \mdc.MYDOMAIN.in  

Trusted DC Connection Status Status = 0 0x0 NERR_Success  

The command completed successfully

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-09-16*

Sounds good. Once health has been confirmed 100% you can follow along here.  

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-16*

Hi All,    

Thanks for revert    

I observed that on the W2K8 R2 based DC, i could see the errors in FRS eventvwr - JRNL_WRAP_ERROR    

The other DCs of 2K12 R2 did not had the sysvol & netlogon folders shared but these were ON i.e appearing shared on the W2K8R2 DC    

& thus all the machines couldnot logon if W2K8R2 DC gets down    

on the W2K8R2 DC, I initiated a non authoritative restore with 'D2' as Burflags. Ref was below link    

 https://learn.microsoft.com/en-US/troubleshoot/windows-server/networking/use-burflags-to-reinitialize-frs#considerations-before-you-configure-authoritative-or-nonauthoritative-restores-of-frs-members    

Oops & the sysvol & netlogon folders got disappeared from the W2K8R2 DC as well & now everything went down including the W2K8R2 DC Services. No users could login    

the reason was being it a non authoritative restore it was trying to replicate sysvol & other data from other DCs BUT the other DC's were already bad & were in same state or  issues    

errors can be observed in the FRS Logs    

on the W2K8R2 DC, I cut the data from the 'pre-existing folders' (sysvol) to original location of sysvol    

restarted FRS services but same issue    

I then changed the registry Bur Flags to 4 i.e Authoritative restore & restarted FRS Service again    

Bingo!    

it recovered the DB well & also replicated successfully to the other W2KR2 DCs & the sysvol & netlogon folders appeared shared on them    

Started observing information in FRS Logs - ....is no more preventing this server to be a domain controller on all DCs    

Everything is fine now    

Have to consider Migration of FRS to DFSR SYSVOL

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-09-15*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\dc3.txt`  

then put `unzipped` text files up on OneDrive and share a link.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-15*

Hello  

Thank you for reaching out.  

I would suggest you to verify if the AD health is good and all your DC are replicated with each other.  

Also please run dcdiag to check any replication errors.   

Hope this helps,   

Thank you.
