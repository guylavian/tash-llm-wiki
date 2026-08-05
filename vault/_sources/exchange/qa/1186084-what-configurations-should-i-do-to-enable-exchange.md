---
title: "What configurations should I do to enable Exchange Mailbox reading through javax Mail?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1186084/what-configurations-should-i-do-to-enable-exchange
question_id: 1186084
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# What configurations should I do to enable Exchange Mailbox reading through javax Mail?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1186084/what-configurations-should-i-do-to-enable-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've been trying to adapt a old java code to connect in a online exchange mailbox.

Here is the code based on this totorial

```
public static void main(String[] args) throws MessagingException, NoSuchProviderException {
		final var tokenProvider = new RopcTokenProvider();

		final var accessToken = tokenProvider.getAccessToken();

		final var user = "******@contoso.com";
		final var host = "outlook.office365.com";

		final Properties props = new Properties();
		props.put("mail.debug", "true");
		props.put("mail.imaps.debug", "true");
		props.put("mail.store.protocol", "imaps");
		props.put("mail.imaps.auth.plain.disable", true);
		props.put("mail.imaps.port", 993);
		props.put("mail.imaps.ssl.enable", "true");
		props.put("mail.imaps.starttls.enable", "true");
		props.put("mail.imaps.auth.mechanisms", "XOAUTH2");

		Session session = Session.getInstance(props);
		Store store = session.getStore("imaps");
		store.connect(host, user, accessToken);
		final var inbox = store.getFolder("INBOX");
	}

	private static interface TokenProvider {
		String getAccessToken();
	}

	private static class RopcTokenProvider implements TokenProvider {

		@Override
		public String getAccessToken() {
			final var tennantId = "tennant-id";
			final var clientId = "clientId";
			final var clientSecret = "clientSecret";
			final var url = "https://login.microsoftonline.com/%s/oauth2/v2.0/token";

			final var headers = new HttpHeaders();
			headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);

			final var map = new LinkedMultiValueMap();
			map.add("client_id", clientId);
			map.add("client_secret", clientSecret);
			map.add("scope", "https://outlook.office365.com/.default");
			map.add("grant_type", "client_credentials");

			final var request = new HttpEntity>(map, headers);

			final var restTemplate = new RestTemplate();

			final var oAuthTokenDTOResponseEntity = restTemplate.postForEntity(
					String.format(url, tennantId),
					request,
					String.class
			);

			final var body = oAuthTokenDTOResponseEntity.getBody();

			try {
				return new ObjectMapper().readValue(body, OAuthTokenDTO.class).getAccessToken();
			} catch (IOException e) {
				throw new RuntimeException(e);
			}
		}
	}

	private static class OAuthTokenDTO {
		@JsonProperty("token_type")
		private String tokenType;
		@JsonProperty("expires_in")
		private String expiresIn;
		@JsonProperty("ext_expires_in")
		private String extExpiresIn;
		@JsonProperty("access_token")
		private String accessToken;

		public String getTokenType() {
			return tokenType;
		}

		public void setTokenType(String tokenType) {
			this.tokenType = tokenType;
		}

		public String getExpiresIn() {
			return expiresIn;
		}

		public void setExpiresIn(String expiresIn) {
			this.expiresIn = expiresIn;
		}

		public String getExtExpiresIn() {
			return extExpiresIn;
		}

		public void setExtExpiresIn(String extExpiresIn) {
			this.extExpiresIn = extExpiresIn;
		}

		public String getAccessToken() {
			return accessToken;
		}

		public void setAccessToken(String accessToken) {
			this.accessToken = accessToken;
		}
	}
```

My application is configured in azure with these permissions set

But when I execute the code I have this problem with IMAP authentication

```
DEBUG: JavaMail version 1.6.2
DEBUG: successfully loaded resource: /META-INF/javamail.default.address.map
DEBUG: getProvider() returning javax.mail.Provider[STORE,imaps,com.sun.mail.imap.IMAPSSLStore,Oracle]
DEBUG IMAPS: mail.imap.fetchsize: 16384
DEBUG IMAPS: mail.imap.ignorebodystructuresize: false
DEBUG IMAPS: mail.imap.statuscachetimeout: 1000
DEBUG IMAPS: mail.imap.appendbuffersize: -1
DEBUG IMAPS: mail.imap.minidletime: 10
DEBUG IMAPS: enable STARTTLS
DEBUG IMAPS: closeFoldersOnStoreFailure
DEBUG IMAPS: trying to connect to host "outlook.office365.com", port 993, isSSL true
* OK The Microsoft Exchange IMAP4 service is ready. [ZwBQZQATIOy==]
A0 CAPABILITY
* CAPABILITY IMAP4 IMAP4rev1 AUTH=PLAIN AUTH=XOAUTH2 SASL-IR UIDPLUS ID UNSELECT CHILDREN IDLE NAMESPACE LITERAL+
A0 OK CAPABILITY completed.
DEBUG IMAPS: AUTH: PLAIN
DEBUG IMAPS: AUTH: XOAUTH2
DEBUG IMAPS: protocolConnect login, host=outlook.office365.com, user=contoso@contoso, password=
DEBUG IMAPS: AUTHENTICATE XOAUTH2 command trace suppressed
DEBUG IMAPS: AUTHENTICATE XOAUTH2 command result: A1 NO AUTHENTICATE failed.
Exception in thread "main" javax.mail.AuthenticationFailedException: AUTHENTICATE failed.
	at com.sun.mail.imap.IMAPStore.protocolConnect(IMAPStore.java:732)
	at javax.mail.Service.connect(Service.java:366)
	at javax.mail.Service.connect(Service.java:246)
	at Another.main(Another.java:39)
```

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-03-03*

Verify you are requesting the access token correctly:

https://learn.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth#add-the-pop-and-imap-permissions-to-your-aad-application
