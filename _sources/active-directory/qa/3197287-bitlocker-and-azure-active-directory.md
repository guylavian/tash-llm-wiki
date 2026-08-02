---
title: "Bitlocker and Azure Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3197287/bitlocker-and-azure-active-directory
question_id: 3197287
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 7
qa_tags: []
---
# Bitlocker and Azure Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3197287/bitlocker-and-azure-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When setting up Bitlocker on an Azure AD connected device, you have the following options: https://i.imgur.com/MHbPBu6.png

A question about the exact wording of "Save to your cloud domain account". IMO that's not totally clear where it stores it. It infers, to me, that it would save it against my user domain account. However, I suspect it's saved against the device in Azure
 AD as that's the only place I can see this. Is this correct?

At the moment, the laptops are set-up by IT using their own account and a key step is to save the Bitlocker key. However, when a user first logs on, we also save it there. I suspect this later step is not needed.

Supplemental question - on the page linked below (which is the link from the Bitlocker screen), it says to access your Microsoft Azure account to get the Bitlocker key:

https://support.microsoft.com/en-gb/help/4026181/windows-10-find-my-bitlocker-recovery-key

Can I also confirm that this misleading for normal users as the profile page that this takes you to has no information about Bitlocker:

https://i.imgur.com/MeWkcdN.png

And that the only way a user can retrieve their Bitlocker recovery key is to ask an admin with access to the Azure portal to look it up based upon their computer name?

## Answer (community) — community member

*upvotes: 0 · updated: 2019-03-21*

Hi Rob-Nicholson-Malt

My name is Sarah Kong and I am an independent adviser that is here to try and help you with your issue.

On-premise domain accounts and Azure AD accounts are 2 separate accounts that you can login with.

You can join your PC to both Onprem AD and Azure AD.

What makes the difference is which one you login in with.

For my example let's say my work\onprem account is kong@microsoft.com and my Azure AD account is ******@kong.onmicrosoft.com.

If i login with the kong@microsoft.com then i am authenticating to my onprem servers.

If I login with the ******@kong.onmicrosoft.com then i am authenticating to Azure AD.

So as for your questions when you enable bitlocker which account are you logged in with?  onprem or azure AD?

And if onprem i hope you have a GPO on your DCs that says recovery key stored in Active Directory.  If that is the case then you don't have to worry about saving it to the cloud and yes IT staff would retrieve the key from the computer object for the user.

If they are logging in with their Azure AD account and enabling bitlocker then same thing IT will get it from the Devices in Azure AD.
