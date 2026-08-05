---
title: "ADFS - the connection was reset error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2200128/adfs-the-connection-was-reset-error
question_id: 2200128
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# ADFS - the connection was reset error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2200128/adfs-the-connection-was-reset-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi 

Within the existing ADFS farm, we installed another server, secundary. The installation went well, but unfortunately when verifying via this node, the ticket issuance ends with an error. When you enter the URL address

 /adfs/ls/idpinitiatedsignon.aspx a dialog will appear with the selection of a claim provider. 

When choosing : 

"You are not signed in. 

 Sign in to this site." 

page appears, 

"

page compared to the login that is secured , this is not secured.... I ran Set-AdfsAlternateTlsClientBinding -Thumbprint on the primary server, unfortunately it didn't help. 

ADFS Server is operated on Windows 2019, the installation of the secondary server is Windows 2022. The database is internal. 

adfs certificte is from digicert autority.mayby problem with checking crl ? 

Thank you for your ideas

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-06*

thank you,

production adfs server is in intenal site. connectivity to internet is throught proxy server... I try define proxy server in the netsh.... it is correct for adfs server ? or is another configuration place ?

thanx

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-06*

Hello 

Thanks for posting in Microsoft Community. 

According to the problem you described, it is mainly that a replica node in the ADFS environment failed to issue tickets correctly and encountered authentication problems when accessed through /adfs/ls/idpinitiatedsignon.aspx. Here are some possible causes and solutions, I hope to help you locate and solve the problem. 

CRL (Certificate Revocation List) Check Problem 

As you mentioned, the certificate revocation list (CRL) may be a potential cause. ADFS checks the CRL when verifying the certificate. If it cannot access the CRL distribution point (for example, due to network problems or misconfiguration), it may not be able to verify the validity of the certificate, resulting in authentication failure. 

Solve CRL problems: 

Check network access to CRL distribution point: 

Confirm that the ADFS server (including the master server and the replica server) can access the Internet (or CRL distribution point, if it is a private network). 

You can confirm whether the CRL distribution point is accessible by manually accessing the CRL URL (found in the properties of the certificate), or use curl or wget to test whether there is a network or DNS problem. 

Verify CRL availability: 

Open the properties of the certificate (via the MMC management console) and view the CRL distribution point under the Details tab to confirm that its URL is valid and accessible. 

If the network or firewall blocks access to the CRL, you may need to adjust the firewall configuration or disable CRL checking (but this is not recommended in a production environment). 

Manually check the CRL: 

You can manually download the CRL through a browser or use a PowerShell script to confirm that the CRL is valid and available. 

Clear the CRL cache: 

ADFS usually caches CRLs to ensure that they are not expired. If necessary, you can clear the cache by restarting the ADFS service or using PowerShell: Clear-AdfsCertificate 

Certificate trust issues 

Another possible cause is a certificate trust issue, specifically the certificate trust between the master and replica servers. If the replica node's certificate is not installed correctly or is not trusted on the master node, it will cause authentication failures. 

Certificate synchronization: 

Ensure that the ADFS certificate (issued by DigiCert) has been correctly installed on both the master and replica servers. 

You can check if the certificate is listed under the Certificates tab via the ADFS Management Console. 

SSL/TLS Binding: 

You mentioned that you have configured it on the master server using Set-AdfsAlternateTlsClientBinding -Thumbprint, but it seems to have no effect. Make sure that both the master and replica servers have the SSL/TLS certificate properly bound. To do this: 

Run the following PowerShell command on both the master and replica servers: Get-AdfsSslCertificate 

Check if both servers are using the same valid SSL certificate. 

If there is a discrepancy, update the binding to ensure that both servers are using the same trusted SSL certificate. 

I hope the above information is helpful to you. 

Best regards 

Runjie Zhai
