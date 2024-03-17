# HTTP requests
LPM has a script in `src/lpm/http.loza` that can send HTTP requests to a URL.

```bash
import_once 'src/lpm/http.loza'

println lpm.http.req('https://github.com')->read()->decode()
```

Function `lpm.http.req` arguments:
- `url`: The URL
- `method`: The HTTP method (default is `GET`)
- `data`: The request payload
- `headers`: The request headers as `dict`

Output of the function is a Python `HTTPResponse` object.
Basicaly you can see this example for getting status code and response text:

```bash
$res = lpm.http.req('https://github.com')
println $res->getcode()
println $res->read()->decode() # (you should decode the output)
```

The response object is a file-like object. means you can download the response partially:

```bash
println $res->read(1024)->decode()
# ...
```
