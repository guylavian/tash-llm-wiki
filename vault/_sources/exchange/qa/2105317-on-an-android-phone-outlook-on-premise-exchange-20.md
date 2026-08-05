---
title: "On an Android phone, outlook on premise exchange 2016 does not work when connected to a server."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2105317/on-an-android-phone-outlook-on-premise-exchange-20
question_id: 2105317
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-intune-android", "office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# On an Android phone, outlook on premise exchange 2016 does not work when connected to a server.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2105317/on-an-android-phone-outlook-on-premise-exchange-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning!

We use an on premise Exchange 2016 mail server in AD domain. Our internal mail works without any problems.

We have users who also use outlook on their phones (Android version 14).

He has had no problems for months, but when he changed the password on his local account he could no longer connect to the mail server on his phone.

This is the error message: An error occurred during authentication.

Connection works with other mail apps, but not with the outlook app.

Access is enabled in the EAC.

What could be the problem?

Thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-11-18*

Hi László,

Thank you for the update. I understand that the issue persists and that switching to another mail app isn't a suitable solution for your company. Since other mail apps work fine, but the Outlook app is still causing authentication errors, here are a few additional steps to consider:

-Review the Exchange server logs (specifically the IIS logs and Event Viewer logs) for any specific errors related to the Outlook app or failed authentication attempts. There may be more details in the logs that could point to the root cause.

-Verify that no security policies or device management settings (e.g., Microsoft Intune) are interfering with the Outlook app’s ability to authenticate the device correctly.

If none of these steps resolve the issue, it may be worth reaching out to Microsoft Support for more in-depth troubleshooting.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-14*

Hi Jake Zhang,

Thanks for the suggested options, but unfortunately the problem is still not solved.

The company manager insists on the outlook application, so the other commenter's idea (gmail mail settings) is not a good solution for us.

Thanks again.

All the best,

László Tótváradi

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-18*

Hi @Tótváradi László,

Welcome to the Microsoft Q&A platform!

Based on your description, let me first explain that when a user changes their password in an Active Directory (AD) environment, it sometimes takes some time for the change to propagate through the system. Here are some things to check and try:

-  Make sure the password change has been fully propagated to the AD environment. Sometimes, there can be delays in synchronization, which can cause authentication issues.

-  The Outlook app on your phone may be caching old credentials. Try clearing the cache or resetting the app:

-  Go to Settings > Apps > Outlook > Store > Clear Cache.

-  If this doesn't work, you may need to clear your data or reinstall the app.

-  Remove the email account from the Outlook app and add it again. This can force the app to reauthenticate with the new credentials.

-  As mentioned in the search results, IIS token caching may be a factor. The default value is 15 minutes, but it can be controlled through the registry. You may need to adjust the UserTokenTTL registry setting on the server running IIS.

-  The security settings of some devices may interfere with the authentication process. Make sure the device is not blocking the connection due to security policies.

-  Since other mail applications are working, this indicates that the issue is specific to the Outlook application. While not a solution, using an alternate mail application may be a temporary workaround.

-  Make sure the Outlook application is up to date. There may be a bug in the version you are using that is causing the authentication issue.

-  Make sure there are no network issues that could cause the authentication to fail. Sometimes, a poor network connection can cause authentication errors.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
