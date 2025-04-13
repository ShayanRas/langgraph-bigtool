import os
from supabase import create_client, Client
import dotenv
import logging

dotenv.load_dotenv()
SUPABASE_URL: str = os.environ.get("SUPABASE_URL")
SUPABASE_KEY: str = os.environ.get("SUPABASE_KEY")

#---logger--#
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


if not SUPABASE_URL:
    logger.error("Supabase URL not found in environment variables.")
    raise ValueError("Supabase URL not found in environment variables.")
if not SUPABASE_KEY:
    logger.error("Supabase Key not found in environment variables.")
    raise ValueError("Supabase Key not found in environment variables.")

# Option 1: Provide a function to get a client instance
def get_supabase_client() -> Client:
    """Creates and returns a Supabase client instance."""
    try:
        logger.debug(f"Attempting to create Supabase client for URL: {SUPABASE_URL[:20]}...") # Optional debug log
        client: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        logger.info("Successfully created Supabase client.") # <<< Success message here
        return client
    except Exception as e:
        logger.error(f"Error creating Supabase client: {e}")
        print(f"Error creating Supabase client: {e}")
        raise # Re-raise the exception after logging
