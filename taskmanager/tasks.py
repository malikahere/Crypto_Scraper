# tasks.py

from celery import shared_task
from .models import Job, Task
from .coinmarketcap import CoinMarketCap

from django.core.exceptions import ValidationError

@shared_task
def scrape_coin_data(coin_name):
    job_id = job_id
    scraped_data = CoinMarketCap.scrape_data(coin_name)
    if scraped_data:
        Task.objects.create(
            coin_name=coin_name,
            job_id=job_id,
            price=scraped_data.get('price'),
            price_change=scraped_data.get('price_change'),
            market_cap=scraped_data.get('market_cap'),
            market_cap_rank=scraped_data.get('market_cap_rank'),
            volume=scraped_data.get('volume'),
            volume_rank=scraped_data.get('volume_rank'),
            volume_change=scraped_data.get('volume_change'),
            circulating_supply=scraped_data.get('circulating_supply'),
            total_supply=scraped_data.get('total_supply'),
            diluted_market_cap=scraped_data.get('diluted_market_cap'),
        )

@shared_task
def start_scraping(coins):
    try:
        CoinMarketCap.validate_coins(coins)
        job = Job.objects.create(coins=coins)
        for coin in coins:
            scrape_coin_data.delay(coin)
        return job.id
    except ValidationError as e:
        # Log the error or handle it accordingly
        return {'error': str(e)}