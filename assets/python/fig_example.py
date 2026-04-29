import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Match LNCS serif font (Times)
matplotlib.rcParams["font.family"] = "serif"
matplotlib.rcParams["font.serif"] = ["Times New Roman", "Times", "DejaVu Serif"]
matplotlib.rcParams["mathtext.fontset"] = "stix"

# 1. Setup the Design Space
x = np.linspace(1, 5, 400)
y = np.linspace(1, 5, 400)
X, Y = np.meshgrid(x, y)
Z = X * Y  # Adoption Potential ~ Agency * Autonomy

# 2. Plotting
# Figure size matched to LNCS textwidth (12.2cm = 4.8in) at ~4:3 ratio
fig, ax = plt.subplots(figsize=(4.8, 3.4))

# Create Contour Plot with distinct linestyles for scientific publication
contours = ax.contour(
    X,
    Y,
    Z,
    levels=[4.5, 9, 16],
    colors="k",
    linewidths=1.0,
    linestyles=[":", "--", "-."],
)

# Label the Contours — manual positions to keep labels inside the plot
fmt = {4.5: "Low Viability", 9: "Moderate Viability", 16: "High Viability"}
ax.clabel(
    contours, inline=True, fontsize=7, fmt=fmt, use_clabeltext=True, inline_spacing=3,
    manual=[(2.8, 1.6), (3.8, 2.4), (3.8, 4.2)],
)

# 3. Formatting Axes — no title (handled by LaTeX caption)
ax.set_xlabel("Autonomy", fontsize=9)
ax.set_ylabel("Agency", fontsize=9)

# Axes edges exactly at L1 and L5
ax.set_xlim(1, 5)
ax.set_ylim(1, 5)

# Custom Ticks matching the taxonomy
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_xticklabels(["L1", "L2", "L3", "L4", "L5"], fontsize=8)

ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(["L1", "L2", "L3", "L4", "L5"], fontsize=8)

# 4. Clean Annotations with Circular Labels
point_color = "#1f77b4"
bbox_style = dict(boxstyle="circle,pad=0.3", fc="white", ec=point_color, lw=1.0)

# A: Baseline (Bottom-Left)
ax.text(1.3, 1.3, "A", fontsize=9, fontweight="bold", ha="center", va="center", color=point_color, bbox=bbox_style)

# B: Supertool (Top-Left, High Agency/Low Autonomy)
ax.text(1.3, 4.5, "B", fontsize=9, fontweight="bold", ha="center", va="center", color=point_color, bbox=bbox_style)

# C: Autonomous Monitor (Right, Low-Mid Agency/High Autonomy)
ax.text(4.5, 2.5, "C", fontsize=9, fontweight="bold", ha="center", va="center", color=point_color, bbox=bbox_style)

# D: Transformative Agent (Top-Right, High Agency/High Autonomy)
ax.text(4.5, 4.5, "D", fontsize=9, fontweight="bold", ha="center", va="center", color=point_color, bbox=bbox_style)

# 5. Configuration name labels above each circled letter
name_style = dict(fontsize=6.5, fontstyle="italic", ha="center", va="bottom", color=point_color)

ax.text(1.3, 1.48, "Baseline",              **name_style)
ax.text(1.3, 4.68, "Supertool",             **name_style)
ax.text(4.5, 2.68, "Autonomous\nMonitor",   **name_style)
ax.text(4.5, 4.68, "Transformative\nAgent", **name_style)

# 6. No grid, no quadrant dividers — ticks only
plt.tight_layout()

plt.savefig("../../paper/figures/fig_example.pdf", bbox_inches="tight")
plt.savefig("../../paper/figures/fig_example.png", bbox_inches="tight", dpi=150)
print("Saved to ../../paper/figures/fig_example.pdf + .png")
