---
title: "exchange 2019 issue with backup exchange logs/databases"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2119489/exchange-2019-issue-with-backup-exchange-logs-data
question_id: 2119489
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# exchange 2019 issue with backup exchange logs/databases

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2119489/exchange-2019-issue-with-backup-exchange-logs-data (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I have single on-prem Exchange 2019 installed on win2k22 with 5 mailbox databases. We're using netbackup version 10 server to backup databases/logs and client 9 on OS Since Monday evertything correctly, now during exchange full backup or differential incremental we're getting error on the master server , Nov 14, 2024 1:30:05 PM - begin writing Nov 14, 2024 1:30:22 PM - Error bpbrm (pid=1546320) from client exchange01: ERR - Terminating backup. Nov 14, 2024 1:30:22 PM - Error bpbrm (pid=1546320) from client exchange01: ERR - failure reading file: Microsoft Information Store:\DB02\Logs_1731587341 (BEDS 0x0: ) Nov 14, 2024 1:30:22 PM - Error bptm (pid=1546848) system call failed - Connection reset by peer (at ../child.c.1373) Nov 14, 2024 1:30:22 PM - Error bptm (pid=1546848) unable to perform read from client socket, connection may have been broken Nov 14, 2024 1:30:22 PM - Error bptm (pid=1546786) media manager terminated by parent process Nov 14, 2024 1:30:22 PM - Error bpbrm (pid=1546320) could not send server status message to client On the exchange client side (in the bpfis file) we're getting status as below right before  an error shows in the master server (activity monitor -> job ) 13:29:41.707 [27284.21008] <2> stop_keep_alive_thread: INF - Stop keep_alive thread 13:29:43.708 [27284.21008] <4> get_backup_status: INF - Create Named Pipe successful for VSS Backup Complete. 13:30:21.976 [27284.21008] <4> get_backup_status: INF - Connect Named Pipe successful for VSS Backup Complete. 13:30:21.977 [27284.21008] <4> get_backup_status: INF - Message received on named pipe - DB_status:EX_DB 4 DB02:EX_SRVR 11 exchange01:EX_STATUS 13. 13:30:21.977 [27284.21008] <2> onlfi_vfms_logf: INF - INF - vss__update_db_backup_health: Received backup status - 13 for <DB02> from server exchange01. 13:30:21.977 [27284.21008] <2> onlfi_vfms_logf: INF - INF - vss__update_db_backup_health: Found <DB02> in the backup status list. In the bpbkar file we see other error 13:30:21.965 [26628.6884] <2> exchange_shadowcopy_access::V_Read_Metadata_Header(): INF - StreamInfo: Id:STAN, FSAttrib:0x0, TFAttrib:0x0, CAlgor:0x61, Flags:0x0, Size:1048576 13:30:21.968 [26628.6884] <2> exchange_shadowcopy_access::V_Read_FI_File(): INF - backup of 'E00002673BE.log' is complete, 1048576 bytes read 13:30:21.969 [26628.6884] <2> exchange_shadowcopy_access::_createMetadataString(): INF - Exchange metadata - '5 1 PfI 2097154 128 133 C:\Program Files\Veritas\NetBackup\online_util\fi_cntl\bpfis.fim.exchange_1731587341.1.0.MIS_SG1_Logs_E00002673BE.log.MetaData.txt 75 /\?/GLOBALROOT/Device/HarddiskVolumeShadowCopy12/DB02_LOGS/E00002673BE.log' 13:30:21.969 [26628.6884] <2> exchange_shadowcopy_access::V_Read_Metadata_Header(): ERR - invalid STRM header, ID is 0x4145544e 13:30:21.969 [26628.6884] <4> tar_base::V_vTarMsgW: INF - tar message received from dos_backup::tfs_readdata 13:30:21.969 [26628.6884] <2> tar_base::V_vTarMsgW: ERR - Terminating backup. I checked vss writers status on the exchange and all of them are stable and no errors, application logs for any errors , permissions for netbackup client , network and storage system in terms of issues and stability, antivirus but still not luck. Can you please point out what should be checked and investigated ?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-19*

Hi, @Jack

Great to know that the issue has already been resolved and thanks for sharing the solution so that others experiencing the same thing can easily reference this! Since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others", I'll repost your solution in case you'd like to "[Accept]” the answer : )     

--------------   

Issue Symptom: 

Exchange 2019 issue with backup exchange logs/databases

 

Resolution: 

I ended up by upgrading Netbackup client from version 9 to 10.0.01.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-11-19*

Hi @Anonymous  

Thank for the Veritas link but this link was the one of first links which i checked . It not helped at all as I did not had any `Storage Group Consistency Check` errors.

Logs are from Veritas, because from windows application logs weren't helpfull at all and there were no erros reletated to backup. However exchange backups are based on VSS services, and all these settings must be heatlhy eg. vss providers so at least these kind of suggestions I was expected from this forum even if logs are from 3rd party.Anyway I checked VSS based on article https://techcommunity.microsoft.com/blog/exchange/troubleshoot-your-exchange-2010-database-backup-functionality-with-vsstester-scr/594367 but everything was fine. Finally I ended up by upgrading Netbackup client from version 9 to 10.0.01, this worked.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-18*

Hi, @Jack

Since the process logs you provide are from the Netbackup client, which is not covered by Microsoft's services, we are unable to provide accurate troubleshooting. Based on my personal search, this article may mention your problem NetBackup for Microsoft Exchange backups fail with Status Code 13 and "Exchange Validation" failure

In order to get more professional guidance, it is recommended that you contact Veritas technical support. Support | Veritas

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
