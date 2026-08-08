---
title: "Exchange Preset Security Policies in Defender"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2007615/exchange-preset-security-policies-in-defender
question_id: 2007615
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-microsoft-defender-defender-for-cloud", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Preset Security Policies in Defender

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2007615/exchange-preset-security-policies-in-defender (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

I enabled Exchange Preset Security Policies in Defender portal with Standard Protection.

This is suppose to include Safe Links and Safe Attachments protections.

When I browse to 

Microsoft Defender -> Email & collaboration -> Policies & Rules -> Anti-phishing or Anti-spam or Anti-malware, I can see a new policy rule named "Standard Preset Security Policy".

But when I browse to Safe attachments or Safe links, I do not see new "Standard Preset Security Policy", instead I see an advice to enable Preset Security Policies.

How can I know, if Preset Security Policies has enabled Safe attachments or Safe links policies?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-30*

Hi

And thanks! I somehow managed to miss the setting for all users regarding links and attachments.

Now I can see Preset Policy for both.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-29*

Hello, @IMK,

Welcome to the Microsoft Q&A platform!

As Andy David said, if you successfully apply Exchange Preset Security Policies to a group or to all recipients, then you should see the preset policies listed for Safe links and Safe attachments.

I'm just going to reproduce your problem and provide an action to fix it for your reference.

After my testing, the Exchange Preset Security Policy is not visible and recommended to be enabled when the setup is complete only when the applicable object is set to None under the Apply Defender for Office 365 protection interface, but not when the other three options are selected. As is shown in the image below.

To solve your problem, I suggest you follow the steps I have given below.

1.Browse to Microsoft Defender -> Email & collaboration -> Policies & Rules ->Threat policies -> Preset security policies, select Manage protection settings.

-  According to your actual situation, select the scope of application you need under the Apply Exchange Online Protection interface, and be careful not to select None, or you will encounter the same problem under the interface of Anti-phishing, Anti-spam and Anti-malware.

-  Do the same as 2 under the Apply Defender for Office 365 protection interface.

-  Follow the process to complete the rest of the setup and make sure that Standard protection is turned on after the setup is complete.

After completing the above operations , As shown in the screen, you should see the preset policies listed for Safe links and Safe attachments.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Thank you for your support and understanding.

Best Wishes,

Alex Zhang
