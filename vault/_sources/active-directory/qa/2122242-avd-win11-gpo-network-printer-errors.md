---
title: "AVD - Win11 - GPO Network Printer errors"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2122242/avd-win11-gpo-network-printer-errors
question_id: 2122242
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-virtual-desktop", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# AVD - Win11 - GPO Network Printer errors

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2122242/avd-win11-gpo-network-printer-errors (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone, 

We have a W2K16 Print server setup with Win10 drivers for all Print Devices 

We noticed that when the GPO runs to map printers (via AD group membership) some users don't get all the printers mapped and some get. This is from AVD Win11. 

These are the errors on the Session hosts:

`Group Policy Object did not apply because it failed with error code '0x80070057 The parameter is incorrect.' This error was suppressed.`

`Group Policy Object did not apply because it failed with error code '0x80070771 The specified printer has been deleted.' This error was suppressed.`

`Group Policy Object did not apply because it failed with error code '0x80070bc4 No printers were found.' This error was suppressed.`

Logging the user out and back in resolves the issue but it's happing random to any users every day.

Thanks, M

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-05-27*

Old question, but someone might find this useful:

The AVD hosts are probably missing the printer driver.

It's a huge security risk to let normal user accounts install printer drivers so this is most likely blocked. If you browse to the print server and try to add manually you might get an UAC prompt (although that popup can also be blocked)

Install the printer driver on clients before adding new printers or updating printer drivers.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-22*

Hi SenhorDolas,

Thank you for reaching out to the Microsoft Q&A platform.

Here are some steps you can take to troubleshoot and resolve this issue:

Make sure your printer drivers are up-to-date and work with Windows 11.

Check for any Windows update pending and apply any necessary patches.

Check the GPO settings for printer mapping and the printers are correctly configured and that the GPO is linked to the correct Organizational Unit (OU).

https://learn.microsoft.com/en-us/troubleshoot/windows-client/group-policy/scenario-guide-gpo-to-map-network-drive-doesn-t-apply-as-expected

The GPO is set to apply to the correct group of users and that there are no conflicting policies Check the permissions on the printers the users have the necessary permissions to access the printers.

Please find the below document link for your reference:

https://learn.microsoft.com/en-us/troubleshoot/windows-server/printing/use-group-policy-to-control-ad-printer#configure-printer-specific-settings-for-users

If an answer has been helpful, please consider accept the answer and "Upvote" to help increase visibility of this question for other members of the Microsoft Q&A community.

Thank You.
