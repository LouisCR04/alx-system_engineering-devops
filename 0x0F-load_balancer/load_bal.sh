#!/usr/bin/env bash
# Installs & configures HAproxy as required

sudo apt update
sudo apt-get install -y --no-install-recommends software-properties-common
sudo add-apt-repository ppa:vbernat/haproxy-2.8 -y
sudo apt update
sudo apt install -y haproxy=2.8.\*

hgproxy_conf_file="/etc/haproxy/haproxy.cfg"

# Configure Load Balancer
fname="frontend http"
fbind="bind *:80"
fmode="mode http"
fdefault="default_backend web-backend"
frontend="$fname\n\t$fbind\n\t$fmode\n\t$fdefault\n"

bname="backend web-backend"
bbalance="balance roundrobin"
bserver1="server 448362-web-01 54.90.41.29:80 check"
bserver2="server 448362-web-02 54.88.199.223:80 check"
backend="$bname\n\t$bbalance\n\t$bserver1\n\t$bserver2"

sudo sed -i "$ a $frontend" $hgproxy_conf_file
sudo sed -i "$ a $backend" $hgproxy_conf_file
echo "ENABLED=1" | sudo tee -a /etc/default/haproxy

sudo service haproxy restart
