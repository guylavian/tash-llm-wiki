---
title: "Win2022 ADFS, Why does the SOAP metadata response (WS-Transfer Get from adfs/services/trust/mex) return different endpoints than the HTTP GET request from the browser?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5769884/win2022-adfs-why-does-the-soap-metadata-response-w
question_id: 5769884
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# Win2022 ADFS, Why does the SOAP metadata response (WS-Transfer Get from adfs/services/trust/mex) return different endpoints than the HTTP GET request from the browser?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5769884/win2022-adfs-why-does-the-soap-metadata-response-w (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello

We have a local legacy application that is using Windows Authentication with WS Trust.

For that the "adfs/services/trust/13/windowstransport" endpoint has been activated on the ADFS.

Requesting the metadata in the browser (HTTP GET request to adfs/services/trust/mex) I can see that the endpoint is successfully returned in the xml result.

The legacy application is using the .NET Framework class: MetadataExchangeClient, which by default uses a WS-Transfer Get request to read the metadata, so it uses a SOAP POST request to adfs/services/trust/mex with the action 'http://schemas.xmlsoap.org/ws/2004/09/transfer/Get'.

The SOAP response however does not contain the 'adfs/services/trust/13/windowstransport' endpoint. Most of the other endpoints still seem to be contained in the response as expected.

Is that a configuration setting on the ADFS that has to be adjusted for that to work?

In the previous ADFS version that was used (Win2016) the metadata was correct in both cases, it just failed to work after switching to Win2022.

Thanks for the help.

Regards,

Karsten

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2026-02-13*

It turned out that the issue was caused by a missing SPN registration on the ADFS.

After the SPN registration was done, the metadata url was correctly returning the endpoint in both formats, and event the metadata returned by the HTTP GET method was correct now (previously it did contain errors that could not be read by the WsdlImporter class).

## Answer (community) — community member

*upvotes: 0 · updated: 2026-02-10*

The discrepancy between the SOAP metadata response from the WS-Transfer Get request and the HTTP GET request in your ADFS setup may be related to how the endpoints are configured in Windows Server 2022 compared to Windows Server 2016. In ADFS, certain endpoints may not be included in the SOAP response due to configuration settings or the specific behavior of the WS-Transfer protocol.

Here are a few points to consider:

-  Endpoint Configuration: Ensure that the `adfs/services/trust/13/windowstransport` endpoint is properly configured and enabled in your ADFS settings. Sometimes, specific endpoints may not be included in the metadata published for SOAP requests if they are not configured to be exposed.

-  Differences in ADFS Versions: The behavior of metadata publishing may have changed between Windows Server 2016 and 2022. It's possible that certain endpoints are treated differently in the newer version, which could explain why they appear in the HTTP GET response but not in the SOAP response.

-  Testing with Different Protocols: You might want to test the metadata retrieval using different protocols or methods to see if the issue persists across all types of requests. This could help identify if the problem is specific to the WS-Transfer protocol.

-  Review Documentation: Check the official Microsoft documentation for any notes on changes in ADFS behavior or additional configuration steps that may be required for Windows Server 2022.

-  Logs and Traces: Review the ADFS logs for any errors or warnings that may indicate why the endpoint is not being included in the SOAP response. Tools like Fiddler can help trace the requests and responses to see if there are any discrepancies in the communication.

If the problem continues, consider reaching out to Microsoft support or community forums for more targeted assistance regarding ADFS on Windows Server 2022.

References:

-  AD FS troubleshooting: AD FS metadata endpoints

-  Sign in to Microsoft 365, Azure, or Intune fails after you change the federation service endpoint
