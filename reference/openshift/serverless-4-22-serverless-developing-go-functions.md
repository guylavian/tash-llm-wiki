---
title: "Developing Go functions"
type: reference
domain: openshift
slug: serverless-4-22-serverless-developing-go-functions
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-developing-go-functions
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Developing Go functions

[id="serverless-developing-go-functions"]
= Developing Go functions

After you have created a Go function project, you can modify the template files provided to add business logic to your function. This includes configuring function invocation and the returned headers and status codes.

[id="prerequisites_serverless-developing-go-functions"]
== Prerequisites

* Before you can develop functions, you must complete the steps in Setting up {FunctionsProductName}.

// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-go-functions.adoc

[id="serverless-go-template_{context}"]
= Go function template structure

When you create a Go function using the Knative (`kn`) CLI, the project directory looks like a typical Go project. The only exception is the additional `func.yaml` configuration file, which is used for specifying the image.

Go functions have few restrictions. The only requirements are that your project must be defined in a `function` module, and must export the function `Handle()`.

Both `http` and `event` trigger functions have the same template structure:

.Template structure
[source,terminal]
----
fn
├── README.md
├── func.yaml <1>
├── go.mod <2>
├── go.sum
├── handle.go
└── handle_test.go
----
<1> The `func.yaml` configuration file is used to determine the image name and registry.
<2> You can add any required dependencies to the `go.mod` file, which can include additional local Go files. When the project is built for deployment, these dependencies are included in the resulting runtime container image.
+
.Example of adding dependencies
[source,terminal]
----
$ go get gopkg.in/yaml.v2@v2.4.0
----

[id="serverless-developing-go-functions-about-invoking"]
== About invoking Go functions

When using the Knative (`kn`) CLI to create a function project, you can generate a project that responds to CloudEvents, or one that responds to simple HTTP requests. Go functions are invoked by using different methods, depending on whether they are triggered by an HTTP request or a CloudEvent.

// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-go-functions.adoc

[id="serverless-invoking-go-functions-http_{context}"]
= Functions triggered by an HTTP request

When an incoming HTTP request is received, functions are invoked with a standard Go Context as the first parameter, followed by the `http.ResponseWriter` and `http.Request` parameters. You can use standard Go techniques to access the request, and set a corresponding HTTP response for your function.

.Example HTTP response
[source,go]
----
func Handle(ctx context.Context, res http.ResponseWriter, req *http.Request) {
  // Read body
  body, err := ioutil.ReadAll(req.Body)
  defer req.Body.Close()
  if err != nil {
	http.Error(res, err.Error(), 500)
	return
  }
  // Process body and function logic
  // ...
}
----
// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-go-functions.adoc

[id="serverless-invoking-go-functions-cloudevent_{context}"]
= Functions triggered by a cloud event

When an incoming cloud event is received, the event is invoked by the CloudEvents Go SDK. The invocation uses the `Event` type as a parameter.

You can leverage the Go Context as an optional parameter in the function contract, as shown in the list of supported function signatures:

.Supported function signatures
[source,go]
----
Handle()
Handle() error
Handle(context.Context)
Handle(context.Context) error
Handle(cloudevents.Event)
Handle(cloudevents.Event) error
Handle(context.Context, cloudevents.Event)
Handle(context.Context, cloudevents.Event) error
Handle(cloudevents.Event) *cloudevents.Event
Handle(cloudevents.Event) (*cloudevents.Event, error)
Handle(context.Context, cloudevents.Event) *cloudevents.Event
Handle(context.Context, cloudevents.Event) (*cloudevents.Event, error)
----

[id="serverless-invoking-go-functions-cloudevent-example_{context}"]
== CloudEvent trigger example

A cloud event is received which contains a JSON string in the data property:

[source,json]
----
{
  "customerId": "0123456",
  "productId": "6543210"
}
----

To access this data, a structure must be defined which maps properties in the cloud event data, and retrieves the data from the incoming event. The following example uses the `Purchase` structure:

[source,go]
----
type Purchase struct {
  CustomerId string `json:"customerId"`
  ProductId  string `json:"productId"`
}
func Handle(ctx context.Context, event cloudevents.Event) (err error) {

  purchase := &Purchase{}
  if err = event.DataAs(purchase); err != nil {
	fmt.Fprintf(os.Stderr, "failed to parse incoming CloudEvent %s\n", err)
	return
  }
  // ...
}
----

Alternatively, a Go `encoding/json` package could be used to access the cloud event directly as JSON in the form of a bytes array:

[source,go]
----
func Handle(ctx context.Context, event cloudevents.Event) {
  bytes, err := json.Marshal(event)
  // ...
}
----

// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-go-functions.adoc

[id="serverless-go-function-return-values_{context}"]
= Go function return values

Functions triggered by HTTP requests can set the response directly. You can configure the function to do this by using the Go http.ResponseWriter.

.Example HTTP response
[source,go]
----
func Handle(ctx context.Context, res http.ResponseWriter, req *http.Request) {
  // Set response
  res.Header().Add("Content-Type", "text/plain")
  res.Header().Add("Content-Length", "3")
  res.WriteHeader(200)
  _, err := fmt.Fprintf(res, "OK\n")
  if err != nil {
	fmt.Fprintf(os.Stderr, "error or response write: %v", err)
  }
}
----

Functions triggered by a cloud event might return nothing, `error`, or `CloudEvent` in order to push events into the Knative Eventing system. In this case, you must set a unique `ID`, proper `Source`, and a `Type` for the cloud event. The data can be populated from a defined structure, or from a `map`.

.Example CloudEvent response
[source,go]
----
func Handle(ctx context.Context, event cloudevents.Event) (resp *cloudevents.Event, err error) {
  // ...
  response := cloudevents.NewEvent()
  response.SetID("example-uuid-32943bac6fea")
  response.SetSource("purchase/getter")
  response.SetType("purchase")
  // Set the data from Purchase type
  response.SetData(cloudevents.ApplicationJSON, Purchase{
	CustomerId: custId,
	ProductId:  prodId,
  })
  // OR set the data directly from map
  response.SetData(cloudevents.ApplicationJSON, map[string]string{"customerId": custId, "productId": prodId})
  // Validate the response
  resp = &response
  if err = resp.Validate(); err != nil {
	fmt.Printf("invalid event created. %v", err)
  }
  return
}
----
// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-typescript-functions.adoc

[id="serverless-testing-go-functions_{context}"]
= Testing Go functions

Go functions can be tested locally on your computer. In the default project that is created when you create a function using `kn func create`, there is a `handle_test.go` file, which contains some basic tests. These tests can be extended as needed.

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
$ go test
----

[id="next-steps_serverless-developing-go-functions"]
== Next steps

* Build and deploy a function.
