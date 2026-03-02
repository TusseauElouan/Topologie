from tp1_switch_router.python.network_devices import (
    EthernetFrame,
    IPPacket,
    L2Switch,
    L3Switch,
    Router,
)


def test_l2_switch_floods_unknown_destination() -> None:
    switch = L2Switch()
    frame = EthernetFrame(source_mac="aa:aa:aa:aa:aa:01", destination_mac="bb:bb:bb:bb:bb:01")
    assert switch.forward_frame(frame, ingress_port="Fa0/1") == "flood"


def test_l2_switch_unicasts_when_destination_is_known() -> None:
    switch = L2Switch()
    switch.learn_mac("bb:bb:bb:bb:bb:01", "Fa0/2")
    frame = EthernetFrame(source_mac="aa:aa:aa:aa:aa:01", destination_mac="bb:bb:bb:bb:bb:01")
    assert switch.forward_frame(frame, ingress_port="Fa0/1") == "unicast:Fa0/2"


def test_l3_switch_routes_ip_packet_and_decrements_ttl() -> None:
    switch = L3Switch()
    switch.add_route("192.168.20.0/24", "192.168.1.254")

    packet = IPPacket(source_ip="192.168.10.10", destination_ip="192.168.20.10", ttl=8)
    frame = EthernetFrame(
        source_mac="aa:aa:aa:aa:aa:01",
        destination_mac="bb:bb:bb:bb:bb:01",
        payload=packet,
    )

    assert switch.forward_frame(frame, ingress_port="Gi0/1") == "routed:192.168.1.254"
    assert packet.ttl == 7


def test_l3_switch_drops_ip_packet_without_route() -> None:
    switch = L3Switch()
    packet = IPPacket(source_ip="192.168.10.10", destination_ip="10.10.10.1")
    frame = EthernetFrame(
        source_mac="aa:aa:aa:aa:aa:01",
        destination_mac="bb:bb:bb:bb:bb:01",
        payload=packet,
    )
    assert switch.forward_frame(frame, ingress_port="Gi0/1") == "drop:no-route"


def test_router_prefers_connected_network_then_static_route() -> None:
    router = Router()
    router.add_interface("Gi0/0", "192.168.20.0/24")
    router.add_route("0.0.0.0/0", "200.10.0.1")

    connected_packet = IPPacket(source_ip="10.0.0.2", destination_ip="192.168.20.99")
    internet_packet = IPPacket(source_ip="10.0.0.2", destination_ip="8.8.8.8")

    assert router.route_packet(connected_packet) == "connected:Gi0/0"
    assert router.route_packet(internet_packet) == "next-hop:200.10.0.1"

