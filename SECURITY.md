# Security Policy for Jok3r

## Important Context

**Jok3r is a penetration testing automation framework designed for security professionals.**

This tool intentionally implements functionality that security scanners may flag as vulnerabilities, including:

- Command execution via subprocess with `shell=True`
- Dynamic command construction from user input
- Interaction with potentially malicious code and exploits
- SQL injection testing capabilities
- Code injection testing capabilities
- Execution of third-party security tools

**These patterns are not vulnerabilities in this context** - they are essential features for a penetration testing framework.

## Intended Use

Jok3r is designed for:
- **Authorized security testing only**
- Network penetration testing
- Web application security assessment
- Security research in controlled environments

## Security Considerations

### 1. Execution Environment
- **Run only in isolated testing environments** (VMs, containers, dedicated test networks)
- **Never run on production systems** or networks without proper authorization
- Use appropriate network isolation and segmentation

### 2. Input Validation
While Jok3r processes potentially malicious inputs as part of its testing functionality:
- Configuration files should come from trusted sources
- Tool definitions should be reviewed before use
- User inputs in the CLI are validated where appropriate

### 3. Subprocess Execution
The framework uses `subprocess.Popen` with `shell=True` to:
- Execute security testing tools with complex command-line arguments
- Support bash built-ins and piping between tools
- Enable virtualenv activation and other shell-dependent features

**This is intentional and necessary** for the framework to function. The commands executed are:
- Defined in configuration files (not arbitrary user input)
- Logged for audit purposes
- Run in the context of the user's permissions

### 4. Third-Party Tools
Jok3r executes numerous third-party security tools. Users should:
- Understand the tools being executed
- Review tool configurations in `settings/` directory
- Keep tools updated through the framework's update mechanism
- Verify tool sources and integrity

## Reporting Security Issues

### Real Security Concerns
If you discover a **genuine security vulnerability** that could allow:
- Unintended code execution beyond the framework's design
- Privilege escalation outside testing scope
- Data exfiltration of non-test data
- Other security issues affecting the tool itself (not its testing capabilities)

Please report it by opening a security advisory on GitHub.

### False Positives
If your security scanner flags code patterns that are:
- Intentional pentesting functionality
- Required for tool execution
- Part of the framework's designed behavior

These are **expected false positives**. Review this document and the CodeQL configuration in `.github/codeql/codeql-config.yml`.

## Security Scanning

This repository includes CodeQL configuration that suppresses known false positives specific to penetration testing frameworks. Security scanners will still flag:
- Actual vulnerabilities in the framework code
- Unsafe file operations
- Authentication/authorization issues
- Unintended information disclosure

## Best Practices for Users

1. **Isolate Your Testing Environment**
   - Use dedicated testing VMs or containers
   - Implement network segmentation
   - Avoid running on shared networks

2. **Authorization is Mandatory**
   - Obtain written permission before testing any system
   - Understand legal implications in your jurisdiction
   - Follow responsible disclosure practices

3. **Audit and Review**
   - Review tool configurations before use
   - Monitor tool execution and outputs
   - Maintain logs of testing activities

4. **Keep Updated**
   - Regularly update Jok3r: `python3 jok3r.py toolbox --update-all`
   - Review changelog for security-relevant changes
   - Update underlying OS and dependencies

## Disclaimer

This tool is provided for authorized security testing only. The developers assume no liability for misuse or damage caused by this program. Users are responsible for complying with all applicable laws and regulations.
