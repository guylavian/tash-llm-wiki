---
title: "Out of Office messages drop in exchange online O365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/176723/out-of-office-messages-drop-in-exchange-online-o36
question_id: 176723
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator", "Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Out of Office messages drop in exchange online O365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/176723/out-of-office-messages-drop-in-exchange-online-o36 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Greetings    

I have a hybrid exchange environment but used for migration modern/minimal method of migration.    

All is good all users are using cloud exchange no one is using on perm but server is still up and running.    

3 days ago we noticed that OOF messages are failing. and I found all of them have similar picture    

Here text copied from message trace box     

Nov 26, 2020 3:56:03 AM    

Receive    

Message received by: CO6PR14MB4402.namprd14.prod.outlook.com    

Nov 26, 2020 3:56:03 AM    

Submit    

The message was submitted.    

Nov 26, 2020 3:56:03 AM    

Receive    

Message received by: MWHPR14MB1808.namprd14.prod.outlook.com using TLS1.2 with AES256    

Nov 26, 2020 3:56:04 AM    

Drop    

Reason: [{LED=250 2.1.5 RESOLVER.OOF.IntToExt; handled internal OOF addressed to external recipient};{MSG=};{FQDN=};{IP=};{LRT=}]    

Nov 26, 2020 3:56:04 AM    

Drop    

Reason: [{LED=250 2.1.5 RESOLVER.OOF.IntToExt    

    

Could you please advice where I should look solution I have tried different scenarios and currently setup is like this:    

Allow external and legacy out of office replies are set on Default domain.    

Thanks in advance.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 4 · updated: 2020-12-02*

Whoa! I thought the external recipient was not getting the OOF?     

What you are seeing in the message logs is normal. Its dropping the internal one because, well, its internal.     

Here is message tracking from a test OOF i just sent to internal and external recipients    

The internal OOF will be dropped and prevented from going External.    

    

The External OOF should show delivered.    

In other words, there are two message tracking  entries. One for the internal that failed and one for the external that is delivered.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2020-11-26*

Curious if this applies:    

https://learn.microsoft.com/en-us/exchange/troubleshoot/send-emails/understand-troubleshoot-oof-replies#remote-domain-blocks-oof-replies    

```
Get-RemoteDomain | ft -AutoSize Name, DomainName, AutoReplyEnabled
```

If the value of the setting is false, no automatic replies will be sent to users in that domain. This setting takes precedence over the automatic replies that are set up at the mailbox level or over the OOF type (as discussed earlier). Keep in mind that false is the default value for new remote domains that you create and also for the built-in remote domain named "Default" in Exchange Online.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-01*

Hi @Mikayel Mikayelyan  ,    

3 days ago we noticed that OOF messages are failing.     

So do you mean it has been working fine previously? If this is the case, have you made any changes to your environment right before the issue started?    

Does this affect other external domains aside from gmail.com?    

I just checked in my test tenant and the oof message can arrive at the gmail.com account properly. The Default domain's settings related to OOF are exactly the same as the screenshot shared by Andy:    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-27*
