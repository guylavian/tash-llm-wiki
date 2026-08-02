---
title: "Connecting by mapi - Outlook 2024 - Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2265470/connecting-by-mapi-outlook-2024-exchange
question_id: 2265470
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Connecting by mapi - Outlook 2024 - Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2265470/connecting-by-mapi-outlook-2024-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello. 

We are testing Outlook 2024 Pro Plus LTSC.

This version requires a password when connecting via NTLM.

Exchange 2016 is on-premise.

There are no such problems in version 2016, 2019.

I did a dump using Fiddler and chat gpt told me: Windows does not consider mail.contoso.su a “local intranet”

After which it offered to do a write:

Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\mail.contoso.su]

“https"=dword:00000001

And that fixed the problem of requiring a password, now Outlook connects automatically.

ChatGPT explained the problem like this:

Why Outlook 2024 was asking for a password, but older versions were not

📌 The reason is due to changes in WinINET and IE security zones

Starting with Outlook 2022+ (including 2024), Microsoft has tightened the NTLM/SSO transfer policy, especially when switching to Modern Authentication (even if you don't use it). This is due to:

increased protection against credential leakage and NTLM relay attacks

New behavior when handling IE zones and trusted nodes

In Outlook 2016/2019:

Outlook often passed NTLM credentials over HTTPS even if the host was out of the intranet zone

The behavior was more loyal, especially if a valid certificate was present

In Outlook 2024:

Outlook does not pass login/password over NTLM if the site is not recognized as local (intranet zone)

As a result - 401, Outlook does not see automatic possibility → asks for password

-  Can anyone explain this behavior and cite official sources?

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-05-14*

Hi Андрей Михалевский,

Thank you for posting your question in the Microsoft Q&A forum.

The July 2023 Outlook security updates limit access to UNC, SMB, and file:// type URLs to only those the system identifies as Local, Intranet, or Trusted Sites. After you install the Outlook Desktop July 11th security updates, when you open a link in an email, if the path points to a Fully Qualified Domain Name (FQDN) or IP address, you may not be able to open the link or receive the following error message: Something unexpected went wrong with this URL.

For your reference:

Outlook blocks opening FQDN and IP address hyperlinks after installing protections for Microsoft Outlook Security Feature Bypass Vulnerability released July 11, 2023 - Microsoft Support

Hyperlinks are not working - Outlook | Microsoft Learn

However, we cannot confirm that if your current issue for Outlook 2024 connection issue is related to these security considerations. Also, there could be many reasons cause outlook prompt password issue. In general, we need to check IIS logs, security logs, MAPI/HTTP or Autodiscover logs from Exchange server side to investigate why auth failure with 401.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
