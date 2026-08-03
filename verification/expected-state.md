# Expected operational state

This document defines success before any troubleshooting begins.

## BGP underlay

| Check | Expected result |
|---|---|
| CE-A session | `Established` with peer AS 65010 |
| CE-B session | `Established` with peer AS 65020 |
| OTT-PE-01 accepted customer prefix | 198.51.100.10/32 only |
| TOR-PE-01 accepted customer prefix | 198.51.100.20/32 only |
| Unexpected default route | Absent |

## MPLS transport

| Check | Expected result |
|---|---|
| IS-IS adjacency across each core link | Up |
| PE-to-PE loopback reachability | Present through the IGP |
| LDP session across each enabled core adjacency | Operational |
| Transport label for remote PE loopback | Present |
| MPLS forwarding entry | Resolves through the intended core path |

## L3VPN service

| Check | Expected result |
|---|---|
| MP-BGP VPN session to route reflector | Established |
| Remote VPN route in `bgp.l3vpn.0` | Present with expected RD and route target |
| Remote route imported into `BLUE.inet.0` | Present |
| Route leaking into the default table | Absent |
| CE-A to CE-B service reachability | Successful in the isolated lab |

## EVPN service

| Check | Expected result |
|---|---|
| EVPN family negotiated | Yes |
| Local endpoint advertisement | Present in `bgp.evpn.0` |
| Remote endpoint installation | Present on the opposite PE |
| Service/VNI state | Up and consistently mapped |
| Unrelated service import | Absent |

## Evidence format

For every test, capture:

1. Timestamp and lab software version
2. Node and routing instance
3. Command executed
4. Relevant output only
5. Pass/fail result
6. Explanation of any deviation

Defining expected state first prevents troubleshooting from becoming a sequence of unverified guesses.
