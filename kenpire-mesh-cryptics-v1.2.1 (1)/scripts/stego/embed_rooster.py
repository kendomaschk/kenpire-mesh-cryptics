#!/usr/bin/env python3
import json, base64, hashlib, sys
from PIL import Image, PngImagePlugin

poster_in, poster_out, payload_json = sys.argv[1:]
payload = json.load(open(payload_json))

raw = json.dumps(payload, separators=(",", ":")).encode()
b64u = base64.urlsafe_b64encode(raw).decode().rstrip("=")

im = Image.open(poster_in).convert("RGBA")
meta = PngImagePlugin.PngInfo()
meta.add_text("kenpire.rooster.trigger", b64u)
im.save(poster_out, pnginfo=meta)

h = hashlib.sha256(open(poster_out, "rb").read()).hexdigest()
print("sha256:", h)
