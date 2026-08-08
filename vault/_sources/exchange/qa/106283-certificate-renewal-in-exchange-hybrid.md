---
title: "certificate renewal in exchange hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/106283/certificate-renewal-in-exchange-hybrid
question_id: 106283
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# certificate renewal in exchange hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/106283/certificate-renewal-in-exchange-hybrid (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

dears,  

i have a running hybrid configuration between exchange 2013 and office365 operational since 2 years. i have users running on both on premises and office365.  

the public certificate is about to expire this week, i couldnt renew it as i have a problem with the payment.  

therefore, i re-issued a new one from another provider, but i still didnt complete the request.  

cab you advise please on the procedure?  

does it need downtime?  

do i need to do anything on the HCW level knowing that the old certificate is used by the HCW and the o365 connector.  

your help is appreciated  

thank you in advance

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2020-09-24*

Hi,  

You can follow the below steps,  

-  Complete the request by selecting the new certificate  

-  Export the certificate and import it on the other exchange servers if any  

-  Assign the services to the certificates - This might require the restart of IIS which affects the client connections, so do if after hours and one at a time.   

-  If you have the certificate on the load balancer, then share the new certificate with the certificate chain to update  

-  Make sure to have the certificate chain installed on all the exchange servers as the provider is different  

-  For HCW, suggest to re-run it if you are planning to use the certificate for the SMTP service and select the new certificate (this wouldn't have been required incase of renewal) - Also make a note of the existing hybrid configuration using the command Get-HybridConfiguration

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-25*

hello,  

well noted.  

one question, if the certificate is expired and i dndt renew it yet.  

what would be the behavior that i will faced? other than outlook clients?  

will something happen on the mail flow level between onprem and o365?  

thank you
