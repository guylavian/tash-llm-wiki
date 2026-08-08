---
title: "Exchange not syncing default alert times on calendar appointments with iOS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1501296/exchange-not-syncing-default-alert-times-on-calend
question_id: 1501296
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 2
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-other-l1"]
---
# Exchange not syncing default alert times on calendar appointments with iOS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1501296/exchange-not-syncing-default-alert-times-on-calend (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,

I am an IT Admin and my problem is a known issue, the problem is a sync issue when using any iOS device with MS Exchange account syncing with the Apple Calendar app. I sent this to Microsoft Support but hoping that someone out here may have a resolution? I dreadfully think its a backend developer issue on either MS/Apple or Both but hoping someone has found a fix.

SCENARIO:

When you enter an appointment on an iOS device and you choose the default alert time (IE: 5, 10, 15 Min) and save the appointment, the appointment syncs with Exchange with an alert time of "None" on every device except for the device the appointment was entered into. That device will show the chosen alert time.
Even, if you then go back into that appointment on the iPhone and edit only the alert time to something else (ie: 15 min to 30 min) it wont sync the change to the server, BUT if you edit the appointment and change anything else, such as the description, location or notes AND the alert time then the alert time will change. across all devices.
However, if you MANUALLY choose the alert time when creating the appointment then it will sync that alert time to the Exchange server and be displayed on all other devices.

PLEASE NOTE:

This issue was replicated on 4 DIFFERENT PHYSICAL iPhones and iPads, with 2 DIFFERENT exchange accounts and the same result occurred. Thus proving that this is not a phone or account issue but and issue with the iOS to Exchange sync.

This issue DOES NOT occur when syncing with Google, Yahoo! or iCloud proving the issue IS MICROSOFT and the sync that goes on with Apple iOS.

We researched and see that this issue all over the web but do not see a resolution as of yet.

Again This IS NOT THE IPHONE as it was tested on multiple iPhones and its NOT THE ACCOUNT as it happened with multiple accounts.

IT IS a Microsoft EAS issue as it does not happen with Google, Yahoo! or iCloud accounts. ONLY Microsoft.

I also realize that it is a MS/Apple iOS issue but it needs to be resolved ASAP so any help would be appreciated!

## Answers

_No answers on this thread._
