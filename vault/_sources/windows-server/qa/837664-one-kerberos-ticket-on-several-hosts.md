---
title: "One Kerberos Ticket on several hosts?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/837664/one-kerberos-ticket-on-several-hosts
question_id: 837664
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-remote-desktop-terminal-services", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# One Kerberos Ticket on several hosts?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/837664/one-kerberos-ticket-on-several-hosts (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

we have implemented ATP and now we are getting warnings, that one Kerberos Ticket of one employee was used on two machines. It is ok?  

Alert Description: An actor took employee's Kerberos ticket from TS-Server and used it on 2 computers to access 1 resource.  

{"$id":"23","IsValid":false,"Type":"DomainResourceIdentifier","ResourceName":"ldap/dc.domain.local"},{"$id":"24","IsValid":false,"Type":"ResourceAccessInfo","IpAddress":"192.168.100.174","Time":"04/27/2022 08:57:38"}  

{"$id":"25","IsValid":false,"Type":"DomainResourceIdentifier","ResourceName":"ldap/dc.domain.local"},{"$id":"26","IsValid":false,"Type":"ResourceAccessInfo","IpAddress":"192.168.100.171","Time":"04/28/2022 07:59:06"},  

important notice: TS-Server has several IP-Adresses (bindet to a user), so 100.174 and 100.171 is the same TS-Server. We also have another TS-Server with serveral IPs too, that's why I'm asking whether Kerberos Ticket is the same on all machines?  

Thank you in advance!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-06*

Hello LimitlessTechnology-2700,  

If the ticket is always different, why then we are getting message, that the same ticket is used from different IP adresses?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-06*

Hello @Anahaym       

In fact the ticket will be different based on the network. For example, during the request for TGT the client sends a plaintext message to the authentication server. This message contains:     

-username;    

-the name of the requested service (in this case this is the Ticket Granting Server – TGS);    

-the network address;    

-the requested lifetime of the TGT.    

After verifying different information, the server generates a random key called the session key that is to be used between the client and the TGS.    

The authentication server then sends back two messages to the client:    

-  Message A is encrypted with the client secret key. The client secret key is not transferred but is retrieved from the password (more to speak the hash) found in the user database. This happens all on the server side. The message contains:    

TGS name;    

timestamp;    

lifetime;    

the TGS session key (the key generated in the beginning of this step).    

-  Message B is the Ticket Granting Ticket, encrypted with the TGS secret key, that contains    

your name;    

the TGS name;    

timestamp;    

your network address;    

lifetime;    

the TGS session key (same as in message A).    

Hope this helps with your query,    

-----------------    

--If the reply is helpful, please Upvote and Accept as answer--
