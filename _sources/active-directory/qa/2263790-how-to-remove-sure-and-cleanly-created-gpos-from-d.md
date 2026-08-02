---
title: "How to remove sure and cleanly created GPOs from DC with Windows 2019 Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2263790/how-to-remove-sure-and-cleanly-created-gpos-from-d
question_id: 2263790
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# How to remove sure and cleanly created GPOs from DC with Windows 2019 Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2263790/how-to-remove-sure-and-cleanly-created-gpos-from-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have created some GPOs for RDP and Local Admin for some Clients machines. Now I want to remove these sure and cleanly from DC and Client machines.

What is the best method to do that?

for example:

I have created a group named "LOCAL_ADMIN" and put some Users Member in that. Created a GPO named "LOCAL_ADMIN" and give him the "Administrator(build.in)".

Now I wan to remove it really and leave no residue.

I know I can remove the GPO easy with GPO Console, but I think it is not the right way.

best Regards and thank you for help

Nick

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-05-08*

Hello,

  Thank you for posting the question on Microsoft Windows forum!

  Based on your query of removing GPO cleanly with assurance from DC and client machines, you can try the following steps with GPMC and Powershell command:

Step 1: Backup Your GPOs

```
Before removing anything, it's always best practice to **back up your GPOs** in case you need to restore them later.
```

-  Using Group Policy Management Console (GPMC):

-  On command prompt, type gpmc.msc

-  Navigate to Group Policy Objects.

-  Right-click Group Policy Objects → Select Back Up All.

-  Choose a backup location and click Back Up.

-  Using PowerShell:

-  Backup-GPO -Name "GPOName" -Path "C:\GpoBackups" -Comment "Backup before deletion for individual  GPO"

-  Backup-GPO -All -Path "C:\GpoBackups"

Step 2: Remove GPOs from DC and Clients

-  Navigate to Group Policy Objects.

-  Select the GPOs you want to remove.

-  Right-click and choose Delete.

-  Using PowerShell:

-  Remove-GPO -Name "GPOName"

Step 3: Force Policy Update on Clients

   After removing the GPOs, force an update on client machines to ensure they no longer apply the policies. Run the following command either on command prompt or Powershell.

-  gpupdate /force

Step 4: Verify Removal

-  On command prompt, run the command rsop.msc on elevated mode.  

-  On Powershell, run Get-GPO -All    On the other hand, you can check the Unique ID of the removed GPO.  The following is my example:

Before Deleting the GPO.

-  I have a GPO named "Hide F Drive" that I intend to remove from my AD environment  

-  navigate to this path C:\Windows\SYSVOL\sysvol\contoso.com\Policies to locate the GUID of removing GPO.  

-  Running the  Powershell to check it.  

After Deleting the GPO.

-  The GUID of removed GPO disappears  

-  Checking the Powershell command to make sure the deleted GPO "Hide F Drive" is removed successfully.    Hope the above information is helpful
