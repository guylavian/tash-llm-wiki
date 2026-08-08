---
title: "Upgrading Entra Connect fails with \"HttpRequestException\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2239535/upgrading-entra-connect-fails-with-httprequestexce
question_id: 2239535
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 1
qa_tags: []
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# Upgrading Entra Connect fails with "HttpRequestException"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2239535/upgrading-entra-connect-fails-with-httprequestexce (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi 

We are trying to upgrade to the latest version of Entra Connect 2.4.129 from 2.3. This fails after i authenticate with my GA account with this message (see picture). I have verified that there is no CA policy blocking the authentication. We are at the latest .NET and TLS 1.2 are enabled. Any tips and tricks will be highly appreciated. 

The trace file states: "System.Net.Http.HttpRequestException: An error occurred while sending the request. ---> System.Net.WebException: The underlying connection was closed: An unexpected error occurred on a send. ---> System.IO.IOException: Unable to read data from the transport connection: An existing connection was forcibly closed by the remote host. ---> System.Net.Sockets.SocketException: An existing connection was forcibly closed by the remote host

   at System.Net.Sockets.Socket.EndReceive(IAsyncResult asyncResult)"

Thanks

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2025-03-27*

Hi, 

Just an update, i have now been to complete the upgrade process. We needed to add some IP adr. and this URL: https://s1.adhybridhealth.azure.com/providers/Microsoft.ADHybridHealthService/diagnostics/logs/installer/product/AzureADConnect/version/2.4.129.0/machine/SERVERNAME?result=unknown&type=AzureADConnect-Wizard&activityId=frth02911-643c-4754-8698-8a3e676ce1f6&component=SynchronizationRule_{bgt35e-f3b3-465a-8622-cd4ad4eff4f6}.xml&tenantId=XXXXXXX-1234-4567-7777-yu6745df23&machineId=d26657567-2665c-66459a-8c88-ad77673445af80

[10:34:31.488] [  1] [INFO ] UploadFile: WebException caught on post:System.Net.WebException: The remote server returned an error: (403) Forbidden.

When this was allowed in our firewall then i was able to complete the setup. Looks like more URLs are needed to complete the upgrade than a regular "day-to-day" sync?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-15*

Hi, i can check with our network department, and hear if they can provide me with these details. 

/ Hans Petter

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-27*

Thanks for your reply, Abiola.

Yes, i have ran this script and i think these settings is as it should be ? 

Kr. 

Hans Petter

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2025-03-27*

Hello Malme, Hans Petter,

I know you mentioned you have enabled TLS. This can be caused by it and it has resolved for many others.

Pls can you verify Connect is actually using that TLS using this script  https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-tls-enforcement

If it is not, you will need to ensure it does using https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-tls-enforcement

If this is not the case please follow up so we can help further

You can mark it 'Accept Answer' and 'Upvote' if this helped you

(Please note: If you have Priority Community support please wait for a dedicated Microsoft support representative to assist you, as they have access to the necessary backend resources. If you have not yet opened a support case, we recommend reaching out through the support channel available under your subscription level.)

Regards,

Abiola
