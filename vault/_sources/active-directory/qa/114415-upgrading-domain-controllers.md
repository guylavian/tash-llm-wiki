---
title: "upgrading domain controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/114415/upgrading-domain-controllers
question_id: 114415
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# upgrading domain controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/114415/upgrading-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

upgrading two DCs from 2008r2 to 2012. we have licenses for 2012, will look at moving to 2019 next fiscal year.  

runing dcdiag on DC returns a few errors, and some in event viewer on DC, but not sure if it is something that would keep from going forward.  

1-key distribution center cannot find suitable certificate to use for smart card logons - we do not use this at all, so safe to ignore from google.  

2-DCOM was unable to communicate with computer ******@mydomain.com usany any of the configured protocols. - that server was an old exchange server , removed years ago.  

3-Certificate enrollment for Local system failed to enroll for a DomainController certificate with request ID N/A from oldserver.ourdomain.com\mail.emaildomain.com  

this refers back to that same old exchange server that is no longer around, was setup as certificate server back then, but we do not a have certificate server now.  

4-Automatic certificate enrollment for local system failed (0x800706ba) The RPC server is unavailable. - this once again appears to reference the old exchange server that was a certificate server, but we no longer have a certificate server.  

so would any of these prevent me from adding two new DCs today?  that way I can watch for errors for couple of days, then demote the old DCs and promote new ones on Sunday.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2020-10-02*

domain functional level is 2008r2, not planning on raising that yet. do I have to migrate to DFS before I add or promote the 2012 DCs?  

No this isn't a requirement for Server 2012. After the migration is complete and health is confirmed 100% then migrating sysvol replication from older FRS technology to DFSR is recommended.  

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2020-10-01*

Hi,  

It seems there is a autoenrollment already set to let domain controller to get a certificate automatically.  

It seems that the DC is unable to contact PKI (RPC error).  

Check if there is any issue on your PKI settings , network flow or template setting.   

despite this error , you can promote a additional DC and demote the old one. But you should be sure that new DC get a certificate if there is any application already use LDAPS protocol.  

Please don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2020-10-01*

Nothing listed should be a show stopper. You could work through this one for some cleanup of the cert remnants.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/delete-enterprise-windows-certificate-authority    

Some general info    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2012, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-02*

I have added the two new servers, and when I test each DC running dcdiag /s:servername, I receive no error on any of the DCs, the 2 old or two new.  

But if I run this command  "dcdiag/s:servername /c /v /f that is supposed to run test on ALL DCS I then get this error:  

The File Replication:Service is having trouble enabling replication from  new server to old server c:\windows\sysvol\domain using the DNS Name newserver  

its weird that this does not show up when I run dcdiag individually, is just the difference between 2008r2 and 2012, or is it something else?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-02*

domain functional level is 2008r2, not planning on raising that yet.  do I have to migrate to DFS before I add or promote the 2012 DCs?
