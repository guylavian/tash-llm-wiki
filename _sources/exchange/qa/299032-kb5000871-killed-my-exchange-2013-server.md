---
title: "KB5000871 killed my Exchange 2013 server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/299032/kb5000871-killed-my-exchange-2013-server
question_id: 299032
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# KB5000871 killed my Exchange 2013 server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/299032/kb5000871-killed-my-exchange-2013-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I tried to install KB5000871 on my Exchange 2013 cu23 server and it failed with some dll not copied.  

Other attempts to start it with UAC disabled and "as administrator" end "prematurely".  

I know there are a lot of same issues today with this failed update.  

And may be someone has found the cure.  

Log file has this:

```
Property(S): msgInterimIncorrectRollup = Installation cannot continue. The Setup Wizard has determined that this Interim Update is incompatible with the current Microsoft Exchange Server 2013 Cumulative Update 23 configuration.

    CAQuietExec:  Error 0x80070001: Command line returned an error.
    CAQuietExec:  Error 0x80070001: CAQuietExec Failed
    CustomAction CA_CUSTOMER_PREPATCH_INSTALL returned actual error code 1603 but will be translated to success due to continue marking

    MSI (s) (B4:20) [15:56:08:409]: Product: Microsoft Exchange Server -- Configuration failed.

    MSI (s) (B4:20) [15:56:08:409]: Windows Installer reconfigured the product. Product Name: Microsoft Exchange Server. Product Version: 15.0.1497.2. Product Language: 9. Manufacturer: Microsoft Corporation. Reconfiguration success or error status: 1603.

    MSI (s) (B4:20) [15:56:08:409]: Attempting to delete file C:\Windows\Installer\70f290.msp
    MSI (s) (B4:20) [15:56:08:409]: Unable to delete the file. LastError = 32
    MSI (s) (B4:20) [15:56:08:440]: Deferring clean up of packages/files, if any exist
    MSI (s) (B4:20) [15:56:08:440]: Attempting to delete file C:\Windows\Installer\70f290.msp
    MSI (s) (B4:20) [15:56:08:440]: MainEngineThread is returning 1603
    MSI (s) (B4:B4) [15:56:08:440]: RESTART MANAGER: Session closed.
    MSI (s) (B4:B4) [15:56:08:440]: No System Restore sequence number for this installation.
    === Logging stopped: 04.03.2021  15:56:08 ===
    MSI (s) (B4:B4) [15:56:08:440]: User policy value 'DisableRollback' is 0
    MSI (s) (B4:B4) [15:56:08:440]: Machine policy value 'DisableRollback' is 0
    MSI (s) (B4:B4) [15:56:08:440]: Incrementing counter to disable shutdown. Counter after increment: 0
    MSI (s) (B4:B4) [15:56:08:440]: Note: 1: 1402 2: HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Installer\Rollback\Scripts 3: 2 
    MSI (s) (B4:B4) [15:56:08:440]: Note: 1: 1402 2: HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Installer\Rollback\Scripts 3: 2 
    MSI (s) (B4:B4) [15:56:08:440]: Decrementing counter to disable shutdown. If counter >= 0, shutdown will be denied.  Counter after decrement: -1
    MSI (s) (B4:B4) [15:56:08:440]: Destroying RemoteAPI object.
    MSI (s) (B4:00) [15:56:08:440]: Custom Action Manager thread ending.
    MSI (c) (68:04) [15:56:08:455]: Decrementing counter to disable shutdown. If counter >= 0, shutdown will be denied.  Counter after decrement: -1
    MSI (c) (68:04) [15:56:08:455]: MainEngineThread is returning 1603
    === Verbose logging stopped: 04.03.2021  15:56:08 ===
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-29*

Thank you this just saved my life, I just copied missing dll´s and it worked after reboot, even I've installed the SU from WSUS, that thing broke one of my exchange servers, fortunately I had a backup of those files.    

Thank you!
