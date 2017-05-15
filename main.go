package main

import (
	"flag"
	"github.com/laincloud/entry/server"
)

func main() {
	//server.StartServer("8888", "unix:///var/run/docker.sock")
	var port string
	flag.StringVar(&port,"port","8888","http listen port")
	flag.Parse()
	server.StartServer(port,"unix:///var/run/docker.sock")
}
