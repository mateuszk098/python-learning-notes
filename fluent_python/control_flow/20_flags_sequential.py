import time
from pathlib import Path
from typing import Callable, LiteralString

import httpx

POP20_CC = ("CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR").split()
BASE_URL = "http://www.fluentpython.com/data/flags"
DEST_DIR = Path("downloads/")


def save_flag(img: bytes, filename: str) -> None:
    with open(DEST_DIR / filename, "wb") as f:
        f.write(img)


def get_flag(cc: str) -> bytes:
    url = f"{BASE_URL}/{cc}/{cc}.gif".lower()
    resp = httpx.get(url, timeout=6, follow_redirects=True)
    resp.raise_for_status()
    return resp.content


def download_one(cc: str) -> "str":
    try:
        image = get_flag(cc)
    except httpx.HTTPStatusError as exc:
        res = exc.response
        if res.status_code == 404:
            status = "not found"
        else:
            status = f"http error {res.status_code}"
    except httpx.RequestError as exc:
        status = f"download error: {exc}"
    else:
        save_flag(image, f"{cc}.gif")
        status = "ok"
    print(cc, end=" ", flush=True)
    return status


def download_many(cc_list: list[LiteralString]) -> int:
    for cc in sorted(cc_list):
        status = download_one(cc)
    return len(cc_list)


def main(downloader: Callable[[list[LiteralString]], int]) -> None:
    DEST_DIR.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    count = downloader(POP20_CC)
    elapsed = time.perf_counter() - t0
    print(f"\n{count} flags downloaded in {elapsed:.2f}s")


if __name__ == "__main__":
    main(download_many)
