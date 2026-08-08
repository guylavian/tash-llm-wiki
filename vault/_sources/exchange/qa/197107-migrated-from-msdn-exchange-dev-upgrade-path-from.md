---
title: "[Migrated from MSDN Exchange Dev]Upgrade path from Exchange 2013 SP1 to CU22/CU23"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/197107/migrated-from-msdn-exchange-dev-upgrade-path-from
question_id: 197107
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# [Migrated from MSDN Exchange Dev]Upgrade path from Exchange 2013 SP1 to CU22/CU23

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/197107/migrated-from-msdn-exchange-dev-upgrade-path-from (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note]  

This question was originally asked on the MSDN Exchange Development forum which focuses on development questions on Exchange.  

As the former Outlook forums on TechNet have been migrated to Microsoft Q&A forum, we migrated this question manually in order to continue the discussion here.

[MSDN Link]  

Upgrade path from Exchange 2013 SP1 to CU22/CU23

[Original post]  

I'm planning to migrate current Exchange server 2013 SP1 (CU4) to Exchange 2016. The minimum requirement is to upgrade to Exchange 2013 CU10 that can co-exist with Exchange 2016. However I can only download Exchange 2013 CU22 / CU23 but not CU10.

The Exchange mailbox server with DAG is running on two Window server 2012R2.

1) Where can I download Exchange 2013 CU10 or above, except CU22 and CU23?

2) What is the upgrade path to Exchange 2013 CU22/CU23? and prerequisite works?  

Thanks,

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2020-12-14*

Hi,    

Its always recommended to stay in the latest CU of Exchange. Though the minimum CU is 10 for co-existence with Exchange 2016, as per the latest release and support, its recommended to upgrade to CU22/23.     

Each CU release is supported for three months after the release of the next CU. Because CUs become unsupported after six months, Microsoft removes them from the download center. The removal takes place three months after support ends, so a CU is available for a total of nine months. At any given time you can expect to find only the three most recent CUs for each of Exchange 2013 and 2016 available for download.    

To upgrade from Exchange server 2013 SP1 (CU4) to CU22/23, is a big step. Please find the below steps,    

-  Upgrade the .Net framework to the supported version first and then the Exchange - Exchange 2013 CU 22 supports 4.7.2 and CU23 supports both 4.7.2 & 4.8 - https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix?view=exchserver-2019#microsoft-net-framework    

-  Prepare the Active directory as the schema needs to be updated - https://learn.microsoft.com/en-us/exchange/prepare-active-directory-and-domains-exchange-2013-help    

-  verify the other software pre-requisites - https://learn.microsoft.com/en-us/exchange/exchange-2013-prerequisites-exchange-2013-help#windows-server-2012-r2-and-windows-server-2012-prerequisites    

-  Upgrade using GUI or unattended setup    

Additionally, please find the references for upgrading in DAG environment    

https://learn.microsoft.com/en-us/exchange/managing-database-availability-groups-exchange-2013-help#performing-maintenance-on-dag-members    

https://practical365.com/exchange-server/exchange-2013-installing-cumulative-updates/    

Once the Exchange 2013 has been upgraded, please to install the Exchange 2016 by following its system and software requirements.    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/system-requirements?view=exchserver-2016    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prerequisites?view=exchserver-2016    

If the above suggestion helps, please click on "Accept Answer" and upvote it

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-14*

Hi,

1) Where can I download Exchange 2013 CU10 or above, except CU22 and CU23?

Microsoft provides download files only for N-2 versions for an Exchange Server cumulative update (CU), where "N" is the latest CU.  

You may find the older versions from some third-party sources but it is always recommended to download the latest updates.

2) What is the upgrade path to Exchange 2013 CU22/CU23? and prerequisite works?

You need to install .Microsoft .NET Framework 4.7.2 and Visual C++ Redistributable Packages for Visual Studio 2013 for Exchange 2013 CU23.  

  

And prepare Active Directory and domains via the CU23 setup.exe before upgrade.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
