---
title: "Extend on premises Active Directory domain to Azure using virtual machines."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/238849/extend-on-premises-active-directory-domain-to-azur
question_id: 238849
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Extend on premises Active Directory domain to Azure using virtual machines.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/238849/extend-on-premises-active-directory-domain-to-azur (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I am not sure if this is the right place to ask.  

We are looking to extend our on premises Active Directory domain into Azure. I know there are some replication services available, but I am particularly interested in running our own 2016 Azure server which we then run DCPROMO on to become a domain controller.  

I know we will need to use AD sites and services to separate out the various subnets so clients know which DC is closest, but cannot find much else about what we need to do?  

In particular, what ports need to be allowed from our on premises clients to our cloud based domain controllers in the event of an on premises domain controller being unavailable?  

Do we need to allow all traffic from our on premises networks to reach our Azure based AD servers, or etc?  

I have tried a couple of posts in a couple of forums and reading various articles, but not many cover this type of scenario.  

Any help or advice people can provide would be greatly appreciated.  

Kind regards,  

Luke

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-21*

Hello anonymous userC-0496,    

Thank you for posting here.    

Here are the answers for your references.    

Q1:I know we will need to use AD sites and services to separate out the various subnets so clients know which DC is closest, but cannot find much else about what we need to do?    

A1:If we promote a DC, we will select a site for this DC to put this DC.    

The subnet is linked to one specific site (site1), if one client belongs to this subnet, then the client will select one DC in this site1 to authenticate.    

Only if the DCs in this site1 are unavailable, this client will find DC in other sites to authenticate.    

For more information about site, subnet and client, we can refer to the links below (especially the first link, it is a good article to read).    

Using Catch-All Subnets in Active Directory    

https://learn.microsoft.com/en-us/previous-versions/technet-magazine/dd797576(v=msdn.10)?redirectedfrom=MSDN    

How to Create an Active Directory Subnet/Site with /32 or /128 and Why    

https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/how-to-create-an-active-directory-subnet-site-with-32-or-128-and/ba-p/256105    

Q2:In particular, what ports need to be allowed from our on premises clients to our cloud based domain controllers in the event of an on premises domain controller being unavailable?    

A2:For port requirements in on premises AD, we can refer to the following links.    

Active Directory and Active Directory Domain Services Port Requirements    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd772723(v=ws.10)?redirectedfrom=MSDN    

Active Directory Replication over Firewalls    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/bb727063(v=technet.10)?redirectedfrom=MSDN    

Q3:Do we need to allow all traffic from our on premises networks to reach our Azure based AD servers, or etc?    

Q3:See A2.    

Hope the information above is helpful. If anything is unclear, please feel free to let us know.    

Best Regards,    

Daisy Zhou
