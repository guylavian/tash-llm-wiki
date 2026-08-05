---
title: "Exchange Server 2016 with Oracle Primavera"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/345004/exchange-server-2016-with-oracle-primavera
question_id: 345004
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange Server 2016 with Oracle Primavera

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/345004/exchange-server-2016-with-oracle-primavera (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,   

I have Exchange 2016 and Oracle Primavera Unifier application. I want to send an email to the internal user using Exchange Server.  

I created a receive connection with the following settings.  

Name: Oracle587  

Authentication: Basic / Integrated  

Permission Group: Exchange User   

Remote network settings: 192.168.xxx.xxx  

Network Binding: Port 587  

The issue is that I can send the email using my exchange user but the message sent is not showing in the sent items even I have the mailbox of the user. If I enable the TLS, the application give the error " Could not convert socket to TLS;".  

Please help me should I enable TLS and if we don't enable TLS. Why the send message is not showing in the Sent Item. User is authenticated successfully and when I sent the message it also pick the name of the user from Active Directory.  

Your prompt response will highly appreciated.  

Best Regards,  

Faheem

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-06*

Further, if I enable SSL/TLS on the Oracle App It give the message.  

"Could not to the smtp server xxx.abc.com : port 465

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-06*

The main issue which I am facing is that email is being sent but the emails are not saving in the sent items. What can be the main cause of it or is it the default behavior of the Exchange Server.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-06*

Hi @Anonymous      

According to your description above, you scenario is internal relay. For internal SMTP relay there's no specific configuration required on the server or the connectors, however it is recommended that you use a DNS alias for hub server 2010 or mailbox server 2016 instead of the real server name. This will allow you to configure all of your devices and applications with the DNS alias.    

When Exchange Server 2016 is first installed the setup routine automatically creates a receive connector that is pre-configured to be used for receiving email messages from anonymous senders to internal recipients. This allows inbound internet email to be received by the server, and is also suitable for internal relay scenarios.    

The receive connector is named “SERVERNAMEDefault Frontend SERVERNAME”, and the bindidngs and port for this connector    

EXSERVER\Default Frontend EXSERVER      {[::]:25, 0.0.0.0:25}     

You could do some relay test from the server hosting the application via command promot/telnet.  If this works then the issue is not with relaying but the application itself for which you wil have to contact the vendor for.    

Here is an article introduces about SMTP relay in Exchange server 2016 in detail for your reference: How to Configure Exchange Server 2016 for SMTP Application Relay    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
