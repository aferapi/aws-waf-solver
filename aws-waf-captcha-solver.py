# AwsWafCaptcha: solving AwsWaf

::: tip Create the task with the [createTask](../api-createtask.md) method and get the result with
the [getTaskResult](../api-gettaskresult.md) method.
:::

The task type `types` that we support:

- `AntiAwsWafTask`  this task type require your own proxies.
- `AntiAwsWafTaskProxyLess`  this task type don't require your own proxies.

## Create Task

Create a recognition task with the [createTask](../api-createtask.md) method.

#### Task Object Structure

| Properties     | Type     | Required | Description                                                                                            |
|----------------|----------|----------|--------------------------------------------------------------------------------------------------------|
| type           | String   | Required | `AntiAwsWafTask` <br> `AntiAwsWafTaskProxyLess`                                                        |
| websiteURL     | String   | Required | The URL of the page that returns the  captcha info                                                     |
| awsKey         | Optional | Required | When the status code returned by the websiteURL page is 405, you need to pass in awsKey                |
| awsIv          | Optional | Required | When the status code returned by the websiteURL  page is 405, you need to pass in awsIv                |
| awsContext     | Optional | Required | When the status code returned by the websiteURL  page is 405, you need to pass in awsContext           |
| awsChallengeJS | Optional | Required | When the status code returned by the websiteURL  page is 202, you only need to pass in awsChallengeJs; |
| proxy          | String   | Required | Learn [Using proxies](../api-how-to-use-proxy)                                                         |

::: warning
If the obtained token is not available, it may be because of the ip
please try to use the AntiAwsWafTask mode to pass in your own proxy.
:::

#### Example Request

``` json
POST https://api.capsolver.com/createTask
Host: api.capsolver.com
Content-Type: application/json

{
    "clientKey": "YOUR_API_KEY",
    "task": {
        "type": "AntiAwsWafTask", //Required
        "websiteURL": "https://efw47fpad9.execute-api.us-east-1.amazonaws.com/latest", //Required
        "awsKey": "",
        "awsIv": "",
        "awsContext": "",
        "awsChallengeJS": "",
        "proxy": "http:ip:port:user:pass" // socks5:ip:port:user:pass // Optional
    }
}
```

After you submit the task to us, you should receive in the response a 'Task id' if it's successfull. Please
read [errorCode: full list of errors](../api-createtask.md) if you didn't receive the task id. For more information, you can
also refer to this blog post [How to solve aws amazon captcha token](https://www.capsolver.com/blog/All/how-to-solve-aws-amazon-captcha-token)

#### Example Response

``` json
{
    "errorId": 0,
    "errorCode": "",
    "errorDescription": "",
    "taskId": "61138bb6-19fb-11ec-a9c8-0242ac110006"
}
```

## Getting Results

After you have the taskId, you need to submit the taskId to retrieve the solution. Response structure is explained
in [getTaskResult](../api-gettaskresult.md).

Depending on the system load, you will get the results within the interval of `5s` to `30s`

#### Example Request

``` json
POST https://api.capsolver.com/getTaskResult
Host: api.capsolver.com
Content-Type: application/json

{
    "clientKey": "YOUR_API_KEY",
    "taskId": "61138bb6-19fb-11ec-a9c8-0242ac110006"
}
```

#### Example Response

```json
{
  "errorId": 0,
  "taskId": "646825ef-9547-4a29-9a05-50a6265f9d8a",
  "status": "ready",
  "solution": {
    "cookie": "223d1f60-0e9f-4238-ac0a-e766b15a778e:EQoAf0APpGIKAAAA:AJam3OWpff1VgKIJxH4lGMMHxPVQ0q0R3CNtgcMbR4VvnIBSpgt1Otbax4kuqrgkEp0nFKanO5oPtwt9+Butf7lt0JNe4rZQwZ5IrEnkXvyeZQPaCFshHOISAFLTX7AWHldEXFlZEg7DjIc="
  }
}
```

## Use SDK Request

::: code-group

```python
# pip install --upgrade capsolver
# export CAPSOLVER_API_KEY='...'

import capsolver

# capsolver.api_key = "..."
solution = capsolver.solve({
    "type": "AntiAwsWafTask",
    "websiteURL": "https://efw47fpad9.execute-api.us-east-1.amazonaws.com/latest",
    "proxy": "ip:port:user:pass"
})
```

```go [golang]
package main

import (
	"fmt"
	capsolver_go "github.com/capsolver/capsolver-go"
	"log"
)

func main() {
	// first you need to install sdk
	//go get github.com/capsolver/capsolver-go
	//export CAPSOLVER_API_KEY='...' or
	//capSolver := CapSolver{ApiKey:"..."}

	capSolver := capsolver_go.CapSolver{}
	solution, err := capSolver.Solve(map[string]any{
		"type": "AntiAwsWafTaskProxyLess",
		"websiteURL": "AntiAwsWafTask",
		 "proxy":"ip:port:user:pass"
	})
	if err != nil {
		log.Fatal(err)
		return
	}
	fmt.Println(solution)
}

```
