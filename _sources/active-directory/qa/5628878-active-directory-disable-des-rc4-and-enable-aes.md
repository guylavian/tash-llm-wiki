---
title: "Active directory: disable DES/RC4  and enable AES"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5628878/active-directory-disable-des-rc4-and-enable-aes
question_id: 5628878
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Active directory: disable DES/RC4  and enable AES

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5628878/active-directory-disable-des-rc4-and-enable-aes (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
For security reasons, I want to disable the risky DES/RC4 protocols and enable AES via GPO.
I've been checking the events on my domain controllers and I don't find any 4769 events. Does this mean I'm ready to enable AES?

Thanks
```

## Answer (community) — community member

*upvotes: 0 · updated: 2025-11-19*

To disable DES and RC4 encryption protocols and enable AES in your Active Directory environment, you can configure the encryption types allowed for Kerberos via Group Policy. Here are the steps you should follow:

-  Open Group Policy Management: Navigate to the Group Policy Management Console on your domain controller.

-  Edit the Default Domain Policy: Locate the Default Domain Policy or create a new GPO that will apply to your domain controllers.

-  Configure Encryption Types: Go to Computer Configuration > Policies > Windows Settings > Security Settings > Local Policies > Security Options. Look for the policy named Network security: Configure encryption types allowed for Kerberos.

-  Enable AES Encryption: Ensure that you check the options for AES128_HMAC_SHA1 and AES256_HMAC_SHA1 to enable AES encryption.

-  Disable RC4: If you want to disable RC4, make sure that it is not selected in the same policy settings.

Regarding the absence of Event ID 4769, this event indicates that a Kerberos ticket was requested. If you are not seeing these events, it may suggest that there are no requests for tickets using the RC4 encryption type, which could imply that your environment is ready to enable AES. However, it's essential to ensure that all systems in your environment support AES before making this change.

Always test the configuration in a controlled environment before applying it broadly to avoid any disruptions.

References:

-  Turn off the AllowNT4Crypto setting on all the affected domain controllers

-  Disable RC4 while installing Operations Manager
