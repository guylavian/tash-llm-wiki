---
title: "Replace ADFS Certificate Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/663698/replace-adfs-certificate-error
question_id: 663698
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Replace ADFS Certificate Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/663698/replace-adfs-certificate-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I had my ADFS certificate expire as I use Lets Encrypt but yet the command that I am aware of to update needs the service Active Directory Federation Services needs to be started for this to run. Yet it can't start when the certificate is expired it appears. I had to rebuild the environment last time to fix the issue and then let it happen again and don't want to have to rebuild.    

Now the instructions I followed before were here manage-ssl-certificates-ad-fs-wap    

Works perfectly fine as long as the service is started. WAP updates no issues regardless.    

Find thumprint via dir Cert:\LocalMachine\My\    

Then in screenshot is when I try to update the certificate with said thumprint    

    

Starting the service gives this error    

    

I am wondering what are the proper steps to update the certificate when it expires and experience these errors? I couldn't find proper steps easily and hoping someone will know.    

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-12-15*

I just went ahead and rebuilt it. Faster that way as I am an Azure Engineer and can just have it build itself almost with ARM Templates and Powershell/Powershell DSC scripts I make. It really shouldn't be that hard to say replace a ADFS certificate if it expires, its pretty stupid honestly.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-12-15*

The issue cannot be the same with `netsh` as the error you have with `Set-ADFSSSLCertificate` is a local network connection failing whereas NETSH is not using the network at all to set the info. But granted that the underlying issue is maybe the same.  

-  Let's make sure the certificate is trusted (from store and CRL perspective). From the ADFS server, run the following command: `certutil -urlfetch -verify <your cert.cer>`. And share the output?  

-  Let's make sure the ADFS service has access to the private key of the certificate. You can do that from the certificate MMC by right-clicking on the imported certificate and select  All Tasks > Manage Private key.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-12-15*

Still same issue...

netsh I actually already did try before and still same issue... at this point I honestly could rebuild it again quicker than troubleshoot this...

I am running powershell as admin always as well

winrm quickconfig  

WinRM service is already running on this machine.  

WinRM is already set up for remote management on this computer.

Trying gives the exact same error to set adfs certificate

$SSLCert = Get-ChildItem –Path "cert:\LocalMachine\My" | Where-Object {$.subject -like 'cn=*.hostnameofmyadfsdns' -and $.Issuer -Like "CN=R3*"}  

$thumbprint = $SSLCert.Thumbprint

check first to make sure appid is the same as what you add below

netsh http show sslcert

delete old cert thumprint and create new

netsh http delete sslcert hostnameport=localhost:443  

netsh http delete sslcert hostnameport=hostnameofmyadfsdns:443  

netsh http delete sslcert hostnameport=hostnameofmyadfsdns:49443

add new thumbprint for adfs cert

netsh http add sslcert hostnameport=localhost:443 certhash=$thumbprint appid='{5d89a20c-beab-4389-9447-324788eb944a}' certstore=my  

netsh http add sslcert hostnameport=hostnameofmyadfsdns:443 certhash=$thumbprint appid='{5d89a20c-beab-4389-9447-324788eb944a}' certstore=my  

netsh http add sslcert hostnameport=hostnameofmyadfsdns:49443 certhash=$thumbprint appid='{5d89a20c-beab-4389-9447-324788eb944a}' certstore=my

After this it still gives same error yet the certificate is set properly according to this... so its a bit confusing what exactly its complaining about and there is really no help out there unless I placed a Microsoft ticket but this is a testlab so I won't waste our Premier hours on that.

Thanks

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-12-15*

This command is leveraging remote WinRM (even if you are entirely local). You need to make sure the WinRM is enabled and configured. You can use the command `winrm quickconfig`, then make sure the "Windows Remote Management (WS-Management)" service is started. Also make sure you run this command in an elevated prompt.  

If that still fails, you can also set the certificate the old school way using `netsh` but let's try the proper way first  checking the WinRM route.
