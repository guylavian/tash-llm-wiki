---
title: "GPO - wpad config - admin template missing section"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2285465/gpo-wpad-config-admin-template-missing-section
question_id: 2285465
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# GPO - wpad config - admin template missing section

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2285465/gpo-wpad-config-admin-template-missing-section (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello I am looking to disable the following settings however the Connection Page Folder in gpo does not exist. I've tried looking at older and newer admin template files in this case its inetres.admx and inetres.adml. So far none contain the config for the settings to appear.

Settings in question:

-  User Configuration > Administrative Templates > Windows Components > Internet Explorer > Internet Control Panel > Connection Page

-  Disable changing automatic configuration settings = Enabled

-  Automatically detect settings via Internet Options = Unchecked

ive tried different admin templates from these versions 

https://www.microsoft.com/en-us/download/details.aspx?id=104003

Windows Server 2022 August 2021 Update

Windows 10 May 2021 Update (21H1)

Windows 10 October 2022 Update (22H2)

Windows 11 Sep 2024 Update (24H2)

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-06-19*

Hello,

 Thank you for posting question on Microsoft Windows forum!

 Based on your description, the Connection Page folder and its settings are missing from Group Policy because these settings were probably removed from Microsoft's ADMX templates starting with Windows 10 2004 (20H1) and newer OS versions due to the deprecation of Internet Explorer. The followings are the plausible explanations of **Why the "Connection Page" Folder Might Be Missing.

-  Deprecation of Internet Explorer Maintenance (IEM): Many Internet Explorer-related GPO settings, particularly those found under "Internet Explorer Maintenance," have been deprecated since Windows Server 2008 R2 and Windows 7. Microsoft transitioned to using Group Policy Preferences (GPP) for managing browser settings, and then further moved towards settings in the modern "Settings" app for Edge and newer Windows versions. While inetres.admx and inetres.adml still contain many IE settings, some older, less relevant ones might have been removed or restructured.

-  Shifting Focus to Microsoft Edge: With the increasing push towards Microsoft Edge as the default browser, many GPO settings that specifically targeted Internet Explorer's older functionalities have either been removed, changed, or are now managed through different paths that influence Edge (and by extension, the underlying network settings Windows uses).   You can try the below steps for the possible workaround by using Registry Keys directly via Group Policy Preferences (GPP)

-  Disable changing automatic configuration settings

-  Registry Path: `HKEY_CURRENT_USER\Software\Policies\Microsoft\Internet Explorer\Control Panel`

-  Value Name: `Autoconfig`

-  Type: `REG_DWORD`

-  Value: `1` (Enabled)

-  Disable "Automatically detect settings"

-  Registry Path: `HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\CurrentVersion\Internet Settings`

-  Value Name: `AutoDetect`

-  Type: `REG_DWORD`

-  Value: `0` (Unchecked/Disabled)

-  Step-by-Step for Deployment

-  Open Group Policy Management Console (gpmc.msc).

-  Navigate to your target GPO (User Configuration).

-  Create Registry Items (via Preferences):

-  Go to: User Configuration → Preferences → Windows Settings → Registry.

-  Right-click → New → Registry Item.

-  Configure both keys as specified above.

-  Apply the GPO to the relevant Organizational Unit (OU).

  Please note: Perform the above steps in testing environment first before deploying it in production one.

Hope the above information is helpful!
