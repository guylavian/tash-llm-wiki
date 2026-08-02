---
title: "Exchange 2013 - CU23 installation - schema's entries vs currect exchange version not match"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/238026/exchange-2013-cu23-installation-schemas-entries-vs
question_id: 238026
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange 2013 - CU23 installation - schema's entries vs currect exchange version not match

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/238026/exchange-2013-cu23-installation-schemas-entries-vs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I want to finally update single Exchange 2013 to latest available CU23.  

My plan is to make it right and in few steps, so first install prerequisites (eg. .NEt 4.7.2), then update schema and last make an update and install CU.  

I started to check my current Ex version in comparison to schema's keys and I see big disprepancy.  

In PS current version shows Version 15.0 (Build 847.32) which refers to Exchange Server 2013 SP1, the same version is listed in Program & Features.  

But I checked schema attributes in domain (rangeUpper,objectVersion) and they poiting that I have installed other CU (which is not true as CU23 will be the very first).  

See below,  

DSQUERY.exe * "CN=Ebro,CN=Microsoft Exchange,CN=Services,CN=Configuration, DC=xxx,DC=xxx,DC=com" -Scope base -Attr msExchProductId  ==>15.00.1320.004  

DSQUERY.exe * "CN=Microsoft Exchange System Objects, DC=xxx,DC=xxx,DC=com" -Scope base -Attr objectVersion ===>13236  

DSQUERY.exe * "CN=Ebro,CN=Microsoft Exchange,CN=Services,CN=Configuration, DC=xxx,DC=xxx,DC=com" -Scope base -Attr objectVersion  ===> 16130  

DSQUERY.exe * "CN=ms-Exch-Schema-Version-Pt,CN=schema,CN=configuration, DC=xxx,DC=xxx,DC=com" -Scope base -Attr rangeUpper ===>15312  

It looks that based on above entries I am somewhere in CU10-21.  

Where should I look to check if there are any CU installed (as I wrote there isn't any CU installed in ADD/Remove programs) , or maybe I can leave it and just install CU23 ??

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-21*

Hi,@Jack       

According to the msExchProductId 15.00.1320.004 ,it seems that your Active Directory was formerly prepared for Exchange CU17.    

If you didn't actually install Exchange CU17 or have uninstalled CU17 , the changes in active directory will remain and not be removed.    

While you don't need to worry about it.    

You may just need to perform the Prepare Active Directory and domains steps when you install CU23.    

And as Ashok suggested, make sure all the prerequisites are installed.    

Here is also a Microsoft document on this topic for your reference:    

What changes in Active Directory when Exchange 2013 is installed?    

    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-20*

Hi @Jack   ,

You can check the Exchange version using Get-ExchangeServer | select Name,AdminDisplayversion

Schema version indicates that Active directory preparation has been done with the Exchange server media.

For this upgrade, you can ignore the existing values and follow the below steps,

1.Ensure that all Exchange 2013 system requirements are met  

https://learn.microsoft.com/en-us/exchange/exchange-2013-system-requirements-exchange-2013-help  

2.Install the pre-requisites - Especially .NET Framework  

https://learn.microsoft.com/en-us/exchange/exchange-2013-prerequisites-exchange-2013-help  

3.Prepare the Active Directory - You can also verify the same values once the AD preparation has been done with CU23 setup  

https://learn.microsoft.com/en-us/exchange/prepare-active-directory-and-domains-exchange-2013-help  

4.Install the Update using GUI or unattended mode  

https://learn.microsoft.com/en-us/exchange/upgrade-exchange-2013-to-the-latest-cumulative-update-or-service-pack-exchange-2013-help

If the above suggestion helps, please click on "Accept Answer" and upvote it
