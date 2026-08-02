---
title: "Exchange Logs Help"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1143569/exchange-logs-help
question_id: 1143569
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Logs Help

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1143569/exchange-logs-help (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I need some help deciphering the Exchange transport logs. I have several logs that look roughly the same as the ones below, except that the external WAN differs, about 100-200 per day, intermittently in bursts. I am not sure if it's back scatter or probes for open relay. What's puzzling is that the source is the internal Exchange server's IP address, so I believe it may be the server trying to send out an NDR if it's back scatter OR possibly the servers reply to the sender being denied by our UTM firewall's block list.    

The alerts are driving my SOC admin crazy. I cannot black list the WAN IPs they are too many. We have no open relay, SPF -all and ESET security for Exchange. If I can figure out exactly what they are, I can try to block them at the edge without changing the alert monitoring levels.    

The red squares indicate where our local Exchange server IP is. Since the local IP is before the remote WAN IP, I'm thinking EXCH is the source, or is it backwards somehow?    

    

    

Thanks

## Answer (community) — community member

*upvotes: 1 · updated: 2022-12-28*

Hi @Falcon IT Services  ,    

From your screenshot, the Exchange Front End Transport service is receiving e-mail messages.    

By default, the default Receive connector named Default Frontend <ServerName> in the Front End Transport service enables protocol logging.    

And one SMTP conversation that represents receiving a single email message generates multiple SMTP events. Each event is recorded on a separate line in the protocol log    

You mean you don't want to receive emails from WAN IPs? If so, it is always recommended to blacklist it to block it.    

Reference article: protocol-logging

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-28*

Thank you that's what I suspected, but I wasn't sure because the internal IP was before the WAN IP, usually in router logs I see it the other way around. Thank you for clarifying it for me LilyLi2, have a great Christmas and a happy New Year.
