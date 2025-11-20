# Data-Driven Growth Strategy for Nexus Beauty: Enhancing Sales and Profitability through Holistic Wellness Analytics

## 1. Project Overview and Client Context

**Client:** Nexus Beauty  
**Industry:** Holistic Health, Beauty, and Wellness  
**Goal:** Utilize advanced data science and machine learning to identify key drivers of sales and profit and generate actionable strategic recommendations for business optimization.

Nexus Beauty operates as a holistic total wellness center dedicated to enhancing the complete well-being of its clients—focusing not just on external beauty but also on internal health and spiritual balance. The business offers a comprehensive menu of high-quality beauty and wellness services, prominently featuring:

- Advanced Facial Treatments
- Targeted Body Treatments (including slimming and detox)
- Relaxing Massage and Spa Therapies

Nexus Beauty distinguishes itself through its tranquil, therapeutic environment and its signature offering: the Nexus Beauty Signature Therapy. Students will analyse the performance of these core service categories to support strategic growth.

## 2. Problem Statement

Nexus Beauty seeks to move beyond traditional business intuition by adopting a data-first approach to optimizing its operations. The challenge for students is to leverage five years of historical sales data to answer critical business questions and develop a high-impact, data-backed strategy that directly maximizes revenue and profit margin across its service offerings.

## 3. Data Provided

Students will be provided with a cleaned, four-year historical daily sales dataset:
- Daily_Received.csv
- Retail_Product_List.csv
- Sale_Ticket_Detail.csv
- Salon_Product_List.csv
- Service_List.csv

**Note:** Bear in mind that the data may be insufficient, incomplete, or even incorrect. You just have to make the best out of it.

## 4. Methodology and Suggested Key Tasks

Here are some suggested steps for you to take, it should not be limited to these. Your most important objective is to make recommendations to the Business Owner.

### Phase 1: Data Understanding and Exploration (EDA)

1. **Revenue Analysis:** Calculate daily and service-specific revenue. For example, Revenue Performance Analysis: Calculate and analyze the Revenue Per Treatment (RPT) (Total_Sales_Revenue / Number_of_Treatments) to determine the highest-value service offerings.

2. **Time Series Decomposition:** Identify and visualize seasonal trends (monthly, weekly), long-term growth patterns, and any significant outliers or events (e.g., high-impact promotions).

3. **Service Performance:** Compare the sales volume and profitability of core offerings (Facials, Body, Massage, Signature Therapy) to determine the most valuable services.

### Phase 2: Suggested Feature Engineering and Machine Learning

1. **Sales and Demand Forecasting:** Develop a Time Series Forecasting model (e.g., ARIMA, Prophet, or advanced models like LSTMs/Recurrent Neural Networks) to accurately predict daily demand and revenue for the next 90-180 days.

2. **Revenue Driver Analysis:** Use standard model interpretability techniques (like Feature Importance from a Random Forest or XGBoost model) to quantify the precise impact of different features (e.g., which service category or time feature drives the most revenue).

3. **Association Rule Mining (Important):** Use Market Basket Analysis (Apriori or Fp-growth) to discover common service pairings. (For your Main Recommendation)

### Phase 3: Strategic Recommendation Generation

The final and most critical phase is translating technical findings into commercial strategy. Students must develop at least five detailed, distinct, prioritized recommendations and justify them with financial data and model outputs.

## 5. Expected Deliverables

1. **Technical Report (Markdown/PDF):** A detailed document outlining data preparation, model selection, performance metrics, key analytical findings including recommendations to the business owner.

2. **Trained Models:** Clean, executable code and serialised models capable of making new predictions (e.g., Python code with scikit-learn or similar libraries).

3. **Final Recommendation Deck:** This is the most important section. A professional presentation summarizing the top 3-5 high-impact recommendations for Nexus Beauty, including:
   - **Optimal Service Mix:** Which services to promote and which to de-emphasize. (Using Market Basket Analysis) This is most important of delivery.
   - **Promotion Strategy:** Data-backed suggestions on timing and type of promotions.
   - **Scheduling Optimization:** Recommendations on staffing and operational capacity based on demand forecasts. (Optional)
   - **Financial Impact:** Quantified projection of the potential sales/profit lift for each recommendation.

### Deliverable Breakdown

| Deliverable | Purpose and Audience | Tone and Content |
|-------------|---------------------|------------------|
| **Technical Report (Markdown/PDF)** | **Audience:** Instructor/TA. This is the detailed, academic proof. It shows how the analysis was performed, how the models were built, and how well they performed. | Highly detailed, technical language. Includes code snippets, methodology, feature engineering rationale, and all model performance metrics (e.g., RMSE, R-squared). Including Strategic Recommendations (mentioned in Rubric) |
| **Final Recommendation Deck (Presentation)** | **Audience:** Nexus Beauty Business Owner. This is the strategic summary. It shows what the students found and why the owner should implement the changes. | Professional, non-technical, and strategic language. Focuses only on the top 3-5 recommendations, supporting visualizations, and the quantified Revenue Lift. |

## Marking Rubric: Nexus Beauty Data Science Project (Total: 100 Points)

This rubric assesses the depth of technical execution, the quality of analytical insights, and the strategic value of the final recommendations.

### Part 1: Technical Report and Methodology (25 Points)

| Criteria | Max Points | Exemplary (90-100%) | Proficient (70-89%) | Needs Improvement (50-69%) | Deficient (< 50%) |
|----------|------------|---------------------|---------------------|---------------------------|-------------------|
| **Data Understanding & EDA (Revenue Focus)** | 10 | Comprehensive EDA, including detailed Revenue Per Treatment (RPT) calculations, time-series decomposition, and identification of key seasonal/weekly revenue patterns. | Good coverage of EDA; correctly calculates RPT and identifies general revenue trends, but visualizations may lack depth. | Basic data profiling and trend identification; fails to effectively calculate or analyze Revenue Per Treatment (RPT). | Minimal or incorrect EDA; superficial analysis of the data. |
| **Methodology & Documentation** | 10 | Technical report is exceptionally well-structured, clearly outlining all data preparation steps, model choices, and feature engineering rationale. | Report is clear and logically structured; methodology is explained with appropriate detail. | Methodology sections are present but lack clarity or logical flow; some key steps are missing or vague. | Report is disorganized; model and data preparation steps are not documented or are incomplete. |
| **Feature Engineering Quality** | 5 | Creatively and correctly engineered exogenous features (e.g., lag features, holiday flags) that significantly enhance model performance. | Correctly engineered standard time-based features (Day of Week, Quarter). | Engineered features are basic or contain errors; minimal impact on modeling. | No feature engineering performed beyond basic date extraction. |

### Part 2: Model Implementation and Performance (25 Points)

| Criteria | Max Points | Exemplary (90-100%) | Proficient (70-89%) | Needs Improvement (50-69%) | Deficient (< 50%) |
|----------|------------|---------------------|---------------------|---------------------------|-------------------|
| **Demand Forecasting Accuracy** | 15 | Selected and tuned an advanced time-series model (e.g., Prophet, LSTM) achieving high accuracy (low error metrics) in predicting Revenue with clear out-of-sample validation. | Implemented a reliable model (e.g., ARIMA) with solid accuracy; validation process is sound. | Model selection is basic or inappropriate; accuracy is moderate; validation is incomplete. | Model is non-functional or error metrics indicate poor forecasting performance. |
| **Revenue Driver Analysis** | 5 | Used standard model interpretability methods (e.g., Feature Importance) from the forecasting model to clearly identify and rank the features driving the most Revenue (e.g., service category, day of week). | Feature importance is identified but may be basic (e.g., using coefficients from linear models) or interpretation is minimal. | Attempted to identify drivers, but metrics are confusing or results are poorly presented. | No attempt to identify which factors drive revenue. |
| **Code Quality and Reproducibility** | 5 | Code is clean, modular, well-commented, and includes a serialized model that runs instantly for new predictions. | Code is functional and mostly clear; model serialization is complete. | Code is messy and requires effort to run or debug; serialization is incomplete. | Code does not run or is missing crucial components (e.g., the trained model files). |

### Part 3: Strategic Recommendations (40 Points)

| Criteria | Max Points | Exemplary (90-100%) | Proficient (70-89%) | Needs Improvement (50-69%) | Deficient (< 50%) |
|----------|------------|---------------------|---------------------|---------------------------|-------------------|
| **P1: Optimal Service Mix (MBA) (MOST IMPORTANT)** | 20 | Market Basket Analysis (MBA) is executed flawlessly, yielding high-confidence association rules. Recommendations for cross-promotion and product bundling are directly and powerfully driven by the MBA results and RPT data. | MBA executed correctly, providing clear service pairings. Recommendations are logical but could explore more complex bundling opportunities. | MBA is attempted but rules are weak or misapplied. Recommendations are present but lack direct support from the analysis. | MBA is not attempted or fails entirely; service mix recommendations are based only on simple volume metrics. |
| **P2: Promotion Strategy** | 10 | Recommendations are precisely tied to time-series and revenue driver findings (e.g., target specific low-demand days/seasons, or promote the highest-RPT service). | Recommendations offer clear guidance on the type of promotion (e.g., BOGO, discount) and are generally supported by the data. | Recommendations on promotions are generic (e.g., "run more sales") or lack strong evidence from the analysis. | No actionable promotion strategy provided. |
| **P3: Financial Impact** | 5 | Every core recommendation includes a robust, quantified projection of expected Revenue Lift, using model outputs and clear business assumptions. | Financial impact is quantified for most recommendations using reasonable assumptions, but projections could be more detailed. | Financial impact is mentioned but not fully quantified; projections are vague or based on unsubstantiated assumptions. | Recommendations lack any attempt at quantifying the expected business benefit. |
| **P4: Scheduling Optimization (Optional)** | 5 | Detailed recommendations on staffing or capacity adjustments provided, directly linked to high-resolution demand forecasts (e.g., shifts needed on peak days). | Basic capacity adjustment recommendations provided, supported by overall demand forecasts. | Brief mention of scheduling, but without specific capacity recommendations. | Not addressed. |

### Part 4: Final Recommendation Deck (10 Points)

| Criteria | Max Points | Exemplary (90-100%) | Proficient (70-89%) | Needs Improvement (50-69%) | Deficient (< 50%) |
|----------|------------|---------------------|---------------------|---------------------------|-------------------|
| **Professionalism and Clarity** | 5 | Deck is visually compelling, highly professional, and perfectly tailored for the business owner audience, using clear, non-technical language for strategic points. | Deck is well-designed and covers all required content, but may occasionally use overly technical language. | Deck is functional but visually basic; content is sometimes confusing or poorly structured for a business audience. | Deck is incomplete, poorly formatted, or difficult to follow. |
| **Communication of Key Insights** | 5 | Recommendations are immediately visible and compelling. Visualizations used in the deck are highly effective and directly support the strategic conclusions. | Key findings and recommendations are clearly communicated, supported by functional charts/graphs. | Visual aids are included but may be cluttered or do not directly relate to the recommendation. | Fails to clearly present the top recommendations and supporting evidence. |