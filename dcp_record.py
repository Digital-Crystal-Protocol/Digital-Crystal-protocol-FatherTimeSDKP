---

## **ledger_check.py**

```python
import hashlib
import pathlib

# Path to the root of the repository
repo_path = pathlib.Path(__file__).parent

# Initialize SHA-256 hash object
sha = hashlib.sha256()

# Iterate over all files recursively, sorted for deterministic hashing
for f in sorted(repo_path.rglob("*")):
    if f.is_file() and not f.name.startswith("."):  # skip hidden/system files
        sha.update(f.read_bytes())

# Compute the final ledger hash
ledger_hash = sha.hexdigest()

# Canonical CID for verification
canonical_cid = "bafybeib3xw3tapl4nb6ukum2j7m3subrhstgneqhs4lvemzipszbimcffm"

# Output verification results
print(f"Ledger hash: {ledger_hash}")
if ledger_hash == canonical_cid:
    print("Status: VERIFIED ✅")
else:
    print("Status: MISMATCH ⚠️ - Repository integrity compromised")
import json
import datetime

def generate_dcp_record():
    """Generates and archives the Digital Crystal Protocol Authorship & Applicability Matrix (JSON)."""
    record = {
        "protocol": "Digital Crystal Protocol (DCP) v3.0 QCC-AE",
        "version": "v3.0",
        "trace_id": "DS-SDKP-QCC-FT-001",
        "author": {
            "full_name": "Donald Paul Smith",
            "aliases": ["Father Time", "FatherTimeSDKP"]
        },
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "doi_anchor": "10.5281/zenodo.15399806",
        "domains": {
            "cosmology": ["SDKP", "VFE1", "SD&N", "EOS"],
            "quantum_vibration": ["VFE1", "QCC"],
            "temporal": ["CWT (Amiyah Rose Smith Law)", "SDVR"],
            "computation": ["QCC-AE", "Kapnack Solver", "SGL"]
        },
        "limitations": [
            "Conventional linguistic systems",
            "Subjective/aesthetic judgments",
            "Unverified external hypotheses (QCC Validation Required)"
        ]
    }

    filename = "DigitalCrystalProtocol_ApplicabilityMatrix_v3.0.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=4, ensure_ascii=False)
    print(f"✅ DCP Record Created: {filename}")
    return record

if __name__ == "__main__":
    generate_dcp_record()
