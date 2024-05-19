import asyncio
import itertools


async def spin(msg: str) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, end="", flush=True)
        try:
            # Zatrzymujemy przetwarzanie bez blokowania innych współprogramów.
            await asyncio.sleep(0.1)
        # asyncio.CancelledError jest zgłaszany, gdy metoda cancel jest wywoływana
        # dla obiektu Task, sterującego tym współprogramem.
        except asyncio.CancelledError:
            break
    blanks = " " * len(status)
    print(f"\r{blanks}\r", end="")


async def slow() -> int:
    await asyncio.sleep(3)
    return 42


async def supervisor() -> int:  # Rodzimy współprogramy jest definiowany z async def
    # asyncio.create_task planuje późniejsze wykonanie funkcji spin
    # natychmiast zwracając obiekt Task.
    spinner = asyncio.create_task(spin("thinking!"))
    print("spinner object:", spinner)
    # Słowo kluczowe await wywołuje slow blokując supervisor
    # aż do powrotu z funkcji slow
    result = await slow()
    # Task.cancel() zgłasza wyjątek CancelledError wewnątrz współprogramu spin.
    spinner.cancel()
    return result


# Main to jedyna zwykła funkcja w całym programie.
# Pozostałe są współprogramami.
def main() -> None:
    # asyncio.run rozpoczyna pętlę zdarzeń, aby sterować współprogramem
    # któy wprawia w ruch pozostałe współprogramy.
    result = asyncio.run(supervisor())
    print("Answer:", result)


if __name__ == "__main__":
    main()
