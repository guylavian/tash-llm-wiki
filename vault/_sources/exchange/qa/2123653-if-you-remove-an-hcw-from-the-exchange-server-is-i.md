---
title: "If you remove an HCW from the Exchange server, is it prohibited to do it again?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2123653/if-you-remove-an-hcw-from-the-exchange-server-is-i
question_id: 2123653
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# If you remove an HCW from the Exchange server, is it prohibited to do it again?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2123653/if-you-remove-an-hcw-from-the-exchange-server-is-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After removing the Hybrid Configuration Wizard (HCW) from the Exchange server, is it possible to reconfigure the HCW on the same Exchange server where the HCW setup was removed? FYI, the same Microsoft 365 tenant will be used.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-28*

Hello, @Camille Ross Ann Rudio,

Welcome to the Microsoft Q&A platform!

Yes, after removing the Hybrid Configuration Wizard (HCW) from an Exchange server, you can still reconfigure the HCW on the same Exchange server, even if you are using the same Microsoft 365 tenant. Here are the general steps to follow:

1.Download and Install HCW: You can download the HCW from the Exchange Admin Center or the Microsoft 365 Admin Center.

2.Run the HCW: Launch the HCW and sign in with your Microsoft 365 global administrator account.

3.Follow the prompts: The wizard will guide you through the necessary steps to re-establish the hybrid configuration. You will need to provide appropriate credentials for both your on-premises Exchange server and your Microsoft 365 tenant.

4.Verify and finalize: After the HCW completes, it will provide you with a summary of the configuration changes made. Verify that everything looks correct and finalize the setup.

If you encounter any issues or need detailed guidance, Microsoft's documentation on the Hybrid Configuration Wizard can be very helpful: https://learn.microsoft.com/en-us/exchange/hybrid-configuration-wizard. 

One point you need to note is that, since you're using the same Microsoft 365 tenant, you won't need to reverify your domain ownership if the federation trust still exists and is valid. However, ensure that all prerequisites are met, such as having the necessary permissions and valid certificates. If you need to change the mail flow configuration, you will need to re-run the HCW and make the necessary adjustments.

In addition, a case study similar to your needs is provided for your reference: https://learn.microsoft.com/en-us/answers/questions/183403/re-running-reconfiguring-exchange-hcw，

If the answer is helpful please click on ACCEPT ANSWER as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.

Best Wishes,

Alex Zhang
