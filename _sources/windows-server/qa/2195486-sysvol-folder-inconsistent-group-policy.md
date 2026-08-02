---
title: "SYSVOL FOLDER INCONSISTENT GROUP POLICY"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195486/sysvol-folder-inconsistent-group-policy
question_id: 2195486
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# SYSVOL FOLDER INCONSISTENT GROUP POLICY

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195486/sysvol-folder-inconsistent-group-policy (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,      

```
I have one Windows Server 2019 and 3 Windows Server  2016 Domain controllers all are working good and replication status is healthy.  The only problem I am facing is when I am trying to edit an old policy with in the Group Policy Folder using Active Directory Management Console and it gives me the below error.
```

Thanks

Skakhttps://learn-attachment.microsoft.com/api/attachments/543b12de-30a7-4ff4-aeff-d845ef94c850?platform=QnA

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-29*

Hello   

Good day!  

You mean you will see the error message when you click any group policy object?  

If so, you can try to compare the permissions on this GPO on different machine.  

Meanwhile, what change did you make before the error message occurs?  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-29*

Hello,

 i have every thing and all logs are perfect , please check the attached[![](https://learn-attachment.microsoft.com/api/attachments/04f2bc86-5c07-46fb-84f5-6f89638b6f0f?platform=QnA"https://we.tl/t-s2wOZIeHWF" title="we.tl" rel="ugc nofollow">https://we.tl/t-s2wOZIeHWF

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-29*

Hello Syed Khairuddin,  

Good day!  

1.Please check AD replication status. Run commands below on PDC.  

repadmin /showrepl >C:\rep1.txt  

repadmin /replsum >C:\rep2.txt

repadmin /showrepl * /csv >c:\repsum.csv  

2.If AD replication, please check SYSVOL replication engine, if it is DFSR.  

Check method:  

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\LocalState registry subkey. If this registry subkey exists and its value is set to 3 (ELIMINATED), DFSR is being used. If the subkey does not exist, or if it has a different value, FRS is being used.  

3.Check SYSVOL replication status.

Are the folders under C:\Windows\SYSVOL\domain\Policies the same on all the DCs?  

You can try to create file1 under C:\Windows\SYSVOL\domain\Policies on DC1 and check if the file is replicated to other DCs.  

You can try to create file2 under C:\Windows\SYSVOL\domain\Policies on DC2 and check if the file is replicated to other DCs.

You can try to create file3 under C:\Windows\SYSVOL\domain\Policies on DC3 and check if the file is replicated to other DCs.

You can try to create file4 under C:\Windows\SYSVOL\domain\Policies on DC4 and check if the file is replicated to other DCs.  

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-28*

My bad it was wrong screenshot question, when I Click any policy with the GPO Folder I get this error

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-28*

Hello Syed Khairuddin,  

Thank you for posting in Microsoft Community forum.

 I am sorry, I do not understand what folders you cannot see?   

Would you please tell us in details?

 

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
