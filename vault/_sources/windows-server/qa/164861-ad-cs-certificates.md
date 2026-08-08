---
title: "AD CS certificates"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/164861/ad-cs-certificates
question_id: 164861
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
---
# AD CS certificates

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/164861/ad-cs-certificates (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In our Windows 2012R2 CA, I duplicate the "RAS and IAS Server" template to verify our NPS server to clients. When I publish that template, what determines the NPS server uses that certificate? I see that the server is a member of RAS and IAS servers group. Is that all it takes in Active directory? I don't see any other identifier that designates the NPS server will use that certificate.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-17*

Hello,    

Thank you so much for posting here.    

To configure the certificate template and autoenrollment, we could refer to the following articles:    

Configure the Server Certificate Template    

https://learn.microsoft.com/en-us/windows-server/networking/core-network-guide/cncg/server-certs/configure-the-server-certificate-template    

NPS Server Certificate: Configure the Template and Autoenrollment    

https://forsenergy.com/en-us/radius/html/4e4f927d-3273-40b5-a33b-f550be1587e2.htm    

For any question, please feel free to contact us.    

Please note: Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
