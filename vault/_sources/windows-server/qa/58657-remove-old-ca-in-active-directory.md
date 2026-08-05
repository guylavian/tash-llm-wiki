---
title: "Remove Old CA in Active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/58657/remove-old-ca-in-active-directory
question_id: 58657
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
---
# Remove Old CA in Active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/58657/remove-old-ca-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This is related to my previous question about Old Root CA certificate that appears in trusted root cert store of my servers/ computers.  

I check the Group policy and the old Root certificate is not published there.   

So probably that the Root CA certificate was published in AD via CERTUTIL -DSPUBLISH, also the Old certificate is Publish not only in CN=Certification Authorities. But also in CN=AIA, CN=Enrollement Services and CN=KRA. Also the old PKI server is also in CN=CDP.   

I also launch Enterprise PKI > Manage AD containers and i see the objects there  

What is the best way to clean this up  So that  new servers  will not get that Expired Certificate?   

What is the best way also to cleanup the one in production?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-05*

Hello,  

Thank you so much for posting here.  

To remove the old CA, we could refer to:  

How to decommission a Windows enterprise certification authority and remove all related objects  

https://support.microsoft.com/en-in/help/889250/how-to-decommission-a-windows-enterprise-certification-authority-and-r  

For any question, please feel free to contact us.  

Best regards,  

Hannah Xiong
