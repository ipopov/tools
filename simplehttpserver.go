// $ go build simplehttpserver.go
// $ ./simplehttpserver --port 8080
package main

import (
       "flag"
       "fmt"
       "log"
       "net/http"
)

func main() {
     port := flag.Int("port", 8080, "")
     flag.Parse()

     host_port := fmt.Sprintf(":%d", *port)
     log.Printf("serving on %s...", host_port)
     http.ListenAndServe(host_port, http.FileServer(http.Dir(".")))
}
