import itertools
import time
from threading import Event, Thread


# Ta funkcja działa w osobnym wątku. Argument done jest wystąpieniem
# Event, prostego obiektu do synchronizowania wątków.
def spin(msg: str, done: Event) -> None:
    for char in itertools.cycle(r"\|/-"):
        status = f"\r{char} {msg}"
        print(status, end="", flush=True)
        # Metoda wait obiektu Event zwraca True, gdy zdarzenie jest
        # ustawione przez inny wątek. W przeciwnym razie zwraca False jeśli
        # upłynie czas timeout.
        if done.wait(timeout=0.1):
            break
    blanks = " " * len(status)
    print(f"\r{blanks}\r", end="")


# Ta funkcja będzie wywoływana przez główny wątek.
def slow() -> int:
    # Zablokowanie głównego wątku na 3 sekundy i zwolenienie blokady GIL.
    # W ten sposób wątek spin może kontynuować swoje działanie.
    time.sleep(3)
    return 42


def supervisor() -> int:
    # Wystąpienie obiektu Event jest kluczowe do synchronizacji wątków.
    done = Event()
    spinner = Thread(target=spin, args=("thinking!", done))
    print("spinner object:", spinner)
    spinner.start()  # Uruchamiamy wątek spinner.
    result = slow()  # Blokujemy wątek main.
    done.set()  # Ustawiamy flagę obiektu Event na True, aby zatrzymać wątek spinner.
    spinner.join()  # Czekamy na zakonczenie wątku spinner.
    return result


def main() -> None:
    result = supervisor()
    print("Answer:", result)


if __name__ == "__main__":
    main()
