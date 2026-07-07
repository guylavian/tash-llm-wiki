---
title: "Chapter 4. Themes based on React - Red Hat build of Keycloak 26.2 Server Developer Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-theme-react
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/server_developer_guide/theme_react
guide: server_developer_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "The admin console and account console are based on React. To fully customize these you can use the React based npm packages. There are two packages: @keycloak/keycloak-admin-ui: This is the base theme for the admin console. @keycloak/keycloak-account-ui: This is the base theme for the account console. Both packages are available on npm. 4.1. Installing the packages To install the packages, run the…"
---

# Chapter 4. Themes based on React - Red Hat build of Keycloak 26.2 Server Developer Guide

Chapter 4. Themes based on React
The admin console and account console are based on React. To fully customize these you can use the React based npm packages. There are two packages:
-
@keycloak/keycloak-admin-ui
: This is the base theme for the admin console. -
@keycloak/keycloak-account-ui
: This is the base theme for the account console.
Both packages are available on npm.
4.1. Installing the packages
To install the packages, run the following command:
pnpm install @keycloak/keycloak-account-ui
4.2. Using the packages
To use these pages you’ll need to add KeycloakProvider in your component hierarchy to setup what client, realm and url to use.
import { KeycloakProvider } from "@keycloak/keycloak-ui-shared";
//...
<KeycloakProvider environment={{
serverBaseUrl: "http://localhost:8080",
realm: "master",
clientId: "security-admin-console"
}}>
{/* rest of your application */}
</KeycloakProvider>
4.3. Translating the pages
The pages are translated using the i18next
library. You can set it up as described on their [website](https://react.i18next.com/). If you want to use the translations that are provided then you need to add i18next-fetch-backend
to your project and add:
backend: {
loadPath: `http://localhost:8080/resources/master/account/{lng}}`,
parse: (data: string) => {
const messages = JSON.parse(data);
return Object.fromEntries(
messages.map(({ key, value }) => [key, value])
);
},
},
4.4. Using the pages
All "pages" are React components that can be used in your application. To see what components are available, see the [source](https://github.com/keycloak/keycloak/blob/main/js/apps/account-ui/src/index.ts). Or have a look at the [quick start](https://github.com/keycloak/keycloak-quickstarts/tree/main/extension/extend-account-console-node) to see how to use them.
4.5. Theme selector
By default the theme configured for the realm is used, with the exception of clients being able to override the login theme. This behavior can be changed through the Theme Selector SPI.
This could be used to select different themes for desktop and mobile devices by looking at the user agent header, for example.
To create a custom theme selector you need to implement ThemeSelectorProviderFactory
and ThemeSelectorProvider
.
4.6. Theme resources
When implementing custom providers in Red Hat build of Keycloak there may often be a need to add additional templates, resources and messages bundles.
The easiest way to load additional theme resources is to create a JAR with templates in theme-resources/templates
resources in theme-resources/resources
and messages bundles in theme-resources/messages
.
If you want a more flexible way to load templates and resources that can be achieved through the ThemeResourceSPI. By implementing ThemeResourceProviderFactory
and ThemeResourceProvider
you can decide exactly how to load templates and resources.
4.7. Locale selector
By default, the locale is selected using the DefaultLocaleSelectorProvider
which implements the LocaleSelectorProvider
interface. English is the default language when internationalization is disabled.
With internationalization enabled, the locale is resolved according to the logic described in the Server Administration Guide.
This behavior can be changed through the LocaleSelectorSPI
by implementing the LocaleSelectorProvider
and LocaleSelectorProviderFactory
.
The LocaleSelectorProvider
interface has a single method, resolveLocale
, which must return a locale given a RealmModel
and a nullable UserModel
. The actual request is available from the KeycloakSession#getContext
method.
Custom implementations can extend the DefaultLocaleSelectorProvider
in order to reuse parts of the default behavior. For example to ignore the Accept-Language
request header, a custom implementation could extend the default provider, override it’s getAcceptLanguageHeaderLocale
, and return a null value. As a result the locale selection will fall back on the realm’s default language.
