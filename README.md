# CookieRain

A tool to export [Netscape formatted](http://curl.haxx.se/rfc/cookie_spec.html) cookies via [CookieCloud](https://github.com/easychen/CookieCloud).
Which is able to use on tools like [youtube-dl](https://github.com/ytdl-org/youtube-dl) or [yt-dlp](https://github.com/yt-dlp/yt-dlp), etc.

## Usage

1. Setting up your CookieCloud API, include:
   - [Backend API server](https://github.com/easychen/CookieCloud#%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%AB%AF)
   - Browser extension ([Chrome](https://chrome.google.com/webstore/detail/cookiecloud/ffjiejobkoibkjlhjnlgmcnnigeelbdl) / [Edge](https://microsoftedge.microsoft.com/addons/detail/cookiecloud/bffenpfpjikaeocaihdonmgnjjdpjkeo))
2. `git clone https://github.com/unacro/CookieRain && cd CookieRain`
3. `poetry install`
4. `cp .env.example .env` and edit the `.env` file
5. `poetry run start`
