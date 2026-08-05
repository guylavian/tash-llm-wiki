---
title: "Exchange 2016 CU19 update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/242047/exchange-2016-cu19-update
question_id: 242047
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 CU19 update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/242047/exchange-2016-cu19-update (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have been tasked with installing CU19 on an Exchange 2016 server (running on a Windows 2012 R2 VM).  I have never installed or updated Exchange in my life, so this should be... fun.  This Exchange server is the only one in our enclave, not connected to the internet in any way, so will be offline to users while I go through this process.  

OS: Windows Server 2012 R2, build 9600  

Exchange: Version 15.1, build 1415.2, CU8  

.NET Framework 4.8.0  

I have the CU19 .iso file moved over and ready to go.  I have updated the server with the latest patches available.  I believe all I need to do at this point is to stop the HubTransport, put it into Maintenance mode, take a Snapshot of the VM (gotta be safe!), mount the .iso file, run the Setup.exe file, and let it roll.  However I see references online to having to run "PrepareAD" from the command line.  I'm not sure why I have to do this, or even if I truly DO need to do this?  I saw something else about how I need to ensure "ADSchema" is updated as well.  Again, not sure how/why I need to this if at all.    

Finally, I see that if there are any customizations for our current Exchange server they will be lost when I run the CU19 update - can this actually be true?  It seems strange to me that an update wouldn't at least give you the option of retaining any customized settings/files in this day and age.  Assuming it IS true, how do I know if any of these customizations exist so that I can save them off first?  

I'm a bit paranoid about this given that, again, I have no previous experience with supporting Exchange and the people who originally set this up are all gone and unreachable for questions.  

Thanks!  

Sudz

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-01-28*

That fixed my issue, the upgrade completed successfully!  I only had to change the "DiscoverySearchMailbox", no need to mess with any others.  Our Admin accounts as it turns our are not mailbox enabled (didn't know that prior to this, again I'm new to the office) so that explains the discrepancy.  

Thanks again for all your help!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-28*

Failing!  I got as far along as "Step 13 of 17: Mailbox role: Mailbox Service" and an error gets thrown, with my option to 'exit' the installation.  It's complaining that I need to "upgrade the discovery mailboxes to R5 version, this will fix the RecipientDisplayType property of the discovery mailbox which was wrong in R4".  I am investigating now to see what the mitigation is.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-25*

Andy, thank you for this information!  I guess part of my problem is being new to supporting MS infrastructure servers, I'm not entirely sure what is required and what isn't.  I am actually doing this during regular hours, our users will just have to be without email for a couple of hours I guess.  It is indeed a single Exchange server, in a single domain (no parent or child domains).  

The Snapshot I'm referring to is via vSphere 6.7.  I'm not sure I understand what MS is referring to when they say "...making a virtual machine snapshot of an Exchange guest virtual machine isn't supported".  I have taken snapshots of this server before.  Either way, I'll try to make sure we have a good/recent NetBackup backup of the VM.  

With regards to the /PrepareSchema, /PrepareAD, and /PrepareAllDomains commands (probably don't need PrepareDomain?), are these things I can run ahead of time - like the day before my planned upgrade?  Or do I need to do them literally just prior to running Setup.exe?  

Eric, I'm not sure what customizations, I guess that was sort of my question.  The MS article I was reading was saying that they would be overwritten so be sure to have backups of them, and it gave two examples ("Any customized Exchange or Internet Information Server (IIS) settings that you made in Exchange XML application configuration files on the Exchange server (for example, web.config files or the EdgeTransport.exe.config file) will be overwritten when you install an Exchange CU.").  

Scott  

p.s. - Sorry, I tried to post this as a comment on the other answers but for some reason nothin happens when I hit 'submit' after putting in my comment.  It was less than 1000 characters, so I don't know what the issue is.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-25*

Agree with Andy, you don't have to keep it in maintaince mode, and you can run the command prepareAD with the setup.exe open, then click "retry" and go on.    

In addition， what kind of customizations do you mean?  Settings in EAC or the server side? In mose cases, updating/installing a new server would not change the former settings.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
