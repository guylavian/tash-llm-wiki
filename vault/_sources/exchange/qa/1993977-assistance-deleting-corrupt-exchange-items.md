---
title: "Assistance deleting corrupt exchange items"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1993977/assistance-deleting-corrupt-exchange-items
question_id: 1993977
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Assistance deleting corrupt exchange items

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1993977/assistance-deleting-corrupt-exchange-items (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We need to inform you that you will need to use Postman or work with Microsoft to match the itemID to the item name. Once the item name has been identified, you can self-service by either moving the malformed item to another location or deleting it if it is no longer needed. These actions will allow backups to successfully complete

• Martyn Jones

AAMkADY1YjQxZDI3LTk2M2MtNDk3Yy04NjFkLWJhY2RmNDY1NGQxNwBGAAAAAABFAlRw0mDVEZVhALDQSfYABwDmNr07LmD1SK1VX-wI266cAAACRaxOAADmNr07LmD1SK1VX-wI266cAAACRdw5AAA=

AAMkADY1YjQxZDI3LTk2M2MtNDk3Yy04NjFkLWJhY2RmNDY1NGQxNwBGAAAAAABFAlRw0mDVEZVhALDQSfYABwDmNr07LmD1SK1VX-wI266cAAACRaxOAADmNr07LmD1SK1VX-wI266cAAACRdx9AAA=

AAMkADY1YjQxZDI3LTk2M2MtNDk3Yy04NjFkLWJhY2RmNDY1NGQxNwBGAAAAAABFAlRw0mDVEZVhALDQSfYABwDmNr07LmD1SK1VX-wI266cAAACRaxOAADmNr07LmD1SK1VX-wI266cAAACRdxkAAA=

AAMkADY1YjQxZDI3LTk2M2MtNDk3Yy04NjFkLWJhY2RmNDY1NGQxNwBGAAAAAABFAlRw0mDVEZVhALDQSfYABwDmNr07LmD1SK1VX-wI266cAAACRaxOAADmNr07LmD1SK1VX-wI266cAAACRdyMAAA=

AAMkADY1YjQxZDI3LTk2M2MtNDk3Yy04NjFkLWJhY2RmNDY1NGQxNwBGAAAAAABFAlRw0mDVEZVhALDQSfYABwDmNr07LmD1SK1VX-wI266cAAACRaxOAADmNr07LmD1SK1VX-wI266cAAACRdymAAA=

Gemma Johnson

AAMkAGQwOTQ2NjZjLTNjNjEtNGMxNC1iOTNkLWJjMTg2MTVlZTEzMwBGAAAAAAC9GLPCK7GMRpV4LXhH1VFGBwDmNr07LmD1SK1VX-wI266cAAADQp8HAADmNr07LmD1SK1VX-wI266cAAADQ06uAAA=

AAMkAGQwOTQ2NjZjLTNjNjEtNGMxNC1iOTNkLWJjMTg2MTVlZTEzMwBGAAAAAAC9GLPCK7GMRpV4LXhH1VFGBwDmNr07LmD1SK1VX-wI266cAAADQp72AADmNr07LmD1SK1VX-wI266cAAADRP_bAAA=

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-26*

Hello, @Flemingo,

Welcome to the Microsoft Q&A platform!

Based on your description, I understand that you would like to use Postman to assist you in removing corrupt exchange items, but unfortunately the method you want to use is not currently supported by Exchange.

As an alternative, I will suggest you remove corrupted Exchange items using Exchange inbuilt way. You could try to manage and delete corrupt item through Retention Policy in EAC by following the steps below:

1.Log in to EAC.

2.In the left-hand navigation pane, select "Recipients".

3.In the "Mailboxes" tab, select the mailbox that you want to manage.

4.Double-click the selected mailbox to open its properties window as screenshot below.

5.In the "Retention Policy" section, you can view and manage the retention policies assigned to the mailbox. Retention policies can help you automatically delete or move old or corrupt items. For more information about retention policies, you can refer to this document: Retention tags and retention policies in Exchange Online | Microsoft Learn.

6.Use In-Place Hold and Litigation Hold: If you need to retain specific items for future reference, you can use the "In-Place Hold and Litigation Hold" feature. This will ensure that these items are not deleted. For more information, you can refer to this document: In-Place Hold and Litigation Hold in Exchange Server | Microsoft Learn.

Please feel free to contact me if you have any queries. If my reply is helpful to you, please mark it as the answer so that other users can refer to it. Thank you for your support and understanding.

Best Wishes,

Alex Zhang
