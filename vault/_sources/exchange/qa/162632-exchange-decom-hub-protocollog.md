---
title: "Exchange DECOM (Hub ProtocolLog)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/162632/exchange-decom-hub-protocollog
question_id: 162632
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Exchange DECOM (Hub ProtocolLog)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/162632/exchange-decom-hub-protocollog (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good afternoon,  

Going through a DECOM process for the old Exchange environment (sing ORG sing DAG) after completing a migration.  Question is... I'm seeing nothing as far as queue is concerned or Frontend Protocol logs, but in the Hub ProtocolLog I'm seeing activity related to mail flow even though 100% of the mailboxes on the old Exchange servers have been migrated successfully.    

Is this something that needs to be addressed prior to powering off these servers for a few days to make sure everything is accounted for before powering them back on to perform the Database dismounts and Exchange uninstall?  Any feedback on this would be great.  Just checking to see if there is some ghost I have not tracked down.  

Thanks,  

CWT

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-13*

I like your idea as I will run with that. Here is a log example from the Hub ProtocolLog SMTP Receive:

10.10.10.10 = OLD Exchange server  

30.30.30.30 = NEW Exchange server

2020-11-13T21:01:15.079Z,OLDEXCHANGE\Default OLDEXCHANGE,08C8881116H56738,172,10.10.10.10:2525,30.30.30.30:22855,>,250 XProxyFrom accepted,  

2020-11-13T21:01:15.080Z,OLDEXCHANGE\Default OLDEXCHANGE,08C8881116H56738,173,10.10.10.10:2525,30.30.30.30:22855,<,MAIL FROM:<control@keyman  .com> SIZE=0 AUTH=<> XMESSAGEVALUE=MediumHigh,  

2020-11-13T21:01:15.080Z,OLDEXCHANGE\Default OLDEXCHANGE,08C8881116H56738,174,10.10.10.10:2525,30.30.30.30:22855,,08C8881116H56738;2020-11-13T20:57:34.926Z;13,receiving message  

2020-11-13T21:01:15.081Z,OLDEXCHANGE\Default OLDEXCHANGE,08C8881116H56738,175,10.10.10.10:2525,30.30.30.30:22855,<,RCPT TO:<@damericz.com>,  

2020-11-13T21:01:15.081Z,OLDEXCHANGE\Default OLDEXCHANGE,08C8881116H56738,176,10.10.10.10:2525,30.30.30.30:22855,>,250 2.1.0 Sender OK,  

2020-11-13T21:01:15.081Z,OLDEXCHANGE\Default OLDEXCHANGE,08C8881116H56738,177,10.10.10.10:2525,30.30.30.30:22855,>,250 2.1.5 Recipient OK,  

2020-11-13T21:01:15.082Z,OLDEXCHANGE\Default OLDEXCHANGE,08C8881116H56738,178,10.10.10.10:2525,30.30.30.30:22855,<,DATA,  

2020-11-13T21:01:15.083Z,OLDEXCHANGE\Default OLDEXCHANGE,08C8881116H56738,179,10.10.10.10:2525,30.30.30.30:22855,>,354 Start mail input; end with <CRLF>.<CRLF>,  

2020-11-13T21:01:15.085Z,OLDEXCHANGE\Default OLDEXCHANGE,08C8881116H56738,180,10.10.10.10:2525,30.30.30.30:22855,,,receiving message with InternetMessageId <@NEWEXCHANGE.DOMAIN.net>  

2020-11-13T21:01:15.861Z,OLDEXCHANGE\Default OLDEXCHANGE,08C8881116H56738,181,10.10.10.10:2525,30.30.30.30:22855,>,"250 2.6.0 <1d3133bf-c8cb-40d8-b807-6dfcfd0d9e9f@NEWEXCHANGE.DOMAIN> [InternalId=42842298777605, Hostname=OLDEXCHANGE.DOMAIN] 3454 bytes in 0.777, 4.338 KB/sec Queued mail for delivery",

CWT

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-13*

So you would expect to open the Hub>ProtocolLog>SmtpReceive logs and see a lot of mailflow?  I'm seeing SERVER1\Default SERVER1 10.10.10.10:2525 20.20.20.20:51870 with mail from and mail to recipient OK, DATA etc?  This is on a server that has zero mailboxes outside of -monitoring ones.  

Is this normal and is there a way to check?  If I do a messagetracking lookup and see an edge server receiving only from the new Exchange servers is that the best validation?  

Thanks,  

CWT
