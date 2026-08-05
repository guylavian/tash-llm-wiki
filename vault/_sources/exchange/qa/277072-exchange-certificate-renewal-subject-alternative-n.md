---
title: "Exchange Certificate Renewal Subject Alternative Name Split DNS Autodiscover"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/277072/exchange-certificate-renewal-subject-alternative-n
question_id: 277072
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Certificate Renewal Subject Alternative Name Split DNS Autodiscover

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/277072/exchange-certificate-renewal-subject-alternative-n (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2016, on a split dns environment with existing local AD CA certificate, will have certificate replaced with 3rd party. The are 3 domains on this server...  

domain1.com  

domain2.com  

domain2.local  

I will be ignoring the domain2.local SAN's in the new certificate, but how do i handle the autodiscover?  

The Virtual directories [ecp,ews,mapi,activesync,oab,owa] all point at correctly resolving fqdn CN="mail.domain1.com"... my concern is with autodiscover...   

if i do an nslookup locally, it resolves to the correct IP of the exchange server, but shows the fqdn as  "autodiscover.domain2.local". 3rd party verification will require access to the .local domain to verify ownership, which won't work.  

Do I need to change this resolution to the fqdn CN=mail.domain1.com. How do i change this?  

When generating the CSR, the server includes autodiscover.domain1.com AND autodiscover.domain2.com... How do i handle this scenario?   

If i do a local lookup of autodiscover.domain1.com OR autodiscover.domain2.com... they both come up empty. Are some DNS records missing?  

The autodiscover is NOT used off premises, only on the local network. I just don't want to muck up any internal config by screwing up the autodiscover in the certificate.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-18*

Hi @jeff mcnabney   ,    

If the external users use autodiscover on both domain1.com and domain2.com servers, then you gonna need both autodiscover.domain1.com and autodiscover.domain2.com.    

But if there are no external users that will use autodiscover, i think you won't need this. But in this case why do we need the certificate?     

I think, as Andy said, it's a better choice to add the autodiscover.domain.com as the SAN.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
