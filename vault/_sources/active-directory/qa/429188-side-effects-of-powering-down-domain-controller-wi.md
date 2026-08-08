---
title: "Side Effects of Powering Down Domain Controller without Demoting"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/429188/side-effects-of-powering-down-domain-controller-wi
question_id: 429188
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Side Effects of Powering Down Domain Controller without Demoting

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/429188/side-effects-of-powering-down-domain-controller-wi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a pair of legacy domain controllers that I want to demote and shutdown. I've already created a pair of Windows Server 2019 DCs and migrated the FSMO roles to one. We have a fairly large environment with many LDAP connections, or domain joined appliances. I've spent the last 6 months trying to find every reference do the legacy domain controllers that I can from everything that I've inherited with little to no documentation. MFDs, UPS's, server / appliance NICs, applications, DHCP scopes, etc.   

To see if I'd discovered enough, I wanted to schedule a shutdown test of the two legacy DCs. I have some concerns though about how w32tm, Kerberos, and domain joined devices work with round robin requests. If I merely shutdown the DCs rather than demote them and then shut them down, since devices and member servers reference time through w32tm in a round robin method (as far as I know) from DCs, I think this could cause issues if the device was registered to one of the DCs I shutdown. Similarly, with devices which reference the root of the domain, example.local, rather than specific DCs, this DNS entry will also return in round robin, and I believe that will pose an issue as well.  

Am I correct in my assumptions? Is biting the bullet and demoting the DCs really the recommended way to move forward? Do non-windows domain joined devices (like linux appliances) typically have to be rejoined to the domain after a change like this?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-10*

Hi,  

Based on my understanding, it will be a safe way to shut down the DC before demotion and remove.  

Before any big changes, remember to back up the DCs. And make sure there are no errors in the output of the following commands:  

Dcdiag /v >c:\dcdiag1.log      

Repadmin /showrepl >C:\repl.txt   

Repadmin /showreps *   

Transfer the FSMO roles correctly, and make the clients use the good one as the DNS servers.  

If there are also other roles installed on the DC which you want to demote and remove, make sure there is a replace server.  

Shut down one server at a time and monitor if there any issues.  

If everything ok, demote it.  

If the other DCs are working well, it will not affect the device in the domain, we don't need to rejoin them to domain.  

Best Regards,
