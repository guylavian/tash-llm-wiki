---
title: "Exchange 2019 DAG Autoreseed Disk Reclaimer not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/348095/exchange-2019-dag-autoreseed-disk-reclaimer-not-wo
question_id: 348095
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 DAG Autoreseed Disk Reclaimer not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/348095/exchange-2019-dag-autoreseed-disk-reclaimer-not-wo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to test the Autoreseed feature.  I unplug a disk and the normal Event IDs showing the DB status is failed, its trying to repair, repeat a number of times, then it gets to the Event ID 1149 disk Reclaimer showing it searching for available spare volumes.   

The Volume Manager found the following volumes:  

UnknownVolumeCount=0  

UnEncryptedEmptySpareVolumeCount=0  

EncryptingEmptySpareVolumeCount=0  

EncryptedEmptySpareVolumeCount=2  

QuarantinedVolumeCount=0  

NotUsableAsSpareVolumeCount=18  

ErrorVolumeCount=0  

ReFSVolumeCount=0  

---UnEncryptedEmptySpareVolumeList---  

---EncryptingEmptySpareVolumeList---  

---EncryptedEmptySpareVolumeList---  

D:\ExchangeVolumes\Volume16\  ( \?\Volume{df9fa9d4-517c-43f0-8d98-e19428a8644e}\ )  

D:\ExchangeVolumes\Volume17\  ( \?\Volume{190fb710-e0ca-4f8f-a8fb-9a525fc5ae0e}\ )  

Even though if shows two available volumes it never uses them.  It just continues with the repeating errors that the DB is failed.  

Any clues?  

Thanks!!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-14*

Yes.  I have attached what the normal mount points look like as well as the two spare volumes.    

    

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-12*

I have already went through that article, thank you.  

I unecrypted one of the spare volumes and it still does the same thing.  

Here are the events:  

Log Name:      Microsoft-Exchange-HighAvailability/Seeding  

Source:        Microsoft-Exchange-HighAvailability  

Date:          4/12/2021 9:53:49 AM  

Event ID:      1119  

Task Category: Auto Reseed Manager  

Level:         Error  

User:          SYSTEM  

Description:  

Automatic Reseed Manager failed to resume database copy 'MBXDB1903' as part of repair workflow 'FailedSuspendedCopyAutoReseed' after a maximum of 3 attempts. The workflow will next attempt to assign a spare volume and reseed the database copy.  

Log Name:      Microsoft-Exchange-HighAvailability/Seeding  

Source:        Microsoft-Exchange-HighAvailability  

Date:          4/12/2021 9:53:49 AM  

Event ID:      1111  

Task Category: Auto Reseed Manager  

Level:         Error  

User:          SYSTEM  

Description:  

Automatic Reseed Manager failed to execute repair workflow 'FailedSuspendedCopyAutoReseed' for database 'MBXDB1903'. Error: The Automatic Reseed Manager encountered an error: The automatic repair operation for database copy 'MBXDB1903\HEX1902' will not be run because one of the prerequisite checks failed. Error: Could not determine which databases should be grouped on the same volume. Please ensure that the databases in the DAG have their DatabaseGroup properties set according to the database-volume grouping desired. If the DatabaseGroup property is left blank, please manually assign the database mount points as desired.  

Other ideas?  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-09*

The root D:\ExchangeVolumes contains the  ..Volume## folders/mount points as per the article you linked.  the spare volumes have the appropriate folders that are empty.  I used that article to setup the AutoReseed and have gone through it numerous times to verify all matches.  

Is there any logs or something that actually says what specifically is failing?  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-08*

Yes, bitlocker is enabled on the spare volumes and AutoDagBitlockerEnabled is already set.  Here is the output of the command you suggested.  

AutoDagSchemaVersion             : 1.0  

AutoDagDatabaseCopiesPerDatabase : 2  

AutoDagDatabaseCopiesPerVolume   : 6  

AutoDagTotalNumberOfDatabases    : 0  

AutoDagTotalNumberOfServers      : 0  

AutoDagDatabasesRootFolderPath   : D:\ExchangeDatabases  

AutoDagVolumesRootFolderPath     : D:\ExchangeVolumes  

AutoDagAllServersInstalled       : False  

AutoDagAutoReseedEnabled         : True  

AutoDagDiskReclaimerEnabled      : True  

AutoDagBitlockerEnabled          : True  

AutoDagFIPSCompliant             : False  

AutoDagAutoRedistributeEnabled   : True  

AutoDagSIPEnabled                : False  

The above paths are the correct locations of the mount points on the D: drive.  

I found this error in the event viewer but not sure how to handle it: Could not determine which databases should be grouped on the same volume. Please ensure that the databases in the DAG have their DatabaseGroup properties set according to the database-volume grouping desired. If the DatabaseGroup property is left blank, please manually assign the database mount points as desired.  

I looked up the parameter for DatabaseGroup, but the technet article says it is used only internally by Microsoft.  

Thank you

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-08*

Hi @David McBride   ,    

---EncryptedEmptySpareVolumeList---    

Does that mean you have encrypted these volumes with Bitlocker? If so:    

    

Also check the DAG AutoReseed settings with     

```
Get-DatabaseAvailabilityGroup DAG | Format-List *auto*
```

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
