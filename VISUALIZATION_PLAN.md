# Business-Friendly Visualization Plan

## Objective
Transform technical data science figures into clean, professional, business-friendly visualizations suitable for executive presentation.

## Design Principles

### 1. Clarity Over Complexity
- Remove technical jargon (R², RMSE, etc.)
- Use simple, direct labels
- One clear message per chart

### 2. Visual Hierarchy
- Highlight key insights with color
- Use annotations and callouts
- Larger fonts (14-16pt minimum for readability)

### 3. Professional Styling
- Spa/wellness color palette: Soft teal (#4A9B9B), Sage green (#8FB996), Warm beige (#F5E6D3)
- Clean, minimal design
- Consistent branding across all figures

### 4. Executive-Friendly
- Focus on business impact (revenue, percentage changes)
- Clear before/after comparisons
- Direct answers to "so what?"

---

## Figure Redesign Specifications

### Figure 1: Association Rules - Top Service Combinations
**Original:** `association_rules_scatter.png` (scatter plot with lift/confidence axes)
**New:** `business_service_bundles.png`

**Changes:**
- Show only TOP 3 rules (not all 10)
- Horizontal bar chart format showing confidence %
- Each bar labeled with service names and lift multiplier
- Title: "Most Powerful Service Combinations"
- Subtitle: "Customers who buy Service A are X times more likely to buy Service B"
- Color: Green gradient (higher confidence = darker green)
- Add revenue impact annotations

**Metrics to Display:**
1. Body Slimming → Toning: 78% confidence, 12x more likely
2. Body Slimming + Laser → Toning: 71% confidence, 11x more likely
3. Body Slimming → Laser: 71% confidence, 11x more likely

---

### Figure 2: Day-of-Week Revenue Pattern
**Original:** `seasonal_patterns.png` (complex decomposition with multiple subplots)
**New:** `business_weekly_demand.png`

**Changes:**
- Extract ONLY the day-of-week bar chart
- Sort by revenue (highest to lowest)
- Color code: Red (below average), Green (above average)
- Add horizontal line showing daily average
- Annotate Tuesday (lowest) and Saturday (highest) with specific numbers
- Title: "Weekly Revenue Pattern: Saturday Peak vs Tuesday Valley"
- Subtitle: "92% difference between best and worst days"
- Show dollar amounts on bars (not just Y-axis)

**Key Annotations:**
- Saturday: 4,123 MYR (+38% above average) - GREEN
- Tuesday: 2,149 MYR (-28% below average) - RED
- Add gap callout showing 1,974 MYR opportunity

---

### Figure 3: Monthly Revenue Trends
**Original:** `revenue_trends.png` (line chart with multiple series)
**New:** `business_monthly_trends.png`

**Changes:**
- Simple line chart showing average daily revenue by month
- Highlight September (RED marker/annotation) as trough
- Highlight January (GREEN marker/annotation) as peak
- Add shaded regions to show "high season" vs "low season"
- Title: "Seasonal Revenue Patterns: January Peak, September Trough"
- Subtitle: "54% revenue drop during weakest month"
- Clean background, minimal gridlines

**Key Annotations:**
- January: 4,434 MYR/day (PEAK)
- September: 2,030 MYR/day (TROUGH)
- Add vertical annotation showing 54% gap

---

### Figure 4: Service Portfolio Distribution
**Original:** `rpt_analysis.png` (complex histogram with multiple bins)
**New:** `business_service_tiers.png`

**Changes:**
- Simple 3-bar horizontal bar chart
- Categories: Entry-level (78%), Mid-tier (14%), Premium (8%)
- Each bar shows: percentage, number of services, example service names
- Color: Bronze (entry), Silver (mid), Gold (premium)
- Title: "Service Portfolio: Heavy Concentration in Entry-Level"
- Subtitle: "78% of services priced under 300 MYR"
- Add callout: "Opportunity: Shift customers to mid-tier"

**Visual Style:**
- Use actual metallic-looking colors (bronze/silver/gold)
- Show service count inside bars
- Add example service names below each bar

---

### Figure 5: Top Revenue Drivers
**Original:** `xgboost_feature_importance.png` (technical feature importance with feature names)
**New:** `business_revenue_drivers.png`

**Changes:**
- Show ONLY top 5 drivers
- Translate technical names to business terms:
  - "TransactionCount x AvgValue" → "Transaction Size"
  - "day_of_week" → "Day of Week"
  - "Revenue_EMA_7" → "Recent Trends"
  - "AvgRevenuePerEmployee" → "Staff Productivity"
  - "UniqueCustomers" → "Customer Volume"
- Horizontal bar chart with percentage contribution
- Title: "What Drives Daily Revenue?"
- Subtitle: "Top 5 controllable factors"
- Color: Blue gradient
- Add icons for each factor (calendar, people, chart, etc.)

---

### Figure 6: 90-Day Forecast
**Original:** `90day_forecast.png` (technical time series with confidence bands)
**New:** `business_demand_forecast.png`

**Changes:**
- Simplify to show only predicted revenue line
- Remove or lighten confidence interval shading
- Add key milestones/dates (holidays, month boundaries)
- Highlight high-demand periods (weekends) with subtle shading
- Title: "90-Day Demand Forecast"
- Subtitle: "Predicted daily revenue: Nov 22 - Feb 19"
- Show summary statistics in callout box:
  - Average: 5,344 MYR/day
  - Peak: 9,590 MYR
  - Low: 2,265 MYR
- Color: Single color line (teal) with smooth curve
- Minimal gridlines

---

## Additional Custom Visuals (Simple Diagrams)

### Visual 7: Customer Pathway Diagram
**File:** `business_customer_pathway.png`
**Purpose:** Slide 3 - show before/after customer journey

**Design:**
- Two-row comparison diagram
- BEFORE: Customer → [Service A] → ⏰ weeks pass → ❓ Maybe Service B?
- AFTER: Customer → [Service A] → 📅 scheduled → [Service B] → 📅 scheduled → [Service C]
- Use icons and arrows
- Color: Gray (before), Green (after)
- Simple, clean flowchart style

---

### Visual 8: Week Calendar Comparison
**File:** `business_tuesday_calendar.png`
**Purpose:** Slide 4 - show empty vs filled Tuesday slots

**Design:**
- Two side-by-side weekly calendars
- BEFORE: Tuesday shows empty appointment slots (white/gray)
- AFTER: Tuesday shows filled appointments (green)
- Simple, icon-based (not detailed)
- Use checkmarks for filled slots

---

### Visual 9: Service Tier Pyramid
**File:** `business_service_pyramid.png`
**Purpose:** Slide 6 - show Good/Better/Best hierarchy

**Design:**
- Classic pyramid with 3 levels
- Colors: Bronze (bottom), Silver (middle), Gold (top)
- Each level labeled with tier name and price range
- Arrow pointing to "Better" tier saying "Recommended Focus"
- Clean, professional styling

---

### Visual 10: Implementation Roadmap
**File:** `business_roadmap.png`
**Purpose:** Slide 9 - show 3-phase rollout

**Design:**
- Horizontal timeline with 3 colored sections
- Phase 1 (Months 1-3): GREEN - "Quick Wins"
- Phase 2 (Months 4-6): YELLOW - "Strategic Initiatives"
- Phase 3 (Months 7-12): BLUE - "Optimize & Scale"
- Each phase shows 2-3 key milestones
- Simple, clean, professional

---

## Technical Specifications

### File Settings:
- **Format:** PNG
- **DPI:** 300 (print quality)
- **Dimensions:** 1920x1080 (16:9 ratio for slides)
- **Font Family:** 'Arial' or 'Segoe UI' (professional, readable)
- **Font Sizes:**
  - Title: 24pt
  - Subtitle: 16pt
  - Labels: 14pt
  - Annotations: 12pt

### Color Palette:
```python
COLORS = {
    'primary_teal': '#4A9B9B',
    'sage_green': '#8FB996',
    'warm_beige': '#F5E6D3',
    'alert_red': '#D84B4B',
    'success_green': '#6BBF59',
    'neutral_gray': '#7F8C8D',
    'bronze': '#CD7F32',
    'silver': '#C0C0C0',
    'gold': '#FFD700'
}
```

### Libraries:
- **matplotlib** for base plotting
- **seaborn** for styling
- **pandas** for data manipulation
- **numpy** for calculations

---

## Output Directory Structure

```
outputs/
└── figures/
    └── business/
        ├── business_service_bundles.png         (Slide 3)
        ├── business_weekly_demand.png           (Slide 4)
        ├── business_monthly_trends.png          (Slide 5)
        ├── business_service_tiers.png           (Slide 6)
        ├── business_revenue_drivers.png         (Slide 7)
        ├── business_demand_forecast.png         (Slide 7)
        ├── business_customer_pathway.png        (Slide 3 - diagram)
        ├── business_tuesday_calendar.png        (Slide 4 - diagram)
        ├── business_service_pyramid.png         (Slide 6 - diagram)
        └── business_roadmap.png                 (Slide 9 - diagram)
```

---

## Success Criteria

Each figure should:
✅ Be understandable by non-technical executives in < 5 seconds
✅ Have one clear main message
✅ Use business language (not technical jargon)
✅ Show specific dollar amounts or percentages
✅ Be visually consistent with others (colors, fonts, style)
✅ Work well on projector screens (high contrast, large text)
✅ Tell part of the overall story

---

## Next Steps

1. ✅ Create detailed plan (this document)
2. ⏳ Create notebook: `05_business_visualizations.ipynb`
3. ⏳ Generate all 6 business-friendly data figures
4. ⏳ Create 4 custom diagram visuals
5. ⏳ Review and refine based on clarity
6. ⏳ Update PRESENTATION_OUTLINE.md with new figure references
