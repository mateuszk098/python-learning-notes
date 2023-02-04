## **_KONFIGURACJA NAZW:_**
---
### * _Ustawienie nazwy użytkownika dla wszystkich repozytoriów:_
>**git config --global user.name "user_name"**
### * _Ustawienie emaila dla wszystkich repozytoriów:_
>**git config --global user.email "email"**         
### * _Ustawienie nazwy użytkownika dla konkretnego repozytorium:_
>**git config --local user.name "user_name"** 
### * _Wyświetlenie wszystkich ustawień:_
>**git config --global --list**            
### * _Konfiguracja aliasu (skrótu polecenia do wykonania):_
>**git config --global alias.history "log --graph --oneline --all"**
### * _Usunięcie aliasu (skrótu polecenia do wykonania):_
>**git config --global --unset alias.history**
### * _Wykonanie aliasu:_
>**git history**
### * _Wykonanie aliasu i przekazanie wyniku do pliku:_
>**git history > history.txt**

---

## **_PRACA Z REPOZYTORIUM:_**
---
### * _Tworzenie nowego repozytorium:_
>**git init**
### * _Status -  informacje na temat obecnej gałęzi, commity w local repository oraz stan staging area. Polecenie to nie mówi jednak jakie zmiany są w working tree:_
>**git status**
### **_DODAWANIE PLIKÓW DO STAGING AREA (STAGE):_**
### * _Dodanie określonego pliku:_
>**git add <file_name>**
### * _Dodanie wszystkich plików z rozszerzeniem .txt:_
>**git add <*.txt>**
### * _Dodanie wszystkich plików zaczynających się na abc (wielkość liter ma znaczenie):_
>**git add <abc_*>**
### **_USUWANIE PLIKÓW ZE STAGING AREA (UNSTAGE):_**
### * _Usuwanie określonego pliku ze staging area:_
>**git restore --staged <file_name>**  
### * _Usuwanie wszystkich plików z rozszerzeniem .txt:_
>**git restore --staged <*.txt>**
### * _Usuwanie wszystkich plików zaczynających się na abc:_
>**git restore --staged <abc_*>**

---

## **_COMMITY:_**
---
### * _Dodanie commitu do repozytorium lokalnego:_
>**git commit -m "message"**
### * _Informacje na temat najnowszego commitu:_ 
>**git show**          
### * _Informacje na temat danego commitu np. d122a6a:_ 
>**git show <commit_sha1>**
### * _Historia commitów:_
>**git log**
### * _Historia commitów w postaci grafu:_
>**git log --graph**        
### * _Historia commitów w postaci grafu bez dodatkowych informacji:_
>**git log --graph --oneline**
### * _Historia commitów w postaci grafu we wszystkich gałęziach bez dodatkowych informacji:_
>**git log --graph --oneline --all**
### * _Historia commitów nawet tych usuniętych ale jedynie przez krótki czas:_
>**git reflog**     

---

## **_RÓŻNICE:_**
---
### * _Różnice między plikami w working tree oraz staging area:_
>**git diff**
### * _Różnice między plikami w staging area oraz local repository:_
>**git diff --staged**
### * _Różnice między plikami w working tree oraz commitem w local repository:_
>**git diff <commit_sha1>**
### * _Różnice między plikami w working tree oraz najnowszym commitem w local repository:_
>**git diff HEAD**
### * _Odrzucenie zmian:_ 
>**git restore <file_name>**
### * _Wycofywanie zmian ze staging area:_
>**git reset <file_name>**
### * _Przywracanie pliku do stanu w jakim był w ostatnim commicie:_
>**git checkout HEAD <file_name>**

---

## **_DODAWANIE ŁAT:_**
---
**_Rozbijanie zmiany na kilka commitów. Prośba o wybranie danej opcji, najczęściej wybieramy e czyli edit, wtedy możemy edytować dany plik i usunąć z niego zmiany, których nie chcemy w danym commicie. Zapisujemy i mamy gotowy plik do commitu. Następnie dodajemy commit i mamy plik w working area z pozostałą zmianą, którą możemy dodać w nowym commicie._**
### * _Rozbijanie commitu na kilka commitów:_
>**git add --patch <file_name>**

---

## **_CZYM JEST HEAD:_**
---
**_HEAD to unikalny wskaźnik w projekcie, jest on tylko jeden i nie można zmienić jego nazwy. Wskaźnik ten może pokazywać na gałąź (branch) lub bezpośrednio na rewizję (commit). Wyznacza on położenie w projekcie, tzn. gdzie aktualnie się znajdujemy. Sytuacja w której HEAD pokazuje na gałąź jest sytuacją normalną. Z kolei jeśli HEAD pokazuje bezpośrednio na commit to jest to sytacja wyjątkowa. Wtedy mamy "detached HEAD". Jeżeli HEAD pokazuje na brancha np. master to wykonując commit, zarówno HEAD jak i master przesuną się na ten commit. Natomiast jeśli startujemy w punkcie kiedy mamy "detached HEAD" i wykonamy commit to przesuniemy HEAD na ten commit ale master pozostanie tam gdzie był. Taka sytuacja jest niebezpieczna, ponieważ zmieniając w tym momencie commit, przesuwamy HEAD a więc pozostawiamy przed chwilą wykonany commit jako sierotę (nic na niego nie pokazuje)._**

---

## **_BRANCHE I COMMITY:_**
---
### * _Stworzenie nowego brancha o danej nazwie:_
>**git branch <branch_name>**   
### * _Przełączenie się na dany branch (HEAD będzie wskazywał na ten branch):_
>**git checkout <branch_name>**
### * _Stworzenie nowego brancha i przeskok na niego:_       
>**git checkout -b <branch_name>**           
### * _Stworzenie nowego brancha 2 commity przed branchem master:_
>**git checkout -b <branch_name>  master~2** 
### * _Zmiana nazwy lokalnego (na którym się znajdujemy) brancha:_             
>**git branch -m <new_branch_name>**
### * _Skok na dany commit, spowoduje to odłączenie wskaźnika HEAD od brancha:_
>**git checkout <commit_sha1>**
### * _Skok na dany commit na siłę (usunięcie aktualnie wprowadzonych zmian):_     
>**git checkout --force <commit_sha1>**
### * _Skok dwa commity w tył względem HEAD:_
>**git checkout HEAD~2**
### * _Skok jeden commit w tył względem HEAD:_
>**git checkout HEAD~**

**_Nie można jednak skakać do przodu bo commity mają indentyfikatory dla swoich rodziców a nie dzieci. To powoduje, że wskazują one zawsze na commit poprzedni. Możemy za to przeskoczyć na branch, który wskazuje na czubek, czyli najnowszy commit. Z perspektywy gita branch to tylko i wyłącznie wskaźnik na commit. Dlatego jest on bardzo lekki._**

### * _Wyświetlenie branchy w projekcie:_
>**git branch --list**       
### * _Wyświetlenie branchy zaczynających się na feat:_
>**git branch --list feat*** 
### * _Wyświetlenie branchy domergowanych do master:_
>**git branch --merged master**
### * _Wyświetlenie branchy, które nie są domergowane do master:_
>**git branch --no-merged master**
### * _Wyświetlenie wszystkich branchy, zarówno zdalnych jak i lokalnych:_
>**git branch -a**
### * _Wyświetlenie wszystkich branchy (zdalnych i lokalnych) ze wszystkimi informacjami:_
>**git branch -lavv**
### * _Usuwanie brancha:_
>**git branch -d <branch_name>**
### * _Usunięcie brancha na siłę, nawet jeśli nie jest domergowany:_
>**git branch -D <branch_name>**

---

## **_PLIKI NIEŚLEDZONE:_**
---
### * _Usunięcie plików nieśledzonych (checkout ich nie usuwa). Flaga n oznacza na niby (pokaże co się stanie jeśli to wykonasz), d - weź pod uwagę katalogi:_
>**git clean -nd**
### * _Usunięcie plików nieśledzonych (f od force):_
>**git clean -fd**       

---

## **_MERGOWANIE ZMIAN:_**
---
### * _Mergowanie zmian z brancha <branch_name> do brancha na którym się znajdujemy:_
>**git merge <branch_name>**
### * _Mergowanie zmian typu no-fast-forward, czyli stworzy się nowy commit:_
>**git merge --no-ff <branch_name>**
### * _Przerwanie mergowania w stanie np. (master|MERGING):_
>**git merge --abort**
### * _Kontynuwanie mergowania (po rozwiązaniu konfliktu i dodaniu zmiany do staging area):_
>**git merge --continue**   

---   

## **_RESETOWANIE I ODWRACANIE ZMIAN_**
---
### * _Usunięcie konkretnego pliku ze staging area:_
>**git reset <file_name>** 
### * _Przesunięcie wskaźnika HEAD oraz wskaźnika branchowego na dany commit.   Polecenie działa podobnie jak git checkout ale git checkout przesuwa tylko wskaźnik HEAD:_
>**git reset <commit_sha1>**
### * _Przesunięcie wskaźnika HEAD oraz wskaźnika branchowego na dany commit.Propaguje zmiany do working tree i staging area, zastąpi wszystkie zmiany na te,które przychodzą z danego commita. Podobne do git checkout ale git checkout będzie próbował je dopisać:_
>**git reset --hard <commit_sha1>** 
### * _Przesunięcie wskaźnika HEAD oraz wskaźnika branchowego na dany commit. Propaguje zmiany do staging area (jest to wariant domyślny):_
>**git reset --mixed <commit_sha1>** 
### * _Przesunięcie wskaźnika HEAD oraz wskaźnika branchowego na dany commit. Nie propaguje zmian:_ 
>**git reset --soft <commit_sha1>** 
### * _Wprowadzenie zmiany dokładnie przeciwnej jaka została wprowadzona w <commit_sha1>. Tej komendy używamy gdy nie jesteśmy pewni czy ktoś nie pobierze danej gałęzi, ponieważ git reset spowoduje rozjechanie wszystkich zmian np. u kogoś kto pracował na danej gałęzi. Git revert może powodować konflikty jeśli wykonamy go na commicie ze środka historii. Polecenie to natychmiast commituje zmiany:_
>**git revert <commit_sha1>**
### * _Wprowadzenie zmiany dokładnie przeciwnej jaka została wprowadzona w <commit_sha1>. To polecenie nie commituje zmian. Zmiany trafią do katalogu roboczego i będziemy mogli wykonać commit ręcznie:_
>**git revert -n <commit_sha1>**
### * _Odwracanie zmian z poprzednich 2 commitów, commity podajemy w odwrotnej kolejności niż w jakiej zostały one wprowadzone:_
>**git revert -n HEAD HEAD~**
### * _Potwierdzenie rozwiązania konfliktów i dokończenie zmian odwracania commitu:_
>**git revert --continue**
### * _Przerwanie odwracania zmian:_
>**git revert --abort**

---

## **_PRACA ZDALNA:_**
---
### * _Klonowanie repozytorium (utworzy folder o nazwie repozytorium):_
>**git clone <link_ssh_or_https>**
### * _Informacja na temat zdalnego repozytorium, najczęściej origin:_
>**git remote**
### * _Informacje z jakiego zdalnego repozytorium pobieramy zmiany i do jakiego te zmiany wypychamy:_
>**git remote -v**
### * _Wyświetlenie listy gałęzi zdalnych:_
>**git branch -r**
### * _Usuwanie brancha zdalnego:_ 
>**git branch -d -r <origin/branch_name>**

>**git push -d origin <branch_name>**

>**git push origin --delete <branch_name>**

### * _Wypychanie nowego lokalnego brancha na repozytorium zdalne:_
>**git push origin -u <branch_name>**
### * _Wypychanie zmian z brancha lokalnego do brancha zdalnego origin:_
>**git push origin <branch_name>**
### * _Wypychanie zmian z informacją o trackingu, w przyszłości wystarczy robić git push i git będzie wiedział o co chodzi:_
>**git push -u origin <branch_name>**
### * _Pobieranie zmian z brancha zdalnego origin (wszystkie branche zdalne):_
>**git fetch origin**
### * _Domergowanie do brancha na którym jesteśmy, brancha zdalnego master (po wcześniejszym git fetch):_
>**git merge origin/master**
### * _Stworzenie i przełączenie się na nowego brancha lokalnego, który został pobrany ze zdalnego repozytorium:_
>**git checkout -b <local_branch> <remote_branch>**
### * _Pobieranie zmian z repozytorium zdalnego. Polecenie git pull jest jednoczesnym poleceniem git fetch oraz git merge to znaczy, że powinniśmy być na odpowiedniej gałęzi kiedy wykonujemy to polecenie. Poniższe polecenie pobierze zmiany ze zdalnego repozytorium origin z gałęzi master i domerguje je do gałęzi na której się znajdujemy:_
>**git pull origin master** 
### * _Ustawienie aby git pull działało bezpośrednio tylko kiedy nie ma konfliktów:_
>**git config --global pull.ff only**
### * _Śledzenie gałęzi. Ustawienie trackingu z remote origin na lokalny branch feature/zakupy:_
>**git branch -u origin/feature/zakupy feature/zakupy**
### * _Usuwanie trackingu brancha feature/zakupy:_
>**git branch --unset-upstream feature/zakupy**
### * _Stworzenie nowego lokalnego brancha z istniejącego brancha zdalnego, przełączenie się na niego i trackowanie:_
>**git checkout -t origin/feature/zakupy**

---

## **_POPRAWKI COMMITÓW I ZMIANA BAZY:_**
---
### * _Poprawka ostatniego commitu. Uwzględni zmiany w staging area i zastąpi ostatni commit:_
>**git commit --amend**
### * _Poprawka ostatniego commitu. Uwzględni zmiany w staging area i zastąpi ostatni commit. Wersja z poprawieniem wiadomości:_
>**git commit --amend -m "message"**
### * _Zmiana bazy. Będąc na gałęzi, której bazę chcemy zmienić wywołujemy git rebase z parametrem, którym jest gałąź, która ma stać się naszą bazą, to polecenie modyfikuje historię brancha, którego bazę zmieniamy:_
>**git rebase <branch_name>** 

---