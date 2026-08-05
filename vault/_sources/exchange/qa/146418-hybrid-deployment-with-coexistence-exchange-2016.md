---
title: "Hybrid deployment with coexistence exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/146418/hybrid-deployment-with-coexistence-exchange-2016
question_id: 146418
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Hybrid deployment with coexistence exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/146418/hybrid-deployment-with-coexistence-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,   

We have plan to exchange 2016 to migrate exchange online. Our plan to deploy new MRS Proxy server with Hybrid rather than touching existing exchange 2016 server. Current infra we have few dedicated server for Transport server (2016).  

we are introducing the new Hybrid server in existing exchange 2016 for MRS proxy for data migration + running HCW on those server.  

-  in this case do we need to open the EOP port from Newly built (hybrid) server only or is it require to open from Existing Exchange server too.  

-  Enable MRS proxy does it needed enable from only Newly built (hybrid) server or is it require to enable from Existing Exchange server too.  

-  When we are running HCW is it necessary to select all Existing exchange 2016 all server or its fine to select only newly built server ?  

-  During HCW does our all existing receive connector and send connector will wipe out ?  

-  Pointing Auto discover continue with existing existing exchange server or need to point Hybrid server ?   

Any inputs and thoughts ?

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-02*

@Anonymous  

Here are some information for your questions:  

-  You can check this article for for details about what ports are needed for hybrid deployment: Hybrid deployment protocols, ports, and endpoints.  

-  MRS proxy should be enabled on all Exchange servers.  

-  Do you mean select an Exchange server for the hybrid connection at the beginning of HCW? If so, you should select the newly installed Exchange server.  

4) No, HCW won't delete your existing send and receive connectors. Additionally, if you choose the full hybrid configuration, new connectors will be created and the "Default Frontend" receive connector will be modified for hybrid mail flow.  

5) Autodiscover record for existing SMTP domains still can be pointed your existing Exchange server.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
