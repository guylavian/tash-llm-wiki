---
title: "AD and ADFS 2016 migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1061708/ad-and-adfs-2016-migration
question_id: 1061708
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Q&A User"]
---
# AD and ADFS 2016 migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1061708/ad-and-adfs-2016-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an Windows Server 2016 with AD and ADFS running on one AWS Account.     

Now I want to change the server from one AWS account to another AWS account due to CIDR limitations.     

I have installed same windows Server 2016 AMI in another AWS account and also configured ADFS in the same server on the new AWS accounts.     

Both the services AD and ADFS are additionally configured with the primary one.     

Now I wanted to migrate from secondary to primary both AD and ADFS.     

I have seen some article to change FSMO roles for AD and powershell commands for ADFS to change from secondary to primary.     

My question here is,    

-  First I have to migrate AD and then only I need to go for ADFS right?    

-  Or is there any other best practice to do it?    

These are the articles I saw for migration of AD and ADFS from secondary to primary    

for ADFS - https://hippidikki.wordpress.com/2016/04/19/changing-adfs-primarysecondary-federation-serverin-a-farm/    

for AD - https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/view-transfer-fsmo-roles    

Can someone guide me with best possible option, since am moving the production server.     

Thanks in advance.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-01*

I tested with test instance in my AWS cloud and it worked like charm by changing the roles for both ADDS and ADFS.     

Now I have one more issue, this is on production where am trying to configure secondary ADFS server by adding to primary one, I stuck on creating SPN account. I get a error     

"There were no SPNs set on the following service account 'XXXXXXX\serviceadmin'. Specify the service account used to configure the other Federation Servers in the farm, or set host SPN for the farm on the service account."    

I tried creating SPN account with "setspn -U -S http/<domainame> <user account> on primary server, but still its getting failed.     

I checked for any duplicate SPN too, but I didn't find any if I use "setspn -x"    

Trying for more than 24 hrs but couldn't able to find out.     

Thanks.
