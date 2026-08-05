---
title: "Migrate Active Directory Certificate Service From Windows Server 2012 R2 Datacenter to Windows Server 2022 Standard"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/745522/migrate-active-directory-certificate-service-from
question_id: 745522
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
---
# Migrate Active Directory Certificate Service From Windows Server 2012 R2 Datacenter to Windows Server 2022 Standard

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/745522/migrate-active-directory-certificate-service-from (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have today one CA server, and that role is installed on the domain controller :(, its running windows server 2012 r2 datacenter.  

Its used for user, computer and nps certificate, mainly used for Wifi and VPN.  

We have installed a new virtual machine that is windows server 2022 standard and we would like to move the CA role over to this machine.  

The new machine will not have the same IP or hostname, guess that should not be a problem ?  

I have looked at some guides, for example   

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-migrating-the-active-directory-certificate-service/ba-p/697674  

https://www.petenetlive.com/KB/Article/0001473  

One thing here is that both of them uninstall the old CA, what I would like to do is to stop the CA service, and if the migration fails, then roll back to start the service again. Is that possible, or would that cause problems ? If I see the new CA server is running fine, I will offcourse uninstall the CA role on the old server.  

I guess I could also do a snapshot, but since the CA role is on the domain controller, I would not like to revert back, or restore any backup.  

Is there any known issues importing the private key from old CA - windows server 2012 r2 to CA - windows server 2022 ?  

Is there any known issues importing the database or registry key from old CA - windows server 2012 r2 to CA - windows server 2022 ?  

Is the Windows Server 2012 R2 CA database is compatible with Windows Server 2022 CA ?   

I also see that we need to Reissue Certificate Templates, does this mean that every machine will need to get new certificates ? Please explain a bit around this  

On other thing, the CA certificate .....The Signature hash algorithm say sha256, but the thumbprint algorithm say sha1 will this be an issue ?  

Comments?  

Thanks for any reply, have not done a CA migration before so any comments are good :)  

/R  

Andy

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-22*

Hi @Limitless Technology       

Thanks for reply, and good information.    

I configured a test environment and did a copy and everything seems ok, except one thing and that's reissue certificate templates.    

I thought that the templates I had published on the old CA server would be copied over, but I cannot see them. Do I manually need to create new ones ?    

Old server:    

    

New server:    

    

If Yes I need to manually create new ones then I guess I will have to cross check the old settings with the new.... or am I missing something here ?    

Hmmm... read something about these custom templates are distributed from AD, so since I have created a new test domain on my lab, and only exported and imported the CA role/database I guess I will not have these custom templates, am I correct ? Then when I will do this in production I will have these custome templates since I am "on" the domain ?     

/R    

Andy
