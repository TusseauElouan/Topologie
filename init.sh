#!/bin/bash

set -euo pipefail

create_architecture() {
    local topo=$1

    mkdir -p $topo/switches/access/marketing/interfaces
    mkdir -p $topo/switches/access/direction/interfaces
    mkdir -p $topo/switches/access/it/interfaces
    mkdir -p $topo/switches/backbone/interfaces/switches
    mkdir -p $topo/
    mkdir -p $topo/routers/active
    mkdir -p $topo/hosts
}

create_architecture $1