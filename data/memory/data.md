# Beauty Salon Data Analysis - Dataset Documentation

This document provides a comprehensive overview of the CSV datasets used in our beauty salon business analysis.

## 1. Retail Product List.csv
**Purpose:** Catalog of retail products sold to customers for home use

**Key Columns:**
- `Code`: Unique product identifier
- `Name`: Product name and description
- `Section`: Product category (mainly "Skin Care")
- `Category`: Subcategory (e.g., "Beaubelle Iconnovations", "Specialty Mask")
- `Cost (MYR)`: Product cost to the business
- `Price (MYR)`: Selling price to customers
- `Lowest Price (MYR)`: Minimum allowable selling price

**Business Context:** Contains 148 products including skincare items, masks, creams, and gift items. Most products have zero cost but positive selling prices, suggesting they may be bundled or promotional items.

## 2. Salon Product List.csv
**Purpose:** Catalog of professional products used during salon treatments (not for direct sale)

**Key Columns:**
- `Code`: Unique product identifier
- `Name`: Product name and description
- `For Sale`: Whether the product can be sold directly to customers (mostly "No")
- `Cost (MYR)`: Product cost to the business
- `Price (MYR)`: Internal pricing for cost calculations

**Business Context:** Contains 113 professional-grade products used by therapists during treatments. Most are marked as not for sale, indicating they're exclusively for salon use during services.

## 3. Service List.csv
**Purpose:** Complete catalog of all services offered by the beauty salon

**Key Columns:**
- `Code`: Unique service identifier
- `Name`: Service name and description
- `Section`: Service category (FACIAL, SLIMMING, etc.)
- `Processing Time`: Duration of service in minutes
- `Price (MYR)`: Service price charged to customers
- `Commission Type`: How staff commission is calculated

**Business Context:** Contains 205 different services including facial treatments, body massages, slimming treatments, and wellness consultations. Prices range from free consultations to premium treatments costing 800 MYR.

## 4. Daily Received_1.csv
**Purpose:** Daily sales summary and payment records

**Key Columns:**
- `Date`: Transaction date
- `Reference No.`: Invoice/receipt number
- `Customer`: Anonymized customer identifier
- `Sale Employee`: Staff member who handled the sale
- `Total (MYR)`: Total amount before payments
- `Cash (MYR)`, `Card (MYR)`, `Others (MYR)`: Payment method breakdown
- `Net Received (MYR)`: Final amount received

**Business Context:** Contains 7,959 daily transaction records from 2021, showing payment patterns and sales performance by employee. Includes various payment methods and tracks actual money received.

## 5. Sale Ticket Detail.csv
**Purpose:** Detailed line-item records for each sale transaction

**Key Columns:**
- `Date`: Transaction date and time
- `Reference No.`: Links to Daily Received records
- `Customer Code`: Anonymized customer identifier
- `Item Code`: Product or service code
- `Item Name`: Full description of product/service sold
- `Price (MYR)`: Listed price
- `Qty`: Quantity sold
- `Discount (MYR)`: Discount amount applied
- `Total (MYR)`: Final line item total
- `FOC`: Free of charge indicator

**Business Context:** Contains 6,323 individual line items showing exactly what was purchased in each transaction. Includes discounts, package deals, and promotional items. Essential for detailed sales analysis and customer behavior tracking.

## Data Relationships
- `Daily Received_1.csv` and `Sale Ticket Detail.csv` are linked by Reference Number
- Product codes in Sale Ticket Detail link to either Retail or Salon Product Lists
- Service codes in Sale Ticket Detail link to Service List
- Customer codes appear across Daily Received and Sale Ticket Detail files

## Analysis Potential
This dataset enables comprehensive analysis of:
- Revenue trends and seasonality
- Service vs product sales performance
- Customer purchasing patterns
- Staff performance and commission tracking
- Payment method preferences
- Pricing strategy effectiveness

## Service Category Mapping for Nexus Beauty Analysis

Based on the task requirements, services can be categorized into these main business units:

### 1. Advanced Facial Treatments (FACIAL Section)
- **Service Codes**: F00001-F00050, FA-*, FE-*, etc.
- **Examples**: Classic Facial Treatments, Anti-Blue Light Facial, Pigmentation treatments
- **Price Range**: 99-800 MYR
- **Key Feature**: Most services have 60-minute processing time

### 2. Body Treatments & Slimming (SLIMMING Section)
- **Service Codes**: B00002-M, BD-GCRF, S00001-S00099
- **Examples**: ExpreSculpt Deep Muscle Toning, Fat Freeze treatments, Body Slimming
- **Price Range**: 99-800 MYR (premium category)
- **Key Feature**: Includes both slimming and body toning services

### 3. Massage & Spa Therapies (No specific section)
- **Service Codes**: BD-AM-*, BD-SM-*, various massage codes
- **Examples**: Aroma Oil Massage, Stress Release Massage, Hand SPA
- **Price Range**: 58-200 MYR
- **Key Feature**: Duration varies from 20-120 minutes

### 4. Nexus Beauty Signature Therapy
- **Note**: May need to be identified through specific naming patterns or premium pricing
- **Potential Indicators**: Higher-priced services, unique treatment names, or bundled packages

## Revenue Calculation Guide

### Key Metrics for Analysis

1. **Revenue Per Treatment (RPT)**:
   ```
   RPT = Total Sales Revenue / Number of Treatments
   ```
   - Use `Sale Ticket Detail.csv` → sum of `Total (MYR)` column
   - Count individual service transactions (Type = 'S')

2. **Service vs Product Revenue**:
   - Services: Items with Type = 'S' in Sale Ticket Detail
   - Products: Items with Type = 'P' in Sale Ticket Detail

3. **Daily Revenue Trends**:
   - Use `Daily Received_1.csv` → `Net Received (MYR)` column
   - Cross-reference with `Sale Ticket Detail.csv` for detailed breakdown

## Data Quality Considerations

### Potential Issues Identified

1. **Missing Data**:
   - Some service entries have empty Section or Category fields
   - Customer codes are anonymized (affects customer journey analysis)
   - Some transactions show zero costs but positive prices

2. **Data Inconsistencies**:
   - Multiple price fields (Price, Lowest Price) may not always align
   - FOC (Free of Charge) items complicate revenue calculations
   - Payment method data spans multiple columns

3. **Time Period Limitations**:
   - Dataset appears to cover primarily 2021
   - Limited historical context for seasonal trend analysis

### Recommendations for Analysis
- Filter out FOC transactions when calculating revenue metrics
- Handle missing category data by creating "Unknown" categories
- Use Reference Numbers to link Daily Received and Sale Ticket Detail records
- Consider package deals when analyzing individual service performance

## Project-Specific Analysis Context

### Required Analyses (per task.md)

1. **Time Series Decomposition**:
   - Use `Daily Received_1.csv` Date column for temporal analysis
   - Look for weekly, monthly, and seasonal patterns
   - Identify outliers or promotional events

2. **Market Basket Analysis**:
   - Use `Sale Ticket Detail.csv` grouped by Reference Number
   - Analyze which services/products are purchased together
   - Focus on service combinations for cross-selling opportunities

3. **Revenue Driver Analysis**:
   - Service category performance (Facial vs Body vs Massage)
   - Price point optimization
   - Staff performance correlation with sales

4. **Sales Forecasting**:
   - Daily revenue prediction using historical patterns
   - Service demand forecasting by category
   - Seasonal adjustment for business planning

## Business Context: Nexus Beauty Holistic Wellness

This beauty salon positions itself as a "holistic total wellness center" focusing on:
- **External Beauty**: Facial treatments, skincare products
- **Internal Health**: Detox treatments, wellness consultations  
- **Spiritual Balance**: Stress relief massages, relaxation therapies

The data analysis should consider how different service categories contribute to this holistic positioning and identify opportunities to enhance the complete wellness experience for customers.