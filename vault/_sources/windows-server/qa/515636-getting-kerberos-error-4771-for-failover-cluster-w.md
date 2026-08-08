---
title: "Getting Kerberos error (4771) for Failover Cluster (Windows server 2019)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/515636/getting-kerberos-error-4771-for-failover-cluster-w
question_id: 515636
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["sql-server-other-l1", "windows-business-windows-server-high-availability-clustering-high-availability"]
---
# Getting Kerberos error (4771) for Failover Cluster (Windows server 2019)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/515636/getting-kerberos-error-4771-for-failover-cluster-w (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to debug some erros (1260) we are getting in Failover Cluster manager.    

    

I found it very strange, as the cluster is able to create and modify DNS records successfully. Both the cluster and nodes computer accounts have permissions to edit the records. So I searched the DNS (AD) servers's logs for correlated events. In the DNS Audit log, I could see that the records could indeed be updated successfully:     

    

But, In AD security event logs, the following events are being logged:    

    

I checked the AD objects and both the nodes and the cluster (CNO) itself have full permissions on the CNO.    

I ran out of ideas. The cluster was created by a colleague that since left the company, so I don't know if the objects were created manually or automatically by the failover cluster manager.    

Do anyone know anything that I could have missed?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-09*

So we have had this same issue that i have battled for a month, checking literally every nook and cranny relating to security, authentication, and DNS. I finally found the root cause, and I wanted to get this out there since our env is identical in regards to using gMSA on 2012r2 for ad.    

TLDR: in my case, it is KB related. KB5006672, KB5005568, KB5005030, and KB5004244 all cause this. It is really easy to test as well for anyone who wants to confirm:    

In your failover cluster manager, double click on your cluster under cluster core resources to check dns status:    

    

This will be your confirmation check after uninstalling each KB.    

Uninstall any KB's that are mentioned. It looks like it started happening in july of 2021 the earliest. Preview cumulative updates can also potentially hold this problem.    

After uninstall, if DNS shows OK, that was the root cause. please note that since these are cum sec updates, and further monthly updates can potentially cause as well.    

    

I also tested this on a sandbox ADDS .local domain that was on server 2019 with AD most up to date. The thinking was since (my/the) environment is security heavy, a GPO could have been causing the issues. We confirmed that is not the case and just used an out of the box domain w/o any GPO's whatsoever, and still reproduced the DNS cred missing problem with said KB articles.     

Hope this helps.     

PS: if this does end up fixing anyones problem (as of november 9th, 2021), please open a ticket with microsoft and share your findings. The more light people can shed, the better.     

edit: our environment was AD on 2012r2, and cluster was on server 2019 using group managed service accounts.    

also tested on an "out-of-the-box" test AD environment with only default settings on server 2019, and reproduced the issue confirming it was windows update related.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-17*

Hi @Marcos dos Santos de Oliveira  ,    

Here is an introduction to error 4771.    

It has an error code, please take a closer look at the Description of the event fields.    

You should be 0x18 (because I didn't see it in the screenshot). Usually, the reason for this error is the wrong password was provided.    

This can be something as simple as a mapped drive, cached password in a scheduled task or service.    

Check the account status in AD and enter the correct account password and try again.    

Best regards,    

Seeya    

If the response is helpful, please click "Accept Answer" and upvote it, as this could help other community members looking for similar queries.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
