---
title: "Exchange Server 2016 Delete Expired SSL Certificate Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2186508/exchange-server-2016-delete-expired-ssl-certificat
question_id: 2186508
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Exchange Server 2016 Delete Expired SSL Certificate Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2186508/exchange-server-2016-delete-expired-ssl-certificat (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

I have renewed ssl certificate for on prem Exchange 2016 Server and want to delete old ssl certificate. But encounter this error as shown in the screenshot.

Is this the correct way to fix it?

---Get Info---

Get-SendConnector | fl Name, Fqdn, TlsCertificateName

Get-ExchangeCertificate | fl Thumbprint, Subject, Services

Get-ExchangeCertificate | Format-List Thumbprint, Subject, Services, NotAfter

---Update SendConnector---

Set-SendConnector -Identity "Outbound to Office 365" -TlsCertificateName " "

---Verify---

Get-SendConnector | fl Name, Fqdn, TlsCertificateName

Test-Mailflow -TargetEmailAddress 

---Restart Service---

Restart-Service MSExchangeTransport

Then go to Exchange Admin Center > servers > certificates and delete the old certificates. Is this the correct way to do it?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-22*

Hello Tom_Kh00,  

Thank you for posting in Microsoft Community forum.  

From the description above, I understand your question is related to Exchange server certificate.   

Since there are no engineers dedicated to Exchange server certificate in this forum. in order to be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.

Here is the link for Q&A forum.  

Questions - Microsoft Q&A  

Click the "Ask a Question" button in the upper right corner to post your question and type "Exchange" tag and select any tags related to your productions.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
