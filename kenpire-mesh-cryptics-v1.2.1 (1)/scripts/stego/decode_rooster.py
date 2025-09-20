#!/usr/bin/env python3
import base64, json, sys
from PIL import Image

png = Image.open(sys.argv[1])
b64u = png.text.get("kenpire.rooster.trigger")
assert b64u, "no rooster trigger in PNG metadata"

pad = "=" * ((4 - len(b64u) % 4) % 4)
payload = json.loads(base64.urlsafe_b64decode(b64u + pad).decode())
print(json.dumps(payload, indent=2))
