---
title: "[Migrated from MSDN Exchange Dev]Exchange Self-Signed Certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/150649/migrated-from-msdn-exchange-dev-exchange-self-sign
question_id: 150649
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]Exchange Self-Signed Certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/150649/migrated-from-msdn-exchange-dev-exchange-self-sign (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.

We are working to setup encrypted TLS emails between us and another vendor. Additionally, we have Mimecast SPAM filtering for our incoming and outgoing emails.

During the testing phase of this project, Mimecast is telling us that it is only seeing our Self-Signed Certificate when we send outgoing email, as opposed to our 3rd Party SSL; (with GoDaddy).

Mimecast advised me to ensure that the SMTP service was removed from the Self-Signed Certificate. Unfortunately, I have been unable to do so. It is grayed out in the EAC, and when I run the command within the Shell, it acts like it removes it, but does not. SMTP is enabled on multiple certificates within our Exchange environment.

I believe that Mimecast is correct, as I sent an email to my personal account, and I can see, within the header information, the private IP and DNS name of one of our Exchange Servers.

We have 2 Exchange DAG nodes, (2013 CU23). Below are the commands that I've tried running.

Exchange Server 1 (For Self-Signed Cert)  

Enable-ExchangeCertificate –Thumbprint 33B3BB4B500041DF82AD23649BE9199589D966B6 –Service None

Exchange Server 1 (With GoDaddy Cert)  

Enable-ExchangeCertificate –Thumbprint E2B663ABE9B9FDCFCD80986F151BC9A1378509AB –Services SMTP,IIS,IMAP,POP

Exchange Server 2 (For Self-Signed Cert)  

Enable-ExchangeCertificate –Thumbprint A631A9C4B60DBFFC0F53EF3C4590845AF565B0B2 –Service None

Exchange Server 2 (With GoDaddy Cert)  

Enable-ExchangeCertificate –Thumbprint E2B663ABE9B9FDCFCD80986F151BC9A1378509AB –Services SMTP,IIS,IMAP,POP

Below is some of the output I received on one of the Exchange Servers:

[PS] C:\Windows\system32>Enable-ExchangeCertificate -Thumbprint E2B663ABE9B9FDCFCD80986F151BC9A1378509AB -Services SMTP,IIS,IMAP,POP  

Creating a new session for implicit remoting of "Enable-ExchangeCertificate" command...

Confirm  

Overwrite the existing default SMTP certificate?

Current certificate: '33B3BB4B500041DF82AD23649BE9199589D966B6' (expires 11/1/2025 5:59:11 PM)  

Replace it with certificate: 'E2B663ABE9B9FDCFCD80986F151BC9A1378509AB' (expires 7/15/2022 6:26:12 PM)  

[Y] Yes [A] Yes to All [N] No [L] No to All [?] Help (default is "Y"): Y  

[PS] C:\Windows\system32>Get-ExchangeCertificate  

After that, when I run Get-ExchangeCertificate, I still see SMTP assigned to the Self-Signed Certificate, and when I send myself another email, I still see the private IP and DNS information of the Exchange Server.

Any thoughts\assistance would be much appreciated. Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-20*

Hi @Tee EL   ,    

Please try to run the following command to check whehter to bind the certificate successfully：    

```
Get-Receiveconnector | fl *tls*
```

You can also enable the protocol log on the receive connector, protocol logging records the SMTP conversations that occur on Send connectors and Receive connectors during message delivery. You can use this log to confirm whether you are receiving mail through the receive connector to which you bind the certificate. By default, this log is enabled on Default Frontend receive connector and implicit and invisible Send connector in the Front End Transport service on Mailbox servers.     

For more information: Configure protocol logging    

Based on my konwledge, the Default frontend receive connector receives emails through port 25. Please check whether the receive connector has TLS authentication enabled.    

For more information: Network ports for clients and mail flow in Exchange    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-17*

I performed these steps, and it worked. Still, my SPAM Filter vendor, (Mimecast), is telling me that they are still capturing the Self-Signed Certificate, instead of the 3rd Part, GoDaddy Certificate.

When I run openssl commands to verify the certificate on port 25, I receive data that points to no certificate. However, when I run the same command on port 443, I get the desired result. What am I missing?

Port 25:  

$ openssl s_client -showcerts -connect myserver.mydomain.lcl:25  

CONNECTED(00000003)

140466606376608:error:140770FC:SSL routines:SSL23_GET_SERVER_HELLO:unknown protocol:s23_clnt.c:759:

no peer certificate available

No client certificate CA names sent

SSL handshake has read 7 bytes and written 295 bytes

New, (NONE), Cipher is (NONE)  

Secure Renegotiation IS NOT supported  

Compression: NONE  

Expansion: NONE

Port 443  

openssl s_client -showcerts -connect myserver.mydomain.lcl:443  

CONNECTED(00000003)  

depth=2 C = US, ST = Arizona, L = Scottsdale, O = "GoDaddy.com, Inc.", CN = Go Daddy Root Certificate Authority - G2  

verify error:num=20:unable to get local issuer certificate

verify return:0

Certificate chain  

0 s:/OU=Domain Control Validated/CN=myserver.mydomain.com  

i:/C=US/ST=Arizona/L=Scottsdale/O=GoDaddy.com, Inc./OU=http://certs.godaddy.com/repository//CN=Go Daddy Secure Certificate Authority - G2  

-----BEGIN CERTIFICATE-----  

MIIG1DCCBbygAwIBAgIIFHE3JArzXy0wDQYJKoZIhvcNAQELBQAwgbQxCzAJBgNV  

BAYTAlVTMRAwDgYDVQQIEwdBcml6b25hMRMwEQYDVQQHEwpTY290dHNkYWxlMRow  

GAYDVQQKExFHb0RhZGR5LmNvbSwgSW5jLjEtMCsGA1UECxMkaHR0cDovL2NlcnRz  

LmdvZGFkZHkuY29tL3JlcG9zaXRvcnkvMTMwMQYDVQQDEypHbyBEYWRkeSBTZWN1  

cmUgQ2VydGlmaWNhdGUgQXV0aG9yaXR5IC0gRzIwHhcNMjAwNDE5MTI0NjEzWhcN  

MjIwNzE1MjMyNjEyWjA8MSEwHwYDVQQLExhEb21haW4gQ29udHJvbCBWYWxpZGF0  

ZWQxFzAVBgNVBAMTDndtLnBkY2FyZWEuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOC  

AQ8AMIIBCgKCAQEArZxWQdTmmBpDYTZVBOCWXi4Mm8iv4/CuoFqW4eHFDhuoEudB  

ZRodwM7ETpGyJNulREBPEXCu9v3gVmweUG9BUxu/B0SopE0CQ+sk//x8qSRg/guk  

A8VQJJfGNxCUnbNpnBB+7kXn1C0N3+7g1pHrewu8vXN4QPURNzTDKn1o4JaAr2pw  

S0yCviovkXYzSJVozsJ6yxh7ouNMvn/r4WbYeVIN0OHY8jo9N4+RkeT830xqCJ8h  

AX/JWVWAhoLAUJjQUDtQmId47ZFKx6WTX2rwj+uclK+KFdJVi6e5dLMqpBh8e38v  

HzbbDEuM6ymErDiynNfGS7qht2Zgafwdw66GxwIDAQABo4IDXzCCA1swDAYDVR0T  

AQH/BAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwDgYDVR0PAQH/  

BAQDAgWgMDgGA1UdHwQxMC8wLaAroCmGJ2h0dHA6Ly9jcmwuZ29kYWRkeS5jb20v  

Z2RpZzJzMS0xODg5LmNybDBdBgNVHSAEVjBUMEgGC2CGSAGG/W0BBxcBMDkwNwYI  

KwYBBQUHAgEWK2h0dHA6Ly9jZXJ0aWZpY2F0ZXMuZ29kYWRkeS5jb20vcmVwb3Np  

dG9yeS8wCAYGZ4EMAQIBMHYGCCsGAQUFBwEBBGowaDAkBggrBgEFBQcwAYYYaHR0  

cDovL29jc3AuZ29kYWRkeS5jb20vMEAGCCsGAQUFBzAChjRodHRwOi8vY2VydGlm  

aWNhdGVzLmdvZGFkZHkuY29tL3JlcG9zaXRvcnkvZ2RpZzIuY3J0MB8GA1UdIwQY  

MBaAFEDCvSeOzDSDMKIz1/tss/C0LIDOMEcGA1UdEQRAMD6CDndtLnBkY2FyZWEu  

Y29tghJ3d3cud20ucGRjYXJlYS5jb22CGGF1dG9kaXNjb3Zlci5wZGNhcmVhLmNv  

bTAdBgNVHQ4EFgQUrHZnzpIns1lkAL++hi/gLv4nbzQwggGABgorBgEEAdZ5AgQC  

BIIBcASCAWwBagB2AKS5CZC0GFgUh7sTosxncAo8NZgE+RvfuON3zQ7IDdwQAAAB  

cZJ5qRQAAAQDAEcwRQIhAMk6a0AS3PvVBYGwcj/u35tL4QN/c1+EfHRW3b4ULXhB  

AiBdBGbHZkE/2MyhVKgrKYHP+iqUwk1zsL5inqC7r/UT2QB3ALvZ37wfinG1k5Qj  

l6qSe0c4V5UKq1LoGpCWZDaOHtGFAAABcZJ5q8EAAAQDAEgwRgIhAN7jMpeA6Wwn  

XiiBVvZ0OljmW49iVLaElCsGm3aUiFTQAiEAqU9mTlkC+GhC1UWgEJ9VZQ7kSsh3  

s/lnBtgVpdImAIUAdwBWFAaaL9fC7NP14b1Esj7HRna5vJkRXMDvlJhV1onQ3QAA  

AXGSea4bAAAEAwBIMEYCIQCVtjfzTAPHA79CfT/8If8YaMceGKXvsQwhnu2rKrxG  

wgIhAMlfLLj6bCKtm+Ebwum20+LYL5xVbqB+Q1XcGNMPnIEgMA0GCSqGSIb3DQEB  

CwUAA4IBAQAvMxPCr6HFyu7LfCdflDeB/rgOUDG23sA9+54QuHLpzWg5NIFZio3X  

JM+PcKj3a4yP2mUIBjeEn/GlWi/u96iYaAu3v0dXiOYf9n7n/Jhdcv3wlTM85zlf  

tMKXpbZjlBbnKqUPdGFXmIqWX0KGJw9kgw5WnAp+A+z7WcP6vJRV1iMl3+e1sH4Z  

q2U972STw0I0+XfT08gEAXvrwD7bmpzluqcCmthYooTjiIpaXbGBfnEDUj8SAkyo  

UeLZbWZAkppGFHUnoGELqAHKHMGqbqptEMFysFwKRMWBP3xwaXns05n3ucn1ReXE  

PrJcajaKQQ74zjvGm1o/nZ8A9GmBOg4Y  

-----END CERTIFICATE-----  

1 s:/C=US/ST=Arizona/L=Scottsdale/O=GoDaddy.com, Inc./OU=http://certs.godaddy.com/repository//CN=Go Daddy Secure Certificate Authority - G2  

i:/C=US/ST=Arizona/L=Scottsdale/O=GoDaddy.com, Inc./CN=Go Daddy Root Certificate Authority - G2  

-----BEGIN CERTIFICATE-----  

MIIE0DCCA7igAwIBAgIBBzANBgkqhkiG9w0BAQsFADCBgzELMAkGA1UEBhMCVVMx  

EDAOBgNVBAgTB0FyaXpvbmExEzARBgNVBAcTClNjb3R0c2RhbGUxGjAYBgNVBAoT  

EUdvRGFkZHkuY29tLCBJbmMuMTEwLwYDVQQDEyhHbyBEYWRkeSBSb290IENlcnRp  

ZmljYXRlIEF1dGhvcml0eSAtIEcyMB4XDTExMDUwMzA3MDAwMFoXDTMxMDUwMzA3  

MDAwMFowgbQxCzAJBgNVBAYTAlVTMRAwDgYDVQQIEwdBcml6b25hMRMwEQYDVQQH  

EwpTY290dHNkYWxlMRowGAYDVQQKExFHb0RhZGR5LmNvbSwgSW5jLjEtMCsGA1UE  

CxMkaHR0cDovL2NlcnRzLmdvZGFkZHkuY29tL3JlcG9zaXRvcnkvMTMwMQYDVQQD  

EypHbyBEYWRkeSBTZWN1cmUgQ2VydGlmaWNhdGUgQXV0aG9yaXR5IC0gRzIwggEi  

MA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC54MsQ1K92vdSTYuswZLiBCGzD  

BNliF44v/z5lz4/OYuY8UhzaFkVLVat4a2ODYpDOD2lsmcgaFItMzEUz6ojcnqOv  

K/6AYZ15V8TPLvQ/MDxdR/yaFrzDN5ZBUY4RS1T4KL7QjL7wMDge87Am+GZHY23e  

cSZHjzhHU9FGHbTj3ADqRay9vHHZqm8A29vNMDp5T19MR/gd71vCxJ1gO7GyQ5HY  

pDNO6rPWJ0+tJYqlxvTV0KaudAVkV4i1RFXULSo6Pvi4vekyCgKUZMQWOlDxSq7n  

eTOvDCAHf+jfBDnCaQJsY1L6d8EbyHSHyLmTGFBUNUtpTrw700kuH9zB0lL7AgMB  

AAGjggEaMIIBFjAPBgNVHRMBAf8EBTADAQH/MA4GA1UdDwEB/wQEAwIBBjAdBgNV  

HQ4EFgQUQMK9J47MNIMwojPX+2yz8LQsgM4wHwYDVR0jBBgwFoAUOpqFBxBnKLbv  

9r0FQW4gwZTaD94wNAYIKwYBBQUHAQEEKDAmMCQGCCsGAQUFBzABhhhodHRwOi8v  

b2NzcC5nb2RhZGR5LmNvbS8wNQYDVR0fBC4wLDAqoCigJoYkaHR0cDovL2NybC5n  

b2RhZGR5LmNvbS9nZHJvb3QtZzIuY3JsMEYGA1UdIAQ/MD0wOwYEVR0gADAzMDEG  

CCsGAQUFBwIBFiVodHRwczovL2NlcnRzLmdvZGFkZHkuY29tL3JlcG9zaXRvcnkv  

MA0GCSqGSIb3DQEBCwUAA4IBAQAIfmyTEMg4uJapkEv/oV9PBO9sPpyIBslQj6Zz  

91cxG7685C/b+LrTW+C05+Z5Yg4MotdqY3MxtfWoSKQ7CC2iXZDXtHwlTxFWMMS2  

RJ17LJ3lXubvDGGqv+QqG+6EnriDfcFDzkSnE3ANkR/0yBOtg2DZ2HKocyQetawi  

DsoXiWJYRBuriSUBAA/NxBti21G00w9RKpv0vHP8ds42pM3Z2Czqrpv1KrKQ0U11  

GIo/ikGQI31bS/6kA1ibRrLDYGCD+H1QQc7CoZDDu+8CL9IVVO5EFdkKrqeKM+2x  

LXY2JtwE65/3YR8V3Idv7kaWKK2hJn0KCacuBKONvPi8BDAB  

-----END CERTIFICATE-----  

2 s:/C=US/ST=Arizona/L=Scottsdale/O=GoDaddy.com, Inc./CN=Go Daddy Root Certificate Authority - G2  

i:/C=US/O=The Go Daddy Group, Inc./OU=Go Daddy Class 2 Certification Authority  

-----BEGIN CERTIFICATE-----  

MIIEfTCCA2WgAwIBAgIDG+cVMA0GCSqGSIb3DQEBCwUAMGMxCzAJBgNVBAYTAlVT  

MSEwHwYDVQQKExhUaGUgR28gRGFkZHkgR3JvdXAsIEluYy4xMTAvBgNVBAsTKEdv  

IERhZGR5IENsYXNzIDIgQ2VydGlmaWNhdGlvbiBBdXRob3JpdHkwHhcNMTQwMTAx  

MDcwMDAwWhcNMzEwNTMwMDcwMDAwWjCBgzELMAkGA1UEBhMCVVMxEDAOBgNVBAgT  

B0FyaXpvbmExEzARBgNVBAcTClNjb3R0c2RhbGUxGjAYBgNVBAoTEUdvRGFkZHku  

Y29tLCBJbmMuMTEwLwYDVQQDEyhHbyBEYWRkeSBSb290IENlcnRpZmljYXRlIEF1  

dGhvcml0eSAtIEcyMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv3Fi  

CPH6WTT3G8kYo/eASVjpIoMTpsUgQwE7hPHmhUmfJ+r2hBtOoLTbcJjHMgGxBT4H  

Tu70+k8vWTAi56sZVmvigAf88xZ1gDlRe+X5NbZ0TqmNghPktj+pA4P6or6KFWp/  

3gvDthkUBcrqw6gElDtGfDIN8wBmIsiNaW02jBEYt9OyHGC0OPoCjM7T3UYH3go+  

6118yHz7sCtTpJJiaVElBWEaRIGMLKlDliPfrDqBmg4pxRyp6V0etp6eMAo5zvGI  

gPtLXcwy7IViQyU0AlYnAZG0O3AqP26x6JyIAX2f1PnbU21gnb8s51iruF9G/M7E  

GwM8CetJMVxpRrPgRwIDAQABo4IBFzCCARMwDwYDVR0TAQH/BAUwAwEB/zAOBgNV  

HQ8BAf8EBAMCAQYwHQYDVR0OBBYEFDqahQcQZyi27/a9BUFuIMGU2g/eMB8GA1Ud  

IwQYMBaAFNLEsNKR1EwRcbNhyz2h/t2oatTjMDQGCCsGAQUFBwEBBCgwJjAkBggr  

BgEFBQcwAYYYaHR0cDovL29jc3AuZ29kYWRkeS5jb20vMDIGA1UdHwQrMCkwJ6Al  

oCOGIWh0dHA6Ly9jcmwuZ29kYWRkeS5jb20vZ2Ryb290LmNybDBGBgNVHSAEPzA9  

MDsGBFUdIAAwMzAxBggrBgEFBQcCARYlaHR0cHM6Ly9jZXJ0cy5nb2RhZGR5LmNv  

bS9yZXBvc2l0b3J5LzANBgkqhkiG9w0BAQsFAAOCAQEAWQtTvZKGEacke+1bMc8d  

H2xwxbhuvk679r6XUOEwf7ooXGKUwuN+M/f7QnaF25UcjCJYdQkMiGVnOQoWCcWg  

OJekxSOTP7QYpgEGRJHjp2kntFolfzq3Ms3dhP8qOCkzpN1nsoX+oYggHFCJyNwq  

9kIDN0zmiN/VryTyscPfzLXs4Jlet0lUIDyUGAzHHFIYSaRt4bNYC8nY7NmuHDKO  

KHAN4v6mF56ED71XcLNa6R+ghlO773z/aQvgSMO3kwvIClTErF0UZzdsyqUvMQg3  

qm5vjLyb4lddJIGvl5echK1srDdMZvNhkREg5L4wn3qkKQmw4TRfZHcYQFHfjDCm  

rw==

-----END CERTIFICATE-----

Server certificate  

subject=/OU=Domain Control Validated/CN=myserver.mydomain.com

issuer=/C=US/ST=Arizona/L=Scottsdale/O=GoDaddy.com, Inc./OU=http://certs.godaddy.com/repository//CN=Go Daddy Secure Certificate Authority - G2

No client certificate CA names sent

SSL handshake has read 4719 bytes and written 509 bytes

New, TLSv1/SSLv3, Cipher is ECDHE-RSA-AES256-SHA384  

Server public key is 2048 bit  

Secure Renegotiation IS supported  

Compression: NONE  

Expansion: NONE  

SSL-Session:  

Protocol : TLSv1.2  

Cipher : ECDHE-RSA-AES256-SHA384  

Session-ID: C63F000048922F864C7E0ABB6D9E4E9E13C91301EAD2D21E80265EE3CDFE5E8A  

Session-ID-ctx:  

Master-Key: 7A7F18C1320CFB4D91CB4E809614D8AD5B691DD95245756CD62FAE968AC5BE85035486AC0293C79F2CA428BD252AC5EA  

Key-Arg : None  

PSK identity: None  

PSK identity hint: None  

SRP username: None  

Start Time: 1605213867  

Timeout : 300 (sec)  

Verify return code: 20 (unable to get local issuer certificate)

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-04*

Hi,  

Based on my knowledge, if the service is assigned to the certificate, we will not be able to delete the service unless we apply for a new certificate and assign the service to the new certificate, and then remove the old certificate. However, we cannot delete the three self-signed certificates that come with Exchange, otherwise there may be problems with the use of Exchange.

1.First of all, I run the following command line in my Exchange 2013 lab environment, also ineffective

```
Enable-ExchangeCertificate -Thumbprint <> -Services None
```

2.Please following the steps below to bind the specific certificate to the receive/send connector and see if the issue is resolved:  

1）Please run the following command to get information of your certificate:

```
Get-ExchangeCertificate
```

2）Please run the following command to Capture the certificate as a variable.

```
$cert = Get-ExchangeCertificate -Thumbprint <>
```

3) In order to configure the certificate on the receive connector, please run the following command to create a special string that contains the issuer and the subject of the certificate:

```
$tlscertificatename = "$($cert.Issuer)$($cert.Subject)"
```

4) Please run the following command to configure the receive connector:

```
Set-ReceiveConnector "<>" -TlsCertificateName $tlscertificatename  
Set-SendConnector "<>" -TlsCertificateName $tlscertificatename
```

For more information you could refer to: Configuring the TLS Certificate Name for Exchange Server Receive Connectors and Configuring a Certificate on Exchange Receive Connector  

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
