---
title: "Cannot validate Exchange Hybrid config due to expired cert."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195248/cannot-validate-exchange-hybrid-config-due-to-expi
question_id: 2195248
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Cannot validate Exchange Hybrid config due to expired cert.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195248/cannot-validate-exchange-hybrid-config-due-to-expi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am setting up an Exchange on-prem, 2 server DAG, to O365 hybrid migration.  I have run the HCW utility but when it comes to validate connector flow from O365 to my server, I get the error:

“450 4.4.317 Cannot connect to remote server [Message=CertificateExpired Expected Subject: email.domain.com. Presented Subject: CN=email.domain.com. Thumbprint: 94E711DD84BC285CD2911DAC3D0C9E3ABB29671E.] [LastAttemptedServerName=email.domain.com] [LastAttemptedIP=x.147.128.25:25] [SmtpSecurity=-1;-1] [DM6NAM11FT035.eop-nam11.prod.protection.outlook.com 2025-01-04T16:37:07.429Z 08DD2CB85E2FE9DB]”

When I run Get-ExchangeCertificate, none of my certs have the mentioned thumbprint.  If I run Remove-ExchangeCertificate -Thumprint 94E711DD84BC285CD2911DAC3D0C9E3ABB29671E.  I get an error that the cert was not found.  I have not kept a record of past certs that have been setup on this server so don't know if this is an old cert or what.  When I was going through the HCW and asked to select a cert, it only showed one public cert, the current/correct one.  Where else can I look for this orphaned cert?  When I run OWA from offsite, the page loads with the current/correct cert.

Error I get when looking on the server for the cert:

[PS] C:\Users\Administrator.domain\Desktop>Get-ExchangeCertificate -Thumbprint 94E711DD84BC285CD2911DAC3D0C9E3ABB29671E | Format-List *A special Rpc error occurs on server EXCH-1: The certificate with thumbprint 94E711DD84BC285CD2911DAC3D0C9E3ABB29671Ewas not found.   + CategoryInfo          : NotSpecified: (:) [Get-ExchangeCertificate], InvalidOperationException   + FullyQualifiedErrorId : [Server=EXCH-1,RequestId=5fd8f139-abf1-444e-8683-e0adcc9ec83c,TimeStamp=1/4/2025 5:10:19   PM] [FailureCategory=Cmdlet-InvalidOperationException] 71D7F7B0,Microsoft.Exchange.Management.SystemConfiguration Tasks.GetExchangeCertificate   + PSComputerName        : exch-1.domain.com

Between my 2 on-prem servers, I found 2 receive connectors, one on each server, and 1 send connector, the one created by the HCW, that had TLS cert associations.  I found a doc (don't know if I can link it or not) that shared how to update the associated TLS cert on a connector by entering these commands against each of the 3 connectors:

Get-ExchangeCertificate

$cert = Get-ExchangeCertificate -Thumbprint DE67EC3C8D679DC35D171341FEC5148D012B1BAE2

$tlscertificatename = "<i>$($cert.Issuer)<s>$($cert.Subject)"

Set-ReceiveConnector "EXSERVERClient Frontend EXSERVER" -TlsCertificateName $tlscertificatename

Set-SendConnector "Outbound to Office 365" -TlsCertificateName $tlscertificatename

Everything ran and I got no errors other than the warning that nothing was changed because the issuer was the same, the doc mentioned this.  

Unfortunately this did not solve the issue.  I rebooted the server.  Nothing.  I reran the HCW.  Nothing.  I deleted the send connector.  Reran the HCW.  Nothing. I edited the connector to not use TLS for the verification.  That allowed me to then verify the connector between my org and MS.  I still cannot send email to the M365 hosted mailbox.  I reenabled the TLS and cannot verify again, no surprise.

Also, I checked the SMTP receive log and there are zero instances of the expired cert thumbprint recorded.  The send log does have a whole bunch of “Failed to connect. Winsock error code: 10060, Win32 error code: 10060, Destination domain” errors.  Looks like those are likely due to Comcast, my ISP, blocking port 25.  I will call them and see if they can't unblock 25.

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-08*

So I found the orphaned cert, it was in my firewall.  I looked at the one place in the firewall that I knew about, but as it turns out there was a second cert location.  Anyway, that issue is resolved but another immidiately popped up.  Now when I click on the Validate button I get:

450 4.4.317 Cannot connect to remote server [Message=451 4.4.0 TLS negotiation failed with error ConnectionAborted] [LastAttemptedServerName=email.domain.com] [LastAttemptedIP=x.147.128.25:25] [SmtpSecurity=-2;-2] [CO1NAM11FT009.eop-nam11.prod.protection.outlook.com 2025-01-08T20:32:00.975Z 08DD2F9B58D61006]

I have confirmed via inbound and outbound email, that TLS 1.2 is enabled and being used.  Now if I try to Validate with no TLS setting, the validation still fails but now it fails because the firewall and my Exchange server require TLS.  I also reran the HCW, still in Full Hybrid mode, but that did not solve it.  I also ran the Set-Receive and Set-Send commands again, as per your suggestion.

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-08*

Hello

Thanks for posting in Microsoft Community.

The issue you're encountering with the Exchange hybrid configuration is primarily related to the expired certificate, and it seems like there are a few layers to this problem.

Issue Breakdown:

Expired Certificate: The error message indicates that the certificate has expired (CertificateExpired), but when you run Get-ExchangeCertificate, the thumbprint provided doesn't

match any certificates in your current configuration.

Certificate not found: When you attempt to remove the expired certificate using Remove-ExchangeCertificate -Thumbprint <thumbprint>, it doesn't find the certificate.

Failed TLS Verification: You're unable to verify the TLS connection between your Exchange environment and Office 365 via the Hybrid Configuration Wizard (HCW), possibly due to the expired certificate being referenced somewhere.

Steps to Troubleshoot and Resolve:

-  Verify Existing Certificates in Exchange

You have already run Get-ExchangeCertificate without seeing the expired certificate. However, there are a couple of places to check:

IIS and SMTP Services: Certificates might be bound to these services even if they don't appear in the standard Get-ExchangeCertificate query.

Other certificate stores: Ensure you're checking both the Local Machine and Personal stores in MMC (Microsoft Management Console).

To check for certificates in the MMC:

Press Win + R, type mmc, and hit Enter.

In MMC, go to File > Add/Remove Snap-in, then select Certificates.

Add Certificates for the Computer account and choose Local Computer.

Browse to Personal > Certificates and Trusted Root Certification Authorities > Certificates to check if the certificate appears in either of these locations.

-  Check for Old Certificate Bindings

Exchange can still be referencing old certificates that have expired, especially if they were bound to IIS or SMTP services. You can verify these bindings using the following command:

netsh http show sslcert

This will list all certificates bound to the server’s HTTP(S) ports. If the expired certificate is bound here, you may need to manually unbind it and rebind the new certificate.

-  Re-run the Hybrid Configuration Wizard (HCW)

Once you’ve confirmed that the correct, valid certificate is present in all the necessary places, run the HCW again:

Run HCW in hybrid mode and let it attempt to validate the connectors again.

During the validation process, ensure that the TLS certificate that is being used is the correct one.

If the expired cert is still being referenced anywhere, you can try manually updating the certificate associations on the connectors using the following PowerShell commands:

Get-ExchangeCertificate

$cert = Get-ExchangeCertificate -Thumbprint <valid-cert-thumbprint>

$tlscertificatename = "<i>$($cert.Issuer)<s>$($cert.Subject)"

Set-ReceiveConnector "EXSERVERClient Frontend EXSERVER" -TlsCertificateName $tlscertificatename

Set-SendConnector "Outbound to Office 365" -TlsCertificateName $tlscertificatename

-  Disable TLS Verification Temporarily

To allow the HCW to progress while you investigate, you can temporarily disable TLS verification between your Exchange server and Office 365:

In the Hybrid Configuration Wizard, when prompted for TLS validation, choose to disable TLS for the verification process. This will let you proceed even if the certificate is not valid.

After this, make sure to go back and enable TLS for the send/receive connectors.

-  SMTP Logs and Port 25

You mentioned getting Winsock error code: 10060 in your SMTP send logs, which usually indicates a network connectivity issue—in this case, likely due to your ISP blocking port 25. You should:

Contact your ISP (Comcast) and ask them to unblock port 25 if it is indeed being blocked.

In the meantime, you can attempt using port 587 for sending mail instead of port 25.

-  Check Firewall and Proxy Settings

If you're running behind a firewall or proxy, ensure that it's not blocking the connection to Office 365. Also, make sure the required ports (usually 25, 587, and 443) are open for communication.

-  Confirm Email Flow

After fixing the certificate and port issues:

Test email flow from your Exchange server to an Office 365 mailbox.

Use tools like Telnet or Microsoft Remote Connectivity Analyzer to check if the TLS handshake is successful and if the connector is now functional.

-  Review Event Logs

If things are still not working, check the Event Viewer (especially under Applications and Services Logs > Microsoft > Exchange > Hybrid or Application logs) for any further clues or errors related to the hybrid configuration or certificate validation.

I hope the above information is helpful to you.

Best regards

Runjie Zhai
