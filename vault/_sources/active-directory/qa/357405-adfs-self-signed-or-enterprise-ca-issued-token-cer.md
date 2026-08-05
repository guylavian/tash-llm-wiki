---
title: "ADFS - Self signed or enterprise CA issued token certificates are not working from the outside"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/357405/adfs-self-signed-or-enterprise-ca-issued-token-cer
question_id: 357405
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS - Self signed or enterprise CA issued token certificates are not working from the outside

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/357405/adfs-self-signed-or-enterprise-ca-issued-token-cer (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

It is time for our ADFS token certificate renewal as it is expiring soon.   We have been using a certificate from Sectigo (public CA) and it has worked great.  However, all of the public CAs are now expiring their certificates in just one year.   So going forward, we want to have our token be a self signed or issued from our enterprise CA.  It appears Microsoft actually recommends using their self signed certificate for the token certificate.   I can then update the expiration date for 3 years.     

That said, our initial testing was good.   I temporarily changed the new token certificate to be our primary.   I updated a couple SSO apps to use the new token cert.  The SSO connection worked if our device is on the internal network.   Any device outside the network fails.    I also want to mention that some of our apps did work from the outside and inside.  

We have an ADFS server and a web proxy server.   I'm not sure where the issue is.  

Anyone have any ideas?   Any help would be greatly appreciated.  

Thank you,  

Matt

## Answers

_No answers on this thread._
