---
title: "Developing Node.js functions"
type: reference
domain: openshift
slug: serverless-4-22-serverless-developing-nodejs-functions
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-developing-nodejs-functions
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Developing Node.js functions

[id="serverless-developing-nodejs-functions"]
= Developing Node.js functions

After you have created a Node.js function project, you can modify the template files provided to add business logic to your function. This includes configuring function invocation and the returned headers and status codes.

[id="prerequisites_serverless-developing-nodejs-functions"]
== Prerequisites

* Before you can develop functions, you must complete the steps in Setting up {FunctionsProductName}.

// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-nodejs-functions.adoc

[id="serverless-nodejs-template_{context}"]
= Node.js function template structure

When you create a Node.js function using the Knative (`kn`) CLI, the project directory looks like a typical Node.js project. The only exception is the additional `func.yaml` file, which is used to configure the function.

Both `http` and `event` trigger functions have the same template structure:

.Template structure
[source,terminal]
----
.
├── func.yaml <1>
├── index.js <2>
├── package.json <3>
├── README.md
└── test <4>
    ├── integration.js
    └── unit.js
----
<1> The `func.yaml` configuration file is used to determine the image name and registry.
<2> Your project must contain an `index.js` file which exports a single function.
<3> You are not restricted to the dependencies provided in the template `package.json` file. You can add additional dependencies as you would in any other Node.js project.
+
.Example of adding npm dependencies
[source,terminal]
----
npm install --save opossum
----
+
When the project is built for deployment, these dependencies are included in the created runtime container image.
<4> Integration and unit test scripts are provided as part of the function template.

[id="serverless-developing-nodejs-functions-about-invoking"]
== About invoking Node.js functions

When using the Knative (`kn`) CLI to create a function project, you can generate a project that responds to CloudEvents, or one that responds to simple HTTP requests. CloudEvents in Knative are transported over HTTP as a POST request, so both function types listen for and respond to incoming HTTP events.

Node.js functions can be invoked with a simple HTTP request. When an incoming request is received, functions are invoked with a `context` object as the first parameter.

// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-nodejs-functions.adoc

[id="serverless-nodejs-functions-context-objects_{context}"]
= Node.js context objects

Functions are invoked by providing a `context` object as the first parameter. This object provides access to the incoming HTTP request information.

.Example context object
[source,javascript]
----
function handle(context, data)
----

This information includes the HTTP request method, any query strings or headers sent with the request, the HTTP version, and the request body. Incoming requests that contain a `CloudEvent` attach the incoming instance of the CloudEvent to the context object so that it can be accessed by using `context.cloudevent`.

[id="serverless-nodejs-functions-context-objects-methods_{context}"]
== Context object methods

The `context` object has a single method, `cloudEventResponse()`, that accepts a data value and returns a CloudEvent.

In a Knative system, if a function deployed as a service is invoked by an event broker sending a CloudEvent, the broker examines the response. If the response is a CloudEvent, this event is handled by the broker.

.Example context object method
[source,javascript]
----
// Expects to receive a CloudEvent with customer data
function handle(context, customer) {
  // process the customer
  const processed = handle(customer);
  return context.cloudEventResponse(customer)
    .source('/handle')
    .type('fn.process.customer')
    .response();
}
----

[id="serverless-nodejs-functions-context-objects-cloudevent-data_{context}"]
== CloudEvent data

If the incoming request is a CloudEvent, any data associated with the CloudEvent is extracted from the event and provided as a second parameter. For example, if a CloudEvent is received that contains a JSON string in its data property that is similar to the following:

[source,json]
----
{
  "customerId": "0123456",
  "productId": "6543210"
}
----

When invoked, the second parameter to the function, after the `context` object, will be a JavaScript object that has `customerId` and `productId` properties.

.Example signature
[source,javascript]
----
function handle(context, data)
----

The `data` parameter in this example is a JavaScript object that contains the `customerId` and `productId` properties.
// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-nodejs-functions.adoc

[id="serverless-nodejs-function-return-values_{context}"]
= Node.js function return values

Functions can return any valid JavaScript type or can have no return value. When a function has no return value specified, and no failure is indicated, the caller receives a `204 No Content` response.

Functions can also return a CloudEvent or a `Message` object in order to push events into the Knative Eventing system. In this case, the developer is not required to understand or implement the CloudEvent messaging specification. Headers and other relevant information from the returned values are extracted and sent with the response.

.Example
[source,javascript]
----
function handle(context, customer) {
  // process customer and return a new CloudEvent
  return new CloudEvent({
    source: 'customer.processor',
    type: 'customer.processed'
  })
}
----

[id="serverless-nodejs-function-return-values-headers_{context}"]
== Returning headers

You can set a response header by adding a `headers` property to the `return` object. These headers are extracted and sent with the response to the caller.

.Example response header
[source,javascript]
----
function handle(context, customer) {
  // process customer and return custom headers
  // the response will be '204 No content'
  return { headers: { customerid: customer.id } };
}
----

[id="serverless-nodejs-function-return-values-status-codes_{context}"]
== Returning status codes

You can set a status code that is returned to the caller by adding a `statusCode` property to the `return` object:

.Example status code
[source,javascript]
----
function handle(context, customer) {
  // process customer
  if (customer.restricted) {
    return { statusCode: 451 }
  }
}
----

Status codes can also be set for errors that are created and thrown by the function:

.Example error status code
[source,javascript]
----
function handle(context, customer) {
  // process customer
  if (customer.restricted) {
    const err = new Error(‘Unavailable for legal reasons’);
    err.statusCode = 451;
    throw err;
  }
}
----
// Module included in the following assemblies
//
// * /serverless/functions/serverless-developing-nodejs-functions.adoc

[id="serverless-testing-nodejs-functions_{context}"]
= Testing Node.js functions

Node.js functions can be tested locally on your computer. In the default project that is created when you create a function by using `kn func create`, there is a *test* folder that contains some simple unit and integration tests.

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on the cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a function by using `kn func create`.

.Procedure

. Navigate to the *test* folder for your function.
. Run the tests:
+
[source,terminal]
----
$ npm test
----

[id="next-steps_serverless-developing-nodejs-functions"]
== Next steps

* See the Node.js context object reference documentation.
* Build and deploy a function.
