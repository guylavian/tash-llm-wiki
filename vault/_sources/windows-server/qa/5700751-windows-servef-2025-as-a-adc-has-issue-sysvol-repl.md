---
title: "windows servef 2025 as a adc has issue sysvol replication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5700751/windows-servef-2025-as-a-adc-has-issue-sysvol-repl
question_id: 5700751
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor", "Q&A User"]
---
# windows servef 2025 as a adc has issue sysvol replication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5700751/windows-servef-2025-as-a-adc-has-issue-sysvol-repl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i have 3  domain one pdc is 2022 and 2 adc is 2026 and created 2025 server as a adc and sysvol and netlog folder is missing and followed fix sysvol article but in ADSIEDIT.MSC  tool which 2025 server adc is not showing netlogon and policy in sysvol folder is not showing 3 domain controller is working fine replication is okk in new server 2025 server  has issue netlogon folder and sysvol is showing but policy is not showing below contect is missing in new server 

```
→ CN=SYSVOL Subscription
→ CN=Domain System Volume
→ CN=DFSR-LocalSetting
```

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-01-26*

Hi Mohammed Ahmed,

Just checking in, were you able to get the issue resolved? If so, it would be great if you could mark the answer as Accepted so others in the community can benefit from your experience. Have a nice day!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2026-01-10*

authoritative/non-authoritative restore steps outlined in Microsoft’s DFSR documentation i tried these documents on working pdc 2022 and adc 2016  but adc 2025 has no SYSVOL Subscription, Domain System Volume, and DFSR-Local Settings objects in ADSIEdit. any other steps how to get these settings.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-01-09*

Hi Mohammed Ahmed,

From what you’ve shared, replication across your existing domain controllers is healthy, but the new 2025 ADC is missing the SYSVOL Subscription, Domain System Volume, and DFSR-LocalSettings objects in ADSIEdit. This typically indicates that the Distributed File System Replication (DFSR) configuration did not complete properly during domain controller promotion. I recommend verifying that the DFSR service is running on the 2025 server and checking the Event Viewer (DFS Replication logs) for errors. You may also need to run the `dfsrdiag pollad` command to force the server to read its Active Directory configuration, and confirm that the server is listed under the CN=Domain System Volume container in ADSIEdit.

If the objects are still missing, you may need to reinitialize SYSVOL replication by following the authoritative/non-authoritative restore steps outlined in Microsoft’s DFSR documentation. In some cases, demoting and re-promoting the ADC can be the cleanest way to ensure SYSVOL and Netlogon are provisioned correctly.

Once replication is healthy and the policies appear under SYSVOL, your new ADC should function as expected. If this guidance helps resolve your concern, please don’t forget to press “Accept Answer” so I know it worked for you.

Jason.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-01-09*

It seems that your Windows Server 2025 ADC is experiencing issues with SYSVOL and NETLOGON shares not replicating correctly. Here are some steps you can take to troubleshoot and potentially resolve the issue:

-  Check Replication Status: Ensure that the replication status is healthy across all domain controllers. You can use the command `REPADMIN /SHOWREPS` to check the replication status between your servers.

-  Event Viewer: Check the Event Viewer for any errors or warnings related to SYSVOL and NETLOGON shares. Look specifically for DFS Replication event logs that might indicate issues with the replication process.

-  DFS Replication State: Use the command to check the state of the SYSVOL replicated folder:

```
For /f %i IN ('dsquery server -o rdn') do @echo %i && @wmic /node:"%i" /namespace:\\root\microsoftdfs path dfsrreplicatedfolderinfo WHERE replicatedfoldername='SYSVOL share' get replicationgroupname,replicatedfoldername,state
```

   Ensure that the state is reported as normal (state 4).

-  Content Freshness: Verify if content freshness is enabled on the affected domain controller. You can check this with:

```
wmic.exe /node:%computername% /namespace:\\root\microsoftdfs path DfsrMachineConfig get MaxOfflineTimeInDays
```

   If content freshness protection is triggered, you may need to resume replication.

-  Rebuild SYSVOL: If the above steps do not resolve the issue, you may need to consider rebuilding the SYSVOL tree. This involves backing up the current SYSVOL contents, disabling the membership of the affected domain controller, and then re-enabling it after ensuring a healthy replication topology.

-  ADSIEDIT.MSC: Since you mentioned that the 2025 server is not showing the expected entries in ADSIEDIT.MSC, ensure that the DFSR service is running and that the server is properly configured to participate in the replication group.

If these steps do not resolve the issue, you may need to consult further documentation or consider reaching out to Microsoft support for more in-depth assistance.

References:

-  Troubleshoot missing SYSVOL and NETLOGON shares on Windows domain controllers

-  How to troubleshoot missing SYSVOL and Netlogon shares
