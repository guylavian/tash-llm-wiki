---
title: "Blocking attachments in OWA not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1487206/blocking-attachments-in-owa-not-working
question_id: 1487206
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Blocking attachments in OWA not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1487206/blocking-attachments-in-owa-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have exchange server 2019. I have my OWA portal setup. I need to block users from opening or downloading attachments.  In the EAC GUI I  have gone to Permissions>Outlook Web App Policies" I have created a new policy and unchecked "Direct File Access" and on public and private or OWA devices. I have done the same for mobile and modified the default policies in both as well. However users can still open/download attachments. What am I missing? Additionally I have user powershell to mod the policies and I see the checkboxes in the GUI populate and depopulate when I toggle the script back and forth.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-11*

Hello @Ummmmbeer  ,
Welcome to our forum！

According to your description, it seems that you want to restrict downloading attachments from Exchange 2019 OWA but it does not take effect. And if you've had the chance to test it with other users? Also, please make sure that the policy has been assigned to all the relevant users.

As you mentioned using PowerShell to change the policy, it is recommended that you first use 'Get-OwaMailboxPolicy | Fl' to check whether DirectFileAccessOnPublicComputersEnabled and DirectFileAccessOnPrivateComputersEnabled  are both set to false.

If not, I suggest you try running Get-OwaMailboxPolicy | Set-OwaMailboxPolicy -DirectFileAccessOnPublicComputersEnabled $false -DirectFileAccessOnPrivateComputersEnabled $false command. It will take about two minutes to complete. After that, you could run Get-OwaMailboxPolicy | Fl again to see if it has been set to false. And then you could test again to see if it works.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in [our documentation] to enable e-mail notifications if you want to receive the related email notification for this thread.
