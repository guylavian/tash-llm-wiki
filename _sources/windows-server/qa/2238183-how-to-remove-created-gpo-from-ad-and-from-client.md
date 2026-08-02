---
title: "How to remove created GPO from AD and from client Computers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2238183/how-to-remove-created-gpo-from-ad-and-from-client
question_id: 2238183
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to remove created GPO from AD and from client Computers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2238183/how-to-remove-created-gpo-from-ad-and-from-client (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have created many GPOs( for example : local Admin right, RDP right) on my AD windows server 2019 and deploy it to many Clients.

Now I have to remove all these created GPOs from AD and from All Windows Client machines.

I want to remove these GPOs safely and without residue. 

How can I do that efficiency?

With PW script or create a remove GPO?

Regards

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-25*

Hello PerserPolis-1732,  

Thank you for posting in Q&A forum.  

Here is some other information for your references.

1.Deleting or removing or disabling GPO objects via Group Policy Management will make the client machines do not apply the group policy settings (except security setting policies) within these GPO objects after the group policy refresh on client machines (For computer configuration, the group policy will refresh when you restart the machines. For user configuration, the group policy will refresh when you sign out and sign in the domain accounts. And the group policy will update automatically after by default 90-120 minutes in the backgroup), it will not remove the AD domain accounts or AD groups. 

Background Refresh of Group Policy

https://learn.microsoft.com/en-us/previous-versions/windows/desktop/Policy/background-refresh-of-group-policy

2.If you want to remove or delete AD domain accounts and AD groups. You can open Active Directory Users and Computers, and find the domain accounts and domain groups, then delete them.

Please note: Please back up the Domain Controllers using built-in Windows server backup tool one by one (if you do not have recent Domain Controller backups). Or if you have enabled Recycle Bin on domain controller, you can restore the deleted AD objects if you still want them.

Enable and use Active Directory Recycle Bin

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/adac/active-directory-recycle-bin?tabs=adac

3.Security settings can persist even if a setting is no longer defined in the policy that originally applied it.

Security policy settings

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/security-policy-settings#persistence-of-security-settings-policy

4.You can also check the group policy result that applied on client machines by the steps below.

For checking Computer Configuration within gpresult, we can follow steps below. 

Logon this machine using administrator account. 

Open CMD (run as Administrator). 

Type gpresult /h C:\gpo.html and click Enter. 

Open gpo.html and check gpo setting under "Computer Details". 

For checking User Configurations within gpresult, we can follow steps below. 

Logon the machine using normal domain user account (that applies this gpo). 

Create a folder named F1 in C drive. 

Open CMD (do not run as Administrator). 

Type gpresult /h C:\F1\gpo.html and click Enter. 

Open gpo.html and check gpo settings under "User Details".

I hope the information above is helpful. 

If you have any questions or concerns, please feel free to let us know. 

Best Regards, 

Daisy Zhou 

============================================ 

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-24*

Hi,

I propose a 2 step task here.

Back up Group Policy Objects (GPOs) before deletion is a crucial step to ensure you can restore them if needed. Here are the steps to back up GPOs using both the Group Policy Management Console (GPMC) and PowerShell:

Using Group Policy Management Console (GPMC)

Open GPMC:

Open the Group Policy Management Console by typing gpmc.msc in the Run dialog (Win + R).

Navigate to Group Policy Objects:

In the left pane, expand your domain and navigate to "Group Policy Objects."

Backup All GPOs:

Right-click "Group Policy Objects" and select "Back Up All."

In the "Back Up Group Policy Object" dialog box, enter the path to the location where you want to store the GPO backups and enter a description.

Click "Back Up" to start the backup process1.

Using PowerShell

Open PowerShell:

Open PowerShell with administrative privileges.

Backup Specific GPO:

Use the following command to back up a specific GPO:

Backup-GPO -Name "GPOName" -Path "C:\GpoBackups" -Comment "Backup before deletion"

Backup All GPOs:

Use the following command to back up all GPOs in the domain:

Backup-GPO -All -Path "C:\GpoBackups"

PART 2

Removing and disabling all Group Policy Objects (GPOs) from a network can be done using the Group Policy Management Console (GPMC) or PowerShell. Here are the steps for both methods:

Using Group Policy Management Console (GPMC)

Open GPMC:

Open the Group Policy Management Console by typing gpmc.msc in the Run dialog (Win + R).

Navigate to Group Policy Objects:

In the left pane, expand your domain and navigate to "Group Policy Objects."

Select Multiple GPOs:

In the right pane, you can select multiple GPOs by holding down the Ctrl key and clicking on each GPO you want to delete.

Alternatively, you can select a range of GPOs by holding down the Shift key and clicking the first and last GPO in the range.

Delete Selected GPOs:

Right-click on the selected GPOs and choose "Delete."

Using PowerShell

Open PowerShell:

Open PowerShell with administrative privileges.

List All GPOs:

Use the following command to list all GPOs:

Get-GPO -All

Delete Specific GPOs:

Use the following command to delete specific GPOs by their names:

Remove-GPO -Name "GPOName1"

Remove-GPO -Name "GPOName2"

Delete Multiple GPOs in a Loop:

If you have a list of GPO names, you can delete them in a loop:

$gpoNames = @("GPOName1", "GPOName2", "GPOName3")

foreach ($gpoName in $gpoNames) {

```
Remove-GPO -Name $gpoName
```}

Disabling GPOs

Open GPMC:

Open the Group Policy Management Console by typing gpmc.msc in the Run dialog (Win + R).

Navigate to Group Policy Objects:

In the left pane, expand your domain and navigate to "Group Policy Objects."

Disable GPOs:

Right-click on the GPO you want to disable and select "GPO Status" > "All Settings Disabled."
```
