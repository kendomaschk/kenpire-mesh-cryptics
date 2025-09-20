#!/usr/bin/env python3
import base64, json, hashlib, sys
from PIL import Image

PNG_PATH, MANIFEST_PATH = sys.argv[1:3]

im = Image.open(PNG_PATH)
b64u = im.text.get("kenpire.rooster.trigger")
if not b64u:
    sys.exit("No trigger payload found in poster")

pad = "=" * ((4 - len(b64u) % 4) % 4)
payload = json.loads(base64.urlsafe_b64decode(b64u + pad).decode())

sha = hashlib.sha256(open(PNG_PATH, "rb").read()).hexdigest()

print("Rooster trigger payload:", payload)
print("Poster sha256:", sha)

if payload.get("command") == "/pulse morning":
    print("[RoosterOps] Good morning, Mesh. Crowww!")
