---
title: "Deploy Windows Hello face through GPO in windows server 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/252461/deploy-windows-hello-face-through-gpo-in-windows-s
question_id: 252461
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Deploy Windows Hello face through GPO in windows server 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/252461/deploy-windows-hello-face-through-gpo-in-windows-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,  

I need a help to deploy windows Hello face authentication through Group Policy Object (GPO) in windows server 2016 step by step.  

Thank you in advance,

## Answer (community) — community member

*upvotes: 1 · updated: 2021-02-01*

Create the Windows Hello for Business Group Policy object  

The Group Policy object contains the policy settings needed to trigger Windows Hello for Business provisioning and to ensure Windows Hello for Business authentication certificates are automatically renewed.  

Start the Group Policy Management Console (gpmc.msc)  

Expand the domain and select the Group Policy Object node in the navigation pane.  

Right-click Group Policy object and select New.  

Type Enable Windows Hello for Business in the name box and click OK.  

In the content pane, right-click the Enable Windows Hello for Business Group Policy object and click Edit.  

In the navigation pane, expand Policies under User Configuration.  

Expand Administrative Templates > Windows Component, and select Windows Hello for Business.  

In the content pane, double-click Use Windows Hello for Business. Click Enable and click OK.  

Double-click Use certificate for on-premises authentication. Click Enable and click OK. Close the Group Policy Management Editor.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-01-31*

Something here may help.    

https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/hello-deployment-cert-trust    

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-08*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-03*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky
