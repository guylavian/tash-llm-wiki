---
title: "Kerberos in Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/619177/kerberos-in-exchange-2019
question_id: 619177
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Kerberos in Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/619177/kerberos-in-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello.  

We installed exch 2019 in org with 2013 exchange.  

So, after enabling mapi over http, negotiate outlook clients repeat to ask users password, so in virtual directory we are temporary disable negotiate provider.  

I didnt find any user requirements for enabling kerberos.   

In our envriroment we have like 50 mail domains, and only 4 upn suffix. But all users share one primary upn. Different users have different primary mail addresses.  

So here is a question: should users upn equal to primary mail in exchange for successfully kerberos auth?  

And second one:   

How kerberos auth works from internet?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-09*

Hi @70317574    

Should users upn equal to primary mail in exchange for successfully kerberos auth?    

No, If the client uses Kerberos V5 for authentication, it requests a ticket to the server in the target domain from a domain controller in its account domain. The Kerberos Key Distribution Center (KDC) acts as a trusted intermediary between the client and server; it provides a session key that enables the two parties to authenticate each other. If the target domain is different from the current domain, the KDC follows a logical process to determine whether an authentication request can be referred:    

Is the current domain trusted directly by the domain of the server that is being requested?    

```
If yes, send the client a referral to the requested domain.  
If no, go to the next step.
```

Does a transitive trust relationship exist between the current domain and the next domain on the trust path?    

```
If yes, send the client a referral to the next domain on the trust path.  
If no, send the client a logon-denied message.
```

For more information about how kerberos auth works:    

What is the difference between Negotiate and NTLM authentication?    

And Configure Kerberos authentication with Exchange 2019.    

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of the information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
