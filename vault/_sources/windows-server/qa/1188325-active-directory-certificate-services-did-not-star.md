---
title: "Active Directory Certificate Services did not start: Could not load or verify the current CA certificate.  corp-SRV-CA Keyset does not exist 0x80090016 (-2146893802 NTE_BAD_KEYSET)."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1188325/active-directory-certificate-services-did-not-star
question_id: 1188325
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Active Directory Certificate Services did not start: Could not load or verify the current CA certificate.  corp-SRV-CA Keyset does not exist 0x80090016 (-2146893802 NTE_BAD_KEYSET).

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1188325/active-directory-certificate-services-did-not-star (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,

After a OS restart to install updates, the OS shown the watermark of "Windows not activated".  At first tried to fix it through Windows activation troubleshooting, but was not possible:

On Windows Server console, we also noticed that Active Directory Certificate Services was not started, and looking at Event Viewer, there was the message:

Active Directory Certificate Services did not start: Could not load or verify the current CA certificate.  corp-SRV-CA Keyset does not exist 0x80090016 (-2146893802 NTE_BAD_KEYSET).

Seems like key is no longer available for this CA, and that leads to ADCS to not start.

As a test attempt, to see if it was during last restart, tried to restore a previous machine state on a test VM, and also noticed that this was already missing before last reboot.

On test VM tried to remove and install ADCS again, but when trying to install it, I got a message with an error 8007371c.

Tried after on test VM, DISM and SFC, but still ADCS was giving the same error while installing it.

Any of you know how can I solve this? 

Thank you.

## Answers

_No answers on this thread._
