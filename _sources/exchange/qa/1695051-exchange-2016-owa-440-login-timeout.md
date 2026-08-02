---
title: "Exchange 2016 OWA - 440 Login Timeout"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1695051/exchange-2016-owa-440-login-timeout
question_id: 1695051
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 OWA - 440 Login Timeout

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1695051/exchange-2016-owa-440-login-timeout (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!

I have an Exchange 2016 Server on premise - latest CU, latest SU.

Everything worked fine, a few day ago problems started.

Outlooks working fine, iPhone Sync working fine too, but OWA and ECP and Exchange Shell stopped working.

I just receive a white page with: 440 Login Timeout (in OWA and ECP)

Certificate is presented correct, same error external or internal, same error if I try local Server Name or IP address.

I tried all the articles regarding OAuth Certs, lost IIS Bindings and Backend Certs.  

Exchange Healthecker Scripts detects nothing special.

Any ideas what the problem could cause?

Thank you!!  

Roman

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-18*

Hi! This did not solve my Problem.  

I even had an Exchange MVP take a look at it.  

His advise was to set up a fresh/clean Exchange Server (what I already did), move everything to the new Server and uninstall the old Server.

I already changed all the DNS settings and stuff to the fresh Server, so OWA and ECP is working again.

Will move all the Mailboxes and connectors in the next step.

Thanks for you help!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-17*

Hi @Gebauer, Roman，

Welcome to the Microsoft Technical Support Forum.

Based on your description, the error you are experiencing usually indicates a problem in the HTTP request/response cycle and is usually related to configuration issues in IIS, authentication settings, or Exchange redirection settings. 

I recommend that you follow some of the following troubleshooting steps:

1.Check Redirect Settings in IIS：

-  Open IIS Manager. 

-  Navigate to the `Default Web Site`. 

-  Select the HTTP Redirect feature. 

-  Ensure that redirection settings are configured correctly or disable them if they are not needed.

2.Sometimes, issues in the `web.config` file can cause such errors. Look for any custom redirection rules or errors in the `web.config` file for OWA and ECP. 

The `web.config` files are usually located in `C:\Program Files\Microsoft\Exchange Server\V15\ClientAccess\owa` and `C:\Program Files\Microsoft\Exchange Server\V15\ClientAccess\ecp`.

3.Re-check the authentication settings for the OWA and ECP directories in IIS: 

-  Open IIS Manager. - Navigate to the `Default Web Site` and select the `owa` and `ecp` directories. 

-  Under the Authentication feature, ensure that Basic Authentication and Windows Authentication are enabled, and Anonymous Authentication is disabled.

Please feel free to contact me if you have any queries.

Best,

Jake Zhang
