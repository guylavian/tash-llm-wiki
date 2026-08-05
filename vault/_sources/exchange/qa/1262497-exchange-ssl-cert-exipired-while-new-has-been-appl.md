---
title: "Exchange SSL Cert exipired while new has been applied"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1262497/exchange-ssl-cert-exipired-while-new-has-been-appl
question_id: 1262497
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Exchange SSL Cert exipired while new has been applied

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1262497/exchange-ssl-cert-exipired-while-new-has-been-appl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dual on prem server 2016 set up, applied new SSL certificate to both servers showing valid dates.  Still receiving a notice when launching Outlook and Exchange admin site that one of the certificates has expired.  

The cert was applied to primary server then copied over to the secondary and applied.  After restarting IIS and the full server we still received the cert expired notice, so we then worked to get the cert reissued then worked to install this on the server again.  Still we are receiving the notice that the cert has expired.

How can we get the server to recognize that the cert has been applied and is currently valid.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-05-01*

Hello @FMG Support ,

If you have already installed the new SSL certificate on both servers and restarted IIS and the server, but are still receiving a notice that the certificate has expired, there are a few additional steps you can take to troubleshoot the issue:

Verify the certificate details: Check the details of the new SSL certificate to ensure that it has been issued correctly and is valid. You can use a tool like the SSL Checker to verify the certificate details.

Check the certificate binding: Verify that the new SSL certificate is correctly bound to the appropriate website in IIS. You can check this by opening IIS Manager, selecting the website, and checking the bindings in the "Bindings" feature.

Check the certificate chain: Verify that the certificate chain is complete and includes all necessary intermediate certificates. You can use a tool like the SSL Checker to verify the certificate chain.

Clear the certificate cache: Clear the certificate cache on both servers to ensure that the new SSL certificate is properly recognized. You can do this by running the following command in an elevated command prompt: `certutil -urlcache * delete`.

Restart the servers: If none of the above steps resolve the issue, try restarting both servers to ensure that all changes are applied and the new SSL certificate is recognized.

Kindly mark this answer as Accepted in case it helped or post your feedback !

Regards
