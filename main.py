"""
Real Estate AI Lead Engagement System
Entry point — starts all pipeline layers concurrently.
"""

import asyncio
import signal
import sys
from loguru import logger
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from src.ingestion.sheets_poller import SheetsPoller
from src.scraping.pipeline import ScrapingPipeline
from src.conversation.engine import ConversationEngine
from src.intent.detector import IntentDetector
from src.analytics.tracker import AnalyticsTracker
from src.utils.config import Config
from src.api import create_app
import uvicorn

console = Console()


def print_banner():
    banner = Text()
    banner.append("🏠 Real Estate AI Lead System\n", style="bold cyan")
    banner.append("Autonomous Lead Engagement Pipeline\n", style="dim white")
    banner.append("github.com/YOUR_USERNAME/real-estate-ai-system", style="dim blue")
    console.print(Panel(banner, border_style="cyan", padding=(1, 4)))


async def run_pipeline():
    """Start all pipeline layers concurrently."""
    config = Config()

    logger.info("Initializing pipeline components...")

    # Initialize all layers
    analytics = AnalyticsTracker(config)
    intent_detector = IntentDetector(config, analytics)
    conversation_engine = ConversationEngine(config, intent_detector, analytics)
    scraping_pipeline = ScrapingPipeline(config)
    sheets_poller = SheetsPoller(config, conversation_engine, analytics)

    logger.success("All components initialized. Starting pipeline...")

    # Run all tasks concurrently
    await asyncio.gather(
        sheets_poller.start_polling(),           # Layer 1: Lead ingestion
        scraping_pipeline.start_scheduled(),     # Layer 2: Property scraping
        conversation_engine.start_reply_loop(),  # Layer 3: Reply processing
        analytics.start_periodic_flush(),        # Layer 5: Analytics
    )


async def run_api_server(config):
    """Run the FastAPI server for the frontend dashboard."""
    app = create_app(config)
    server_config = uvicorn.Config(
        app,
        host="0.0.0.0",
        port=config.api_port,
        log_level="warning",
    )
    server = uvicorn.Server(server_config)
    await server.serve()


async def main():
    print_banner()

    config = Config()

    logger.remove()
    logger.add(
        sys.stdout,
        level=config.log_level,
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan> - {message}",
    )
    logger.add("logs/system.log", rotation="10 MB", retention="7 days", level="DEBUG")

    # Graceful shutdown handler
    loop = asyncio.get_event_loop()

    def handle_shutdown(sig, frame):
        logger.warning(f"Received signal {sig}. Shutting down gracefully...")
        for task in asyncio.all_tasks(loop):
            task.cancel()

    signal.signal(signal.SIGINT, handle_shutdown)
    signal.signal(signal.SIGTERM, handle_shutdown)

    try:
        await asyncio.gather(
            run_pipeline(),
            run_api_server(config),
        )
    except asyncio.CancelledError:
        logger.info("Pipeline stopped.")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(main())
