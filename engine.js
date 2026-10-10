/* Garland math engine - pure arithmetic, every borrowed number labeled. */
(function (root) {
  "use strict";
  function r2(x) { return Math.round(x * 100) / 100; }

  function garlandPlan(runM, droopPct) {
    if (!(runM > 0) || !(droopPct >= 0)) return { error: "run length must be positive, droop zero or more" };
    var length = runM * (1 + droopPct / 100);
    var strands = Math.ceil(length / 2.7);
    return { runM: runM, droopPct: droopPct, lengthM: r2(length), strands: strands, spareM: r2(strands * 2.7 - length) };
  }

  function bunchPlan(lengthM, spacingCm) {
    if (!(lengthM > 0) || !(spacingCm > 0)) return { error: "length and spacing must be positive" };
    var bunches = Math.ceil(lengthM * 100 / spacingCm) + 1;
    var wireM = r2(bunches * 30 / 100);
    return { lengthM: lengthM, spacingCm: spacingCm, bunches: bunches, wireM: wireM };
  }

  function lightPlan(lengthM, bulbsPerM) {
    if (!(lengthM > 0) || !(bulbsPerM > 0)) return { error: "length and bulb density must be positive" };
    var bulbs = Math.ceil(lengthM * bulbsPerM);
    var strands = Math.ceil(bulbs / 100);
    return { lengthM: lengthM, bulbsPerM: bulbsPerM, bulbs: bulbs, strands: strands, spare: strands * 100 - bulbs };
  }

  function renderGarland(r) {
    return "A " + r.runM + " m run with a labeled " + r.droopPct + "% swag droop needs " + r.lengthM + " m of garland - " + r.strands + " labeled 2.7 m strand" + (r.strands === 1 ? "" : "s") + ", " + r.spareM + " m spare.";
  }

  function renderBunch(r) {
    return r.lengthM + " m of garland takes " + r.bunches + " bunches at a labeled " + r.spacingCm + " cm spacing, wired with " + r.wireM + " m of florist wire (labeled 30 cm a bunch).";
  }

  function renderLight(r) {
    return r.lengthM + " m at a labeled " + r.bulbsPerM + " bulbs a meter is " + r.bulbs + " bulbs - " + r.strands + " labeled 100-bulb strand" + (r.strands === 1 ? "" : "s") + ", " + r.spare + " spare.";
  }

  var api = { garlandPlan: garlandPlan, bunchPlan: bunchPlan, lightPlan: lightPlan, renderGarland: renderGarland, renderBunch: renderBunch, renderLight: renderLight };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  root.GarlandMath = api;
})(typeof window !== "undefined" ? window : this);
