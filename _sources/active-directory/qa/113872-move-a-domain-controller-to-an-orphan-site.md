---
title: "Move a Domain Controller to an Orphan Site."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/113872/move-a-domain-controller-to-an-orphan-site
question_id: 113872
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Move a Domain Controller to an Orphan Site.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/113872/move-a-domain-controller-to-an-orphan-site (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

I have an environment where I have two sites one in India and another in China. I have Domain Controllers under each site that are communicating among themselves. If I demote one of the servers, it will disturb the communication among the other DC's as well. I want to move one of DC's from one of the sites to an orphan site to cut off the traffic coming into that DC. Can this be done and will this disturb the communication among the DC's?  

How do I move the DC to the orphan site?  

Thanks

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-05*

Now the question is, If I do so, then will it cut off the traffic coming in to that DC?  

This is more a networking question. As long as there's no route between the two there will be no communications.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-10-05*

Hi,    

For Moving a Domain Controller to a Different Site    

You can refer to the following procedures in order:    

Chane the static IP address of a domain controller    

Create a delegation for a domain controller    

If the parent DNS zone of any zone that is hosted by this DNS server contains a delegation to this DNS server, use this procedure to update the IP address in all such delegations.    

If your forest root domain has a parent DNS domain, perform this procedure on a DNS server in the parent domain. If you just added a new domain controller to a child domain, perform this procedure on a DNS server in the DNS parent domain. By following recommended practices, the parent domain is the forest root domain.    

Verify that an IP address maps to a subnet and determine the site association    

Determine whether the server is a preferred bridgehead server    

Configure the server to not be a preferred bridgehead server    

Move the Server object to the new site.    

For more details you can refer to :https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc739015(v=ws.10)?redirectedfrom=MSDN    

Then when moved the DC successfully, you can cut down the traffic between from the new sites to other sites.(Make sure that the DC was acted as a DNS server also, or if you but down the traffic, the name resolution will not work.)    

Active Directory Replication over Firewalls

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-10-02*

Hi,  

Welcome to post here!  

To know the questions more clearly, would you please tell more information following, if i misunderstand you ,please feel free to let me know:  

All the DCs from one site(India) can communicate with DCs from the other site (China),right?   

All the DCs within the same sites can communicates with each other, right?  

When you said "move one of DC's from one of the sites to an orphan site to cut off the traffic coming into that DC", do you mean you want to create a new site ,and move one of the DCs into it?Or you just want to cut off the traffic coming into that DC?  

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-01*

If I demote one of the servers, it will disturb the communication among the other DC's as well    

What is meant here?    

I want to move one of DC's from one of the sites to an orphan site to cut off the traffic coming into that DC    

If this will be permanent the you can perform cleanup to remove the DC from active directory.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

--please don't forget to Accept as answer if the reply is helpful--
