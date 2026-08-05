---
title: "DNS IP push using GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2123248/dns-ip-push-using-gpo
question_id: 2123248
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# DNS IP push using GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2123248/dns-ip-push-using-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Everyone,

Previously i had two DNS servers, and I recently added a third one. Now, I have the following DNS servers: Ex:

DNS1 = 192.168.1.1

DNS2 = 192.168.1.2

DNS3 = 192.168.1.3

I need to push all three DNS IPs to the Active Directory member computers using Group Policy. I have tried configuring this through the DNS Client settings, but it hasn't worked.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-27*

Hello

Thank you for posting in Q&A forum.  

Please try the steps below.

- 	On your domain controller, open the Group Policy Management Console (GPMC).

- 	Right-click on your domain or an organizational unit (OU) where you want to apply the policy, and select Create a GPO in this domain, and Link it here. Name the GPO appropriately, such as "DNS Settings".

- 	Right-click the newly created GPO and select Edit.

- 	Go to Computer Configuration > Policies > Administrative Templates > Network > DNS Client.

- 	Find the setting DNS Servers and double-click it.Set it to Enabled and enter the IP addresses of your DNS servers in the order you want them to be used, separated by commas (e.g., 192.168.1.1, 192.168.1.2, 192.168.1.3).

- 	Click Apply and then OK to save the settings.

- 	On the client computers, you can force a Group Policy update by running gpupdate /force in the Command Prompt.

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
