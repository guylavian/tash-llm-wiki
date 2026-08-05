---
title: "netlogon ve sysvol klasörlerinin eşitlenmemesi"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2198694/netlogon-ve-sysvol-klas-rlerinin-e-itlenmemesi
question_id: 2198694
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# netlogon ve sysvol klasörlerinin eşitlenmemesi

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2198694/netlogon-ve-sysvol-klas-rlerinin-e-itlenmemesi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Eski sunucumu ortadan kaldırmak için 2022 server sunucumu additional domain controller olarak kurdum. Fakat netlogon ve sysvol klasörleri oluşmadı. DFS Replikasyon yaptığını görüyorum. 4614 hatası alıyorum.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-23*

Hello Levent YILMAZ1,  

Thank you for posting in Microsoft Community forum.  

1.What is your forest functional level and domain functional level?  

2.How many Domain Controllers are there in your domain except this 2022 DC? What are the OS version of those Domain Controllers?  

3.What is the SYSVOL replication engine? Check method below:  

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\LocalState registry subkey. If this registry subkey exists and its value is set to 3 (ELIMINATED), DFSR is being used. If the subkey does not exist, or if it has a different value, FRS is being used.  

4.Where did you see error 4614?  

5.Please check the AD replication between all Domain Controllers in the domain.  

Run the commands below on PDC.  

repadmin /showrepl >C:\rep1.txt  

repadmin /replsum >C:\rep2.txt

repadmin /showrepl * /csv >c:\repsum.csv  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
