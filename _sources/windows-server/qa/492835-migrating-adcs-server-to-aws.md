---
title: "Migrating ADCS Server to AWS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/492835/migrating-adcs-server-to-aws
question_id: 492835
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Migrating ADCS Server to AWS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/492835/migrating-adcs-server-to-aws (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm planning to migrate my ADCS server to AWS.  

Only one ADCS server is an enterprise CA.   

So, please tell me about the migration method.  

The target ADCS server is installed in an on-premises virtual environment (Vmware).  

The ADCS server is a separate environment from the AD server.  

(Use the AD server as it is without migrating.)  

I'm going to get an image of the ADCS server and move it to AWS.  

(Get the image with VMware function.)  

Is it okay to migrate this way?  

I do not change the hostname or CA name of the ADCS server.  

Only change the IP address.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-29*

Hello @健司 米沢  ,    

Thank you for posting here.    

Hope the information above provided by Crypt32 is helpful to you.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2021-07-28*

If you are migrating image from VMware to AWS, then no migration is required. Make sure that CA server can communicate with domain controllers after migration.
