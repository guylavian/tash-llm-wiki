---
title: "Restart Message for installing AD CS!"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/342910/restart-message-for-installing-ad-cs
question_id: 342910
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Restart Message for installing AD CS!

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/342910/restart-message-for-installing-ad-cs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

When I want to install AD certificate services after choosing:  

Certificate Enrollment Policy Web Service  

Certificate Enrollment Web Service  

Certification Authority Web Enrollment  

I am receiving the message below:  

The request to add or remove features on the specified server failed.   

The operation cannot be completed, because the server that you specified requires a restart.  

I restarted my server n times! Also I stop and started manually the Remote Registry services in services. Finally, I turned off the windows firewall but same error.  

Could anyone help me?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-05*

I checked and I don't have any error in Windows log.  

Also I checked and it has the permission.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-05*

Hi,  

Did you check the event for more details under Event Viewer -> Windows Logs -> System?  

If it was an error with the EventID 7041:This service account does not have the required user right "Log on as a service".  

We need to grant the logon as a service permissions to “NT SERVICE\ALL SERVICES”  

For more details you can refer to: http://woshub.com/unable-add-remove-role-windows-server-requires-restart/  

This response contains a third-party link. We provide this link for easy reference. Microsoft cannot guarantee the validity of any information and content in this link.  

Best Regards,
