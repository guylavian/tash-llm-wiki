---
title: "SCCM generate reports to get device info from collection"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1000568/sccm-generate-reports-to-get-device-info-from-coll
question_id: 1000568
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
answer_author_roles: ["Q&A User"]
---
# SCCM generate reports to get device info from collection

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1000568/sccm-generate-reports-to-get-device-info-from-coll (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear experts,    

We are in need of getting the Display Adapter info (that we can see from Device Manager) from a specific collection of computers. Is there any report option that we can use to get it within SCCM console or SQL server?    

I tried to run following in SQL server but it gave me all the computer info within our domain and seems the Display Adapter info was not up to date?    

```
Select    
SD.Name0 'E206*',  
VC.Name0 'Video Card',  
Convert(VarChar, VC.AdapterRam0 / 1024) + ' MB'  
From v_R_System SD  
Join v_Gs_Video_Controller VC on SD.ResourceID = VC.ResourceID  
Where VC.Name0 <> 'ConfigMgr Remote Control Driver'  
Order By SD.Name0
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-12*

Hi,    

You are using the right way to get the Display Adapter info.    

For the Display Adapter info was not up to date, the hardware inventory will scan and update regularly.  Also we could manually force a hardware inventory cycle.    

    

We could use the Resource Explorer tool to view and troubleshoot for one computer.    

To open the Resource Explorer, open the SCCM console and navigate to Assets and Compliance / Devices     

Right click on any device and select Start then Resource Explorer    

    

For more in-depth troubleshooting, please refer to the following link:    

Troubleshooting Hardware Inventory in SCCM
