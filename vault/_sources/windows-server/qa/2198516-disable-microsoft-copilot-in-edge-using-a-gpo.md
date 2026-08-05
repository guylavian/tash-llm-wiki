---
title: "Disable Microsoft Copilot in Edge using a GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2198516/disable-microsoft-copilot-in-edge-using-a-gpo
question_id: 2198516
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# Disable Microsoft Copilot in Edge using a GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2198516/disable-microsoft-copilot-in-edge-using-a-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Everyone,

I understand that it's not possible to do this as such, but you can disable the sidebar.  I've read that the policy is called Show Hubs sidebar and must be deactivated to hide the Copilot bar. It can be found in computer configuration under Policies => Administrative Templates => Microsoft Edge.

However, I've just imported the Windows 11 Administrative Templates  23H2 and there is no folder called Microsoft Edge directly underneath Administrative Templates.

Can anyone help?

Regards,

Geoff Major
https://4sysops.com/wp-content/uploads/2024/01/Disable-the-sidebar,-and-thus-Copilot-via-Group-Policy.png

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-16*

Hello Geoff Major,  

Good day!  

Thank you for your update and sharing. I am so glad to hear the problem has been resolved.   

Have a nice day!  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-16*

Hello Geoff Major,  

Good day!  

Hope the problem will be resolved soon.  

Have a nice day!

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-15*

Hello Daisy,

The ADMX and ADML files for Microsoft Edge are in the PolicyDefinitions folder, and a Microsoft Edge folder shows under Computer Configuration, Administrative Templates, Windows Components, but this does not include the Show Hubs sidebar policy.  I'll repost my question as suggested.

Kind Regards,

Geoff

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-15*

Hello Geoff Major,  

Thank you for posting in Microsoft Community forum.  

From the description above, there should be ADMX and ADML related to Microsoft Edge. After add it, then you will see Microsoft Edge in group policy.  

Since there are no engineers dedicated to Microsoft Edge in this forum. in order to be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.

Here is the link for Q&A forum.  

Questions - Microsoft Q&A  

Click the "Ask a Question" button in the upper right corner to post your question and type "Microsoft Edge" tag and select any tags related to your productions.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
