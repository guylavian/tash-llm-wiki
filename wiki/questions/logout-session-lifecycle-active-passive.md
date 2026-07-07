---
title: "Logout ו-session lifecycle ב-RHBK 26 באתר Active-Passive — מה באמת מתבטל, ואיפה זה נשבר"
type: question
domain: keycloak
slug: logout-session-lifecycle-active-passive
summary: "ניתוח תלת-חלקי של RP-Initiated Logout, offline/online sessions מול failover, ו-notBefore push revocation במערך Active-Passive multi-site: מה שורד, מה נעלם, ואיפה המלכודות"
sources:
  - guide:server_administration_guide
  - guide:securing_applications_and_services_guide
  - guide:high_availability_guide
  - guide:server_configuration_guide
  - ref:high-availability.md
  - ref:server-administration.md
  - ref:securing-apps-oidc-saml.md
provenance_extracted: 18
provenance_inferred: 5
provenance_ambiguous: 1
tags: [tokens]
status: reviewed
updated: 2026-07-02
---

# Logout ו-session lifecycle ב-RHBK 26 באתר Active-Passive — מה באמת מתבטל, ואיפה זה נשבר

> תרחיש: realm אחד, שלושה clients — OIDC portal (confidential), SAML sharepoint, ו-portal-mobile (mobile, offline token). Active-Passive multi-site עם Infinispan cross-site replication ו-`persistent-user-sessions` מופעל.

---

## שאלה 1: RP-Initiated Logout מ-portal — מה מתבטל ומה שורד?

### מה קורה כשמשתמש לוחץ Logout ב-portal

ה-portal שולח בקשה אל `/realms/{realm}/protocol/openid-connect/logout` עם `id_token_hint` (RP-Initiated Logout). RHBK:

1. **מבטל את SSO user session** — כל ה-client sessions (portal, sharepoint, portal-mobile) המקושרים לאותה user session מסומנים להסרה. ה-SSO cookie מתבטל.
2. **שולח הודעות logout ל-clients** — בהתאם להגדרות כל client.

### מה שורד שלב זה?

| רכיב | שורד? | הסבר |
|------|-------|-------|
| **SAML session של sharepoint** | ✅ לא מבוטל אוטומטית | SAML clients **אינם מקבלים back-channel logout requests** — זוהי מגבלה מתועדת: "Client types such as SAML do not receive a back-channel logout request" (Managing User Sessions, RHBK 26.4). SAML Single Logout (SLO) דורש מנגנון אחר לגמרי (SAML `<LogoutRequest>`). |
| **Offline token של portal-mobile** | ✅ לא מבוטל (`Backchannel logout revoke offline sessions` תלוי) | ברירת מחדל, offline sessions **אינם מבוטלים ב-RP-Initiated Logout**. החריג: אם ל-portal (ה-OIDC client שה-logout מגיע דרכו) מוגדר **Backchannel logout URL** עם **Backchannel logout revoke offline sessions** = ON, ורק דרך **back-channel** (לא front-channel), אז RHBK ישלח Logout Token עם `revoke_offline_access` event, וה-client שמקבל אותו יכול לכבד אותו. אבל לרוב ה-offline token של portal-mobile (client נפרד!) אינו מושפע. |
| **Access/refresh tokens קיימים** | לרוב ✅ לא מבוטלים מיד | RP-Initiated Logout מבטל את ה-session אך לא revokes outstanding tokens. "Clicking Sign out all active sessions does not revoke outstanding access tokens. Outstanding tokens must expire naturally." |
| **SAML session (ברמת RHBK)** | ❌ מבוטל ברמת ה-session המרכזית | ה-user session נסגר, אבל SAML SP לא מקבל הודעה. |

### Front-channel vs Back-channel — ההבדל המעשי עבור sharepoint

| מאפיין | Front-channel logout | Back-channel logout |
|--------|---------------------|---------------------|
| מנגנון | redirect דפדפן ל-`front-channel logout URL` | בקשת HTTP server-to-server (logout token) |
| תלוי בדפדפן? | ✅ חייב שהדפדפן פתוח | ❌ לא — השרת שולח ישירות |
| SAML client מקבל? | ❌ **SAML clients לא תומכים בזה** | ❌ SAML clients מקבלים back-channel logout רק אם יש להם `Admin URL` שמקבל קבאקים בפורמט legacy adapter — וגם זה legacy |
| למה front-channel נוטה להיכשל בשקט? | **הדפדפן חייב להיות באותו tab session** — משתמשים רבים סוגרים tab לפני שה-redirect קורה; חסימות pop-up, ad-blockers, CORS/docker-compose מונעים את ההפנייה. הכשל שקט כי Keycloak מנסה לשלוח, אך לא מאמת שהתקבל. **SAML SLO** מטבעו עובד אחרת לגמרי (redirect של הדפדפן עם `<LogoutRequest>` חתום) — לא זהה ל-OIDC front-channel. |

> **מסקנה:** SAML sharepoint **אינו מקבל** הודעת logout לא דרך front-channel ולא דרך back-channel. SAML SLO מצריך הטמעה נפרדת (SAML `<LogoutRequest>` redirect) שמצריכה קונפיגורציה של `Logout Service POST Binding URL` / `Logout Service Redirect Binding URL` ב-client. **הבעיה הנפוצה**: SAML client קונפיגורציה חלקית -> SLO לא נשלח -> ה-sharepoint session נשאר חי גם אחרי logout מהפורטל.

---

## שאלה 2: Offline session מול regular (online) session — מבנה אחסון, failover, ומלכודת

### ההבדל המבני: cache layers

| היבט | Regular (online) session | Offline session |
|------|-------------------------|-----------------|
| **Cache name** | `sessions`, `clientSessions` | `offlineSessions`, `offlineClientSessions` |
| **Cache type** | Distributed | Distributed |
| **DB persistence (ברירת מחדל)** | ✅ Persistent (נשמר ב-DB + cached) | ✅ Persistent (נשמר ב-DB + cached) |
| **Entry limit per node** | 10,000 (ברירת מחדל) | 10,000 (ברירת מחדל) |
| **Offline flag** | `offline_flag = '0'` | `offline_flag ≠ '0'` (או טבלאות נפרדות `offline_user_session` / `offline_client_session`) |

### persistent-user-sessions ו-multi-site

ב-RHBK 26, `persistent-user-sessions` הוא **feature מופעל כברירת מחדל**. ברגע שמפעילים את ה-`multi-site` feature, **אי אפשר להשבית אותו**:

> "Disabling persistent-user-sessions is not possible when multi-site feature is enabled." (Configuring distributed caches, RHBK 26.4)

המשמעות: **הן sessions רגילות והן offline sessions נשמרות ב-Database**, לא רק ב-cache. זהו תנאי חובה ל-consistency ב-multi-site.

### Failover: מה שורד?

כשהאתר הפעיל נופל:

```
משתמש ← Load Balancer ← גילה שה-Active מת ← מנתב ל-Passive
```

| סוג session | שורד failover? | למה? |
|-------------|---------------|------|
| **Regular user session** (online) | ⚠️ **תלוי** | ה-session data נשמר ב-DB *(שורד)*, אבל ה-cache ב-Passive site קר. Infinispan cache של Regular sessions הוא **Distributed with 1 owner** (בברירת מחדל Embedded), וב-cross-site המידע ב-cache יכול להיות חם/קר תלוי בזמן שחלף. בפועל: המידע ב-DB קיים, **אבל ה-cache ב-Passive לא בהכרח מכיל את ה-entry הספציפי** — הוא צריך להיטעל מה-DB. האתגר הוא **session affinity**: load balancer עלול לנתב בקשה של אותו משתמש ל-Pod אחר ב-Passive site שאין לו את ה-session ב-cache. |
| **Offline session** | ✅ **שורד באופן מהימן** | Offline sessions נשמרות ב-DB (+ cached). מעצם טבען, offline tokens לא מצריכות user session browserית — ה-mobile client פשוט משתמש ב-refresh token מול ה-token endpoint. ה-token validation נעזר ב-DB (או ב-cache) כדי לאמת שה-offline session עדיין תקפה. |
| **Authentication session** (באמצע login) | ❌ **נעלם** | Authentication sessions נשמרות רק ב-`authenticationSessions` Distributed cache **(ללא DB persistence)**. "Authentication sessions are created whenever a user tries to authenticate. They are automatically destroyed once the authentication process completes or due to reaching their expiration time." — cache-only, לא שורד site failure. |

### המלכודת (הרמז לשאלה)

> **המלכודת:** Regular (online) sessions אמנם נשמרות ב-DB, אבל ה-cache layer ב-multi-site עם Embedded Infinispan (ללא Data Grid cross-site replication) עלול להיות קר ב-Passive site. Infinispan Embedded ב-RHBK 26 multi-site architecture משתמש ב-**work cache** (replicated) כדי להפיץ invalidation messages, **לא** כדי להפיץ session data עצמה. ה-session data נטען מה-DB על-דעת.
>
> לעומת זאת, Offline sessions נשענות על **offlineSessions** cache + DB — מנגנון אחסון זהה למהותו.
>
> **ההבדל האמיתי הוא בתדירות השימוש:** Regular session נבדקת כמעט בכל request (refresh, UserInfo, logout, SSO redirect) — והעדר ה-cached entry ב-Passive site cause DB hit. Offline token נבדק רק כשה-mobile client מחליט לרענן את ה-access token שלו (נדיר יותר). **הכשל הוא לא באובדן מידע אלא ב-latency spike** — במיוחד ב-failover המוני.

---

## שאלה 3: NotBefore (not-before / nbf) — מנגנון ביטול גורף

### מה זה notBefore?

NotBefore הוא **revocation policy ברמת realm או client** — timestamp אחד שאומר "כל token שהונפק לפני זמן זה אינו תקף". בניגוד ל-session revocation (שמבטל session בודד), notBefore הוא:

- **גורף** — משפיע על **כל** ה-tokens של אותו realm/client (access, refresh, offline, ID, etc.)
- **מבוסס על זמן** — לא על session ID
- **מתפשט ל-clients** — RHBK "דוחף" (Push) את ה-policy לכל OIDC client עם `Admin URL` מוגדר, כך שהם יודעים לדחות tokens עם `iat` לפני ה-nbf

### NotBefore לעומת session revocation

| מאפיין | Session revocation (admin) | NotBefore push |
|--------|---------------------------|----------------|
| היקף | session **בודד** (user session + client sessions + refresh tokens) | **כל** ה-tokens של realm/client |
| Offline tokens | מבוטלים אם ה-user session נסגר | **מבוטלים** (כי iat שלהם לפני nbf) |
| SAML assertions | לא רלוונטי | **מבוטלים** |
| דורש Admin URL ב-client? | לא | ✅ כן — "Push this revocation policy to any registered OIDC client with the Red Hat build of Keycloak OIDC client adapter" |
| איך RHBK אוכף? | בצד השרת (session invalidated) | בצד השרת + expected שה-client יאכוף גם כן (אבל SAML clients לא מקבלים push) |

### איך notBefore מתפשט לרוחב שני האתרים

ב-Active-Passive multi-site:

1. Admin קובע `Set to now` → RHBK כותב את ה-nbf החדש ל-**Database** (realm או client record).
2. ה-nbf החדש מתפשט ל-Passive site **דרך ה-DB replication** (synchronous Aurora).
3. Infinispan `work` cache שולח **invalidation** ל-local caches של כל ה-Pods בשני האתרים (כולל Passive).
4. RHBK **Push** את ה-policy ל-clients — התהליך הזה הוא *client-initiated*: RHBK שולח HTTP request ל-`Admin URL` של כל client. **זה קורה מ-RHBK instance אחד** (זה שדרכו ביצעת את ה-push). אם ה-push נכשל לחלק מה-clients, ה-nbf עדיין מאוכפף בצד השרת.

### המהירות

- **צד השרת (RHBK):** מיידי — nbf נכתב ל-DB, local caches מתעדכנים דרך invalidation. לוקח שניות בודדות עד ל-Passive site.
- **צד ה-client (push):** תלוי — push הוא HTTP best-effort. אם client לא זמין, ה-push נכשל. ה-client עדיין יאוכף nbf כשהוא יבצע refresh או token introspection.

### המלכודת: "כפתור חירום" ב-Active-Passive

למה הסתמכות על notBefore כ"כפתור חירום" ב-Active-Passive היא מסוכנת:

1. **SAML clients לא מקבלים push** — "Client types such as SAML do not receive a back-channel logout request." SAML SP שומר את ה-SAML session בצד שלו ואין לו Admin URL. Push של notBefore **לא מגיע** ל-SAML SP. ה-sharepoint ימשיך לקבל את המשתמש גם אחרי notBefore.
2. **Offline tokens קיימים נפסלים צד-שרת, אבל...** — Offline sessions נשמרות ב-DB עם ה-nbf timestamp. RHBK יבדוק את ה-nbf בכל ניסיון refresh. אבל **offline tokens הם long-lived** — ייתכן ש-honest client (portal-mobile) ישמור את ה-offline token במשך שעות. הוא לא יגלה שה-nbf השתנה עד לניסיון ה-refresh הבא. לא ניתן "לבטל" offline token שכבר נמצא ביד ה-client — זהו bearer token.
3. **Push לא מגיע ל-mobile clients** — Offline tokens של mobile clients (portal-mobile) אינם מקבלים push (אין Admin URL). ה-nbf מאוכף רק צד-שרת.
4. **Application of the nbf is not retroactive for the offline token that was already issued and is being used** — Offline tokens שנשלפו לפני ה-nbf עדיין עשויים להיות משומשים לזמן קצר עקב caching ב-clients.

### ההבדל המכריע מול session revocation

| | Session revocation (session בודד) | NotBefore |
|---|---|---|
| SAML session | לא מבוטל (SAML SP צדדי) | לא מבוטל (אין push ל-SAML, אבל nbf משפיע על tokens עתידיים) |
| Offline tokens | מבוטלים **אם ה-user session שממנו הונפקו נסגר** | מבוטלים בצד השרת (iat < nbf → reject) |
| מהירות בפריסה | 0 (session-ID specific) | מסתמך על DB replication + invalidation → שניות |

> **לסיכום:** NotBefore הוא מנגנון יעיל לביטול מהיר של tokens *בצד השרת* בשני האתרים, אבל **אינו מחליף** revocation של session בודד (למקרים נקודתיים), ו**אינו אפקטיבי** עבור SAML clients או offline tokens שכבר הונפקו ונמצאים אצל client. כ"כפתור חירום" ב-Active-Passive, הוא עובד מצוין לחסימת **גישה חדשה** דרך OIDC clients, אבל לא מבטל גישה קיימת של SAML SPs או offline mobile clients עד שה-tokens יפוגו או יבוטלו בדרכים אחרות.

---

## References

### RH ground-truth (`kb:` / `guide:` / `ref:`)
- **kb:managing-user-sessions** — Chapter 6. Managing user sessions, RHBK 26.4 Server Administration Guide (session revocation, notBefore, Sign out all active sessions → SAML does not receive back-channel logout)
- **kb:mitigating-security-threats** — Chapter 16. Mitigating security threats, RHBK 26.4 Server Administration Guide (not-before revocation policy, push)
- **kb:caching** — Chapter 10. Configuring distributed caches, RHBK 26.4 Server Configuration Guide (cache types: sessions/offlineSessions, volatile sessions, persistent-user-sessions + multi-site interaction)
- **kb:sso-protocols** — Chapter 10. SSO protocols, RHBK 26.4 Server Administration Guide (RP-Initiated Logout, logout endpoint)
- **kb:managing-clients** — Chapter 13. Managing OpenID Connect and SAML Clients, RHBK 26.4 Server Administration Guide (logout settings: front-channel/back-channel, revocation, offline tokens)
- **kb:multi-cluster-introduction** — Chapter 3. Multi-cluster deployments, RHBK 26.6 High Availability Guide (concepts, data durability, synchronous replication)
- **kb:concepts-multi-site** — Chapter 2. Concepts for multi-site deployments, RHBK 26.2 High Availability Guide (data storage patterns in multi-site)
- **ref:high-availability.md** — HA guide distillation (cross-site replication, external Data Grid)
- **ref:server-administration.md** — Server administration distillation (sessions, tokens, notBefore)
- **ref:securing-apps-oidc-saml.md** — Securing apps distillation (logout, SAML SLO)

### Wiki pages
- [[oidc-logout]] — OIDC logout endpoint & SAML SLO
- [[tokens-and-sessions]] — session lifespans, refresh tokens, offline tokens
- [[session-persistence-volatile]] — DB-backed vs volatile sessions
- [[ha-cross-site]] — Active/Passive multi-site topology
- [[distributed-caches]] — Infinispan cache types (sessions, offlineSessions, etc.)
- [[back-channel-logout]] — server-to-server logout (upstream `web:` tier)
- [[rp-initiated-logout]] — RP-Initiated Logout best practice (upstream `web:` tier)
- [[token-revocation]] — token revocation semantics (upstream `web:` tier)

### Upstream / OSS (`web:`)
- web:https://openid.net/specs/openid-connect-frontchannel-1_0.html (OpenID Connect Front-Channel Logout 1.0, fetched 2026-06-18)
- web:https://openid.net/specs/openid-connect-backchannel-1_0.html (OpenID Connect Back-Channel Logout 1.0, fetched 2026-06-18)
- web:https://datatracker.ietf.org/doc/html/rfc7009 (OAuth 2.0 Token Revocation, fetched 2026-06-18)
