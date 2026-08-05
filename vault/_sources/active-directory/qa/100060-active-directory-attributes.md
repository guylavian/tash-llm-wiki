---
title: "Active Directory attributes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/100060/active-directory-attributes
question_id: 100060
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory attributes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/100060/active-directory-attributes (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Team  

I hope you all are doing good.  I have arequirement where in i need to add below attribute for AD users.  

gender  

nationality  

Division  

Sub Division  

Unit  

Direct Manager's Name  

Matrix Manager's Name  

I am not able to locate above attributes. Please help me with correct process of adding the attributes in AD schema  

Please let me know if extended attributes will work in above scenario

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2020-09-21*

Hello @Gagandeep Singh Hoda  ,

Thank you for posting here.

We can update Schema (add attributes) based on the following steps on the DC holding Schema Master :

1.Copy the script in the following link.  

https://gallery.technet.microsoft.com/scriptcenter/56b78004-40d0-41cf-b95e-6e795b2e8a06#content

2.And save as .vbs file.  

3.Open CMD(run as Administrator), and run the script above.  

We can get the our root OID.

For example, here is root OID in domain named a.local in my lab:  

1.2.840.11356.1.8000.2554.12817.52241.32654.19773.46433.5435124.9031327

4.Open MMC->File->Add/Remove Snap-in->Active Directory Schema->Add  

Tip:If there is no Active Directory Schema, we should open cmd (run as Administrator) and run command: regsvr32 schmmgmt.dll. Then there will be Active Directory Schema in MMC.exe console when we reopen MMC.exe and click Add/Remove Snap-in.

5.Add attribute as below:  

Tip: we can not define the duplicated OID, so we can define as below:

gender--------1.2.840.11356.1.8000.2554.12817.52241.32654.19773.46433.5435124.9031327.1  

nationality--------1.2.840.11356.1.8000.2554.12817.52241.32654.19773.46433.5435124.9031327.2  

Division--------1.2.840.11356.1.8000.2554.12817.52241.32654.19773.46433.5435124.9031327.3  

Sub Division--------1.2.840.11356.1.8000.2554.12817.52241.32654.19773.46433.5435124.9031327.4  

Unit--------1.2.840.11356.1.8000.2554.12817.52241.32654.19773.46433.5435124.9031327.5  

Direct Manager's Name--------1.2.840.11356.1.8000.2554.12817.52241.32654.19773.46433.5435124.9031327.6  

Matrix Manager's Name--------1.2.840.11356.1.8000.2554.12817.52241.32654.19773.46433.5435124.9031327.7

6.After that, we can see the attribute.  

7.Make gender attribute as User attribute.  

8.After the AD replication is complete, or we can make AD replication complete forcely (run command on any one DC: repadmin /syncall /AdeP), then we can see the attribute on all the user Properties.  

Add other attributes based the similar steps above.

Hope the information above is helpful. If anything is unclear, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2020-09-20*

Hi,  

In user properties ,  there is many attributes created by default where you can add those information. Check  General , address and organization tab in user properties.  

Active+Directory+Attributes+List  

Please don't forget to mark this reply as answer if it help you to fix your issue
