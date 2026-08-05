---
title: "Migrate FSMO from PDC to BDC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/47561/migrate-fsmo-from-pdc-to-bdc
question_id: 47561
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Migrate FSMO from PDC to BDC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/47561/migrate-fsmo-from-pdc-to-bdc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have an SRV1 server with Windows Server 2012 R2 that works as a Domain Controller, since it is starting to have hardware problems I also considered it appropriate for greater security to put on another SRV2 server always with Windows Server 2012 R2 to do it I installed the operating system and then I added the server to the domain as a BDC  

which allowed me to promote SRV2 to Backup Domain Controller.  

Now wanting to permanently discontinue SRV1  

I get to open Active Directory Users and computers in Domain Controller I see both the SRV1 and SRV2 servers but when I go to the Operations Master to move the master from SRV1 to SRV2, I go to make the change both for RID PDC and infrastructure tells me that to transfer the operations master role to another computer you must first connect to it. In fact, both in the Master Operations case and in the one below it is shown only in the name SRV1.  

Where am I doing wrong? What mistake can I have made? Why even if you see the two domain controllers tells me that the computer must be connected first?  

Thanks for the support and help.  

I need to use only SRV2 and afetr add a new server SRV2

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-29*

In AD, right click the domain and choose "change domain controller",  then select your new DC.  That's what it means by "first connect to it".  You always transfer roles to the DC you've connected to.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-07-16*

You can change the MMC's current connection by right-clicking top of tree then Change Domain Controller      

      

or from cmd.exe      

ntdsutil      

roles      

connections      

connect to server <servername>      

      

https://support.microsoft.com/en-us/help/255504/using-ntdsutil-exe-to-transfer-or-seize-fsmo-roles-to-a-domain-control      

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-07-16*

Hi,  

Thanks for sharing here!  

Based on my experience, before making the big changes in your environment, backup the DCs.  

Also ,after the promotion of the new DC, make sure that the new DC are working  well , and the replication between the 2 DCs are good.You can confirm that by the command :  

Dcdiag /v >c:\dcdiag.log  

Repadmin /showrepl >C:\repl.txt   

Then if everything works well , transfer the FSMO role by referring the following steps in the link:  

https://support.microsoft.com/en-us/help/255504/using-ntdsutil-exe-to-transfer-or-seize-fsmo-roles-to-a-domain-control  

If still the same error happens , please tell which step the error happens in.  

Best Regards,
