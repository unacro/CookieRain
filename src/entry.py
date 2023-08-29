from loguru import logger
from .cookie_cloud_client.config import Config
from .cookie_cloud_client.client import CookieCloud


def download_video_websites_cookies() -> None:
    cookie_cloud: CookieCloud = CookieCloud(
        Config.get("URL"),
        Config.get("USER_KEY"),
        Config.get("PASSWORD"),
    )
    domain_list: list = [
        "acfun.cn",
        "bilibili.com",
        "youtube.com",
    ]
    if cookie_cloud.save_to(domain_list, Config.get("CACHE_PATH")):
        logger.success(f"Update cookies of {domain_list} success")
    else:
        logger.error(f"Update cookies of {domain_list} failed")


def main() -> None:
    download_video_websites_cookies()


if __name__ == "__main__":
    main()
