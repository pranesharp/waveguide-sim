# Waveguide Mode Bench

An interactive, single-file web app for exploring **TE and TM modes in rectangular waveguides**.

Open it in a browser and play with `m`, `n`, guide dimensions, and operating frequency. See the field patterns, cutoff behaviour, and propagation in real time — no install, no build step, no dependencies.

**Live demo:** `OpticWGSIM.pages.dev`*

---

## Quick start

```bash
git clone https://github.com/pranesharp/waveguide-sim.git
cd waveguide-sim
```

Then just open `run.bat` on windows in any modern browser. That's it.
Index.html lives in ./dat/ along with server.py so i just made it overcomplicated to look cool. That's all.


## Features

- **Cross-section view** — `|E_t|` heatmap, instantaneous E-field arrows, `|E|` contour lines, E-field nulls (nodes), and PEC walls drawn to scale.
- **Side view** — watch the field pattern travel along `+z` with the guide wavelength `λ_g` drawn to scale.
- **Mode fingerprint** — `H_z` (TE) or `E_z` (TM) plot to show *why* the transverse field looks the way it does.
- **Controls** — TE/TM toggle, mode indices `m`, `n` (0–5), width `a`, height `b`, WR-90 X-band preset, and operating frequency `f₀`.
- **Readouts** — `f₀`, `λ₀`, `f_c`, `λ_c`, `β`, `λ_g`, wave impedance `Z`, and propagate/evanescent status.
- **Live BC check** — verifies tangential `E = 0` on every PEC wall for the rendered mode.
- **Guided challenges** — predict → observe → explain exercises (TE₁₀ baseline, node counting, TM modes, degeneracy, dominant mode hunt).
- **"Name That Mode" game** — guess the mode from the field pattern; keeps a streak score.
- **Physics notes** — full field expressions, cutoff and propagation formulas, and why `TE₀₀`, `TM₀₀`, `TM₁₀`, `TM₀₁` cannot exist.
- **Accessible** — colorblind-safe (cividis) colormap, status shown as colour *and* text, reduced-motion support, ARIA descriptions on canvases, full keyboard navigation.

---

## Controls

| Input | Action |
|---|---|
| Family toggle | Switch between TE and TM |
| `m` / `n` sliders | Mode indices (0–5) |
| `a` / `b` sliders | Guide dimensions in mm |
| Preset dropdown | Load standard guides (e.g. WR-90) |
| `f₀` slider | Operating frequency in GHz |
| Mode buttons | Jump to common modes |
| `←` `→` | Adjust a focused slider |
| `Tab` | Move between all controls |

Default setup: **WR-90** (`a = 22.86 mm`, `b = 10.16 mm`) at `f₀ = 10.00 GHz`, where `TE₁₀` propagates with `λ_g ≈ 39.7 mm`.

---

## Idealizations

This is a teaching tool, so it assumes:

- Perfect electric conductors (no wall loss)
- Lossless dielectric filling
- A single mode at a time (no superposition or beating)
- Time is slowed for visibility — the real frequency is shown in the readouts

---

## Sources

1. D. M. Pozar, *Microwave Engineering*, 4th ed., Wiley, 2012 — §3.3–3.4.
2. S. Ramo, J. R. Whinnery, T. Van Duzer, *Fields and Waves in Communication Electronics*, 3rd ed., Wiley, 1994.
3. C. A. Balanis, *Advanced Engineering Electromagnetics*, 2nd ed., Wiley, 2012.
4. R. P. Feynman, *The Feynman Lectures on Physics*, Vol. II, Ch. 24.
5. Nuñez, Anderton & Renslow, *PLOS ONE* 13(7), 2018 — the cividis colormap.
6. EIA rectangular waveguide designation table — WR-90: `a = 22.86 mm`, `b = 10.16 mm`.

---

## License

MIT — see `LICENSE`