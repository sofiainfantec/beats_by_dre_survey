### Beats by Dre: Wireless Speaker Consumer Insights

## Project Overview
This project analyzes survey responses to understand consumer preferences, behaviors, and purchase drivers in the market for high-fidelity wireless speakers. The goal is to provide actionable insights for Beats by Dre to design data-driven strategies for product positioning, marketing, and distribution.

## Business Task
In a rapidly evolving market of portable audio devices, consumers are increasingly drawn towards versatile and mobile options, such as wireless and Bluetooth speakers. This presents Beats by Dre with a new set of consumer preferences to understand.

The central question is:  
**What are the key factors driving the increasing consumer interest in high-fidelity wireless speakers, and how do evolving preferences, lifestyle changes, and audio consumption habits influence this market expansion?**

## Business Hypothesis
Consumers’ growing interest in high-fidelity wireless speakers is primarily driven by three factors:

1. **Enhanced Sound Quality** – Users increasingly value superior audio performance.
2. **Lifestyle Alignment** – Younger demographics (Gen Z and Millennials) prefer portable, stylish, and multifunctional devices.
3. **Brand & Purchase Drivers** – Purchase decisions are influenced by brand reputation, pricing, and trusted retail channels.

If these factors are significant, Beats by Dre can position its high-fidelity speakers as both a **premium lifestyle accessory** and a **technologically superior product**.

## Expected Insights
From the survey analysis, we aim to uncover:

- **User Segmentation**: Age, gender, and income profiles of target consumers.
- **Feature Priorities**: Desired product attributes such as sound quality, battery life, design, connectivity, durability, and price.
- **Competitive Landscape**: Most owned brands and their market share distribution.
- **Purchase Drivers**: Factors like recommendation, online reviews, expert reviews, brand reputation, price, and advertising that influence buying decisions.
- **Sales Channels**: Preferred retail environments including large multi-brand stores, department stores, and online platforms.

## Data
- **Source**: Survey responses collected from consumers who own or have used wireless speakers.  
- **File**: `survey_responses.csv` (included in the repo).  
- **Rows**: Each row represents a survey response.  
- **Columns**: Demographics, product usage, desired features, purchase drivers, spending, and channel preferences.  

## Analysis
All data cleaning, formatting, statistical summaries, and visualizations are performed in the `analysis.py` script.  

### Key Steps:
1. **Data Cleaning**: Remove duplicates, drop empty columns, convert numeric columns.  
2. **Descriptive Statistics**: Summary of all variables to understand distributions and detect missing values.  
3. **Visualizations**: Graphs saved in the `figures/` folder.

## Figures Generated
1. **Frequency of Use** – % of respondents by usage frequency (`frequency_of_use.png`).  
2. **Age Bands** – % of respondents by age groups (`age_bands.png`).  
3. **Gender Distribution** – Pie chart showing gender split (`gender_pie.png`).  
4. **Household Income Distribution** – % of respondents by income (`income_distribution.png`).  
5. **Desired Features** – Average ranking of desired speaker features (`desired_features.png`).  
6. **Respondents by Age & Spending** – Count of respondents stacked by spending range (`age_spending.png`).  
7. **Top 20 Competitor Brands** – % of respondents mentioning each brand (`brand_competitors_top20.png`).  
8. **Purchase Drivers** – Average Likert scale scores for factors influencing purchase (`purchase_drivers.png`).  
9. **Top 10 Purchase Channels** – % of respondents by preferred channel (`purchase_channel_top10.png`).  

## Presentation Slides  
The findings were summarized in an **8-slide business presentation**.  
[View the slides here](https://gamma.app/docs/Insights-Strategic-Recommendations-for-Beats-by-Dre-vljta4hhh6cl732)

## Video Presentation  
I also recorded a walkthrough of the slides explaining the insights and recommendations:  
[Watch the video here](https://www.loom.com/share/debe0b8f739a4b52b6fd35af249693c7?sid=feb609be-4770-4230-83a8-e6fb635e82ab)  

## How to Run
1. Clone the repo:  
   ```bash
   git clone https://github.com/sofiainfantec/beats_by_dre_survey.git

## Run the Analysis in Google Colab  
You can run the full Python analysis directly in your browser without installing anything:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sofiainfantec/beats_by_dre_survey/blob/main/analysis.py)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sofiainfantec/beats_by_dre_survey/blob/main/analysis.ipynb)

