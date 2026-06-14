import subprocess
import os
import sys

def print_banner():
    print("=" * 60)
    print("🛡️  SECDEPLOY-AUDIT: DEVOPS & SECURITY SCANNER INITIALIZED 🛡️")
    print("=" * 60)

def audit_docker_environment():
    print("\n[+] Scanning Local Container Architecture...")
    try:
        # Check if Docker engine is alive and responsive
        result = subprocess.run(["docker", "--version"], capture_output=True, text=True, check=True)
        print(f"  [✓] Docker Engine Active: {result.stdout.strip()}")
        
        # Scan for unencrypted or completely exposed container port bindings
        print("  [!] Auditing exposed network containers...")
        try:
            containers = subprocess.run(["docker", "ps", "--format", "{{.ID}} - {{.Names}} - {{.Ports}}"], capture_output=True, text=True, check=True)
            if containers.stdout:
                print(containers.stdout)
            else:
                print("  [✓] No highly volatile exposed containers running.")
        except subprocess.CalledProcessError as e:
            print(f"  [❌] Error retrieving container information: {e}")
                
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("  [❌] Docker Daemon not detected on local system path.")

if __name__ == "__main__":
    print_banner()
    audit_docker_environment()
