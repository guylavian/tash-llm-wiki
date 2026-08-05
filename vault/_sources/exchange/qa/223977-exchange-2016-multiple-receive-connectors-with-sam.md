---
title: "Exchange 2016 - Multiple receive connectors with same IP&port bindings, but different authentications?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/223977/exchange-2016-multiple-receive-connectors-with-sam
question_id: 223977
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange 2016 - Multiple receive connectors with same IP&port bindings, but different authentications?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/223977/exchange-2016-multiple-receive-connectors-with-sam (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am upgrading from Exchange 2010 to 2016(hybrid for O365) and trying to add in new receive connectors that allow specific Internal server IPs to relay mail with different levels of authentications and same Exchange server IP binding and ports(25), but this does not seem to be an option with 2016 like I have with 2010.   I have some servers that relay mail with certain levels of authentication and other copier/scanners that might have no authentication, etc.  It seems to want to force me to use a different IP or different port, or the default one, and then make changes to authentication methods of all SMTP traffic flowing through it.  Does anyone know if this is still possible?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-11*

Thanks for all of the responses guys. Exchange will not let you add the new connector with the same bindings without getting this error  

The values that you specified for the Bindings and RemoteIPRanges parameters conflict with the settings on Receive connector "EXSRV2016\Default Frontend EXSRV2016". Receive connectors assigned to different Transport roles on a single server must listen on unique local IP address & port bindings.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-11*

@Dave Bryan       

Hi,    

Agree with Ashok, it is possible.    

As is mentioned in the document: Receive connectors    

    

Though all the receive connectors listen on port 25 of the Exchange server, since the source addresses vary from each other, the most matched connectors will be used.    

After you created the receive connectors, you can configure the authentication settings via editing the connectors:    

    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-10*

Hi @Dave Bryan   ,    

Based on my understanding, you can create multiple custom receive connector for the same Exchange server for Application relay. Each connector will be differentiated based on the remote IP addresses and Authentication. While creating receive connector, you have to select Role as "FrontEndTransport" and Type as "Custom"    

https://learn.microsoft.com/en-us/exchange/mail-flow/connectors/receive-connectors?view=exchserver-2016#receive-connector-remote-addresses    

If the above suggestion helps, please click on "Accept Answer" and upvote it
