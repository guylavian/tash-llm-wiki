---
title: "Active Directory users authenticate to DR DC for IPC$ share"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/455928/active-directory-users-authenticate-to-dr-dc-for-i
question_id: 455928
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory users authenticate to DR DC for IPC$ share

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/455928/active-directory-users-authenticate-to-dr-dc-for-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, i have seen the authentication requests from Production site users to DR Domain controller to access IPC$ share using SMB. we have already bound the subnets properly but still users from production site is going to DR site Domain controller and access IPC$. is that normal or there is any misconfiguration?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2021-06-30*

Hi,  

If the site and subnet is configured correctly, the users should find the DCs in the same site for authentication. If there are no available DCs,it will find DCs in other site.  

Not sure how did you configure your sites and if there are DCs in every site.  

Also, make sure DCs in the production site are available.  

To get authenticated dc  

nltest /dsgetdc:domainname          

klist query_bind（kerberos authentication）  

You can also test which DCs are nearest to your workstation in your site (copy nltest.exe from the DC to the workstation’s system32 folder):  

nltest /sc_query:YourDomainName.com  

To find the GC your workstation used (copy nltest.exe from the DC to the workstation’s system32 folder):  

nltest /dgsgetdc:your_domain_name.com /GC  

More information about the The DC Locator Process, you can refer to the following link:  

https://servergurunow.wordpress.com/2017/10/14/dc-locator-process-2/  

https://servergurunow.wordpress.com/2017/10/14/dc-locator-process-2/  

Best Regards,
