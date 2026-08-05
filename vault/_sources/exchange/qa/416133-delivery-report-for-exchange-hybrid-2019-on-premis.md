---
title: "Delivery Report for Exchange Hybrid 2019 ( On Premise )"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/416133/delivery-report-for-exchange-hybrid-2019-on-premis
question_id: 416133
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Delivery Report for Exchange Hybrid 2019 ( On Premise )

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/416133/delivery-report-for-exchange-hybrid-2019-on-premis (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Greetings all,  

anyone have any idea why my Exchange Server 2019 ( hybrid ) can't see or find message track log from office 365.  

The situation when i try to press "Search" on premise.   

"object reference not set to an instance of an object"  

we need to validate is it the email already deliver or not to our on premise account.   

( since my message trace from 365 said it's delivered but the user from on premise did not receive it )  

If it's anomaly, how to fix the problem regarding the situation.  

Thanks before,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-02*

Thanks Kyle,  

will do with your solution for now,   

so right now my best options using Exchange Powershell

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-02*

Thanks for the reply Andy & Kyle,  

if i'm using exchange powershell console in on premise, i can trace the log clearly. the problem is when i'm trying using GUI Web. is it the feature of exchange that disallowed to search delivery report from 365 sender ( hybrid in this position )  

if it so, can someone give me the reference. so at least there is no dispute regarding the function of exchange 2019 on premise.  

Regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-01*

@Natanael Sigit       

Do you mean that you cannot send email from Exchange online to Exchange 2019 mailbox?    

I would suggest you provide the result of command below to us:    

Connect to Exchange online and run command below:    

```
Get-MessageTrace -SenderAddress "******@contoso.com" -RecipientAddress "******@domain.com" -StartDate 05/30/2021 -EndDate 06/1/2021
```

Open Exchange 2019 EMS and run command below:    

```
Get-MessageTrackingLog -Start 05/30/2021 -End "06/1/2021" -Sender "******@domain.com" -Recipients "******@domain.com"
```

I also want to confirm with you, whether all Exchange online mailboxes cannot sent email to Exchange on-premises mailboxes?    

Do you receive any NDR about this email?       

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-31*

Are you using Exchange Powershell on-prem?     

Thats what you need to do     

https://learn.microsoft.com/en-us/exchange/mail-flow/transport-logs/search-message-tracking-logs?view=exchserver-2019
