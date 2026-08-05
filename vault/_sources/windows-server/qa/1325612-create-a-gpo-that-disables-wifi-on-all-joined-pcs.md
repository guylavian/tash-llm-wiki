---
title: "Create a GPO that disables WiFi on all joined PC's in a domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1325612/create-a-gpo-that-disables-wifi-on-all-joined-pcs
question_id: 1325612
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Create a GPO that disables WiFi on all joined PC's in a domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1325612/create-a-gpo-that-disables-wifi-on-all-joined-pcs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

I have been testing out how to block WiFi on all Laptops that joins a domain. But I am not successful yet. This is how I am trying to achieve this:

-  Open up the Group Policy Management (From Domain Controller side)  

-  Under there create a new GPO, we can call it BlockWiFi. Then Right click on it and click on 'Edit'  

-  Add the New Service as following  

-  The meaning of this rule is to shutdown the driver or service, that handles the WiFi in overall. Here we specify that if such service do exists then simply stop the service all together. But if you look more closely on the screenshot from part 2 you see that the rule seems to have an affect on the Domain Controller itself? 

So the question here is how I can apply this rule for all the joined PC on this test Domain Controller?

Thanks in forehand!

Best Regards

Bahador Vafadar

## Answer (community) — community member

*upvotes: 0 · updated: 2023-07-11*

I have managed to solve this issue on my own. Thank you all for your time and effort. :) Much obliged!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-07-07*

Hello

Thank you for posting in our Q&A forum.

To create a Group Policy Object (GPO) in a domain controller to disable WiFi on all domain-joined laptops, you can follow these steps:

-  Open the Group Policy Management Console.

-  Create a new Group Policy Object or select an existing Group Policy Object to edit.

-  Right-click the selected GPO and select Edit to open the Group Policy Management Editor.

-  Navigate to the following location in the editor: Computer Configuration > Policies > Windows Settings > Security Settings > Wireless Networking (IEEE 802.11) Policy.

-  Right-click on Wireless Network (IEEE 802.11) Policies and select Create New Windows Vista and Later Policy.

-  Provide a policy name (such as "Disable WiFi") and click OK.

-  In the policy settings, select the Network Permissions tab.

-  Select the "Block connections to ad-hoc networks" checkbox to disable connections to ad-hoc WiFi networks.

-  Select the "Block connections to infrastructure networks" checkbox to disable connections to infrastructure WiFi networks.

-  Click OK to save the policy settings.
