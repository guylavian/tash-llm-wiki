---
title: "Changing a device in an group in Active Directory. Unable to connect to the school's Wifi."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1186048/changing-a-device-in-an-group-in-active-directory
question_id: 1186048
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
---
# Changing a device in an group in Active Directory. Unable to connect to the school's Wifi.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1186048/changing-a-device-in-an-group-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I purchased from the supplier 10 Dell 1320 Latitude laptops. Once I joined them into the domain of the school, they showed up in Active Directory. I moved all the 10 laptops into the correct OU group. 

On all the devices, I ran gpupdate /force, which pulls the group policy for those devices. It worked on all of them, but one. For the one it didn't work on, the Wi-Fi disconnected. I cannot now, for some reason, join the schools Wi-Fi. When I try to manually connect it, the error reads "Unable to Connect to the device".

I have installed the latest drivers from Dell, and updates from Microsoft. I have checked in the DHCP if something else is using the same IP (which it isn't). I have reimaged the device as well. It connects to the Wi-Fi if it stays in its default location, but once I move it in AD, it is unable to connect. If I try to return it to the default location, it still wont allow connection. 

I need to delete it from AD, then have it join the domain and start again. 

What else would be the error? Could it be that maybe the device is in AD twice?

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2023-03-02*

Hi

Do you have any Wifi Policy or Certificate PKI policy in the GPO? Can you upload the logs from the device ? Suggest you to rename the device to something differen, check the DNS settings, check your gateway settings on the specific device.
