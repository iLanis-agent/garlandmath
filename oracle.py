#!/usr/bin/env python3
"""Oracle mirror of engine.js for Garland math. Writes expected.json (with trailing newline)."""
import json, math

def r2(x): return math.floor(x * 100 + 0.5) / 100

def jsnum(x):
    if isinstance(x, float) and x == int(x) and abs(x) < 1e15:
        return int(x)
    return x

def fmt(x):
    if isinstance(x, float) and x == int(x):
        return str(int(x))
    return repr(x) if isinstance(x, float) else str(x)

def garlandPlan(runM, droopPct):
    if not (runM > 0) or not (droopPct >= 0):
        return {"error": "run length must be positive, droop zero or more"}
    length = runM * (1 + droopPct / 100)
    strands = math.ceil(length / 2.7)
    return {"runM": jsnum(float(runM)), "droopPct": jsnum(float(droopPct)), "lengthM": jsnum(r2(length)),
            "strands": strands, "spareM": jsnum(r2(strands * 2.7 - length))}

def bunchPlan(lengthM, spacingCm):
    if not (lengthM > 0) or not (spacingCm > 0):
        return {"error": "length and spacing must be positive"}
    bunches = math.ceil(lengthM * 100 / spacingCm) + 1
    wireM = r2(bunches * 30 / 100)
    return {"lengthM": jsnum(float(lengthM)), "spacingCm": jsnum(float(spacingCm)), "bunches": bunches, "wireM": jsnum(wireM)}

def lightPlan(lengthM, bulbsPerM):
    if not (lengthM > 0) or not (bulbsPerM > 0):
        return {"error": "length and bulb density must be positive"}
    bulbs = math.ceil(lengthM * bulbsPerM)
    strands = math.ceil(bulbs / 100)
    return {"lengthM": jsnum(float(lengthM)), "bulbsPerM": jsnum(float(bulbsPerM)), "bulbs": bulbs,
            "strands": strands, "spare": strands * 100 - bulbs}

def renderGarland(r):
    return ("A " + fmt(r["runM"]) + " m run with a labeled " + fmt(r["droopPct"]) + "% swag droop needs " + fmt(r["lengthM"]) +
            " m of garland - " + str(r["strands"]) + " labeled 2.7 m strand" + ("" if r["strands"] == 1 else "s") +
            ", " + fmt(r["spareM"]) + " m spare.")

def renderBunch(r):
    return (fmt(r["lengthM"]) + " m of garland takes " + str(r["bunches"]) + " bunches at a labeled " + fmt(r["spacingCm"]) +
            " cm spacing, wired with " + fmt(r["wireM"]) + " m of florist wire (labeled 30 cm a bunch).")

def renderLight(r):
    return (fmt(r["lengthM"]) + " m at a labeled " + fmt(r["bulbsPerM"]) + " bulbs a meter is " + str(r["bulbs"]) +
            " bulbs - " + str(r["strands"]) + " labeled 100-bulb strand" + ("" if r["strands"] == 1 else "s") +
            ", " + str(r["spare"]) + " spare.")

CASES = []
def add(fn, args): CASES.append({"fn": fn, "args": args})

for a in [(5.5, 15), (2.5, 0), (8, 20), (1.2, 10), (4, 25), (10, 15), (3, 5), (6.75, 12), (0.8, 30), (0, 15), (5.5, -5), (2.7, 0)]:
    add("garlandPlan", list(a))
for a in [(6.32, 20), (2.7, 25), (10, 15), (1, 30), (5.5, 20), (0.5, 10), (8, 40), (3.3, 22), (0, 20), (6.32, 0), (4, -10)]:
    add("bunchPlan", list(a))
for a in [(6.32, 20), (5, 15), (2.7, 30), (10, 25), (1.2, 10), (8, 12), (4.4, 50), (0.9, 8), (0, 20), (6.32, 0), (5, -10), (3, 33)]:
    add("lightPlan", list(a))

out = []
for c in CASES:
    fn = {"garlandPlan": garlandPlan, "bunchPlan": bunchPlan, "lightPlan": lightPlan}[c["fn"]]
    res = fn(*c["args"])
    is_err = "error" in res
    if is_err:
        render = res["error"]
    else:
        render = {"garlandPlan": renderGarland, "bunchPlan": renderBunch, "lightPlan": renderLight}[c["fn"]](res)
    out.append({"fn": c["fn"], "args": c["args"], "result": res, "render": render, "isError": is_err})

with open("expected.json", "w") as f:
    f.write(json.dumps(out, separators=(",", ":")) + "\n")
print("wrote", len(out), "cases")
