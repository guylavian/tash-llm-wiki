---
title: "Exchange attachment does not increase"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1048488/exchange-attachment-does-not-increase
question_id: 1048488
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange attachment does not increase

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1048488/exchange-attachment-does-not-increase (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to increase attachment size in exchange 2016, but no matter what i do its restricted.

I'm only doing local mail, not internet, so i don't think Send Connector limit would apply, as its only internal user-to-user

However, the receive connector can only go up to 100MB while the mailbox user is "Unlimited" 'This quota is unlimited' (which i have set)

Is there a way to actually send higher than 100Mb attachment ?

this is what i have when i do cmdlet:

[PS] C:\Windows\system32>get-transportconfig | ft maxsendsize, maxreceivesize

MaxSendSize MaxReceiveSize

Unlimited Unlimited

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-18*

Hi @dss ds   ,    

    

There are many factors that limit the size of an email, also as shown above, not all parameters are unlimited. The maximum valid value of "-MaxSendSize" and "-MaxReceiveSize" is 1.99G, and we also need to consider the 33% increase of mail size, so the actual maximum is only about 1.5G.    

You could refer to the document:    

https://learn.microsoft.com/en-us/powershell/module/exchange/set-transportconfig?view=exchange-ps    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-17*

attachment size is for  testing purposes only, not for legitimate use    

What would be the point of the word "unlimited" if it would ignore them?  Also, you mentioned itr would juse "other limits"    

What other limits if ALL are set to Unlimited?    

eg.     

Organization Transport Settings    

Max. Receive size : Unlimited    

Max. Send Size: Unlimited    

Mailbox user quote: Unlimited for all three options    

Receive connectors    

All are limited to 2047MB... The only one can go further is Send Connector which is irrelevant for me, as this is not communicating with Internet, only local..    

If so, again the question is still valid,, what's  the "Unlimited" option for then? And in what specific circumstances would it be used?    

I also followed this https://www.alitajran.com/attachment-size-limit-exchange-server/#h-change-attachment-size-limit-exchange-2016    

Apart from the specified settings of MaxSend and MaxReceive 200MB and 200MB for both, that seems to be the only way    

i.e if I wanted to send/receive a large PDF attachment, 2Gig, i'd need to issue:     

Set-TransportConfig -MaxSendSize 2000MB -MaxReceiveSize 2000M ??

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-17*

Hi @dss ds   ,    

Agree with Andy, do you have a need to send oversized attachments? Apart from changing the server limits, you need to also account for the client-based ones. You could refer to this similar case:    

https://learn.microsoft.com/en-us/answers/questions/619936/increase-the-attachment39s-size-in-exchange-2016.html    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
