# Security and Sanitization Policy

## Public-content boundary

This repository must contain only fictional, sanitized lab material.

Never publish:

- Employer or customer names
- Real production hostnames, IP addresses, circuit IDs, account numbers, or topology
- Configuration copied from a managed network
- Credentials, tokens, keys, SNMP communities, certificates, or password hashes
- Internal operational procedures that are not approved for public release
- Screenshots containing private browser tabs, ticket numbers, chats, or monitoring data

## Safe examples

Use documentation address ranges, private autonomous-system numbers reserved for labs, fictional device names, and generated output. Recreate the concept rather than redacting a real production configuration.

## Reporting

Use GitHub's private security advisory feature for suspected secret exposure. Do not place sensitive evidence in a public issue.

## Operational warning

The examples are educational. Platform features and Junos syntax vary by hardware and software release. Validate against official documentation and test in an isolated environment before considering any operational use.
