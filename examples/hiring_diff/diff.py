"""Compare two snapshots: which postings opened, which closed."""
import json, sys

old, new = (json.load(open(p)) for p in sys.argv[1:3])
opened = sorted(set(new) - set(old), key=new.get)
closed = sorted(set(old) - set(new), key=old.get)
print(f"{len(old)} -> {len(new)} open jobs | +{len(opened)} opened | -{len(closed)} closed")
for url in opened[:5]:
    print("  +", new[url])
for url in closed[:5]:
    print("  -", old[url])
