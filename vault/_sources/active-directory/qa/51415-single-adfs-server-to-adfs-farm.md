---
title: "single adfs server to adfs farm"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/51415/single-adfs-server-to-adfs-farm
question_id: 51415
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# single adfs server to adfs farm

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/51415/single-adfs-server-to-adfs-farm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a single ADFS on premise using  WID. I want to add another adfs to form a farm. I do not have an existing adfs farm as this will be the first.  

Can some one point me to a good tutorial on how to do this.  

Also, will I need sql database installed for each of the servers  or a separate machine housing only the database?  

Will I use a wild card certificate? Currently the certificate is adfshost01.mydomain.com.  

The ADFS is for internal use only. Not going outside the internet.  

Edit: ADFS is running on Windows Server 2016

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-07-24*

Since you are using ADFS on Windows Server 2016 (aka ADFS 4.0), you already have a farm. A farm of one :)  

So to add nodes to the farm, simply use the Server Manager on that node to add the Active Directory Federation Service role. During the installation you will be asked if you are creating a new farm or joining an existing farm. Just pick that you are joining an existing farm and type the name of your first ADFS server (aka the Primary Server in that situation).  

Before doing that though, make sure you install the SSL/TLS certificate on that new server. And also make sure you know the password of the service account used by ADFS (if you do not use a Group Manage Service Account).  

Then you will need to implement some sort of Load Balancing. It is recommended to use a hardware load balancer.  

If you don't have any, you could use a round-robin in DNS but that's not proper load balancing as the clients cache the answer and the the round-robin* does not allow to check if the service is running.   

* * Technically it could with a bit of scripting and if you are using DNS running on Windows Server 2016. Then you could do some DNS policies.*
