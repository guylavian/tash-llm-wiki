---
title: "ATP on Exchange 2016 / Windows 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/396811/atp-on-exchange-2016-windows-2016
question_id: 396811
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# ATP on Exchange 2016 / Windows 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/396811/atp-on-exchange-2016-windows-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

we recently deployed ATP on our servers and this message is making me nervous: An actor on SERVER sent a suspicious LDAP query, searching for PasswordNotRequired on FQDN DOMAIN.   

We checked server for potential malicious code with different antivirus than Defender but no issue found.  Is there anybody else with similar ALERT ? Could it be that Exchange 2016 CU 19 is querying for such accounts (we do not have one in our domain) ?  

thank you !

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-26*

Hello Lucas,   

well, as I could not manage traffic capture, I decided to remove ATP from EXCH and replace it with 3rd party product  

Thank you for your support, feel free to archive / close this topic.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-20*

Hi @Peter Behrik   ,  

In order to protect the user information, did you run the above command line?

Many communications between AD and Exchange server will use LDAP. And based on the error message, we can only know the time and warning when it happened, we can’t know who caused the warning and what caused the warning. So we need to collect more related information.

1.Please check the event viewer, check are there any related warnings or error logs generated during the time period when the error occurred? You could also check the MSExchange Management in the event viewer.  

2.By grabbing network packets, you can check whether there are related requests sent between AD and Exchange server when the alter appears. So this is also a way to consider.

In addition, are third-party tools such as anti-virus software running in your environment? If possible, please disable them temporarily and check if the warning appears.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-19*

HI,    

well, can you advice as to provide you more details ?    

I can see that alert page refers that this is still happening.    

as it is exchange server, I would be afraid to do network capture on, any other options as it is still active ...

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-17*

Hi @Peter Behrik   ,    

Could you share more information about this message with us? Such as "Times and time frame of the suspicious activities.", "Severity of the suspicious activity, High, Medium, or Low.",etc.    

This message shows that it is searching for objects of "PasswordNotRequired" in the Domain. Based on this message alone, we cannot determine who sent the query request. All mailboxes created in Exchange have passwords.     

In order to prevent other objects from receiving threats, you could run the following command line in the powershell of the DC server to check that the "PasswordNotRequired" of those objects is set to "True". If it is an important object, please run the second command line below to set it to "False".    

```
Get-ADUser -Filter {PasswordNotRequired -eq $true}  
  
Set-ADUser -Indetity "" -PasswordNotRequired $false
```

In addition, have you run the LDAP scanning tool?     

Please refer to: Active Directory attributes reconnaissance (LDAP) (external ID 2210)    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
