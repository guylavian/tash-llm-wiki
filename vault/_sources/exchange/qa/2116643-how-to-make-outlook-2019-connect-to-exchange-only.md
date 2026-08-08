---
title: "How to make outlook 2019 connect to exchange only on the internal LAN"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2116643/how-to-make-outlook-2019-connect-to-exchange-only
question_id: 2116643
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to make outlook 2019 connect to exchange only on the internal LAN

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2116643/how-to-make-outlook-2019-connect-to-exchange-only (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Windows 11 Pro - Outlook 2019

Exchange 2013 role on server2102R2 Hyper-V system

Comcast Business ISP

The comcast modem is not funtioning properly. I can externally access exchanged via outlook 2019 from laptops. The PCs I have in the office on the LAN fail to connect when going out comcast https://mail.mycompany.com 

For a workaround until I can get Comcast to address their modem issue, how can I configure outlook 2019 on the Windows 11 system to use the LAN only and not go out and back in with comcast.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-11*

Hello,

 

Thank you for posting in Q&A forum.

You can follow below steps to finish the configuration:

1.Create a SCP record in internal DNS to point to Exchange server internal IP address.

2.Ensure the internal DNS name matches the external autodiscover name but points to the internal IP address of your Exchange server

3.Go to Outlook 2019 > File > Account Settings > Exchange account and click Change. In excahnge proxy settings uncheck "Use this server only for outgoing mail".

4.Enter the internal IP address of exchange server in the proxy server field and finish the configuration.

 

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

 

Best regards，

Jill Zhou

 

If the Answer is helpful, please click "Accept Answer" and upvote it.
