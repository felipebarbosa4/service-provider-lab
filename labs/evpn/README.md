# Lab 3: EVPN control-plane validation

## Objective

Build a small EVPN fabric and verify that MAC and IP reachability are distributed through BGP rather than learned only through flooding.

## Scope

This lab focuses on control-plane reasoning and verification. The exact encapsulation and platform-specific configuration must be adapted to the Junos image and feature set used in the lab.

## Success criteria

- Underlay reachability exists between VTEP loopbacks.
- EVPN BGP sessions are established with the required family enabled.
- The intended VNI or service identifier is operational.
- Local MAC addresses are advertised as EVPN routes.
- Remote MAC/IP information is installed on the opposite PE.
- Unknown-unicast, broadcast, and multicast behaviour matches the design.

## Verification examples

```text
show bgp summary
show route table bgp.evpn.0
show route table bgp.evpn.0 extensive
show evpn instance
show evpn database
show ethernet-switching table
```

Command availability and output vary by platform and Junos release.

## Route-type questions

For each observed route, record:

- Which EVPN route type is present?
- Which device originated it?
- Which route distinguisher keeps it unique?
- Which route target controls import?
- Which next hop or tunnel endpoint is used?
- What local forwarding entry was created from it?

## Failure injections

### Route-target mismatch

The BGP session remains established, but remote EVPN routes are not imported into the intended service.

### Missing EVPN family

The underlying BGP session may be established for another address family while no EVPN routes are exchanged.

### Incorrect VNI or service mapping

Control-plane routes may exist, but forwarding does not place traffic into the same logical service.

## Evidence to capture

- BGP family state
- EVPN route entries and attributes
- Local and remote MAC database entries
- VNI/service state
- A packet capture or forwarding trace from an isolated lab, when available
