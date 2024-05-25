import math
from concurrent import futures
from dataclasses import dataclass
from time import perf_counter


@dataclass(frozen=True)
class Result:
    number: int
    prime: bool
    elapsed: float


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for number in range(2, math.isqrt(n) + 1):
        if n % number == 0:
            return False

    return True


def check(n: int) -> Result:
    start = perf_counter()
    prime = is_prime(n)
    elapsed = perf_counter() - start
    return Result(n, prime, elapsed)


def main() -> None:
    numbers = (
        142702110479723,
        299593572317531,
        3333333333333301,
        3333333333333333,
        3333335652092209,
        4444444444444423,
        4444444444444444,
        4444444488888889,
        5555553133149889,
        5555555555555503,
        5555555555555555,
        6666666666666666,
        6666666666666719,
        6666667141414921,
        7777777536340681,
        7777777777777753,
        7777777777777777,
        9999999999999917,
        9999999999999999,
    )
    workers = 8
    executor = futures.ProcessPoolExecutor(workers)

    t0 = perf_counter()
    with executor:
        for res in executor.map(check, numbers):
            print(f"Number {res.number:16} Prime: {res.prime:1} Time: {res.elapsed:.6f}s")
    print(f"Total time: {perf_counter() - t0:.2f}s")


if __name__ == "__main__":
    main()
