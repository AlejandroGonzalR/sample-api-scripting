import os
from dotenv import load_dotenv

load_dotenv()

JSON_RESULT_FILENAME = 'result.json'

APIs: dict = {
    'sample_api': {
        'host': os.getenv('SAMPLE_API_HOST'),
        'headers': {},
    },
    # ... Add more APIs clients/sessions or APIs global headers if needed
}
