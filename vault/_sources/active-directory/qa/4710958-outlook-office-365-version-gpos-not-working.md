---
title: "Outlook (Office 365 Version) GPO's not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4710958/outlook-office-365-version-gpos-not-working
question_id: 4710958
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Outlook (Office 365 Version) GPO's not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4710958/outlook-office-365-version-gpos-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

For years, We have used Legacy Microsoft Office Products, Currently we are going to Office 365 (Business Premium) and we are having issues with Group Policy pushing out the config we need. We are looking to have Group Policy disable the Autofill when entering in email address's to avoid sending emails to the incorrect person (Which we have always had disabled) 

Program is, We have tried everything from downloading the new ADMX Templates (Download Administrative Template files (ADMX/ADML) for Microsoft Office from Official Microsoft Download Center) to trying to set up the policies in config.office.com and nothing is working. 

Has anyone run into this? I know we can do it via a Logon Script to edit a registry key but there are additional items with outlook we would like to edit as well so we would love to get the group policy working. 

Below is a snapshot of the current policy that we are trying to use.

User Configuration  (Enabled)hide

Policieshide
Administrative  Templateshide
Policy definitions (ADMX files) retrieved from the central  store.Microsoft Outlook  2016/Miscellaneous/PST Settingshide| Policy | Setting | Comment |
| --- | --- | --- |
| Prevent  users from adding PSTs to Outlook profiles and/or prevent using  Sharing-Exclusive PSTs | Enabled |  |
| |  | No PSTs can be  added |<br>| --- | --- | |Microsoft Outlook  2016/Outlook Options/Otherhide| Policy | Setting | Comment |
| --- | --- | --- |
| Admin-Controlled  Migration to New Outlook | Disabled |  |
| Disable  Outlook features in the Feedback tab under the File menu in Outlook | Enabled |  |
| Disable Outlook Mobile  Hyperlink | Enabled |  |
| Disable support  ticket creation in Outlook | Enabled |  |
| Disable  the Support tab under the File menu in Outlook | Enabled |  |
| Hide the  “Try the new Outlook” toggle in Outlook | Enabled |  |
| Make  Outlook the default program for E-mail, Contacts, and Calendar | Enabled |  |Microsoft Outlook  2016/Outlook Options/Preferences/E-mail Options/Advanced E-mail Optionshide| Policy | Setting | Comment |
| --- | --- | --- |
| When sending a message | Enabled |  |
| | Set importance: | Normal |<br>| --- | --- |<br>| Set sensitivity: | Normal |<br>| Messages expire after (days): | 0 |<br>| Allow commas as address separator | Disabled |<br>| Automatic name checking | Disabled |<br>| Delete meeting request from Inbox when responding | Enabled |<br>| Suggest names while completing To, Cc, and Bcc fields | Disabled |<br>| Add properties to attachments to enable Reply with Changes | Disabled | |

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-24*

Hello JW Luttrell,

Thank you for reaching out to the Microsoft community. 

Based on the information you provided, I have consulted with a senior member of my team about your situation, and I would like to share some more specific directions with you.

I have checked the official documentation for the autocomplete list, but haven't found any direct option to disable it for Exchange Online. Reference: The Outlook AutoComplete list - Outlook | Microsoft Learn

Previously, when you used Legacy Microsoft Office Products, you might have used your own email server, which is why the GPO policy worked properly for disabling the autocomplete list. However, with Office 365 (Business Premium), it synchronizes data from Exchange Online, which might be causing the issue.

We recommend raising a support ticket with Microsoft’s front line support team. Microsoft's back-end support team should collect some more advanced log information from Office 365 Global Admin personnel through a remote session to diagnose the current scenario. If needed, a front-line technical support engineer can also have a specific support team (specialized support) investigate some specific situations further. 

Due to the limited permissions and access resources of our forum moderators, we are unable to collect certain types of log information in public forums for this reason and for the privacy of our users' data. 

After diagnosing the situation, our technical support team can provide possible information from their point of view. 

If there are any known issues, the Technical Support Engineer can provide this information from their back-end resources. 

For the standard procedure information provided above, in your organization, Office 365 Global Admins may need to contact the Office 365 support team on the backend through an open service request so that they can diagnose this particular scenario with some more technical resources,  

For this standard procedure, the following is the official documentation that Global Admins refer to: Get support - Microsoft 365 admin | Microsoft Learn (Online option). 

Note: If you are an end-user person, you may need to contact the Office 365 Global Administrator in your business organization to contact a Technical Support Engineer for further processing.  

Important: If any of your organization's Office 365 Business/Business/Education subscriptions are from a federated partner or reseller and the global admin can't open a service request on their end, they may need to contact the reseller's support provider so they can help the global admin open the service request on their end. After that, the Office 365 support team will participate in the service request that was created. 

Thank you very much for your valuable time in your cooperation.

Sincerely

Feroz Mahmud | Microsoft Community Moderator
