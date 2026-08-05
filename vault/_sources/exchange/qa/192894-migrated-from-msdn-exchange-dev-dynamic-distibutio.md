---
title: "[Migrated from MSDN Exchange Dev] Dynamic Distibution Group: Outlook - No information how many recipients are reached with this Mail"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/192894/migrated-from-msdn-exchange-dev-dynamic-distibutio
question_id: 192894
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# [Migrated from MSDN Exchange Dev] Dynamic Distibution Group: Outlook - No information how many recipients are reached with this Mail

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/192894/migrated-from-msdn-exchange-dev-dynamic-distibutio (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.  

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/ae2b7b89-7a64-4143-9cec-c5b215e7564f/dynamic-distibution-group-outlook-no-information-how-many-recipients-are-reached-with-this-mail?forum=exchangesvrdevelopment   

Hi,  

I have created several dynamic distribution groups : Exchange 2016 (Cu18) The distribution groups contains all recipients of an OU in the Active Directory This wasn't a problem. I can also use the Powershell command to display the individual members.  

Rather, the problem starts in Outlook (2010). In the case of certain dynamic distribution groups:  

When the distribution group is in Outlook selected, the number of recipients, who will receive the message, is not displayed automatically.  

In other cases, Outlook shows me exactly how many recipients are reached.  

If i create the dynamic distribution group with a new name, the error/fault is repeated.  

Hope , anyone can help  

Christof  

Mailtips are enabled  

MailTipsAllTipsEnabled                : True  

MailTipsExternalRecipientsTipsEnabled : False  

MailTipsGroupMetricsEnabled           : True  

MailTipsLargeAudienceThreshold        : 25  

MailTipsMailboxSourcedTipsEnabled     : True

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-12-10*

Does this occur with one specific dynamic distribution group?    

How many recipients are included in this dynamic distribution group?    

In general, when the number of the group members is larger than the configured large audience size (the default size is more than 25 members), the MailTip will show the recipient number. You can use the following command to configures the large audience size:    

```
Set-OrganizationConfig -MailTipsLargeAudienceThreshold 
```

For Outlook 2010, please make sure you install the latest Office service pack and the latest public update. Please check with OWA as well. You also can try Outlook 2019 to see if the issue can be reproduced.     

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
