---
title: "Get command status from Active Directory Domain machines"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2187043/get-command-status-from-active-directory-domain-ma
question_id: 2187043
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Get command status from Active Directory Domain machines

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2187043/get-command-status-from-active-directory-domain-ma (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We need to get the status of few commands from a domain environment of around 400 machines. All may be windows 10 and windows 11 machines. Need to run this activity couple of times in a day. 

This may required few Power Shell commands with admin credentials OR we may run this from GPO. But I don't know where can we save the status result from machines

(Power Shell script running is disabled via GPO so we may need to run PowerShell commands directly)

Commands status result are required (windows 10/11):

-  Last Windows update status

-  Bit Locker installed and configured status

-  Total Local Admin users

-  LAPs is installed on not

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-12*

Hi ZahidHaseeb,

Thank you for posting in the Microsoft Community Forums.

The following is a general step-by-step procedure and strategy for gathering the required information:

-  Prepare PowerShell scripts

First, you need to write one or more PowerShell scripts to obtain the required information. These scripts can be designed to execute on a remote machine and return results.

Sample Script Highlights:

Last Windows Update Status:

Use Get-WindowsUpdateLog (if installed) or parse the C:\Windows\WindowsUpdate.log file to get the most recent update information.

Another way is to check the win32_quickfixengineering WMI class.

BitLocker installation and configuration status:

Use the manage-bde -status command and parse its output to get the status of BitLocker.

Alternatively, use Get-BitLockerVolume (if supported by the PowerShell version).

Total number of local administrator users:

Use the net localgroup administrators command and parse the output to count the number of members.

Alternatively, use a WMI query to retrieve the Win32_GroupUser class where GroupComponent="Win32_Group.Domain='[Domain]',Name='Administrators'".

LAPs (Local Administrator Password Solutions) installation status:

Check specific registry entries or files to confirm that LAPs is installed (this depends on the specific implementation of LAPs).

If there is no direct way to detect this, you may need to rely on event logs or specific service status.

-  Configuring Remote PowerShell

As running scripts directly may be limited, you need to ensure that remote PowerShell (PSRemoting) is enabled on the target machine. This usually involves setting up the WinRM (Windows Remote Management) service and configuring appropriate firewall rules.

-  Deployment and Execution

Use GPO (if allowed):

If the GPO does not completely disable PowerShell, you can attempt to deploy a scheduled task through the GPO that runs PowerShell scripts and collects data at specified times.

Direct Run:

If this is not possible via GPO, you may consider setting up a scheduled task manually on each machine, or using a remote PowerShell session from a central management server to trigger the script.

-  save the results

Central server:

Save the output of the script to a shared location on each machine or send it over the network to a central server.

You can use Invoke-Command combined with the -ComputerName parameter to execute the script remotely and collect the results to the local machine.

Database or log files:

Store collected data in a database for further analysis or simply save it in a text file or CSV file.

-  Monitoring and Automation

Set up monitoring mechanisms to track the execution of scripts and the quality of data collected.

Use automation tools (e.g. Azure Automation, System Center Orchestrator, etc.) to further streamline the process.

Cautions

Permission issues: Ensure that the account executing the script has sufficient permissions to access the remote machine and collect the required information.

Security: Use encrypted connections when transferring data and ensure that sensitive information is properly protected.

Performance impact: Running scripts frequently on a large number of machines may have an impact on network and system performance, so schedule the execution time and frequency appropriately.

Best regards

Neuvi
