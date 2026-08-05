---
title: "Exchange 2019 CU8 Upgrade failed - insufficient privileges to access \\owa\\auth\\15.2.792"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/304724/exchange-2019-cu8-upgrade-failed-insufficient-priv
question_id: 304724
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 CU8 Upgrade failed - insufficient privileges to access \owa\auth\15.2.792

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/304724/exchange-2019-cu8-upgrade-failed-insufficient-priv (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have had an unsual error when upgrading which has stalled after uninstalling and not allowing us to continue.  

Error Message  

Installing product E:\exchangeserver.msi failed. Fatal error during installation. Error code is 1603. Last error reported by  

the MSI package is 'The installer has insufficient privileges to access this directory: C:\Program Files\Microsoft\Exchange  

Server\V15\FrontEnd\HttpProxy\owa\auth\15.2.792. The installation cannot continue.  

Any ideas to resolve the issue would be much appreciated.

## Answer (community) — Q&A User

*upvotes: 3 · updated: 2021-03-10*

I had the same error today - trying to upgrade a DAG (2019x3)  

Maybe the error started because I did not perform the initial update attempt by executing the CU8 install file from an elevated administrator shell (even though I am logged in as the administrator)  

What worked was, changing the ownership of the auth directories  

C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\ecp\auth  

C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth  

to the administrator account, and then setting permissions on that account to full control. I also gave temporary full control to the Everyone account, and verified the SYSTEM account had full control as well.  

I executed .\setup.exe /m:upgrade /IAcceptExchangeServerLicenseTerms from a mounted copy of the CU8 ISO file  

With the above the Copying files went through OK, and then the rest of the installation proceeded without a hitch

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-10*

For anyone else hitting problems with upgrading to latest CU and having to rebuild/recover exchange, just go ahead and pull off all key data such as Certificates, Exchange Database, etc and follow "recover" procedure:    

https://learn.microsoft.com/en-us/exchange/high-availability/disaster-recovery/recover-exchange-servers

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-09*

ZhengqiLou-MSFT, thanks for the reply.  Unfortunately due to the nature of Exchange the folder in question can only be accessed via the install utility through IIS and is not accessible by the user and only the system for security reasons.  Of course, that said I did try a variety of "administrator" permissions methods but to no avail.  

It is not listed as a known issue with the CU8 upgrade and is one of those problems that theoretically doesn't happen, but it did.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-09*

Hi @Stephen Challen   ,    

Good day!    

This error is likely because of the Setup wizard can't access this folder.    

If you manually open this path, you may receive the warning like this:    

    

Then you should click Continue to open it.    

So the point is to give your account a full permission or install the update in admin mode.    

Also you can use the Windows Update to do that:    

Check Advanced options and enable to receive Microsoft products updates.    

    

Then Check for updates, you will see it.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
