---
title: "ADFS SSO intranet/vpn only"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1250500/adfs-sso-intranet-vpn-only
question_id: 1250500
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
---
# ADFS SSO intranet/vpn only

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1250500/adfs-sso-intranet-vpn-only (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

trying to configure ADFS Access Control Policy rule to Permit users from Specific IP addresses only. When enabled it ends up just refreshing the SSO login box window regardless of IP. Basically trying to restrict it to the internal network and vpn only.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-21*

Hi,
I'd be happy to help you out with your question. Sorry for the inconvenience caused.
To start, open the ADFS Management Console and navigate to the Access Control Policies section. Here, you can create a new rule by clicking on the "Add" button.
Give the rule a name and description that you will recognize. Then, under "Claim Types", select "IP Address" from the drop-down menu. This will allow you to specify the specific IP addresses that you want to allow access to ADFS.
Under "Conditions", select "IP Address" from the drop-down menu and set the value to the specific IP addresses that you want to allow. This will ensure that only users accessing ADFS from those specific IP addresses will be permitted.
Next, under "Access Control", select "Permit Access" and click on "Save". This will save the rule and apply it to your ADFS instance.
If you find that the rule is not working as expected and just refreshing the SSO login box window regardless of IP, double-check that the IP addresses you have entered are correct and that the rule is being applied correctly. You may also want to check your firewall settings to ensure that traffic from external IP addresses is not being blocked, which could prevent the rule from working correctly.
For more Information, please refer to Access Control Policies in Windows Server 2016 AD FS - https://learn.microsoft.com/windows-server/identity/ad-fs/operations/access-control-policies-in-ad-fs
If you have any other questions or need assistance with anything, please don't hesitate to let me know. I'm here to help.

If the reply was helpful, please don’t forget to upvote or accept as answer, thank you.
