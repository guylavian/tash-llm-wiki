---
title: "[Migrated from MSDN Exchange Dev] OAB Not Updating on Outlook Clients After Exchange 2013 to 2016 Migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/138647/migrated-from-msdn-exchange-dev-oab-not-updating-o
question_id: 138647
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# [Migrated from MSDN Exchange Dev] OAB Not Updating on Outlook Clients After Exchange 2013 to 2016 Migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/138647/migrated-from-msdn-exchange-dev-oab-not-updating-o (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Origin link: https://social.msdn.microsoft.com/Forums/office/en-US/e869f848-3562-404b-b2d9-e8a2b5e23a45/oab-not-updating-on-outlook-clients-after-exchange-2013-to-2016-migration?forum=exchangesvrdevelopment  

Hello all,  

I hope this is the correct forum to post in. If not, please point me in the right direction.  

We recently migrated from Exchange 2013 to Exchange 2016 using the coexistence method. Ever since then, it appears that non of the Outlook clients are updating their offline address books. When switching them to non-cached mode, the address book is current. When switching back to cached mode, the address book goes back to the way it was originally before switching to non-cached mode.  

It doesn't seem feasible to switch all of our clients to non-cached mode, as a lot of folks are working remotely, and using Outlook in non-cached mode is painfully slow for them.  

I've tried rebuilding the OST file, but this didn't make a difference. Completely deleting and rebuilding the Outlook profile does seem to update the offline address book, but it would be too much of an undertaking to do this for each user on ever computer they use.  

Manually trying to update the offline address book in Outlook yields the following error message: Task '<user account>' reported error (0x8004010F) : 'The operation failed. An object cannot be found.'  

I have tried to research this issue and unfortunately there is no collective solution to it. There are a lot of suggestions, including verifying all of the virtual directories are set up correctly, some registry edits, etc. I have checked all of our virtual directories and everything looks accurate. During the 2013 to 2016 migration, I was very diligent in making sure every detail was correct. Everything else seems to be working great.  

Any thoughts?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-10*

Can you find the OAB file on clients' computer and on Server?    

Path should be C:\Users\Administrator\AppData\Local\Microsoft\Outlook and C:\Program Files\Microsoft\Exchange Server\V15\ClientAccess\OAB.    

If the file not exist in client's PC, press CTRL and right click Outlook icon, select Test email autoconfiguration, type in password and run a test, see if OAB url is reported:    

    

If the file not existing in server, run get-offlineaddressbook|update-offlineaddressbook and see if the file is generated/updated.    

If not, recreate system mailbox as this blog says.    

Restart the PC on both side.    

Some other troubleshooting steps may help:     

https://msexchangeguru.com/2013/12/04/e2013-oab/    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-04*

Eric,  

I did some testing by recreating my own Outlook profile. Upon doing this, the address book was updated and current with all of our users. However, when I manually try updating the OAB by going to File -> Account Settings -> Download Address Book... I still receive the following error message:  

Task '<user>' reported error (0x8004010F) : 'The operation failed. An object cannot be found.'  

Would this indicate some sort of configuration issue within our Exchange environment?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-28*

Eric,

I went ahead and tried recycling the two web app pools you suggested, but I received an error message when trying to restart the OABAppPool:

restart-webitem : Cannot find path 'IIS:\AppPools\OABAppPool' because it does not exist.  

At line:1 char:1  

-  Restart-WebAppPool OABAppPool  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : ObjectNotFound: (IIS:\AppPools\OABAppPool:String) [Restart-WebItem], ItemNotFoundExcepti  

on  

-  FullyQualifiedErrorId : PathNotFound,Microsoft.IIs.PowerShell.Provider.RecycleItemCommand

These are the two commands I ran to recycle these app pools:

Restart-WebAppPool MSExchangeAutodiscoverAppPool  

Restart-WebAppPool OABAppPool

Is this the correct syntax.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-26*

Hi Eric,  

Yes, we did uninstall the 2013 Exchange server using the Control panel.  

As far as I can tell, all of the mailboxes are located on the new Exchange 2016 server. I ran the command: "get-mailbox" and all of the listed mailboxes are on the new server. Would this be the correct way to check the location of the organization mailbox?  

Both the internal and external URL of the OAB virtual directory are the same:  

https://mail.ourdomain.com/OAB  

"mail" is correctly configured in DNS and is pointing to our Exchange 2016 server.  

I will go ahead and try resetting the MSExchangeAutodiscoverAppPool and OABAppPool web app pools and see if that makes any difference.  

If we have to recreate a profile to get the OAB updated, will new users show up automatically moving forward, or would we have to recreate each person's profile every time we add a new user mailbox?  

Thanks for all the help!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-26*

According to your description, it seems OAB file is correctly created but not downloaded by the clients' Outlook.     

Have you unistalled the Exchange 2013 server?     

Where is the organization mailbox located in and where does the OAB url point to?    

Another method you can try is recycling MSExchangeAutodiscoverAppPool and OABAppPool in IIS (you may need to do this at off-work time)    

But I have to mention that, I've seen several similar threads and the step recreating the profile was the only solution to them.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
