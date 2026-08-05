---
title: "Exchange 2013 self signed cert renewal issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/100526/exchange-2013-self-signed-cert-renewal-issue
question_id: 100526
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 self signed cert renewal issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/100526/exchange-2013-self-signed-cert-renewal-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are using Exchange 2013 in our office, we have one cert issued by CA and some self-signed certs (were there by default after the installation)    

I found that the self-signed certs (with the name (1)Microsoft Exchange,  (2)Microsoft Exchange Server Auth Certificate (3) _blank name) are going to expire.     

Is it necessary for us to renew them? can we just ignore them?    

If not, is it correct to follow the procedures below to renew them? no csr is required?    

https://learn.microsoft.com/en-us/exchange/architecture/client-access/renew-certificates?view=exchserver-2019#:~:text=Every%20certificate%20has%20a%20built,Shell%20to%20renew%20Exchange%20certificates.

## Answer (community) — community member

*upvotes: 1 · updated: 2020-09-22*

For a healthy Exchange server, the third certificate should be WMSVC.  

You'd better renew it as well in EAC, otherwise it may cause IISWebManager issue.

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 1 · updated: 2020-09-21*

Yes, you should renew it before the expiration date.     

You can check the following link to renew the exchange self signed certificate:     

https://learn.microsoft.com/en-us/exchange/architecture/client-access/create-self-signed-certificates?view=exchserver-2019

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-30*

Hi all,   

I got serious problem after renewing the "Microsoft Exchange" cert with the procedures below   

https://ehloergosum.com/2020/01/25/renewing-that-pesky-microsoft-exchange-certificate/  

outlook clients cannot login afterward, even clicking "Yes" and type in password will show disconnected at the bottom.OWA also shows it's an insecure website, anyone got ideas on this? thank you

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-22*

Thanks all for the info!  

As we are using DAG, shall we work on the renewal procedures (listed above) for each cert on both servers separately?  

(I am a bit confused on this "If you are using a DAG, then move all the databases to other servers and have at it")  

Yes, I just found that the blank name cert was from the Issuer  WMSVC-<server name>  

Is there any suggested procedures for renewing WMSVC certificate?  

thank you.  

thank you.
