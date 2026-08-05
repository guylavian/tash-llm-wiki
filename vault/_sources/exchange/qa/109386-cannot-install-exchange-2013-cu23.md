---
title: "Cannot install Exchange 2013 CU23"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/109386/cannot-install-exchange-2013-cu23
question_id: 109386
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Cannot install Exchange 2013 CU23

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/109386/cannot-install-exchange-2013-cu23 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We were trying to install Exchange 2013 CU23 in a multi domain environment.  

We started in the root domain on the schema master with:  

-  setup.exe /prepareschema  

-  setup.exe /preparead  

-  setup.exe /preparealldomains  

No error - every command ended with success message.  

Then we synced all domain controllers with:  

-  repadmin /syncall /AeD   and  

-  repadmin /syncal /APeD  

again without any error - all partitions were synced successfully.  

Then we switched to a subdomain onto an Exchange 2012R2 server, fully patched with .NET-Framework 4.8 on it.  

We installed all prerequisites - no problem...  

Then things got weird - we tried to install CU23-Exchange 2013 - with an account having all necessary group memberships.  

Setup prerequisites check gave us a lot of error messages:  

-  Forest functional level not high enought ( but in fact were are having Windows 2008-R2 level )  

-  cannot find Server roles before Exchange 2013 ( but in fact there are still some Exchange 2007 servers)  

-  installing user isn't member of necessary groups ( but in fact we were finally using an account beeing member of Schema-Admins, Enterprise-Admins,Subdomain-Admin, local admin, Exchange Org-Admin)  

We looked into Exchange Server setup logs - but didn't get a good idea...  

Finally we gave up and we deinstalled .NET-Framework 4.8 - installed 4.7.2 and tried installing Exchange 2013 CU21.  

And to our big surprise - Exchange Setup started and finalized without any error...  

Any ideas?  

Yours  

Franz-Georg

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2020-09-29*

@fgc      

Hi,    

I notice that you mentioned there are some Exchange 2007 servers in your environment.    

So I suppose the problem may possibly be resulted from the known issue in CU22 ,and it hasn't been fixed in CU23.    

According to the article:Cumulative Update 22 for Exchange Server 2013    

Known issues in this cumulative update    

In multidomain Active Directory forests in which Exchange is installed or has been prepared previously by using the /PrepareDomain option in SETUP, this action must be completed after the /PrepareAD command for this cumulative update has been completed and the changes are replicated to all domains. Setup will try to execute the /PrepareAD command during the first server installation. Installation will finish only if the user who initiated SETUP has the appropriate permissions.    

After the /PrepareAD command,you should wait for the replication to complete or use repadmin to sync the changes before you run the /PrepareDomain command.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
