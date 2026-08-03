# Lab 1: BGP underlay and policy validation

## Objective

Establish BGP sessions between fictional edge routers, advertise only approved prefixes, and verify that routing policy produces the intended result.

## Success criteria

- All expected sessions reach `Established`.
- The local and peer autonomous-system numbers match the design.
- Only approved prefixes are accepted and advertised.
- The next hop is reachable through the underlay.
- No default route is accepted unless explicitly required.

## Suggested build sequence

1. Configure interface addressing and verify bidirectional reachability.
2. Configure local autonomous-system numbers and router IDs.
3. Create explicit import and export policies.
4. Configure neighbors and activate only the required address family.
5. Verify the session before troubleshooting policy.

## Junos verification examples

```text
show bgp summary
show bgp neighbor 203.0.113.1
show route receive-protocol bgp 203.0.113.1
show route advertising-protocol bgp 203.0.113.1
show route protocol bgp detail
```

The exact command output varies by Junos release. Confirm command availability on the lab image being used.

## Failure injections

### Incorrect peer AS

Change one peer AS and observe whether the session remains in `Active` or repeatedly resets. Restore the correct value and record the transition.

### Missing export policy

Remove the export policy and confirm that the session can remain established while no intended routes are advertised.

### Unreachable next hop

Remove the underlay route to the BGP next hop. Compare BGP session state with route usability; an established control-plane session does not guarantee that every learned route is usable.

## Evidence to capture

- Before-and-after `show bgp summary`
- Received and advertised prefix lists
- Policy configuration
- Relevant log messages
- A brief explanation linking the observed symptom to the root cause
