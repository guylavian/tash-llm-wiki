---
title: "AD and Exchange upgradation with legacy Office 2010"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/413727/ad-and-exchange-upgradation-with-legacy-office-201
question_id: 413727
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# AD and Exchange upgradation with legacy Office 2010

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/413727/ad-and-exchange-upgradation-with-legacy-office-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a query regarding the up-gradation of the Domain and Exchange server. Following is the scenario.  

Primary site = AD 2012 R2 Primary Domain (migrate to 2019 DC)  

                          Exchange 2013 with DAG (migrate to 2019 with DAG)

Branch Office = AD 2012 R2 Child Domain  

                            Exchange 2013 with DAG

DR Site  = AD 2012 R2 Additional Domain Controller (ADC)  (migrate to 2019 ADC)  

                  Exchange 2012 R2 with Primary Site (migrate 2019 with Primary Site)

The query is that one of their executives in Branch Office is using Office 2010 where they have some automation script/software installed with Outlook 2010 which is no longer supports the new version of Office.  

If we upgrade/migrate primary and DR AD 2012 R2 and Exchange 2013 to AD 2019 and Exchange 2019, users in the child domain can still use the existing AD and Exchange and their Office 2010 version without any changes and will not affect their emails as primary and DR site is upgraded.  

Please suggest

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-31*

Hi,     

You can use Outlook 2010 on Exchange 2019 as usual but in Microsoft doc it's not supported:    

    

So I'm not sure all functions will be available.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
