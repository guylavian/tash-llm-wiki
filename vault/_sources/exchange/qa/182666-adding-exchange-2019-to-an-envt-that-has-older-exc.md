---
title: "Adding Exchange 2019 to an env't that has older Exchange versions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/182666/adding-exchange-2019-to-an-envt-that-has-older-exc
question_id: 182666
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Adding Exchange 2019 to an env't that has older Exchange versions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/182666/adding-exchange-2019-to-an-envt-that-has-older-exc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a lab environment where there's Exchange 2007 and Exchange 2010 running.  

I'd like to decommission them and add Exchange 2019.  

It'd be nice to be able to add Exchange 2109 while Exchange 2007 and 2010 are running so that I wouldn't need to recreate some of the configurations but it seems Exchange 2019 cannot coexist with them.  

So I'd need to remove Exchange 2007 and 2010 first then add Exchange 2019 correct?  

What would be the best way to decommission Exchange 2007 and 2010 from the domain?    

Mailboxes do not need to be retained.  

Do I simply run the Exchange installer and uninstall Exchange on each Exchange server?  

TIA

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-04*

Thanks guys.  I have a good idea on what to do now.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-03*

Hi anonymous user ,    

You understand that is correct, Exchange 2007 and Exchange 2010 can’t coexist with Exchange 2019. If we want migration Exchange 2007 and Exchange 2010 to Exchange 2019, we need to migration to Exchange 2013 first, then uninstall Exchange 2007 and Exchange 2010, then install Exchange 2019 and migration from Exchange 2013 to Exchange 2019. But this process is very complicated. If the data in Exchange 2007 and Exchange 2010 in your lab environment does not need to be retained, then you can directly uninstall Exchange 2007 and Exchange 2010, and then directly install Exchange 2019.    

About how to remove the Exchange 2007 from Exchange 2010 organization and how to decommissioning the Exchange 2010, you could refer to these articles provide by Microsoft, The articles describes the uninstallation steps in great detail.    

Remove the Last Legacy Exchange Server from an Exchange 2010 Organization    

Best practices when decommissioning Exchange 2010    

In addition, in order to install Exchange 2019 smoothly, please read these articles before installing Exchange 2019 to understand the requirements of Exchange 2019 on the system and prerequisites.    

Exchange 2019 Server system requirements    

Exchange 2019 Server prerequisites    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
