---
title: "How to fix this GPO error?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2190092/how-to-fix-this-gpo-error
question_id: 2190092
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# How to fix this GPO error?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2190092/how-to-fix-this-gpo-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an error when opening the group policy management on Windows Server 2019, how can I fix that please?

## Answer (community) — community member

*upvotes: 1 · updated: 2023-09-20*

Hello Daisy,

-  The first one is when I open gpo management and the second when I try to edit one, the list is there but can't edit

-  I have another domain controller (old one)

-  copied the logs from files

-  the sysvol is there but no policy or script files on it

- 

Other reports show all successful

Replication Summary Start Time: 2023-09-20 10:00:04  

Beginning data collection for replication summary, this may take awhile:  

  .....  

Source DSA          largest delta    fails/total %%   error  

 DM-DC-02                  06m:08s    0 /   5    0    

 SVR-MAIN                     :51s    0 /   5    0    

Destination DSA     largest delta    fails/total %%   error  

 DM-DC-02                     :52s    0 /   5    0    

 SVR-MAIN                  05m:35s    0 /   5    0    

Will it work fine just by copying policies from the old server?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-21*

Hello Tamer Elmenshawy1,  

Thank you for your reply.  

1.So you have only two Domain Controllers in the domain (the old one and this new Windows Server 2019), am I right?  

2.Did you add this Windows Server 2019 recently? If so, did this issue arise after the new 2019 domain control joined?  

3.Did the issue occur suddenly (but everything is working fine in the past)? If so, have you made any changes in AD environment recently?  

4.Based on "4.the sysvol is there but no policy or script files on it", did you mean "the sysvol is there but no policy or script files" on this Windows Server 2019, however the sysvol is there WITH policy and script files on old DC?   

5.What is the domain functional level and forest functional level?  

6.What is the OS version of the old DC?  

7.What is the SYSVOL type? FRS or DFSR? See checking method below.  

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\LocalState registry subkey. If this registry subkey exists and its value is set to 3 (ELIMINATED), DFSR is being used. If the subkey does not exist, or if it has a different value, FRS is being used.   

8.Check if you can open gpo management and edit any GPO on old DC.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-20*

Hello Tamer Elmenshawy1,  

Thank you for posting in Microsoft Community forum.  

Please check or troubleshoot the issue as below.  

1.When do you receive the error message above? Do you receive the error message when you open group policy management or edit one GPO object?  

2.Do you have more than one Domain Controller in your domain?   

3If you have more than one DCs in your domain, please check if AD replication works fine in your domain. Please run commands below on PDC.  

repadmin /showrepl >c:\rep1.txt  

repadmin /replsum >c:\rep2.txt

repadmin /showrepl * /csv >c:\repsum.csv  

4.Check if the SYSVOL is working fine in your domain. Please check the SYSVOL replication status on Domain Controllers.  

For example 1:  

If you have two Domain Controllers in this domain.  

Create a file named F1 under path \domain.com\SYSVOL\domain.com\policies on DC1.  

Create a file named F2 under path \domain.com\SYSVOL\domain.com\policies on DC2.  

Check if F1 is replicated to DC2 and if F2 is replicated to DC1.  

For example 2:  

If you have three Domain Controllers in this domain.  

Create a file named F1 under path \domain.com\SYSVOL\domain.com\policies on DC1.  

Create a file named F2 under path \domain.com\SYSVOL\domain.com\policies on DC2.  

Create a file named F3 under path \domain.com\SYSVOL\domain.com\policies on DC3.  

Check if F1 and F2 is replicated to DC3  

And check if F1 and F3 is replicated to DC2.  

And check if F2 and F3 is replicated to DC1.  

5.The system cannot find the path specified. This issue may occur when the GPO container is not present in the SYSVOL folder. If you have multiple DCs in your domain, you can restore the GPO container from another DC.  

For example:  

Assue {CCF5CDA2-2935-4C38-B945-59EB4E60EDBD} exists on DC1, but not in DC2, you can try to copy {CCF5CDA2-2935-4C38-B945-59EB4E60EDBD} from DC1 to DC2.  

  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
