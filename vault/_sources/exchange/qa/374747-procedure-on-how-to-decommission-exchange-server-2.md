---
title: "Procedure on how to decommission Exchange Server 2010 with DAG configured after migrating to Exchange Server 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/374747/procedure-on-how-to-decommission-exchange-server-2
question_id: 374747
fetched: 2026-07-25
answer_count: 10
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Procedure on how to decommission Exchange Server 2010 with DAG configured after migrating to Exchange Server 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/374747/procedure-on-how-to-decommission-exchange-server-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

Good Day!  

May I ask what is the proper way of decommissioning of Exchange Server 2010 with DAG configured after migrating to Exchange Server 2013.  

Thanks,  

Raymond

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-04-28*

-  Ensure all mailboxes are moved to 2013 including the arbitration mailboxes    

     Get-Mailbox -Arbitration | New-MoveRequest -TargetDatabase <2013DB>  

-  Remove all database copies from all the servers except the last one     

     https://learn.microsoft.com/en-us/exchange/high-availability/manage-ha/remove-db-copies?view=exchserver-2019  

-  Remove all the mailbox severs from the DAG:    

     https://learn.microsoft.com/en-us/exchange/high-availability/manage-ha/dag-memberships?view=exchserver-2019#use-the-eac-to-manage-database-availability-group-membership  

-  Uninstall Exchange from each 2010 server ( setup will alert if you not removed 2010 as a source server in any send connector or still have a mailbox on the server)    

     Add/Remove Programs and uninstall.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-12*

Hi Kael,  

Good Day!  

This is noted. I will run that command to check the OAB and will update you once we have schedule with the client to do this.  

May I ask if the OAB is required to remove when decommissioning of Exchange Server 2010 after the upgrade to Exchange Server 2013?  

Thanks,  

Raymond

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-06*

Hi Kael,  

Good Day!  

Meaning I need to remove the OAB of 2010 since the Exchange Server 2013 is already added before removing the DAG configuration?  

Thanks,  

Raymond

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-03*

Hi Andy and Kael,  

Good Day!  

Sorry for the late response and thank you for sharing your thoughts.  

I confused in some articles that I have reading because they will remove the databases in each server after removing the database copy and DAG.  

May we ask if do I need to remove the Offline Address Book? If yes, when I will this procedure?  

Thanks,  

Raymond

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-04-29*

Hi Raymond,    

Agree with Andy, if you have finished the migration to Exchange 2013 (moved all the mailboxes including arbitration mailboxes, configured DNS records to point to Exchange 2013),    

to decommission the DAG, you may need to first remove the database copies,then remove the nodes from the DAG and finally remove the DAG.    

In addition, I would recommend to shut down the Exchange 2010 servers for a few days before finally decommissioning them to check if there are any problems with the mail flow or client access.    

There is also an article from Exchange Team Blog for your reference: Best practices when decommissioning Exchange 2010    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
