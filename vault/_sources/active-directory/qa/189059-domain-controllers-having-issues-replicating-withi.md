---
title: "Domain Controllers having issues replicating within only one specific region"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/189059/domain-controllers-having-issues-replicating-withi
question_id: 189059
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controllers having issues replicating within only one specific region

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/189059/domain-controllers-having-issues-replicating-withi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I am taking over managing the AD for our team. The previous individual that was responsible for this has moved and is no longer reachable. We use several regions in AWS, and have basic services on each region such as AD Domain Controller, mail services, projects, etc. Last week I spun up a new Windows Server 2019 machine on each region, and set each up as a Domain Controller. The plan was to take town the old 2016 DC servers once the new 2019 machines are up and running. They all worked fine, except for one single region. Upon inspection, it would appear the old 2016 DC in this same region was never working right to begin with when it was setup by a previous member a few years ago. This region isn't used for much which is why this was never spotted until now.  

Within the broken region, both Domain Controllers, on 2016 and 2019 can communicate with each other just fine. If I create a new server within that region, and join it to the domain, it says it joined to the domain, but it will only appear on those two Domain Controllers. I can not replicate this in any other region.  

When running repadmin /replsummary on the new 2019 DC, it shows all success except for two servers, which are the main two domain controllers located physically in the office. The error message is "experienced the following operational errors trying to retrieve replication information". These both have error code 58. The DNS on the DCs in the broken region are the IPs of those two machines, the same setup as every other region.  

The firewall has been updated, and temporarily opens all communication between all internal resources. I can confirm traffic is going through this rule, so there should be nothing on the network firewall preventing access. Is there something on the Windows Firewall itself that needs to be updated, or added, even though no other region did?  

I have alot of information I can share, but I am not sure what would be most beneficial. I am fairly new to AD, and this has been a learning experience for me. Please let me know what other information would be useful to share. I have been in contact with Microsoft Support, but it has been more then one week and have only been told that they are looking into it and will get back to me soon. After a week of the same messages I am loosing hope that they will help resolve this. I would greatly appreciate anyone's help in trying to resolve this.

## Answer (community) — community member

*upvotes: 1 · updated: 2020-12-14*

Hi,  

Welcome to share your current situation if there are any updates.  

Please feel free to let us know if you need further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2020-12-07*

likely been going on since this region was created a few years ago  

Try standing up a new one but be sure to use another active healthy domain controller for DNS on connection properties.  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2020-12-07*

I spun up a new Windows Server 2019 machine  

How long has the problem been going on? Has tombstone expired? Might try standing up a new one but be sure to use another active healthy domain controller for DNS on connection properties.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2020-12-07*

I'd check the required ports are flowing between sites.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts    

https://www.microsoft.com/en-us/download/details.aspx?id=24009    

also check the event logs for errors since last boot.    

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-07*

Sounds like the site has no connectivity. You can also start a case here with product support.  

https://support.serviceshub.microsoft.com/supportforbusiness  

--please don't forget to `Accept as answer` if the reply is helpful--
