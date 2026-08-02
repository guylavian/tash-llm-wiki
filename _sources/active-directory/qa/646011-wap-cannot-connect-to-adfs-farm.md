---
title: "WAP cannot connect to ADFS Farm"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/646011/wap-cannot-connect-to-adfs-farm
question_id: 646011
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# WAP cannot connect to ADFS Farm

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/646011/wap-cannot-connect-to-adfs-farm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hy!    

I have two ADFS server on farm, there are in MS NLB.    

There are two WAP server in MS NLB. WAP servers has an entry in host file which is point to the ADFS Farm NLB address. WAP01 can connect successfully to ADFS Farm, but WAP02 can't. This is in WAP02 EventViewer:    

The federation server proxy configuration could not be updated with the latest configuration on the federation service.     

Additional Data     

Error:      

Retrieval of proxy configuration data from the Federation Server using trust certificate with thumbprint '2507849F7576DD619C2A7690AA401752D271D3DF' failed with status code 'InternalServerError'.      

EventID 224.    

    

I tried to reestablished the connection with Install-WebApplicationProxy -Thumbprint "SSL cert thumbprint" -FederationServiceName "sso.domain.com" but I get the following error:    

    

And generate an event:    

When I change the host file on WAP02 to point the primary ADFS server, the connection successfully. When I remove the Secondary ADFS from NLB, the connection successfully. Whats wrong?

## Answers

_No answers on this thread._
