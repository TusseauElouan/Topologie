"""TP1 models for L2/L3 switching and routing."""

from dataclasses import dataclass
from ipaddress import ip_address, ip_network
from typing import Dict, Optional


@dataclass
class IPPacket:
    source_ip: str
    destination_ip: str
    protocol: str = "TCP"
    ttl: int = 64
    payload: object = None

    def decrement_ttl(self) -> int:
        if self.ttl > 0:
            self.ttl -= 1
        return self.ttl


@dataclass
class EthernetFrame:
    source_mac: str
    destination_mac: str
    ether_type: str = "0x0800"
    payload: object = None


def _longest_prefix_match(destination_ip: str, table: Dict[str, str]) -> Optional[str]:
    ip_obj = ip_address(destination_ip)
    best_hop = None
    best_prefix_length = -1

    for prefix, hop in table.items():
        network = ip_network(prefix, strict=False)
        if ip_obj in network and network.prefixlen > best_prefix_length:
            best_prefix_length = network.prefixlen
            best_hop = hop

    return best_hop


class L2Switch:
    """Layer 2 switch with MAC learning and frame forwarding."""

    def __init__(self) -> None:
        self.mac_table: Dict[str, str] = {}

    def learn_mac(self, source_mac: str, ingress_port: str) -> None:
        self.mac_table[source_mac] = ingress_port

    def lookup_port(self, destination_mac: str) -> Optional[str]:
        return self.mac_table.get(destination_mac)

    def forward_frame(self, frame: EthernetFrame, ingress_port: str) -> str:
        self.learn_mac(frame.source_mac, ingress_port)
        egress_port = self.lookup_port(frame.destination_mac)
        if egress_port and egress_port != ingress_port:
            return f"unicast:{egress_port}"
        return "flood"


class L3Switch(L2Switch):
    """
    Layer 3 switch extends L2 behavior.
    Same method name (`forward_frame`) is specialized:
    - L2 behavior for non-IP payload.
    - L3 routing behavior for IP payload.
    """

    def __init__(self) -> None:
        super().__init__()
        self.routing_table: Dict[str, str] = {}

    def add_route(self, prefix: str, next_hop: str) -> None:
        self.routing_table[prefix] = next_hop

    def route_packet(self, packet: IPPacket) -> Optional[str]:
        return _longest_prefix_match(packet.destination_ip, self.routing_table)

    def forward_frame(self, frame: EthernetFrame, ingress_port: str) -> str:
        self.learn_mac(frame.source_mac, ingress_port)
        if isinstance(frame.payload, IPPacket):
            frame.payload.decrement_ttl()
            next_hop = self.route_packet(frame.payload)
            if next_hop:
                return f"routed:{next_hop}"
            return "drop:no-route"
        return super().forward_frame(frame, ingress_port)


class Router:
    """Router with connected networks and static routes."""

    def __init__(self) -> None:
        self.interfaces: Dict[str, str] = {}
        self.routing_table: Dict[str, str] = {}

    def add_interface(self, name: str, network_cidr: str) -> None:
        self.interfaces[name] = network_cidr

    def add_route(self, prefix: str, next_hop: str) -> None:
        self.routing_table[prefix] = next_hop

    def route_packet(self, packet: IPPacket) -> Optional[str]:
        packet.decrement_ttl()
        destination = ip_address(packet.destination_ip)

        for interface_name, network_cidr in self.interfaces.items():
            if destination in ip_network(network_cidr, strict=False):
                return f"connected:{interface_name}"

        next_hop = _longest_prefix_match(packet.destination_ip, self.routing_table)
        if next_hop:
            return f"next-hop:{next_hop}"
        return None

