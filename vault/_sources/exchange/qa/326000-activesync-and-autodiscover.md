---
title: "ActiveSync and Autodiscover"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/326000/activesync-and-autodiscover
question_id: 326000
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# ActiveSync and Autodiscover

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/326000/activesync-and-autodiscover (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I've got a question in regard to ActiveSync and Autodiscover.  Consider the below diagram, I am walking through a design to migrate over from Exchange 2010 to 2016.  You'll notice that there is no direct TCP:443 access from the public internet to Exchange 2016, I'm using a reverse proxy device to connect clients via ActiveSync and OWA only.  The Outlook client itself will only ever connect over VPN.    

The service URLs for Exchange 2016 have all been configured with a common FQDN, post.domain.com.  Including the ClientAccessService/Autodiscover URL.  However, with the exception of the ActiveSync ExternalURI field, all other ExternalURIs have been set to $null.    

I don't plan to create an autodisover.domain.com record internally or externally, the hope being that Outlook clients can retrieve the necessary connection info with access to Active Directory DNS(SRV records).  Since they are only allowed to sync Outlook while on VPN.    

We rely on an MDM management tool to push out ActiveSync configurations to all mobile devices, so no reliance on Autodiscover there either.  So in this example, you can see that the reverse proxy URL on the public internet is as1.subdomain.domain.com.  Whereas the internal service URL name is post.domain.com, which the reverse proxy device connects to and resolves internally.    

My question is this...  Let's say an ActiveSync capable device happened to run the VPN client and now has access to internal DNS/SRV records.  Can I expect the ActiveSync device to interact with Autodiscover at any level and overwrite the publicly resolvable as1.subdomain.domain.com to post.domain.com?  This would in effect break ActiveSync once the VPN client was disconnected.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-23*

Hi,    

When I check the procedure that Autodiscover processes for Exchange ActiveSync clients, it seems the url that Outlook client connecting to cannot be customized.    

Since you don't have DNS records for autodiscover.domain.com, it should fail in the step1,2,3 and try connecting to the url in srv record. What do you set for that?    

You've got MDM to apply configuration for all devices, do you mean manually specify the server inforamtion?    

The official doc above may not apply for you situation, you can try enabling ActiveSync device log  and testing in EXRCA.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-23*

Hi @AdamTyler-3751   ,    

Based on my knowledge, the answer is yes. If the Activesync device has the connectivity to the internal DNS, it can connect using Autodiscover SRV method which is one of the discovery steps.     

https://learn.microsoft.com/en-us/previous-versions/office/developer/exchange-server-interoperability-guidance/hh352638(v=exchg.140)    

Alternatively, you can also try pushing the ActiveSync endpoint, http://post.domain.com/Microsoft-Server-ActiveSync using MDM once connected over VPN and see if that works. This is nothing but a manual configuration.    

If the above answer is helpful, please click on "Accept Answer" and upvote it. Thanks for understanding.
