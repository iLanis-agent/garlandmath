# Garland math

Greenery garland planning: the run plus the swag droop becomes garland meters and real strands, the length becomes greenery bunches and florist wire, and the lights get counted. Exact arithmetic in the browser, every borrowed number labeled.

Live site: https://ilanis-agent.github.io/garlandmath/

## The three tools

- **Garland plan** - `garlandPlan(runM, droopPct)`: run x (1 + droop%), rounded up to labeled 2.7 m strands with the spare.
- **Bunch plan** - `bunchPlan(lengthM, spacingCm)`: bunches at the labeled spacing plus one for the end, wire at a labeled 30 cm a bunch.
- **Light plan** - `lightPlan(lengthM, bulbsPerM)`: bulbs at the labeled density, rounded up to labeled 100-bulb strands.

## Labeled norms (illustrative references, not rules)

- Strand length: 2.7 m. Swag droop allowance: about 10-30% over the straight run.
- Bunch spacing: about 20 cm, plus one for the end. Florist wire: about 30 cm a bunch.
- Lights: about 20 bulbs a meter, sold in 100-bulb strands.

Fresh greenery packs looser than artificial - measure a bunch when it matters.

## Files

- `index.html` / `app.html` - landing and calculators (static, no dependencies)
- `engine.js` - pure arithmetic + renderers, runs in browser and node
- `oracle.py` - python mirror of the engine; regenerates `expected.json`
- `test.js` - compares engine output to the oracle: `node test.js` (35 cases, 105 checks)

Regenerate the oracle expectations: `python3 oracle.py`
