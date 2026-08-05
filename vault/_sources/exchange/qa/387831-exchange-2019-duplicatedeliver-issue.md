---
title: "Exchange 2019 DUPLICATEDELIVER issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/387831/exchange-2019-duplicatedeliver-issue
question_id: 387831
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 DUPLICATEDELIVER issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/387831/exchange-2019-duplicatedeliver-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an Exchange 2019 2 node DAG with a Barracuda Security gateway catching all inbound SMTP traffic.  The Barracuda gateway has a feature that allows me to redelivery any email message, but the message is not making it to the Inbox.   

After running Get-MessageTrackingLog on my mailbox, I see that the message is being blocked because of a DUPLICATEDELIVER.  After a little googling, I see that there should be a default time limit of one hour, but that does not seem to be in play.  I have tried to redeliver messages from the prior week without success.  

My question is, where would I find the DUPLICATEDELIVER time setting?  All my Google search came back with Exchange 2007 and 2010, but nothing for 2019.  Also, could there be something else in play here that I am not seeing?  

Thank you,  

Michael

## Answer (community) — community member

*upvotes: 1 · updated: 2021-05-26*

Hi Lou,  

I have seen that article also and tried their recommendation, but they didn't work.  I think I am going to hunt this one for now.  

Thanks again for your help.  

Michael

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-14*

Hello Lou,   

Thanks for your response.   

I have reviewed the article that you provide in the first paragraph, but it is the same article that I was talking about that refers to Exchange 2007 and not 2019.  I did go ahead and make the registry entries as it suggests, but they did not change the duplicate message detection from 7 days to 1 hour.   

You are correct that the issue is with the DUPLICATEDELIVER settings because I was able to re-deliver the message from the gateway after seven days.     

How do we change this to one hour on Exchange 2019?    

Thank you again,   

Michael

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-10*

Hi @Anonymous   ,    

If you want to change the settings, you could see this doc: https://learn.microsoft.com/en-us/previous-versions/office/exchange-server-2007/dd577073(v=exchg.80)?redirectedfrom=MSDN    

Based on my knowledge, I think the DUPLICATEDELIVER event could be occur when the messages are transporting thought the gateway.    

As you said you failed to redeliver a prior week message, and as I know the duplicate message detection is by default 7 days. I think you could remove the gateway to test if the mail could send without any errors.    

    

Also test the internal mail flow to see if they could pass the gateway and delivered successfully.     

If you could, please tell me about the MessageTrackingLog details, if there are any Failed events, use | FL to check it.    

    

```
Get-MessageTrackingLog -MessageSubject "Subject" | Ft TimeStamp,EventId,Source,MessageSubject
```

If you removed the gateway and the mail flow becomes good, you should check the settings of Barracuda or you may get help from their support engineers.     

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
