---
title: "Migration of Exchange Linked Mailboxes from Ex2010 to Ex2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/234548/migration-of-exchange-linked-mailboxes-from-ex2010
question_id: 234548
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Migration of Exchange Linked Mailboxes from Ex2010 to Ex2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/234548/migration-of-exchange-linked-mailboxes-from-ex2010 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In a Resource Forest Scenario, we are migrating from Exchange 2010 in the Resource Forest to Exchange 2016. We are migrating the Linked mailboxes from Ex2010 to Ex2016. For some reason, some mailboxes need access from the Account Forest and from the Resource Forest. For this access we have re-enabled the disabled resource account. On Ex2010, both accounts were able to log into the mailbox. After migration to Ex2016, it is no longer possible to log in with both accounts. The resource forest account gets the following error message:  

InnerException: Microsoft.Mapi.MapiExceptionLogonFailed  

The MAPI log shows the following:  

MoMTException:-2147221231 (rop LogonFailed)   

-> [ConnectionFailedTransientException] Cannot open mailbox /o=CONTOSO/ou=Exchange Administrative Group (FYDIBOHF23SPDLT)/cn=Recipients/cn=hans.musterba6.   

-> [MapiExceptionLogonFailed] Unable to open message store. (hr=0x80040111  ec=-2147221231)    

-> [ServerUnavailableException] Connection must be re-established   

-> [SessionDeadException] The primary owner logon has failed. Dropping a connection.   

-> [ConnectionFailedTransientException] Cannot open mailbox /o=CONTOSO/ou=Exchange Administrative Group (FYDIBOHF23SPDLT)/cn=Recipients/cn=hans.musterba6.   

-> [MapiExceptionLogonFailed] Unable to open message store. (hr=0x80040111  ec=-2147221231)     

We need to be able to log in to the mailbox with both accounts. The account from the resource forest and the account from the account forest.  

Thanks for any Help!  

Kind Regards  

Steve

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-22*

Hi Lou,  

Thank you for your reply. All the details you have shown me are known to me. Behind a Linked Mailbox there is one mailbox and two accounts. The first account (PA) from the resource forest is a placeholder account. This account is normally deactivated. The second account from the Account Forest is the Master Account (MA) and this is usually used to log in to a Linked Mailbox. OK. In Exchange 2010 it was possible to log in to the Linked Mailbox with the account (PA) and with the account (MA). Even if this is unusual it was possible. We activated the (PA) account and logged in. We used this option for special scenarios. After the successful migration of a linked mailbox to Ex2016 it is only possible to log in with the account (MA). When trying to log in to the Linked Mailbox with the account (PA), the error messages appear. We need to login with account (PA) and (MA) to the linked mailbox.  

Kind Regards  

Steve

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-22*

Hi @ThomaSTSandbox ,

Thank you for sharing the details!

We enabled the disabled Account in Forest A

I am sorry but I couldn’t fully understand what disabled accounts you have enabled, if you could, please tell me more details about these accounts.  

According to my test, I migrate the linked mailbox to another database but it can still login. So I would think there are something wrong with these accounts.  

You can check the RecipientTypeDetails using this command: Get-Mailbox | FT Name,ServerName,Database ,RecipientTypeDetails

After the Migration to Ex2016 only the Forest B User can logon to the Mailbox. It is no longer possible to log in with the activeated account from Forest A.

What logon name are you using to login these mailboxes? The linked mailbox could only login using the Master Account as logon name like DomainB\MasterAccount. Linked mailboxes  

If those above don’t help you, you can have a test with a new linked mailbox for a further troubleshooting:  

-  Try creating a new linked mailbox on Ex 2010 then migrate it to Ex 2016 and test login OWA.  

-  Create a new linked mailbox on Exchange 2016 server and test if this one could login OWA.  

If both of the tests are OK, I think you should check the logon name you using to login the linked mailbox.  

If these tests failed, I think there would be issues of the Ex 2016 database, you can create a new database and migrate these linked mailboxes to it and test.

As for the error logs: MapiExceptionLogonFailed: Unable to open message store. (hr=0x80040111 ec=-2147221231)  

This error is related to the permissions of the account or the database, you can try the following steps:  

-  In EMC(Ex 2010), choose this user and click ‘Manage full access permission’ in action panel.  

-  Check if there is NT AUTHORITY\SELF, if no, add self:  

  

-  Restart the Ms Exchange Information Store service on Ex 2016.

Have a nice weekend!

Regards,  

Lou

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-19*

Hi Lou,  

The Environment are:  

Ressource Forest (Forest A) = AD Single Domain Forest with Ex2010 and Ex2016 Coex  

Account Forest (Forest B) = AD Single Domain Forest where the "Normal" User are  

A trust has been established between the two forests.  

Q. Exchange 2010 and Exchange 2016 coexist in the Resource Forest (Forest A)?   

A: Yes   

Q: Do you mean you couldn’t log in the migrated mailbox from both resource and account forest?  

A: Before we Migrated the Linked-Mailbox in the Ressource Forest from Ex2010 to Ex2016 we could Login to the Linked-Mailbox with the Linked-Mailbox Account from Forest A and from Forest B. We enabled the disabled Account in Forest A. After the Migration to Ex2016 only the Forest B User can logon to the Mailbox. It is no longer possible to log in with the activeated account from Forest A.  

Regards  

Steve

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-19*

Hi @ThomaSTSandbox ,    

In a Resource Forest Scenario, we are migrating from Exchange 2010 in the Resource Forest to Exchange 2016.    

I’m not pretty sure, does that mean the Exchange 2010 and Exchange 2016 coexist in the Resource Forest?     

If you could, please tell me the details of your environment. Because in my view, I think you have two forest and the migration was done in THE source forest, if I’m wrong, please correct me.    

After migration to Ex2016, it is no longer possible to log in with both accounts.    

Do you mean you couldn’t log in the migrated mailbox from both resource and account forest?    

Since you said on Ex 2010, both accounts were able to log into the mailbox, could you please tell me the accounts you use to login the mailbox from resource and account forest?    

According to my research, the error messages: [MapiExceptionLogonFailed] Unable to open message store could be related to the settings of the mailbox:    

Please check the the homeMDB value in ADUC: Active Directory Users and Computers -> View Advanced Features-> Double click the problematic user-> Attribute Editor-> Check the homeMDB.    

     

     

In addition, you can create a new user mailbox on Ex 2010(Specify the Ex 2010 database) and migrate it to Ex 2016 and test login.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
