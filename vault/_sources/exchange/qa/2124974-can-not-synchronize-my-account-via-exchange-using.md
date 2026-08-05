---
title: "Can not synchronize my account via Exchange (Using private Mail-Address)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2124974/can-not-synchronize-my-account-via-exchange-using
question_id: 2124974
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Can not synchronize my account via Exchange (Using private Mail-Address)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2124974/can-not-synchronize-my-account-via-exchange-using (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I am using a private hosted e-mail address as my login to microsoft/office. (so no @live.com or @outlook.com or similar) I used to share the contacts and calendar of this account to several devices (Windows/Android) and clients (Thunderbird using TbSync) via Exchange (using https://m.office.com:443 as exchange server) This worked for years. However it does not work anymore.

I'm not able to connect using my email address and my password. I double checked the pw and even set it to a new one, however no client was able to connect.  

Also using the cryptic ...@outlook.com alias does not work.

Using an app password from my security settings also does not work.

Furthermore I'm not able to delete any of the mobile devices (which worked in the past nut not anymore) listed in outlook settings (under account->mobile devices).

So I'm a bit stuck ...

Is there maybe some issue with accounts with private mail addresses as account handle?

Or is it about two-factor authentication, as I lately switched to authentication with the authenticator app? (However turning TFA off also yielded no results and is honestly not an option)

Best regards Florian

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-02*

Hi @Florian Marquardt  ,

Welcome to the Microsoft Q&A platform!

Based on your description, you are dealing with an issue where you cannot sync your account through Exchange. Here are some things you can check and try:

-  Since you recently switched to using an authenticator app, make sure all your devices and clients are compatible with 2FA. Some older clients may not support modern authentication methods. You may need to create an app password specifically for these clients.

-  Double-check the server settings you are using. The URL https://m.office.com:443 should be correct, but make sure there haven't been any changes or updates to the server settings that could affect the connection.

-  Sometimes problems can arise if there is a mix-up between personal and work/school accounts. Make sure you are using the correct account type for each service. If your private email is linked to both personal and work accounts, this can cause conflicts.

-  If you are unable to remove the mobile device from your account settings, it could be due to permissions or sync issues. Try accessing your account settings from another device or browser to see if that helps.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
