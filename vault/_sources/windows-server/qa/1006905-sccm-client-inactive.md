---
title: "SCCM Client inactive"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1006905/sccm-client-inactive
question_id: 1006905
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# SCCM Client inactive

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1006905/sccm-client-inactive (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,    

in my infrastructure I have several inactive SCCM client, but these clients are up and running,    

How I can fix this problem?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-09-16*

Hi @san.khurtsilava  ,    

Agree with @Limitless Technology  . Client status of inactive are indicative of the system either being offline or simply unable to communicate with the MP.     

1,As these clients are up and running, please check the LocationServices.log on the problematic clients to see if there is any useful information about the communication failure.    

2,Please help make sure that there is no firewall or anti-virus to stop the communication between the client and the MPs. Use the following URL to verify that a client can access the management point and the management point certificate information:    

http(s)://<ServerName>/sms_mp/.sms_aut?mplist    

http(s)://<ServerName>/sms_mp/.sms_aut?mpcert    

Where <ServerName> is the NetBIOS/FQDN for the management point computer.    

Hope it helps. Thanks for your time.    

Best regards,    

Simon    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-15*

Hello there,    

By default, a client is marked as inactive if they haven’t completed one of the following within seven days:    

Requested a policy update    

Sent a hardware inventory    

Sent a heartbeat message    

Two Site Maintenance tasks control stale record deletion in SCCM. Within the Configuration Manager console, these can be accessed under Administration/Site Configuration/Sites – Site Maintenance.    

Within Site Maintenance, you will see two tasks named: Delete Aged Discovery Data and Delete Inactive Client Discovery Data. Both of these tasks should be enabled for inactive client data deletion.    

------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–
