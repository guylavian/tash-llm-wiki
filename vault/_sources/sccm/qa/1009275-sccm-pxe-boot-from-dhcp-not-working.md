---
title: "SCCM PXE Boot from DHCP not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1009275/sccm-pxe-boot-from-dhcp-not-working
question_id: 1009275
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-deployment", "microsoft-security-intune-configuration-manager-other-l1"]
---
# SCCM PXE Boot from DHCP not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1009275/sccm-pxe-boot-from-dhcp-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I'm in progress of moving PXE boot from DHCP to IP Helper but at the moment I cant get this as I have to wait for approval.    

Issue I got is that we move our DHCP scope to new DHCP server and none of the PXE setting was transfer. the dhcp server is decommission so i dont know what was setup on the old dhcp server    

I have configure our dhcp server with following settings    

43 = 010400000000FF    

66 = IP address of the PXE Server    

67 = SMSBoot\x64\Wdsmgfw.efi    

On most machine its working but some machine    

-  downloads the PXE image and then hangs on an black screen (nothing happens)    

-  Boots into pxe and then restart the system again    

-  Boots into pxe apply OS and then gives error    

Is they any other option I need to configure to make the PXE work    

We are using SCCM 2103 on Server 2012 R2

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-16*

Hi @lalajee  ,    

1, To narrow down the problem, we need more information.    

- 	Are these problematic machines on the same subnet? Are they the same model?    

- 	Check the smspxe.log to see if there is any useful information.    

- 	For more troubleshooting details, please refer to this link.    

Troubleshooting SCCM Part VII .......... OSD .... Part I | Microsoft Learn    

2, Besides, we don't recommend use DHCP options. Although they may work in some circumstances, in others it can cause issues, perhaps like those you're mentioning. The better approach is to set ip helpers on the switch to point to the IP. WDS will then auto-determine if the endpoint supports UEFI or BIOS and dynamically hand out the correct boot initiator and WIM.    

The following links for your reference:    

You want to PXE Boot? Don't use DHCP Options. - Microsoft Tech Community    

IP Helper-Address Configuration for PXE Boot | Config Mgr manishbangia.com    

Note: Microsoft provides third-party contact information to help you understand the problem. This contact information may change without notice. Microsoft does not guarantee the accuracy of this third-party contact information.
