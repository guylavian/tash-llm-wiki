---
title: "active directory based activation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/478271/active-directory-based-activation
question_id: 478271
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# active directory based activation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/478271/active-directory-based-activation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In active directory based activation how to verify how many activations are used? Is there any tool to check? Please provide link to download.

My ADBA server is 2012R2. we are trying to activate windows 10 clients. What is event log to verify activation is successful or not.

When i give slmgr /dlv it is showing all Zeros.

Name: Windows(R), ServerStandard edition  

Description: Windows(R) Operating System, VOLUME_KMS_2012-R2_WIN10 channel  

Activation ID: XXXXXXXXXXXXXXXXXXXXXXXXXX  

Application ID: XXXXXXXXXXXXXXXXXXXXX  

Extended PID: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  

Product Key Channel: Volume:CSVLK  

Installation ID: XXXXXXXXXXXXXXXXXXXXX  

Use License URL: XXXXXXXXXXX  

configextension=XXXXXXXXXXXXXXXXXX  

Validation URL: XXXXXXXXXXXXXXX  

Partial Product Key: XXXXXXXXXXXXXXXXXX  

License Status: Licensed  

Remaining Windows rearm count: 1000  

Remaining SKU rearm count: 1001  

Trusted time: 7/16/2021 4:48:33 AM

Key Management Service is enabled on this machine  

Current count: 0  

Listening on Port: 1688  

DNS publishing enabled  

KMS priority: Normal

Key Management Service cumulative requests received from clients  

Total requests received: 0  

Failed requests received: 0  

Requests with License Status Unlicensed: 0  

Requests with License Status Licensed: 0  

Requests with License Status Initial grace period: 0  

Requests with License Status License expired or Hardware out of tolerance: 0  

Requests with License Status Non-genuine grace period: 0  

Requests with License Status Notification: 0

Client log: Event ID 12308  

Active Directory Activation has succeeded.  

Sku Id = XXXXXXXXXXXXXXXXXXXXXX  

AO name = Windows(R) Operating System, VOLUME_KMS_2012-R2_WIN10 channel  

AO DN = XXXXXX,CN=Activation Objects,CN=Microsoft SPP,CN=Services,CN=Configuration,DC=kmsserver,DC=com

Does above event confirms my Client is activated sccesfully?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-16*

Hi,    

Not sure if it works but maybe you can refer to this:    

https://learn.microsoft.com/en-us/windows/deployment/volume-activation/plan-for-volume-activation-client    

Thanks for your time.    

Best Regards,    

Danny    

-----------------------------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
