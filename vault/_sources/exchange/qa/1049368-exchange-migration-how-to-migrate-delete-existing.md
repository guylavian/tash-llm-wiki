---
title: "Exchange migration: How to migrate/delete existing users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1049368/exchange-migration-how-to-migrate-delete-existing
question_id: 1049368
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange migration: How to migrate/delete existing users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1049368/exchange-migration-how-to-migrate-delete-existing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

i have to migrate an Exchange 2016 server to Microsoft 365 and it causes some headache.    

Prior to the migration, Office 365 was introduced. Thus the users were added manually and the appropriate licenses were granted.    

I prepared a cutover migration which seemed to be ok after some troubles.    

But the result was unexpected:    

-  All old/disabled users were migrated correctly    

-  All current users failed with an AutoDiscoverFailedConfigurationErrorException error    

Since i have only 20 users who do not have any data on the cloud yet, i decided it would be best to delete those users. Then the migration should create them as planed. But it does not! The users get created but fail with the same error again.    

I tried to delete the migration batch, the endpoint but nothing helped. Which i did not try yet, was to delete the users from the "deleted users" in the Azure AD.    

How must I recover from this situation?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-25*

Well, i opened a support case at Microsoft. It seems that it is a confirmed error for which a fix is planed.    

If i understood it correctly:    

When you assign a license to a new user a postbox gets created.    

Later on the migration finds this and does a soft delete (not a permanent one)    

The migration tries to create a new mailbox.    

At this point is sees the soft deleted mailbox which has a different exchangeguid. Boom, you are doomed and the process stops.    

Why i was not able to clean the user from the Exchange server, i don't know. There where several copies known to the backend.    

We decided to reset the whole tenant as this would be faster than any tries to repair it. Hence there is no procedure for this. So a new tenant from activated. Which lead to the next problem. Microsoft tries to figure out how to transfer our licenses. Yep, they are looking for the procedure to handle this.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-17*

@Magnus Müller       

Here may be a workaround for you:    

User New-MailboxExportRequest command to export data from those Exchange on-premises mailbox.    

Create mailbox on Exchange online manually as before.    

Then use Office 365 network upload tool to import data for these mailboxes.    

After uploading complete, you could delete the Exchange on-premises mailbox if you want.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-15*

Ok, i tried again.

-  deleted a test user from Office 365

-  verified that the user from removed from the Exchange admin console

-  deleted the user from the deleted users in Azure AD

-  stopped the mirgration batch

-  received a status email from the stopped batch

-  restarted the migration batch

-  got an error message because now the user was not present

-  stopped and deleted the batch to force a new user creation

-  created a new batch and started it

-  a new user was created

-  ended up with the same mistake. old users were in sync. my test user (privious O365 user) failed with the same error.  Here is the error message (original in German and translated):

Fehler: AutoDiscoverFailedConfigurationErrorException: Konfigurationsfehler bei AutoErmittlung: Der Migrationsdienst konnte den Migrationsendpunkt nicht mithilfe des AutoErmittlungsdiensts ermitteln. Verwenden Sie ggf. die Exchange-Remoteverbindungsuntersuchung (https://testexchangeconnectivity.com) für die Diagnose von Konnektivitätsproblemen.

Error: AutoDiscoverFailedConfigurationErrorException: Configuration error on autodiscover: The migration service could not discover the migration endpoint with the help of the autodiscover service. Use the Exchange-Remoteconnection test (https://testexchangeconnectivity.com) to diagnose connection issues.

I think this error is misleading as the "old" users without O365 worked.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-15*

If you have already removed them from the deleted users, you should be able to run the batch again and have them generated again.
