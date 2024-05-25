import time
from concurrent import futures
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


# Jedyna zmiana to download_many() z użyciem ThreadPoolExecutor z modułu concurrent.futures
# Typowa modyfikacja na kod współbieżny - zamiana pętli for w funkcję wykonywaną współbieżnie.
# def download_many(cc_list: list[LiteralString]) -> int:
#     # Metoda executor.__exit__ wywoła metodę executor.shutdown(wait=True)
#     # która zaczeka na zakończenie wszystkich wątków.
#     with futures.ThreadPoolExecutor() as executor:
#         # Metoda map() zwraca generator przez który możemy iterować
#         # i pobierać wyniki zakończonych zadań.
#         res = executor.map(download_one, sorted(cc_list))
#     return len(list(res))


# Alternatywna wersja funkcji download_many() z ujawnieniem obiektów Future.
def download_many(cc_list: list[LiteralString]) -> int:
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do: list[futures.Future] = []
        for cc in sorted(cc_list):
            # Metoda submit() zwraca obiekt Future reprezentujący wynik wywołania funkcji.
            future = executor.submit(download_one, cc)
            to_do.append(future)
            print(f"Scheduled for {cc}: {future}")

        # Oczekiwanie na zakończenie wszystkich zadań.
        for count, future in enumerate(futures.as_completed(to_do), 1):
            res = future.result()
            print(f"{future} result: {res}")

    return count


def main(downloader: Callable[[list[LiteralString]], int]) -> None:
    DEST_DIR.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    count = downloader(POP20_CC)
    elapsed = time.perf_counter() - t0
    print(f"\n{count} flags downloaded in {elapsed:.2f}s")


if __name__ == "__main__":
    main(download_many)
