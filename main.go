package main

import (

	"github.com/laincloud/entry/server"
)

func main() {
	server.StartServer("8888", "unix:///var/run/docker.sock")
}
