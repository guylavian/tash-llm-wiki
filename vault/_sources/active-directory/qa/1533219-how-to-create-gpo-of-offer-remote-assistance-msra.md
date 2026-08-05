---
title: "How to Create GPO of Offer remote assistance (MSRA) by using server 2019 AD?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1533219/how-to-create-gpo-of-offer-remote-assistance-msra
question_id: 1533219
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# How to Create GPO of Offer remote assistance (MSRA) by using server 2019 AD?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1533219/how-to-create-gpo-of-offer-remote-assistance-msra (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How to Create GPO of Offer remote assistance (MSRA) by using server 2019 AD?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-15*

Hi @muhammad waleed 

Go to Computer Configuration/Policies/Administrative Templates/System/Remote Assistance node. Right click Configure Offer Remote Assistance setting and click Edit.

On the Configure Offer Remote Assistance window, click Enabled. This enables the policy. You must permit remote control of the computer. So from the drop-down, select Allow helpers to remotely control the computer. Next to helpers, click Show button.

You can enter the names of the helpers. Add each user or group one by one. While adding helpers user or groups, use the following format.

-  <Domain Name><User Name>

-  <Domain Name><Group Name>

Click OK.

For more details please refer to the following article :

 How to Enable Remote Assistance Using Group Policy (GPO)

Please don't forget to accept helpful answer
