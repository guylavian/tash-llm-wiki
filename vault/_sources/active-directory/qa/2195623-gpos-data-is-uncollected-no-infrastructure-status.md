---
title: "GPOs Data is uncollected: No Infrastructure Status information exist for this domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195623/gpos-data-is-uncollected-no-infrastructure-status
question_id: 2195623
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 6
qa_tags: []
---
# GPOs Data is uncollected: No Infrastructure Status information exist for this domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195623/gpos-data-is-uncollected-no-infrastructure-status (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, my name is Williams

How can I resolve this issue: a processing error occurred collecting data using this base domain controller. Please change the base domain controller and try again.

This is on the Windows Server 2016 group policy management console.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-23*

Hello williams.ighofose, 

Thank you for posting on the Microsoft Community Forum.

The error message you are seeing indicates that there is an issue with the base domain controller that you are using to collect data for your GPOs. 

You can try to click domain name and click "Detect Now" button (below).  

In my case below (in my lab), there is only one Domain Controller in the domain.  

If there is still such error message, you can try changing the base domain controller to a different one if you have more than one Domain Controllers in the domain and then try collecting data again.

To change the base domain controller, follow these steps:

-  Open the Group Policy Management Console.

-  Right-click the domain that you want to collect data for, and then click "Change Domain Controller".

-  In the "Change Domain Controller" dialog box, select a different domain controller from the list, and then click "OK".

-  Try collecting data again.  

If there is more than one Domain Controllers, you can try to check the AD replication status and SYSVOL replication status. Please ensure AD replication works fine and SYSVOL replication status is OK.

Run commands below on PDC to check AD replication.  

repadmin /showrepl >C:\rep1.txt  

repadmin /replsum >C:\rep2.txt  

repadmin /showrepl * /csv >c:\repsum.csv  

Check SYSVOL replication status as below (I assume there are two DCs in the domain):

Create new file (file1) or new folder in the path \domain.com\SYSVOL\domain.com\Policies on DC1.  

Create new file (file2) or new folder in the path \domain.com\SYSVOL\domain.com\Policies on DC2.  

Check if file1 and file2 are in \domain.com\SYSVOL\domain.com\Policies on both DC1 and DC2  

I hope you the information above is helpful.

If you have any questions or concerns, please do not hesitate to let us know.

Best Regards,

Daisy Zhou
