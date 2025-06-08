import numpy as np
import pandas as pd


def generate_channel_attribution_data():
    """
    Generate synthetic data showing:
    - Offline influencer mentions (the TRUE driver)
    - Digital impressions that FOLLOW offline mentions
    - Sales driven primarily by offline, not digital
    """
    n_days = 90
    days = np.arange(n_days)
    
    # Offline influencer mentions (true driver)
    # Baseline: ~2 mentions per day
    offline_influencer_mentions = np.random.poisson(2, n_days)
    
    # Campaign bursts - influencer campaigns
    offline_influencer_mentions[30:35] = np.random.poisson(10, 5)  # First campaign
    offline_influencer_mentions[60:65] = np.random.poisson(8, 5)   # Second campaign
    
    # Digital impressions correlate with offline
    # When people hear about product offline, they search online!
    digital_impressions = (
        1000 +  # Baseline impressions
        500 * offline_influencer_mentions +  # People searching after hearing offline
        np.random.normal(0, 100, n_days)  # Random noise
    )
    
    # True effects
    true_digital_effect = 0.001  # Digital has minimal direct effect
    true_offline_effect = 20     # Offline has strong effect
    
    # Generate sales
    sales = (
        100 +  # Baseline sales
        true_offline_effect * offline_influencer_mentions +
        true_digital_effect * digital_impressions +
        np.random.normal(0, 10, n_days)
    )
    
    return pd.DataFrame({
        'day': days,
        'sales': sales,
        'digital_impressions': digital_impressions,
        'offline_mentions': offline_influencer_mentions,
        'true_digital_contribution': true_digital_effect * digital_impressions,
        'true_offline_contribution': true_offline_effect * offline_influencer_mentions
    })

# Generate the data

def generate_seasonal_campaign_data():
    """
    Generate synthetic marketing data with:
    - Strong seasonal pattern (holiday shopping season)
    - Campaign that coincides with peak season
    - Small true campaign effect hidden by seasonality
    """
    n_weeks = 52
    weeks = np.arange(n_weeks)
    
    seasonal_pattern = 50 + 30 * np.exp(-0.5 * ((weeks - 45) / 5)**2)
    
    campaign_spend = np.zeros(n_weeks)
    campaign_spend[40:48] = np.random.uniform(1000, 2000, 8)
    
    true_campaign_effect = 0.05 * campaign_spend
    
    sales = seasonal_pattern + true_campaign_effect + np.random.normal(0, 5, n_weeks)
    
    return pd.DataFrame({
        'week': weeks,
        'sales': sales,
        'campaign_spend': campaign_spend,
        'seasonal_baseline': seasonal_pattern,
        'true_campaign_contribution': true_campaign_effect
    })

