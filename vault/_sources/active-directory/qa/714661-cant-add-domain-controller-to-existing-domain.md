---
title: "Can't add domain controller to existing domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/714661/cant-add-domain-controller-to-existing-domain
question_id: 714661
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Can't add domain controller to existing domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/714661/cant-add-domain-controller-to-existing-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,   

I have been digging through Google and trying fixes all day, I've never run into this problem quite this bad.  I am trying to add another domain controller to my domain.  There is only one currently and this is a 2012 R2 DC with the same being added.  Here is the full error:   

The operation failed because:  

The Active Directory Domain Services Installation Wizard (Dcpromo.exe) was unable to convert the computer account CTG-HQ-DC$ to an Active Directory Domain Controller account.  

Verify that the user running Dcpromo.exe is granted the "Enable computer and user accounts to be trusted for delegation" user right in the Default Domain Controllers Policy.  

For more information, see the resolution section of http://go.microsoft.com/fwlink/?LinkId=178406.  

The error was:  

"The specified network resource or device is no longer available."  

This is what I have verified so far  

-  I can get through all of the screens to promote the DC, it fails on install  

-  On the current DC I have verified that the new server is in Active Directory in the domain controllers OU  

-  Verified that the group policy allows the admin account to enable the trust and the GPO is applying to the current DC  

-  In Sites and Services the server is under the site but the NTDS settings are missing  

-  I can ping the domain from the new server  

-  I can ping the DNS name of the current DC from the new server  

-  The current DC has the proper service records in DNS  

-  DCDIAG on the current DC is clear except for a warning   

Anyone have any thoughts?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-31*

You can also start a case here with product support.  

https://support.serviceshub.microsoft.com/supportforbusiness  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-31*

I already verified that the Admin account has this right and the GPO is populating to the current DC and it is applied via the results screen.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-31*

Looking into it now.  Additional information.  As I am trying to clean out all of the old DCs in DNS manager, once I refresh the screen their SRV, GC, LDAP records all start reappearing.  Very confusing, they are not in ADUC, they don't have site records, they don't physically exist anymore, but they keep coming back.  Even using NTDSUTIL can't connect to them because they don't exist.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-31*

Might work through this one.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/access-denied-error-occurs-dcpromo    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-28*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\dc3.txt`  

then put `unzipped` text files up on OneDrive and share a link.
