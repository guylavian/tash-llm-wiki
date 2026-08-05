# Raw note — Active Directory Certificate Services (AD CS)

- Source: Microsoft Learn, "What is the Certification Authority Role Service?",
  "Certificate templates concepts", "Certificate Enrollment Policy Web Service
  overview", "Certificates and trust in Windows", "TPM key attestation"
  (web:https://learn.microsoft.com/windows-server/identity/ad-cs/, distilled from the
  *windows-server identity* PDF export, fetched 2026-06-18).
- Status: notes-first ground truth (paraphrased — no verbatim) for the
  `active-directory` domain. AD CS is the in-scope `ad-certificate-services` area.

## What it is

AD CS is the Windows Server PKI role. A **certification authority (CA)** attests to
the identity of users/computers/orgs by issuing digitally signed certificates, and
manages, revokes, and renews them. Installing the **Certification Authority role
service** turns a Windows server into a CA.

## CA types (two axes)

**Enterprise vs Standalone:**
- **Enterprise CA** — integrated with AD DS; publishes certs and CRLs to AD; uses AD
  accounts/groups to approve requests; **uses certificate templates**; supports
  **autoenrollment** and automatic approval; required for **smartcard sign-in**
  (maps smartcard certs to AD accounts).
- **Standalone CA** — no AD dependency, **no templates**; all request info must be in
  the request itself; requests sit in a **pending queue** for admin approval by
  default. Use when there's no AD or for an **offline root**.

**Root vs Subordinate:**
- **Root CA** — top of the hierarchy; self-signed (Subject = Issuer); trusted
  unconditionally once its cert is present on clients. If compromised, the whole
  hierarchy is compromised → keep it **offline** (Offline Root CA).
- **Subordinate CA** — gets its cert from a parent; an **intermediate / policy CA**
  separates classes of certs (assurance level, geography) and can be online or
  offline; **issuing CAs** sit at the bottom and serve end entities.

## Private key protection

The CA private key is part of its identity. Protect with a **hardware security
module (HSM)** — a dedicated device exposed via CryptoAPI/CSP that stores keys and
accelerates crypto; one network HSM can be shared across CAs. Without an HSM the key
sits on the CA computer. Offline CAs stay disconnected and physically secured;
issuing CAs must keep the key online to sign.

## Certificate templates

Templates are the **rules/settings applied to incoming requests** on an Enterprise
CA — they preconfigure certs for a task and tell the client how to build a valid
request. **Only an Enterprise CA issues from templates.** Templates are stored in
**AD DS**, so every CA in the forest shares the current template (consistent policy
forest-wide). Managed via the Certificate Templates snap-in (copy/modify, set
read/enroll permissions). Managing templates needs Domain Admins (or equivalent).

## Enrollment off the corporate network

- **Certificate Enrollment Policy Web Service (CEP)** + **Certificate Enrollment Web
  Service (CES)** give policy-based autoenrollment to non-domain or off-network
  machines, over HTTPS using WS-Trust. CEP talks to AD over LDAP/LDAPS (TCP 389/636);
  runs as the IIS DefaultAppPool identity by default.
- **Key-based renewal** — an existing valid cert authenticates its own renewal
  request, enabling auto-renew for off-network machines. Requires username/password
  or client-cert auth (no anonymous); in key-based-renewal mode CEP won't accept
  *new* cert requests. Both services need a **Server Authentication** SSL cert.

## Certificates and trust in Windows

Windows decides whether a PKI chain is trustworthy using **certificate trust lists
(CTLs)** — a Trusted CTL and an Untrusted CTL (publicly-known-fraudulent roots),
delivered by the **Microsoft Root Certificate Program**. The **CTL Updater**
downloads them daily from Windows Update (`ctldl.windowsupdate.com`); CTLs are cached
under `HKLM\SOFTWARE\Microsoft\SystemCertificates\AuthRoot\AutoUpdate`. In
disconnected environments you can redirect updates to an internal share (Group
Policy / `certutil -syncWithWU`) and curate your own trusted roots
(`certutil -generateSSTFromWU`, distribute by Group Policy). Disabling auto-update is
possible but not recommended.

## TPM key attestation

Lets the CA cryptographically verify that the requested key is **protected by a
TPM** the CA trusts — raising assurance that the key can't be exported. Configured on
the certificate template (Required / Preferred). Constraints: **RSA keys only**, not
supported on a **standalone CA**, not for third-party smartcard KSPs, no
non-persistent processing.

## Symptoms / caveats (feed the review MOC)

- Smartcard sign-in or autoenrollment expected but unavailable → CA is **standalone**,
  not **enterprise** (both need AD integration + templates).
- Off-network auto-renew fails → CEP/CES not configured, anonymous auth attempted,
  or missing Server-Authentication SSL cert.
- Root CA compromise = entire hierarchy compromised → keep root **offline**.
