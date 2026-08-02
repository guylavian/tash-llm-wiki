---
title: "Exchange 2013 log files filling the disk."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/158146/exchange-2013-log-files-filling-the-disk
question_id: 158146
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# Exchange 2013 log files filling the disk.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/158146/exchange-2013-log-files-filling-the-disk (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi;  

I am running two Exchange 2013 on DAG mode, I found that the partition where to store the log files is full due the the log files did not clean up automatically.  

I run the following Exchange shell command and it is all good.  What should I do?  

Get-mailboxdatacopystatus  

TestReplicationHealth -Identity Mailboxserver-1  

TestReplicationHealth -Identity Mailboxserver-2  

No error found, all pass.  

However; when I look at the file folder where usually keep the copy queue, there are still a lot of files... some of them are .jrs files, a lot of them are the "E01008xxxx.log - E01009xxxx.log" files.  

I know that this folder should be clean at all times, how can I clean up these files or resync this file?  

C:\OS partition  

D:\ to keep the mailbox.edb files  

E:\ to keep the log files.  A lot of log files since Oct 21st.  

I also run the following command try to see if the VSS but it does not help  

Diskshadow  

add volume E:   (this is the partition to store the log files)  

create  

begin backup  

end backup  

When I run this command.... Get-MailboxDatabase -Server EXSERVER01 -Status | fl Name,*FullBackup  

The result is showing the   

Name                   : Mailbox Database 1923107135  

SnapshotLastFullBackup : True  

LastFullBackup         : 10/21/2020 7:02:06 PM  

Name                   : Mailbox Database 1247985168  

SnapshotLastFullBackup : True  

LastFullBackup         : 10/21/2020 7:02:02 PM  

Name                   : MAILBOX01  

SnapshotLastFullBackup : True  

LastFullBackup         : 10/21/2020 7:02:11 PM  

Name                   : MAILBOX02  

SnapshotLastFullBackup : True  

LastFullBackup         : 10/21/2020 7:02:16 PM  

Please help if anyone know any other steps.  

thanks!

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-11*

@Kane       

Agree with AndyDavid, we can wait for the full backup then check if those transaction logs are truncated successfully.     

If the full backup doesn't perform successfully, you can check the event logs to see if any related logs are generated for further analysis.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-10*

Thank you.  

I am using Veeam backup, due to some Veeam server crashed on Oct 22nd, I took time to rebuild the Veeam server and the job for Exchange backup is running slow and sometime the Veeam is waiting for resources.  

I have turned on the Application-aware processing on Veeam.  

May be, I have to wait for the Veeam to complete the full backup, in the meanwhile; just monitoring the capacity of that particular drive.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-11-10*

Those are the Exchange Transaction logs and they should only be cleared by an Exchange Aware backup or by using Circular Logging.  

Do not run any other type of backup against that drive.

-   What are you using for backups? If so, run a full Exchange Aware backup and the logs will clear

-   If you arent using a backup any longer ( since 10.21?) Then enable Circular Logging:    https://learn.microsoft.com/en-us/exchange/configure-circular-logging-for-a-mailbox-database-exchange-2013-help    Set-MailboxDatabase DB1 -CircularLoggingEnabled $True

WARNING: Do not enable circular logging if you are doing backups. Run a full Exchange aware backup. If you can not do that, then enable circular logging to clear the logs. Note that circular logging means you can not restore the database to the point of failure using a backup program
