---
title: "Force authentication and GPO to get from DC in Azure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/162260/force-authentication-and-gpo-to-get-from-dc-in-azu
question_id: 162260
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
---
# Force authentication and GPO to get from DC in Azure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/162260/force-authentication-and-gpo-to-get-from-dc-in-azu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,  

I'm migrating on-prem DCs to the DC in Azure and trying to make sure that all will be ready for shutting down the on-prem DCs. I've spin up a VM in Azure, joined the domain and promoted to DC. I've moved all FSMO roles to the DC in Azure. The Azure DC is also showing in AD Sites and Services - Sites - Servers, the IP is not however visible under "Subnets". However, when I'm checking which DC the end users authenticate to, they still use the on-prem DCs. How could I force them to authenticate to the DC in Azure?  

See the info below:  

Info:  

on-prem servers: DC01 & DC02  

Azure server: AZDC01  

There is a S2S VPN between the site and Azure which works ok - users on site use the DNS service in AZDC01 already  

How do I check:  

-  set logonserver -> shows on-prem DC02  

-  gpupdate -r      -> all getting from on-prem DC01  

-  netdom query fsmo /domain:domainname -> all is showing the DC in Azure (AZDC01)  

NOTE: I've checked the above 24 hours after moved all roles to AZDC01 so that there was time to get fully synced...  

....probably there is some step that I missed? I'm not very skilled in this so any advice would be appreciated.   

Also, ... do I have to manually update the Azure network IP to the Sites&Services - Subnets?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-19*

Hi,  

Thank you for the update.  

Seeing your description, this is more like an AAD question, I recommend you to post on the AAD forum, they can give you more professional and quick answers  

Hope this information can help you, thank you for your understanding and support  

Best wishes  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-16*

the tip above didn't help as the AZDC01 already had Group Policy Management installed and enabled.  

I was doing a bit more research and looks like machines are authenticationg to a DC by selecting a DC that answer their request first... Found some info about changing Priority and Weight but do not know yet how - will carry on with my research.  

About GPO, I haven't yet found anything useful....  

Worst case scenario, I will plan a maintenance window with the client to shut down the on-prem DCs and test whether machines connects/authenticates/get GPO from AZDC01 in Azure. If I can't find a way how to test it without doing it...  

Btw, I've added Azure DC subnet to Sites & Services and linked to the default site...

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-16*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-11-13*

Sign in to your management VM. For steps on how to connect using the Azure portal, see Connect to a Windows Server VM.    

Server Manager should open by default when you sign in to the VM. If not, on the Start menu, select Server Manager.    

In the Dashboard pane of the Server Manager window, select Add Roles and Features.    

On the Before You Begin page of the Add Roles and Features Wizard, select Next.    

For the Installation Type, leave the Role-based or feature-based installation option checked and select Next.    

On the Server Selection page, choose the current VM from the server pool, such as myvm.aaddscontoso.com, then select Next.    

On the Server Roles page, click Next.    

On the Features page, select the Group Policy Management feature.    

please also find step by step guide click on mentioned below link    

https://learn.microsoft.com/en-us/azure/active-directory-domain-services/manage-group-policy    

If issue resolve please accept answer and up vote thanks
