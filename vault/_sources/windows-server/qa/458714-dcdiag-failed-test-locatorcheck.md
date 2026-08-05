---
title: "Dcdiag failed test LocatorCheck"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/458714/dcdiag-failed-test-locatorcheck
question_id: 458714
fetched: 2026-07-25
answer_count: 11
has_accepted_answer: false
upvotes: 3
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Dcdiag failed test LocatorCheck

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/458714/dcdiag-failed-test-locatorcheck (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Starting test: LocatorCheck  

```
GC Name: \\DC2

     Locator Flags: 0xe003f1fc
     Warning: DcGetDcName(PDC_REQUIRED) call failed, error 1355

     A Primary Domain Controller could not be located.

     The server holding the PDC role is down.

     Time Server Name: \\DC2
     Locator Flags: 0xe003f1fc
     Preferred Time Server Name: \\DC3
     Locator Flags: 0xe003f3fd
     KDC Name: \\DC2
     Locator Flags: 0xe003f1fc
     ......................... Domain failed test LocatorCheck
```

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-07-01*

What do I use to check the that DNS settings are correct on PDC?  

PDC should have own static ip address plus loopback (127.0.0.1) listed for DNS and no others such as router or public DNS  

 --please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-07-01*

Three DCs DC1,2,3  

netdom /query fsmo shows:  

Schema master                 

Domain naming master        DC3  

PDC                         DC3  

RID pool manager            DC3  

Infrastructure master       DC3  

The link given says   

To find PDC emulator, at the command line on a DC run the following  

Netdom query fsmo  

Which of the roles listed is the PDC emulator?  

According to the link   

Go to Administrative Tools -> Services  

  Ensure that the Windows Time service is set to automatic start up and that it is started.  

  Reboot the server then run the dcdiag test again.  

Windows Time services startup type is automatic and service status is running.   

Netdom query dc lists the three DCs.   

Run following commands:  

On PDC emulator:  

w32tm /config /manualpeerlist:time.windows.com,0×1 /syncfromflags:manual /reliable:yes /update  

net stop w32time & net start w32time & w32tm /resync /rediscover  

On Non -PDC DC and Domain Clients:  

w32tm /config /syncfromflags:domhier /update  

net stop w32time & net start w32time & w32tm /resync /rediscover  

Ran PDC emulator command on DC3  and Non-PDC on DC2 and DC1.   

No change  

Can not find the blogs.dirteam.com on Windows Time Service   

What do I use to check the that DNS settings are correct on PDC?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-01*

Hi,  

To know the issue more clearly, please confirm the following information:  

How many DCs do you have?  

Which one has the FSMO roles? Command can be used to confirm that: netdom /query fsmo  

Check if the DNS settings was configured correctly on the PDC.  

Check if the time services is running correctly.  

Following link for your reference:  

https://social.technet.microsoft.com/Forums/en-US/b4febe07-bff1-4e8d-a9c7-9a1fb1cc262e/fsmo-roles?forum=winserverDS  

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-07-01*

Not a lot to go on, but check the PDCe is up and available. Also do `netdom /query fsmo` and check the results are expected.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
