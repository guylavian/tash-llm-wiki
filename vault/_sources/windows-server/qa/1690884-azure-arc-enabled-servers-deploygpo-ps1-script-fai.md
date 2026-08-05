---
title: "Azure Arc-enabled Servers - DeployGPO.ps1 Script fails with \"C:\\<path>\\DeployGPO.ps1 : Exception calling \"ProtectBase64\" with \"2\" argument(s): \"Encryption failed.\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1690884/azure-arc-enabled-servers-deploygpo-ps1-script-fai
question_id: 1690884
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["azure-arc", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Azure Arc-enabled Servers - DeployGPO.ps1 Script fails with "C:\<path>\DeployGPO.ps1 : Exception calling "ProtectBase64" with "2" argument(s): "Encryption failed."

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1690884/azure-arc-enabled-servers-deploygpo-ps1-script-fai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to deploy Azure Arc for a client and attempting to enroll machines at scale following the "Connect machines at sale using Group Policy" KB. I have configured all of the prerequisites and gone through the Azure setup portion of the scripts.

I am having issues with the DeployGPO.ps1 script completing. The script gets through the GPO portion successfully, but hangs at the encryption section and eventually fails with "C:<path>\DeployGPO.ps1 : Exception calling "ProtectBase64" with "2" argument(s): "Encryption failed.". The only place I can find mention of this error is in this github comment thread on the official ArcEnabledServersGroupPolicy repo. I have tried all of the solutions in the comment thread, as well as the linked related thread, without success. I have also confirmed all .NET updates are installed and ensured that no dependencies are being blocked by both the corporate firewall and windows firewall.

In my case, the issue seems to be environment related and specific to the "$encryptedSecret = [DpapiNgUtil]::ProtectBase64($descriptor, $ServicePrincipalSecret)" line in the PowerShell script. There are no issues importing the module required which defines how to use DpapiNgUtil. I have isolated this section of the script with the required variables and was able to have it successfully run in a lab environment, so I know it isn't a bug or mistake in the script itself. Using that same, confirmed working, portion of the script anywhere in the customer environment, even fresh Windows Server 2022 VMs that have not been joined to the domain yet, all fail with the same "Encryption failed" error described above. Installing the agent manually on the VMs works but is not feasible with the number of VMs in the environment.

I am working on getting a support request setup through our partner portal, but figured I would post here as well while that gets approved. Any help is appreciated!

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2024-09-18*

are you following this:

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2024-07-01*

https://techcommunity.microsoft.com/t5/security-compliance-and-identity/onboard-to-azure-arc-with-security-in-mind/ba-p/4114267
