---
title: "Domain controller migration 2008r2 to 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/266844/domain-controller-migration-2008r2-to-2019
question_id: 266844
fetched: 2026-07-25
answer_count: 12
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Domain controller migration 2008r2 to 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/266844/domain-controller-migration-2008r2-to-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I need to migrate domain controller from 2008r2 to 2019 and I would like to know if I can keep the same ip and same name.  

I think I can use temporary ip + name on my new domain controller during the migration and when my new domain controller is operationnal, I just demote the older and remove it from AD. Then I change IP + name on my new DC and reboot + verify DNS are updated and it's ok ?  

Thanks for your answer.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-02-10*

The much safer / simpler solution is to move roles off, decommission, then stand up the new one with correct name and address.    

The two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2021-02-10*

Hi,    

Yes , you can keep the same ip and same name.    

Before going further , i would suggest you back up the old DC.    

Check if the DFSR is used for the sysvol replication.    

command :dfsrmig.exe /getglobalstate    

If the Result: 3 (ELIMINATED)   the  DFSR is used for the replicaiton.    

If not , you need to migrate the FRS TO DFSR before promote the first 2019 server.For more infromation , you can refer to :    

https://learn.microsoft.com/en-us/windows-server/storage/dfs-replication/migrate-sysvol-to-dfsr    

After the dfsr migration , confirm everything works well ,then you can try to rename the old DC and change the ip address of the old DC, for exmaple IP 1 to IP 2.    

Run the cmd as administrator to register A records and PTR records: IPCONFIG /RegisterDNS     

Check whether the related records have been modified successfully in DNS of old DC.    

Restart the netlogon service to trigger the dynamic record list generation that needs to be registered    

Run the cmd as administrator to force push replication on other DCs：    

 Repadmin /syncall /AdeP       

Wait for replication to complete, and check whether changes have been made in DNS and GC    

Then assign the old name and ip address for the new DC.    

Observe for a while and make sure both DCS are working properly.    

We can run the “dcdiag” to check.    

Demote old DC.    

Best Regards,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-10*

Hello,  

There are only 2 DC(SRV1 and SRV2) on the environment. I would like to avoid shut down one of them and build new one after. If there is an issue, I could have 0 DC.  

Could you validate me this :  

I prefer to stay both actual online while I build the new one(SRV3) with "temporary" and IP and promote it as DC.   

I can then verify  Active directory is functionnal with SRV1 / SRV2 / SRV3 (dcdiag / repadmin).  

I can demote SRV1, and shut down it.  

I can swap temporary name and IP from SRV3 to match SRV1  

Now I need to restart netlogon service to force srv service to register on msdcs dns zone  

After all updates are done on DNS, verify dcdiag and repadmin are ok and remove SRV1  

I need to do the same operation for SRV2.  

To test health Active directory :  

dcdiag /a  

To test replication :  

repadmin /replsum  

repadmin /showrepl   

Am I ok ?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-10*

Hello,  

Thanks you for your answer.  

I agree totally for backup + dfs-r and forest level (2008+ too)  

You didn't write when I need to promote my new DC.  

I suppose there will be some issue between renaming old DC and new DC take this name...  

I need to do it during maintenance window.
