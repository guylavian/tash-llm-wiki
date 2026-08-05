---
title: "migrate adcs from 2012 to 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/245701/migrate-adcs-from-2012-to-2019
question_id: 245701
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# migrate adcs from 2012 to 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/245701/migrate-adcs-from-2012-to-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

dears,   

ill need your advise on how to proceed with migrating my adcs from 2012 to 2019.  

i found many blogs explaining that it will be done using backuo/restore.  

but i have 2 questions:  

the first one: what should i change if i want ti change the server name of the new adcs after demoting the first one  

the second one: i can see that after we backup the db, we are uninstalling the role before installing it on the new server. during this time we wont have a downtime? aw we will be running currently without and adcs? can you advise on this point and we can do to increase the duration time of the certiifcate?  

thank you in advance

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-27*

Hello,    

Thank you so much for posting here.    

Thanks so much for the provided information.     

For more information about AD CS migration, we could refer to the below article.     

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc742388(v=ws.10)?redirectedfrom=MSDN    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2021-01-26*

You must follow official ADCS Migration Guide. It is the only correct and supported way to do this.

what should i change if i want ti change the server name of the new adcs after demoting the first one

migration guide covers changes you need to perform if target server uses different host name.

during this time we wont have a downtime?

you will have a downtime. No certificates, nor CRLs can be signed during migration. It is advised to extend CRL validity prior to demoting old CA to allow clients to validate existing certificates. It is recommended to disable Delta CRLs during transition as well. Go to Revoked Certificates node in CA console, select properties, uncheck Delta CRLs, adjust Base CRL validity (make it 1week at least) and then publish CRLs. Then you can start migration process.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-26*

thanks for the answer  

but the question is related to adcs ( certificate services) and not adds  

thanks in advance
