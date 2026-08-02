---
title: "Exchange 2019 Onprem - Accepting external email sent to olddomain.com for newdomain.com"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1034062/exchange-2019-onprem-accepting-external-email-sent
question_id: 1034062
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2019 Onprem - Accepting external email sent to olddomain.com for newdomain.com

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1034062/exchange-2019-onprem-accepting-external-email-sent (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I'm having trouble setting up what is essentially a domain alias so that my new Exchange server can receive mail for addresses from my old domain.    

I am trying to send mail to olddomain.com but allow Exchange at newdomain.com to receive it and deliver it to specific users with aliased secondary SMTP addresses. I have my MX records for olddomain.com pointing to newdomain.com and a distribution group with @olddomain.com as an additional entry under the "email addresses" menu. I am a member of this group. This alias works great internally (@newdomain.com can email ******@olddomain.com and it delivers), but when an email comes to ******@olddomain.com from the internet it is not delivering. It does not make it past the Transport server.    

I can see in my Exchange transport server log (MessageTracking logs) that the email is hitting, so my MX records are working, but the Transport server is just not delivering it to the Mailbox server. I don't see anything in this log that indicates that it is being rejected, but not showing up in my inbox.    

I have olddomain.com specified in ECP on the Mailbox server as Authoritative and my distribution group allows external senders. Not sure what else I am missing here since it works internally if I email ******@olddomain.com from another internal user's email. Do I need to change something on the Transport server itself? Receive and send connector mis-configuration? I am stumped.    

Thanks

## Answer (community) — community member

*upvotes: 1 · updated: 2022-10-05*

@Michael L      

I would suggest you try to add the old domain name to one of your mailbox rather than distribution group, then send emails to this mailbox from the Internet. It could help us check whether the MX created correctly.    

Exchange distribution group will not receive email from the Internet by default, you need to set the "-RequireSenderAuthenticationEnabled" to false for this distribution group.    

```
Set-DistributionGroup -Identity groupname -RequireSenderAuthenticationEnabled $false
```

If you still cannot send emails to this group from external mailbox, whether this external mailbox receive NDR?    

I also suggest you provided information about command below:    

```
Get-TransportService | Get-MessageTrackingLog -Sender ******@externaldomain.com -Recipients ******@domain.com -MessageSubject "subject" -Start 10/04/2022 -End 10/06/2022
```

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
