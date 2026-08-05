---
title: "exchange srv record ISP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/120268/exchange-srv-record-isp
question_id: 120268
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# exchange srv record ISP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/120268/exchange-srv-record-isp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

dears,  

i have an exchange server configured. the public certificate is purchased with just one san :mail.domain.com.  

autodiscover.domain.com isnt included in the SANs  

externally, autodiscover is published via SRV record and it is working fine  

i have 2 questions please:  

-  if i publish autodiscover with cname record will it work with warnings? because isnt included in the certificate or autodiscover won't even be working  

-  my records are being published now on ISP1 and autodiscover is working with srv record like i previously mentionned, my issue is when im switching my records to ISP2 (goddaddy) all my domain records mx,srv... autodiscover stops working. can you advise ? why it is working on isp1 and not on isp2. what could be the issue  

thank you in advance

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2020-10-08*

Hi,    

Please find the below suggestions,    

-  Yes, it will work with CNAME since mail.domain.com is in the certificate    

Refer Step 4 in this article https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/configure-mail-flow-and-client-access?view=exchserver-2019    

-  I would suggest to check with ISP support for this because it could be an issue with DNS replication/record syntax/Nameservers, etc

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-09*

Hi @eg1995  ,    

Regarding the 2 questions listed in your original post, agree with the suggestions provided above by @Ashok M  .     

As per your new concern about using the same certificate for a new domain, yes, that would work with CNAME or SRV record. To add to what AshokM-8240 mentioned, here is an official blog with the configuration steps to add a CNAME record for new domain:    

Exchange 2007 AutoDiscover and Multi-Tenant Hosting    

    

That was an old blog so the SRV record method wasn't covered, but as stated earlier, SRV record is also a solution. Here is an article for your reference:    

Autodiscover for multiple domain without changing single SSL cert    

    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-08*

thank you for your continuous support.  

lets rake this scenario: just mail.domain1.com included in san and autodiscover is published externally pointing to mail.domain1.com.  

lets say i added a new domain domain2, as i wont wanna include autodiscover names in the certficate. will i be able to make autod work on the second domainn if i publish it externally as an srv record pointing to autodiscover.domain1.com??  

will it work if i publish it as cname? like aut.domain2.com pointing to auto.domain1.com?  

thank you again
