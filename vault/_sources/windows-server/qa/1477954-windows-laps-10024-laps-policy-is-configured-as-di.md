---
title: "Windows LAPS - 10024 LAPS policy is configured as disabled"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1477954/windows-laps-10024-laps-policy-is-configured-as-di
question_id: 1477954
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Windows LAPS - 10024 LAPS policy is configured as disabled

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1477954/windows-laps-10024-laps-policy-is-configured-as-di (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We had a working Microsoft LAPS. However, we decided we wanted Windows LAPS so we:

-  deleted the legacy LAPS GPO, create new LAPS GPO using new admx

-  uninstalled the legacy LAPS GUI from the server

-  uninstalled the legacy LAPS agent from workstations

-  deployed the new laps https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-scenarios-windows-server-active-directory [

](https://i.stack.imgur.com/iQYGz.png)

However, the Windows LAPS is doing nothing. The event viewer is showing successions of events 10003, 10024, and 10004. 10024 LAPS policy is configured as disabled.

[

](https://i.stack.imgur.com/wzz0z.png)

Moreover, the ADUC computer properties are showing the LAPS tab but blank account name and password. [

](https://i.stack.imgur.com/RRq39.png)

We rerun the configuration but we cannot seem to find what is amiss. We checked the Windows hotfix and we have the "2023-11 Cumulative Update for Windows Server 2019 for x64-based Systems (KB5032196)". 

We have Windows Server 2019 but we have "Windows 2012 R2" domain functional level.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-03-04*

Was able to solve the problem: The test system was on an old patch level, November 2022. The new LAPS was introduced mid 2023.

What I still can't understand and what leads me to the wrong troubleshooting way is that Find-LapsADExtendedRights still doesn't show the "Domain Admins" as a result.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-03-04*

Have also found the problem cause: The test system was on an old patch level, from November 2022. And the new LAPS was introduced in mid 2023.

After trying with another testsystem and after updating birappl18, LAPS worked as expected.  

What I still can't understand and what leads me to the wrong way is that the "Find-LapsADExtendedRights" still shows no output, despite the domain admins have the right to decrypt passwords (LAPS default configuration).

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-04*

Hello, I'm just joining in. Solving the same problem. Everything should be setup correctly according to "Get started with Windows LAPS and Windows Server Active Directory" article by MS. But it's not working. Event log looks same as OPs. LAPS policy is applied to the OU (and verified). "Get-LapsADPassword -Identity ComputerName -AsPlainText" command returns nothing.

edit my solution: it's working now. There was an error Error code: 0x80070032 on the client machine (LAPS failed to update Active Directory with the new password. The current password has not been modified.) which pointed me to right direction. 

I tried to manually add permissions to write LAPS password - even when I did it via powershell before (Set-LapsADComputerSelfPermission) and it didn't help.

Now my solutions was "Restore defaults" at Advanced security at the computer object. It immediately startet to work.

it has probably something to do with previous version of LAPS I was testing.

I hope this could help you guys too.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-03-01*

Hello @nelson figueroa  , have you been able to solve this problem? Have exactely the same issue.Franz

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-05*

Hello Nelson Figueroa,  

Thank you for posting in Q&A forum.  

1.Please check The Windows Server Active Directory schema have been updated prior to using Windows LAPS.

2.Please check have you run command :Set-LapsADComputerSelfPermission -Identity OUname.  

3.Please check the problem occurs on one machine or all the machines in the OU.  

4.Please check if the user you are using have permission to view the password.  

5.Please check if you can Retrieve a password from Windows Server Active Directory via command below.  

Get-LapsADPassword -Identity ComputerName -AsPlainText  

6.Please check if all the machines or if this machine has the Administrator account named "iohadmin".

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
