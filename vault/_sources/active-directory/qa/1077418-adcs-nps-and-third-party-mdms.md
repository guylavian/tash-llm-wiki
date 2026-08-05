---
title: "ADCS/NPS and third party MDMs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1077418/adcs-nps-and-third-party-mdms
question_id: 1077418
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Q&A User"]
---
# ADCS/NPS and third party MDMs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1077418/adcs-nps-and-third-party-mdms (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So this is a long one, so take this as a challenge to people:    

I am trying to setup an SSID using certificate-based authentication for IOS devices.     

I am using Airwatch as the MDM. Typically, there is very little documentation on this that is up-to-date.    

2 MDM profiles, one uploads the RootCA. Another that makes the SCEP communication and retrieves an identity certificate from the CA. This goes through without a problem and can see the root CA and the individual cert on the device issued from the CA.    

Here is the problem:    

When trying to authenticate with the NPS server, I get the error: "Reason code 8; The specified user account does not exist". Now, looking at the EAP logs, it is using (domain)(device serial) which is what it should be (I think).    

The big question, do I need to create AD objects for every device, or is there a way I can change NPS to not require a matching username, or at least use the SCEP service account to authenticate instead?    

Any help/advice would be greatly appreciated.    

Thanks,    

Ben

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-08*

Not a very full answer for you, but whenever I looked at authenticating network devices via RADIUS (NPS) it needed a user object in AD. I used MAC address, but whatever ID attribute is available to you can be mapped to user I think.
