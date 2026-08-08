---
title: "scheduled task via GPO doesn't work"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2199823/scheduled-task-via-gpo-doesnt-work
question_id: 2199823
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# scheduled task via GPO doesn't work

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2199823/scheduled-task-via-gpo-doesnt-work (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hii! I need to deploy package.msi without startup to n client because these are all server and they cant restart.  

I cant use psexec or sccm tools   

I think the only way is: scheduled task in gpo, but doesnt work.   

In the task i set: action: Create name: deploy NT AUTHORITY\System user account Run whether user is logged on or not Run with highest privileges triggers tab: Once time - status enabled action tab: Start a program; program/script: powershell.exe add arguments: -NonInteractive -ExecutionPolicy Bypass \netsharedpath\package.msi condition: start only if the following network connection is available: any connection settings: allow task to be run on demand

what's wrong?  

i see no error in gpo log / task scheduler log

windows server 2019  

I edit my gpo from the gpom and add my scheduled task under computer because I need it to be deployed on all the computers within the OU  

I don't see any errors in the logs, and the task is not created and consequently the.msi is not installed

I tried starting msiexec.exe instead of powershell, the result is the same. in the event viewer under group policy I have no errors, the gpo apparently is not taken into consideration also because it does not create any tasks. I don't have a log from which to troubleshoot  

Manual Trigger Check: Try manually triggering the scheduled task from the Task Scheduler on a client machine to confirm it can execute as expected. I can't do that because the task I create in the GPO is not created in the task scheduler and therefore I cannot start it on demand the msiexec and/or the script I created work if started manually on the client. What doesn't work is the scheduled task, I don't even understand how to find logs on the scheduled task since if I tell it to create it it doesn't create it or execute it  

EDIT:

so: if I create the task manually from the task scheduler on the client, it works perfectly. 

 If I create the task in the GPO --> computer configuration --> preferences --> control panel settings --> scheduled task 

 --> new task and then the configuration parameters that I mentioned in the first message, he does not create this task in the client. 

 After some tests I discovered that the script did not start directly from the share folder due to execution policy problems, so I added 2 fundamental steps: create a folder on the client, copy the script from the share locally, and finally start the script locally. 

Now the task is configured perfectly and if I create it manually on the client, with these latest changes, it works. 

However, from the GPO it doesn't work, or rather only if I restart the client I see the task created in the task scheduler without it ever having been executed.   

I need a solution WITHOUT REBOOTTING THE CLIENTS.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-19*

Per prima cosa partiamo dai parametri per evitare il reboot dopo l'installazione del file msi,

 devi necessariamente usare con msiexec.exe /norestart e /qb (quest'ultimo dato che si tratta di una installazione non interattiva).

Potresti riportare la linea di comando che usi per l'installazione nel tuo task schedulato, grazie.

Per installare un software in modo automatico, hai tante opzioni ne elenco alcune.

1 Installazione msi via GPO :

https://learn.microsoft.com/it-it/troubleshoot/windows-server/group-policy/use-group-policy-to-install-software

2 installazione usando uno startup script definito nelle GPO(soluzione che preferisco):

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn789196(v=ws.11)#how-to-assign-computer-startup-scripts

3 creare un task schedulato via gpo

Nel tuo caso hai verificato sul client cosa succede con un gpresult ?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-11*

I am also having the same issue. Tried everything , GPO applied but no Schedule task created.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-10*

Hi jonathandijv,

Thank you for posting in the Microsoft Community Forums.

  

To view logs related to scheduled tasks in Windows, you can follow these methods:

-  Using Event Viewer:

-  Open "Event Viewer" by searching for it in Windows.

-  In Event Viewer, expand "Windows Logs" and select "Application" log.

-  In the right pane, you can see entries related to scheduled tasks. These entries will display detailed information about the success or failure of scheduled task executions, including execution time, results, etc.

-  Viewing Scheduled Task Log Files:

-  Scheduled task log files are typically located at `%SystemRoot%\SchedLgU.txt`.

-  You can open this file using a text editor (such as Notepad) and view the scheduled task execution history. These log files record information such as start time, end time, execution result, etc.

-  Using PowerShell:

-  Open a PowerShell terminal.

-  Use the `Get-ScheduledTask` command to list all scheduled tasks in the system.

-  Use the `Get-ScheduledTaskLog` command to view the execution history log of a specific scheduled task.

-  Using Command Line:

-  Run the `SCHTASKS /QUERY /FO LIST /V` command in Command Prompt, which will list all scheduled tasks along with detailed information, including the last run time and result.

-  If you need to view logs for a specific scheduled task, you can use the `SCHTASKS /QUERY /TN "TaskName" /FO LIST /V` command.

  

Best regards

Neuvi Jiang

============================================

If the answer is helpful, click "Accept Answer" and vote for it.

Thanks for the answer, but the problem is that the task is not created and therefore does not generate a log. So I don't see it by launchin Get-ScheduledTask  or in the Event viewer. 

Maybe I was unclear in the question, sorry.   

I believe the problem is with the creation of the task within the GPO

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-10*

Hi jonathandijv,

Thank you for posting in the Microsoft Community Forums.

To view logs related to scheduled tasks in Windows, you can follow these methods:

-  Using Event Viewer:

-  Open "Event Viewer" by searching for it in Windows.

-  In Event Viewer, expand "Windows Logs" and select "Application" log.

-  In the right pane, you can see entries related to scheduled tasks. These entries will display detailed information about the success or failure of scheduled task executions, including execution time, results, etc.

-  Viewing Scheduled Task Log Files:

-  Scheduled task log files are typically located at `%SystemRoot%\SchedLgU.txt`.

-  You can open this file using a text editor (such as Notepad) and view the scheduled task execution history. These log files record information such as start time, end time, execution result, etc.

-  Using PowerShell:

-  Open a PowerShell terminal.

-  Use the `Get-ScheduledTask` command to list all scheduled tasks in the system.

-  Use the `Get-ScheduledTaskLog` command to view the execution history log of a specific scheduled task.

-  Using Command Line:

-  Run the `SCHTASKS /QUERY /FO LIST /V` command in Command Prompt, which will list all scheduled tasks along with detailed information, including the last run time and result.

-  If you need to view logs for a specific scheduled task, you can use the `SCHTASKS /QUERY /TN "TaskName" /FO LIST /V` command.

Best regards

Neuvi Jiang

============================================

If the answer is helpful, click "Accept Answer" and vote for it.
