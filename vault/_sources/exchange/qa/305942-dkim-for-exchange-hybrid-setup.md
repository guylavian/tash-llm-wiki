---
title: "DKIM for Exchange Hybrid Setup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/305942/dkim-for-exchange-hybrid-setup
question_id: 305942
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# DKIM for Exchange Hybrid Setup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/305942/dkim-for-exchange-hybrid-setup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We have an Exchange Hybrid setup: one server on our premises and one office 365. O365 is the front server (receiving all inbounds emails) and relaying them, if applicable, to the on-premise server. Outbound emails from our server are ALL relayed by O365 to external recipients.    

I am not sure about the right thing to do with the DKIM key.    

When we initially installed our server, we added a public TXT entry (dkim._domainkey) to the domain DNS with the DKIM key provided by our server.    

But after the Exchange Hybrid is now setup (with Split Domain Routing) I wonder what I should do:    

-  keep the initial TXT entry with the DKIM key provided by our server as it is    

-  delete the TXT entry with the DKIM key provided by our server and add O365 DKIM keys (done by adding two additional CNAME entires according to that page https://docs.mailshake.com/article/222-dns-record-microsoft). Also, deactivate DKIM marking by our server (as it would be entirely handled by O365)    

-  or keep 1) and add 2), meaning that there will be 3 entries for DKIM in the DNS (one from our server and 2 from Microsoft)    

-  something else    

This page https://learn.microsoft.com/en-us/answers/questions/117045/office365-dkim-and-email-relay-server.html  tends to make me think the answer is 2) but unsure    

It would be great if someone could advise me.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-10*

@MicMac      

As AndyDavid said, enable DKIM for your local domain on Office 365. The mail flow between your Exchange on-premises and Exchange online are trusted which don't need to additional configuration.    

Here are article about enable DKIM for each custom domain in your tenant.    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
