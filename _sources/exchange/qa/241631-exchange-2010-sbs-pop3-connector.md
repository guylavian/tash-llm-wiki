---
title: "Exchange 2010 SBS POP3 Connector"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/241631/exchange-2010-sbs-pop3-connector
question_id: 241631
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2010 SBS POP3 Connector

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/241631/exchange-2010-sbs-pop3-connector (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

****Exchange 2010 SBS POP3 Connector supports to download and distribute the mail from external pop3 mail servers. I have queries below. I am looking for answers from Technical Members.**

1. What is the new version in Exchange SBS.

2. The new version of SBS supports POP3 connectors?

3.Exchange 2019 Enterprise or standard version support the same POP3 connector?

4. If I am running SBS 2010 how can I upgrade to the latest version?

5. Is this product (SBS) supported by Microsoft Support.

6.What's the support roadmap for Exchange SBS?

**Please advise me on above.****

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-25*

Hi @Amjed Ali   ,

-   The latest version of Windows Server is 2019 Essentials and Exchange 2019 CU8.  

    The Exchange and Windows Small Business Server are two different products. The Windows SBS 2011 include Exchange and POP3 Connectors, but after that, Exchange features were removed.

-   No, after Windows SBS 2011, all Exchange features have been removed include POP3 Connectors. But Exchange has already include the POP3 protocol, and there are also some third-party POP3 connectors.

-   Yes, you could use POP3 services provided by Exchange Server.

-   If you are going to upgrade Exchange 2010 to 2019, you will have to first migrate it to Ex 2013 or 2016 and then migrate to Ex 2019.    1). First check the version of the Exchange, at least Exchange 2010 SP3 to coexist with Exchange 2013 and SP3 RU11 to coexist with Exchange 2016. Update guide  

    2). This guide How to Migrate SBS 2011 to Server 2016 (Exchange 2016)? has a guidance on the migration, you can follow it to first migrate to Windows Server 2016 and  

    Exchange 2016.  

    3). And then Migrate Exchange 2016 to Exchange 2019, it would be easier.  

    Please Note: Since these 3 web sites above is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

The Exchange Deployment Assistant could tell you how to do the migration too.

5.Yes, but the support date for SBS 2011 is determined by its individual component product’s respective lifecycles, and all of them have ended support now. But you can still get help from our QA forum: Questions In Tag: Windows-Small-Business-Server  

6.You can find the Start Date and End Date from Search Product and Services Lifecycle Information:  

Exchange and supported operating system platforms: Exchange Server supportability matrix

Regards,  

Lou

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-25*

Hi @Amjed Ali   ,

Please find the below suggestions based on my knowledge and research,

1.What is the new version in Exchange SBS.

Newer version of Exchange is 2019 and SBS is Windows Server 2019 Essentials. However, its not supported to install Exchange on Windows server essentials

2.The new version of SBS supports POP3 connectors?

Exchange Server can be integrated with the Windows server essentials environment by installing it on the second server.

https://learn.microsoft.com/en-us/windows-server-essentials/manage/integrate-an-on-premises-exchange-server-with-windows-server-essentials#install-exchange-server

3.Exchange 2019 Enterprise or standard version support the same POP3 connector?

Yes, POP3 protocol is supported in Exchange 2019

4.If I am running SBS 2010 how can I upgrade to the latest version?

Add a second server to domain i.e. Windows server 2016 standard and install Exchange 2016. Migrate Exchange services from 2010 to Exchange 2016. Install latest service pack and rollup update on the Exchange 2010 before the migration.

Please note that Exchange 2010 cannot be migrated directly to 2019.

https://social.technet.microsoft.com/Forums/en-US/997c98d1-d293-4b7e-8b15-cbe04fae3266/domain-controller-configuration-from-sbs-2011-to-server-2016?forum=smallbusinessserver

https://assistants.microsoft.com/

5.Is this product (SBS) supported by Microsoft Support.

You can check the product lifecycle here - https://support.microsoft.com/en-us/lifecycle/search/1167

6.What's the support roadmap for Exchange SBS?

As stated earlier, newer version of Exchange, 2016 and 2019 is supported to be installed on Windows Server 2016/2019 Standard or Datacenter

If the above suggestion helps, please click on "Accept Answer" and upvote it
