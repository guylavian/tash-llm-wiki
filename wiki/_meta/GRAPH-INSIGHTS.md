# Wiki Graph — Insight View

Visual companion to `python3 -m wikikb insights`. Hand-rendered (Opus 4.8) from the
deterministic `insights --json` snapshot — **261 pages · 1357 page↔page links**. Renders in
Obsidian and GitHub. Regenerate the numbers with `insights --json`; redraw when the shape shifts.

---

## 1. Community / domain map

Clusters from deterministic label propagation, sized by page count, grouped by `domain:`. Box = a
community's anchor page; `N pages` = community size. The four domains barely touch — the wiki is
four near-disjoint brains sharing one vault.

```mermaid
flowchart LR
  subgraph KC["keycloak · 800 ref-notes, 86 cited (10.8%)"]
    direction TB
    KC1["3scale-rhsso-support<br/><b>87 pages</b>"]
    KC2["access-token-validation-resource-server<br/><b>48 pages</b>"]
    KC3["additional-options · 15"]
    KC4["authorization-permissions · 12"]
    KC5["custom-provider-migration · 9"]
  end
  subgraph AD["active-directory · 221 ref-notes, 101 cited (45.7%)"]
    AD1["active-directory-implementation-review<br/><b>69 pages</b>"]
  end
  subgraph IOS["cisco-ios-xe · conceptual (notes-first)"]
    IOS1["bgp<br/><b>15 pages</b>"]
  end
  subgraph OCP["openshift · 3813 ref-notes, 31 cited (0.8%)"]
    OCP1["kubernetes-pod<br/><b>6 pages</b>"]
  end

  classDef kc fill:#fde2e2,stroke:#c0392b;
  classDef ad fill:#e2ecfd,stroke:#2c5fb3;
  classDef ios fill:#e9fde2,stroke:#3a8c2c;
  classDef ocp fill:#f3e2fd,stroke:#7d3ac0;
  class KC1,KC2,KC3,KC4,KC5 kc;
  class AD1 ad;
  class IOS1 ios;
  class OCP1 ocp;
```

**Read:** keycloak dominates (5 communities, ~171 pages) and is well-cited; **openshift is the
gap** — 6 synthesis pages over a 3,813-note corpus (0.8% cited). That sparse OCP box is ROADMAP #1.

---

## 2. Suggested links — what the graph thinks *should* connect

Non-adjacent page pairs with high Adamic-Adar score (shared neighbors) that aren't linked yet. All
remaining suggestions sit inside the keycloak token/OIDC cluster. Each edge = a suggested link,
labelled with its score. `spa-resource-server-implementation-review` is a **wanted page** (dashed,
not yet written) —
two strong suggestions point at it, so it's the next page worth creating.

```mermaid
flowchart TB
  sas["securing-apps-oidc-saml"]
  ti["token-introspection"]
  pkce["pkce"]
  tsb["token-storage-browser"]
  otv["oidc-token-validation"]
  trev["token-revocation"]
  ocbp["oidc-client-best-practices"]
  rtr["refresh-token-rotation"]
  cam["client-authentication-methods"]
  ogt["oidc-grant-types"]
  sir["sso-implementation-review"]
  btu["bearer-token-usage"]
  san["state-and-nonce"]
  nao["native-app-oauth"]
  mbt["mtls-bound-tokens"]
  spa(["spa-resource-server-implementation-review<br/><i>wanted — write me</i>"])

  sas ---|6.15| ti
  pkce ---|5.59| sas
  sas ---|5.55| tsb
  nao ---|5.54| spa
  otv ---|5.51| trev
  ocbp ---|5.46| rtr
  mbt ---|5.43| spa
  cam ---|5.36| otv
  ogt ---|5.33| sir
  btu ---|5.31| san
  cam ---|5.23| sir
  ogt ---|5.04| otv

  classDef ghost fill:#eee,stroke:#999,stroke-dasharray:4 3,color:#666;
  class spa ghost;
```

**Read:** `securing-apps-oidc-saml`, `oidc-token-validation`, and `client-authentication-methods`
are the hubs the graph wants more wired. Writing `spa-resource-server-implementation-review` would
absorb two of the strongest open suggestions.

---

## 3. Knowledge-gap ledger (synthesis ↔ corpus citation coverage)

```mermaid
flowchart LR
  AD["active-directory<br/>221 notes"] --> ADc["101 cited<br/><b>45.7%</b> ✅"]
  KC["keycloak<br/>800 notes"] --> KCc["86 cited<br/><b>10.8%</b> 🟡"]
  OCP["openshift<br/>3813 notes"] --> OCPc["31 cited<br/><b>0.8%</b> 🔴"]
  classDef good fill:#e9fde2,stroke:#3a8c2c;
  classDef mid fill:#fdf6e2,stroke:#b3962c;
  classDef bad fill:#fde2e2,stroke:#c0392b;
  class ADc good;
  class KCc mid;
  class OCPc bad;
```

Citation % = fraction of a domain's immutable `reference/<domain>/` corpus that at least one
synthesis page links. Low % = unused ground truth, i.e. the "what to write next" surface. openshift
is the headline gap (ROADMAP #1: recite the 6 synthesis pages against the corpus → `kb:` tokens →
`crosslink --apply` lights up CITES edges).
