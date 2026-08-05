---
title: "Exchange Hybrid - DDoS Attack"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/284498/exchange-hybrid-ddos-attack
question_id: 284498
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-devices-deployment-config-app-groups"]
---
# Exchange Hybrid - DDoS Attack

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/284498/exchange-hybrid-ddos-attack (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
For the last 2 years our organization has been affected by DDoS attacks 5 times.
```

4 of those attacks were coming from Exchange after analyzing the security logs from AD.  

Preventative Measures We Followed  

1- Installed a new Exchange server (to be used for ECP and Administering our DAG. caused multiple account locks due to some authentication requests proxied to the server as the server didn't hold any databases. we decommissioned the server soon after)  

2- Our security team blocked some suspicious IPs.  

3- Disabled OWA for external users.  

Are there any preventative measures that we can take to secure client requests for ActiveSync and MAPI ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-24*

Hi @Azy1412   ,    

Agree with what Andy said. Enabling modern authentication will improve the security of communication between the client and the server.    

You could also following the steps to prevent Exchange server and client request:    

-  Apply the latest security updates.    

-  Reasonable deployment firewall and Multi-factor authentication (MFA).    

-  Review the sensitive roles and groups.    

-  Restrict access.    

For more information :Defending Exchange servers under attac    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
