---
title: "newly promoted domain controller not functioning"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/430698/newly-promoted-domain-controller-not-functioning
question_id: 430698
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# newly promoted domain controller not functioning

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/430698/newly-promoted-domain-controller-not-functioning (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Team,  

newly promoted domain controller(domain controller 2) not functioning. when we create any new user or changed password of existing user that changes not sync with other Domain Controller(domain controller 1). but at the same time when we made any changed on domain controller 1 that changed replicated on domain controller 2. that means one way replication happen between two DC.  

please hep on this

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-24*

Hi,  

Welcome to share your current situation if there are any updates.  

Please feel free to let us know if you need further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-21*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-15*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-11*

Most of the cases it would also be a new domain controller for a new forest. In most cases, you would need to update the flag as below.    

Open Regedit    

Browse to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters    

Set SysVolReady from 0 to 1    

Close Regedit    

This will create the SYSVOL share. If the NETLOGON share is not created you would need to create the folder scripts in C:\Windows\SYSVOL\domain. When this is done, restart the NETLOGON service.    

This is the easy part. In some cases, although the NETLOGON and SYSVOL shares are working, no group policies or scripts are being replicated using the DFS or DFRS.    

We can verify the replication by running the following command.    

For /f %i IN ('dsquery server -o rdn') do @Echo   %i && @wmic /node:"%i" /namespace:\root\microsoftdfs path dfsrreplicatedfolderinfo WHERE replicatedfoldername='SYSVOL share' get replicationgroupname,replicatedfoldername,state    

The states should translate as below    

reference： http://www.noelpulis.com/fix-missing-sysvol-and-netlogon-after-domain-controller-promotion/      

Hope this information can help you    

Best wishes    

Vicky

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-10*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\problemworkstation.txt`  

then put `unzipped` text files up on OneDrive and share a link.
