---
title: "Need some help with OAuth setup Exchange 2019 Hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2136415/need-some-help-with-oauth-setup-exchange-2019-hybr
question_id: 2136415
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Need some help with OAuth setup Exchange 2019 Hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2136415/need-some-help-with-oauth-setup-exchange-2019-hybr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm in the process of setting up a functioning Hybrid Minimal setup between a single Exchange 2019 server and a M365 tenant.  The customer uses Exchange on-premise and wishes to keep it that way. Some of their users are synced to the M365 tenant using the Entra Connect tool.  These users want to use OneDrive and Teams. They can login with their UPN and passwords are synced correctly. They want the calendar function to work in Teams, at the moment that function doesn't work.

I ran the Hybrid Configuration Wizard, minimal setup, and now it has finally completed succesfully without errors. On previous tries it threw an error regarding MRSProxy that has now been fixed manually and then tested. After running the wizard again all steps now completed without error.

Problem is the wizard did not do anything with OAuth it seems and i'm not sure if this wizard is supposed to handle that automatically.  When i run the Teams Exchange Integration test from Microsofts website it fails due to possible OAuth settings being incorrect or missing.

1 "Verifying if the user's mailbox is discoverable by the Teams service.

The user's mailbox is not discoverable by the Teams service. Please ask your administrators to verify the user has a mailbox and to confirm the connectivity between Teams and Exchange."

2 "Testing the Exchange API endpoint.

The Exchange API endpoint request was not successful.

Additional Details

The Bearer response header did not contain the expected trusted issuer 00000001-0000-0000-c000-000000000000@<tenant GUID>. Please check that your on-premises environment meets the minimum requirements for OAuth authentication and try running the latest version of the Hybrid Configuration Wizard again. You may also inspect the OAuth configuration yourself by using the Get-AuthServer cmdlet in the on-premises Exchange Management Shell."

When i run the command Get-AuthServer i get no result at all. Nothing.  I believe this is the reason the Teams integration might not be working.

Does anyone know what to do next exactly as guides online all seem different. I don't know the impact of me messing with these settings. It confuses me so much I'm a little stuck

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-02*

Hey Caspar,

It looks like the OAuth configuration didn’t get set up properly during the Hybrid Configuration Wizard process, and that's likely causing the issues with Teams integration. Don't worry—this can be fixed manually!

- First, check if OAuth is even enabled on your on-prem Exchange. You can do that with this command:

Get-AuthConfig

If OAuth isn't enabled, you can turn it on by running:

Set-AuthConfig -OAuth2ClientProfileEnabled $true

-Add the Office 365 Authentication Server: Once OAuth is enabled, you need to add Office 365 as an authentication server. Run this:

New-AuthServer -Name "Office 365" -AuthMetadataUrl "https://login.microsoftonline.com/<tenant GUID>/v2.0" -AuthType OAuth

Just replace <tenant GUID> with your actual tenant GUID. This will make sure your Exchange server trusts Office 365 for OAuth.

-After that, run the Teams integration test again from Microsoft’s site. It should now recognize the mailbox and the Exchange API endpoint without errors.

-If all goes well, it might help to run the Hybrid Configuration Wizard again just to make sure everything is aligned properly.

-Lastly, make sure your Exchange server is fully patched. Sometimes, missing updates can cause these kinds of issues.
