---
title: "Does DAG CNO need to be in Exchange Trusted Subsystem?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/348224/does-dag-cno-need-to-be-in-exchange-trusted-subsys
question_id: 348224
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Does DAG CNO need to be in Exchange Trusted Subsystem?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/348224/does-dag-cno-need-to-be-in-exchange-trusted-subsys (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I recently created a Database Availability Group for my Exchange 2019 Mailbox Servers.  

However, I can't seem to add Members to the new DAG.   

In looking at the DAG Tasks logs I keep seeing an Access Denied message.  

I verified my user has adequate permissions (Organization Management), the Witness server is in the Exchange Trusted Subsystem and the Local Administrators group on the witness server has Exchange Trusted Subsystem.   

The DAG CNO took awhile to show up in my AD and I verified it is not in Exchange Trusted Subsystem. Does it need to be?  

Please note - The DAG was created before the Failover Cluster feature was installed on the Exchange Server. One article I read suggested this may be the problem. The DAG does not have permissions to the Failover Cluster Service because Failover Cluster did not exist when DAG was created.  Do I need to recreate the DAG? And if so, how difficult is this task (given there are no members configured in the DAG)?  

Please Advise.  

Thank you,

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-08*

Hi @Catherine Jaszewski   ,    

You could try creating the CNO and give it a full control permission of Exchange Trusted Subsystem and your Exchange servers then disable it to add servers to the DAG.    

    

Add the member servers first and then:    

    

Read this article for more information: Prestage cluster computer objects in Active Directory Domain Services    

Recreating a DAG is not a hard work, before removing the DAG, you should remove all member servers. In your case, you can directly remove it with no efforts.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
