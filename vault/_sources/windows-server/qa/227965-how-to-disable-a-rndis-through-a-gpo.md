---
title: "How to disable a RNDIS through a GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/227965/how-to-disable-a-rndis-through-a-gpo
question_id: 227965
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to disable a RNDIS through a GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/227965/how-to-disable-a-rndis-through-a-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,    

Using a GPO (Win server 2016), I want to disable all RNDIS connexion (e.g : mobile phone data connexion attempts) on Win10 workstations.    

First option, I look over the GUID corresponding to RDIS, but it looks like the NDIS is a part of the "classes-available-to-vendors" (and not reserved for system use) :    

https://learn.microsoft.com/en-us/windows-hardware/drivers/install/system-defined-device-setup-classes-reserved-for-system-use    

https://learn.microsoft.com/en-us/windows-hardware/drivers/install/system-defined-device-setup-classes-available-to-vendors    

I test which GUID I can find on my computer through a shared connexion with my mobile phone, I find the ClassGuid = {4d36e972-e325-11ce-bfc1-08002be10318}.    

Is there any consequences to disable the RNDIS function ?    

Second point, maybe it's safer to disable this through deactivation of USB tethering ?    

Thanks for sharing your ideas !

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-13*

Hi ,    

Thanks for your posting here. Due to our security policy, we have no such mobile device to test in our lab. Did you want to turn off "Enable advanced network functionality" on 'USB to PC' via Windows Registry? If yes, you might refer to the following article:    

Turn on/off "Enable advanced network functionality" via Windows Registry    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If not, let us appreciat that the other members in our forum can share their experience with us about this scenario.    

Best Regards,    

Candy    

--------------------------------------------------------------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-12*

I also found in the registry : SYSTEM/CurrentcontrolSet/Services/NDIS/...    

IfTypes/24    

IfTypes/71    

Parameters/    

State/(undefined value)    

(...)    

    

Do you see how to manage that (?) for instance : deactivate the RNDIS capability through USB shared connexion (e.g : mobile phone) ?    

Thanks
