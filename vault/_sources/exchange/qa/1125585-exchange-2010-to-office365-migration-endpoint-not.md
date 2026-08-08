---
title: "Exchange 2010 to Office365 migration endpoint not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1125585/exchange-2010-to-office365-migration-endpoint-not
question_id: 1125585
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2010 to Office365 migration endpoint not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1125585/exchange-2010-to-office365-migration-endpoint-not (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, one of our clients has an old Exchange 2010 hosted exchange mailserver, they are currently trying to migrate all mailboxes to one Office365 tenant.    

This mailserver contains various companies with multiple domains and email addresses, for example  ******@company1.com, user@company2  .com, ******@company3.com    

The mailserver has only 1 SSL certificate listening on mail.companymailserver.com    

All companies connect to the mailserver using a SVR record  "_autodiscover._tcp  SRV 0 0 443 mail.companymailserver.com"    

Outlook and mobile devices work fine this way.    

We cannot use the "real" autodiscover.company1.com system because this mailserver is shared and does not contain SSL certificates for the separate email domains hence the SRV records for successful autodiscover operation.    

We currently have Azure AD Connect tool successfully syncing users and passwords from the local AD to Office365    

The problem we are facing now is when we want to setup a migration endpoint in Office365 Exchange Online, it cannot connect because it's complaining about autodiscover not being setup as expected when we select "Hybrid".     

At this moment I don't have any way to change that in the current configuration.  It's not just one Exchange 2010 server, it is the Exchange 2010 hosted version that doesn't even come with an Exchange Manager GUI.   For each domain (company1.com, company2.com) we will have to setup separate Migration Endpoints as all domains have their own administrator accounts even though they reside on the same mailserver.  So   AD\administrator   AD\administrator1  AD\administrator2     

Is there any way to bypass or maybe migrate the mailboxes in a different way? We seem to be a little stuck    

Update:    

After messing around I could add the Migration Endpoint by skipping verification. My guess is that the process of adding a new Migration Endpoint does check autodiscover that we don't use. By skipping verification you can create the endpoint with the correct settings.  Next step was to create a test migration batch, and there we got the actual error it is running into. The message is far more detailed and complains about TLS 1.2 not configured correctly on the Exchange 2010 server so that will be our next step to fix. After that we will have to see if that fixed the connection error.  The "Create Migration Endpoint wizard" does not give a clear error message, just says "unable to connect".   The actual Migration Batch shows much more detail. But you cannot start a Migration Batch without an existing Migration Endpoint

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-12-21*

I got it figured out now. We had to enable TLS 1.2 on the Exchange server, it wasn't enabled. That was step one.    

Next was to enable the MRSproxy, this wasn't enabled as well.    

Exchange 2010 Hosted version, uses separate administrator accounts for each organization that is present in the domain/active directory. These administrator accounts are not member of "Domain Admins", it seems that this permission is needed to be able to connect. After that you need to give these administrator accounts full access to all the mailboxes you want to migratie to Office365.     

In Office365 you create a bunch of separate migration endpoints for each domain, using the correct administrator credentials. In our case "Domain\Administrator3" Administrator5,6 etc.    

Also make sure your Exchange 2010 server can be accessed from the United States, we were using a geo filter.  Make sure in the migration batch to select the correct timezone. It seems to fail when you select the wrong timezone, could be a coincidence but happened to me twice.    

We have now successfully migrated a few mailboxes from Exchange 2010 to Office365

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-13*

@Caspar - ABO      

For migrated mailboxes and use the domain name on Office 365, you need to use a real domain and have the ownership of that domain. Otherwise, migrated mailboxes will use the Exchange online default domain name: "@keyman  .onmicrosoft.com".    

If you are using a real domain, I think you will could create Autodiscover record for it.    

So, in your organization, I would suggest you export data from Exchange 2010, then use Office 365 network upload to import to Exchange online mailbox directly.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
