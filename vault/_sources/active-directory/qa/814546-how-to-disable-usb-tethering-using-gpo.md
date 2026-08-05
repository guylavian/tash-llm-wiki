---
title: "How to disable USB tethering using GPO ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/814546/how-to-disable-usb-tethering-using-gpo
question_id: 814546
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-devices-deployment-config-app-groups", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
---
# How to disable USB tethering using GPO ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/814546/how-to-disable-usb-tethering-using-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

For Windows based PCs connected with Windows AD with Group policy, we want to block USB phone tethering. And we have tried following things which seems to be working for some people but not us.    

We have applied computer policy to block device installation    

System/Device Installation/Device Installation Restrictions > Prevent installation of devices that match any of these device IDs    

Device ID "USB\class_e0"    

This was described here: https://social.technet.microsoft.com/Forums/en-US/68c09a6a-07ec-47da-b4e1-d5dd325cc57f/prevent-mtp-amp-usb-tethering?forum=w7itprosecurity    

I have reviewed the process described here.. https://learn.microsoft.com/en-us/windows/client-management/manage-device-installation-with-group-policy    

I am just not sure whether device ID "USB\class_e0" is the correct one or not? Although it appears in device compatible Ids, so I assume it should work.    

Also, I check hardware IDs of few phones and all of them have distinct IDs like    

device 1 USB\VID_22D9&PID_276A&REV_0404&MI_00 USB\VID_22D9&PID_276A&MI_00    

device 2 USB\VID_2717&PID_FF80&REV_0404&MI_00 USB\VID_2717&PID_FF80&MI_00    

device 3 USB\VID_04E8&PID_6863&REV_0400&MI_00 USB\VID_04E8&PID_6863&MI_00    

Now, when I add the complete device ID, the policy works as expected, i.e. the device is not installed and thus usb tethering now blocked for that particular device. Pls check my current policy screenshot    

    

Can I do block all devices together using something like "USB\VID"?    

Or there is something else I am missing here? Pls guide.    

Note that I have already tried running  “gpupdate /force” in command prompt to ensure it has been applied.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-18*

Hi,  

I checked again, I see that USB\class_e0 lists under connected device in Compatible IDs section.  This is good. I already checked this....  

Now, the problem is different that, the Compatible device ID of USB\class_e0 is still not working to block device installation even if I follow the same steps to block it using GP Policy.   

What could be wrong?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-16*

Hello.    

Actually , you can find Device ID in device manager and add these IDs in to GPO. like this picture :    

    

Like these Device IDs :    

USB\Class_e0&SubClass_01    

USB\Class_ef    

USB\Class_06    

USB\Class_e0    

Each device has its own device ID , you should extract from your network or use this below link that is defined by Microsoft   :    

system-defined-device-setup-classes-available-to-vendors
