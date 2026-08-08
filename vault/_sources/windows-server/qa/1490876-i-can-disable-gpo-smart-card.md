---
title: "i can disable gpo smart card?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1490876/i-can-disable-gpo-smart-card
question_id: 1490876
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# i can disable gpo smart card?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1490876/i-can-disable-gpo-smart-card (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning everyone,
I applied a GPO for access with windows hello or smart card. All right now it doesn't recognize my pin or smart card. I am completely cut off from pcs because I can't log in anymore. It won't even log me in remote machine to the server. How do I disable this without being able to log into any pc?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-15*

Hello Roberto Lombardi AN-IT-MGN,
Thank you for posting in Q&A forum.
1.Are you in a domain environment? If so, Domain administrators can use their accounts to log in to Domain Controller and disable or change relevant group policy settings.
2.If your PC is in one workgroup, do you have access to a local administrator account? It can be used to log in and modify or disable group policies that cause issues.
3.Please check that the card reader is in good contact. If it is a card reader with a USB interface, you can try a different USB interface.
4. Maybe you can try a different card reader.

5.Except smart card authentication, did you have phone authentication? If so, you can try phone authentication.  

6.Maybe smart card driver casued the issue, you can try to update or uninstall and install smart card driver after you can login the machine.
I hope the information above is helpful.
If you have any questions or concerns, please feel free to let us know.
Best Regards,
Daisy Zhou

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-01-13*

Hello Roberto, the easy way out of this: you'll have to ask another user with admin rights to disable the GPO.
This is a good example why at least one admin account should be exempt from most if not every new policy applied.
