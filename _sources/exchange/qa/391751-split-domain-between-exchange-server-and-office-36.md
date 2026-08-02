---
title: "Split domain between Exchange Server and Office 365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/391751/split-domain-between-exchange-server-and-office-36
question_id: 391751
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Split domain between Exchange Server and Office 365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/391751/split-domain-between-exchange-server-and-office-36 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

Good Day!  

May I ask how can I configure the split domain between Exchange Server 2013 and Office 365? Because we will upgrade from Exchange Server 2013 to Exchange Server 2019 and we will upgrade also the AD before configuring the Hybrid Setup.  

How can I setup the mail flow while waiting the upgrading of AD is to be done before doing the Hybrid Setup?  

Thanks,  

Raymond

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-19*

Hi anonymous user ,    

Do you means that you want to upgrade on-premises Exchange in Hybrid environment from Exchange 2013 to Exchange 2019?    

I found some articles that guide the process, you can refer to them, although the articles cover Exchange 2010 to Exchange 2016. But the process is similar for Exchange 2013 to Exchange 2019.    

Please refer to: Hybrid Exchange 2010 To Hybrid Exchange 2016 - Part One and Step-by-Step: How to upgrade a Legacy Hybrid Exchange Server to 2016    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-18*

Hi Lucas,  

Good Day!  

I have one domain that will configure in Exchange Server 2019 and Office 365.  

We have environment of Hybrid Setup of Office 365 and Exchange Server 2013. We will upgrading the Exchange Server 2013 to Exchange Server 2019. Before upgrading we will cut the Hybrid Setup and disable the AD Connect.  

Or do you have an idea how can we perform the upgrade from Exchange Server 2013 with Hybrid Setup to Exchange Server 2019.  

Thanks,  

Raymond
