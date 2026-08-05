---
title: "Activesync Issues Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1325236/activesync-issues-exchange-2016
question_id: 1325236
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Activesync Issues Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1325236/activesync-issues-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi guys.

I have Exchange Server 2016, with ActiveSync enabled.

Through Outlook on PC and through OWA, everything works perfectly.

If I go into my account via outlook app on android, it syncs the emails, there are all incoming and they come in, but I can't send the email, it comes back with an error:

"EasSendFailedPermanentException: An EAS Send command failed: The EAS command failed with Status MailSubmissionFailed, Code ='120' and HttpStatus OK. --> The EAS command failed with Status MailSubmissionFailed, Code ='120' and HttpStatus OK. Failure code: da97".

Who can help with the problem?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-07-11*

still persisting the same problem

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-07-11*

Not Solved the proble,

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-07-05*

Hello

Welcome to Microsoft QnA!

First please try the Poweshell

Test-ActiveSyncConnectivity

https://learn.microsoft.com/en-us/powershell/module/exchange/test-activesyncconnectivity?view=exchange-ps

If everything checks out then 

Try another Device

Update the App 

Apply all latest Updates to the Exchange Servers

Research this link

https://support.microsoft.com/en-us/topic/current-issues-with-microsoft-exchange-activesync-and-third-party-devices-53a1ffbe-504c-a424-012a-cb4456e94ba9

It has a lot of details , scroll down there is a mention 

Issue 2.12 - Android device cannot synchronize with Exchange

After the ActiveSync profile is configured, the device receives new items for an undetermined time and then stops updating.  

Cause  

The ActiveSync mailbox policy has a refresh policy defined. The device receives a response with status 143 - Error:PolicyRefresh. The device does not send a provision command as needed.  

IIS log example:

```
Cmd=Sync&User=contoso%5Ce15&DeviceId=android1362622918557&DeviceType=Android&Log=PrxFrom:10.0.1.151_
V141_HH:mail.contoso.com_SmtpAdrs:e15%40contoso.com_NMS1_Fet78_TmTr:TID%3a18%3e%3e%5bID%3aH%5FEPR%2c
Start%3a2%3a40%3a30+PM%2cEnd%3a2%3a40%3a30+PM%2cExcl%3a0+ms%2cChild%3a%5bNONE%5d%2c%5dTID%3a50%3e%3e
%5bID%3aH%5FBPR%2cStart%3a2%3a40%3a30+PM%2cEnd%3a2%3a40%3a30+PM%2cExcl%3a15+ms%2cChild%3a%5bID%3aH%5
FRMBP%2cStart%3a2%3a40%3a30+PM%2cEnd%3a2%3a40%3a30+PM%2cExcl%3a0+ms%2cChild%3a%5bNONE%5d%2c%5d%2c%5d
_Pk3609689902_DevOS:Android+4.1.2_S143_Error:PolicyRefresh_As:AllowedG_Mbx:CLT-E15-MBX1.contoso.local
_Throttle0
```

Solution  

Set the refresh interval for the ActiveSync mailbox policy to Unlimited.

Send us your feedback and more details like what Device is this , Android , iOS , etc

Any recent changes in your config ?

Do you have Hybrid Exchange ?

I hope this helps!

Kindly mark the answer as Accepted and Upvote in case it helped!

Regards
