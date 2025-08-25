# Add these options to your yt-dlp configuration
ydl_opts = {
    # ... your existing options ...
    'nocheckcertificate': True,
    'extractor_retries': 5,
    'fragment_retries': 5,
    'retries': 5,
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-us,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
    },
    'socket_timeout': 30,
    'sleep_interval': 2,
    'max_sleep_interval': 5,
    'sleep_interval_requests': 1
}