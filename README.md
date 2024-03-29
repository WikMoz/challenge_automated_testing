# DARE IT - Testy automatyczne + Python

---
Tutaj znajdziesz mój kod :
- [pages](https://github.com/WikMoz/challenge_automated_testing/tree/main/pages)
- [test cases](https://github.com/WikMoz/challenge_automated_testing/tree/main/test_cases)
---
## Spis treści

## [Zadanie 1 - KONFIGURACJA OPROGRAMOWANIA](#zadanie-1)

## [Zadanie 2 - SELEKTORY](#zadanie-2)
  * [Podzadanie 2](#podzadanie-2)
  
## [Zadanie 3 - PIERWSZY TEST I ASSERT](#zadanie-3)

## [Zadanie 4 - REFACTOR, DEBUGGER I PRZYPADKI TESTOWE](#zadanie-4)
  * [Podzadania 1](#podzadanie-1-1)
  * [Podzadanie 2](#podzadanie-2-1)
  * [Podzadanie 3](#podzadanie-3)
  * [Podzadanie 4](#podzadanie-4-1)
  * [Podzadanie 5](#podzadanie-5)

## [Zadanie 5 - ROBOT FRAMEWORK](#zadanie-5)
  * [Podzadanie 1](#podzadanie-1-2)

## [**Zadanie 6 - RAPORTOWANIE BŁĘDÓW I RAPORT Z TESTÓW**](#zadanie-6)
  * [Podzadanie 2](#podzadanie-2-2)
  * [Podzadanie 3](#podzadanie-3-1)
  * [Podzadanie 4](#podzadanie-4-2)
  
--- 

# Zadanie 1 
**KONFIGURACJA OPROGRAMOWANIA**

Cele zadania 1:
1. [x] wykonać testy eksploracyjne aplikacji,
2. [x] dowiedzieć się jakie programy są niezbędne, aby rozpocząć testowanie automatyczne,
3. [x] założyć własne zdalne repozytorium w GitHubie,
4. [x] sklonować repozytorium i skonfigurować środowisko pracy,
5. [x] sformatować plik README.
---

# Zadanie 2
**SELEKTORY**

Cele zadania 2:
1. [x] dowiedzieć się czym są selektory,
2. [x] dowiedzieć się gdzie szukać selektorów,
3. [x] poznać zapis xPath’ów, 
4. [x] zrozumieć czym się kierować, aby wyodrębnić te “najlepsze” selektory
---

## Podzadanie 2
_Wypisz wszystkie elementy znajdujące się na stronie, a następnie, pod każdym elementem znalezionym na stronie, wymień 3 działające selektory._


**Elementy:**

<details>
  <summary>remind_password_hyperlink_xpath</summary>
<p>

- ```//a[@tabindex='-1']```
- ```//a[starts-with(@class,'Mui')]```
- ```//form[@class='jss1']//child::a ```
</p>
</details>

<details>
  <summary>login_input_xpath</summary>
<p>

- ```//input[@id='login']```
- ```//input[@type='text' and @name='login']```
- ```//input[starts-with(@id,'log')] ```
</p>
</details>
<details>
  <summary>password_input_xpath</summary>
<p>

- ```//input[@id='password']```
- ```//form[@class='jss1']//descendant::input[@name='password']```
- ```//input[@type='password']```
</p>
</details>
<details>
  <summary>language_select_menu_xpath</summary>
<p>

- ```//div[@tabindex="0"]```
- ```//*[@id="__next"]/form/div/div[2]/div/div```
- ```//input[@value='en']//preceding-sibling::div```
</p>
</details>
<details>
  <summary>language_listbox_xpath</summary>
<p>

- ```//ul```
- ```//ul[@role='listbox']```
- ```//*[@id="menu-"]/div[3]/ul```
</p>
</details>
<details>
  <summary>polish_language_option_xpath</summary>
<p>

- ```//li[@data-value='pl']```
- ```//ul/li[1] ```
- ```//*[@id="menu-"]/div[3]/ul/li[1]```
</p>
</details>
<details>
  <summary>english_language_option_xpath</summary>
<p>

- ```//ul/li[2]```
- ```//li[contains(@data-value,'en')]```
- ```//li[@role='option']//following-sibling::li```
</p>
</details>

<details>
  <summary>sign_in_button_xpath</summary>
<p>

- ```//button[@type='submit']//child::span[1] ```
- ```//span[text()='Sign in']```
- ```//span[@class='MuiButton-label']```
</p>
</details>

---
# Zadanie 3

**PIERWSZY TEST I ASSERT**

Cele zadania 3:
1. [x] poznać framework, na którym będziemy pracować,
2. [x] klikać w elementy na stronie za pomocą komend,
3. [x] wypełniać pola tekstem za pomocą komend,
4. [x] wykorzystać assert title, 
5. [x] uruchomić test.


---

# Zadanie 4

**REFACTOR, DEBUGGER I PRZYPADKI TESTOWE**

Cele zadania 4:
1. [x] wykonać refactor naszego kodu,
2. [x] dowiedzieć się jak pracować z debuggerem,
3. [x] zaprojektować i napisać test case’y,
4. [x] zautomatyzować stronę internetową na podstawie swoich TC.

- [pages](https://github.com/WikMoz/challenge_automated_testing/tree/main/pages)
- [test cases](https://github.com/WikMoz/challenge_automated_testing/tree/main/test_cases)

## Podzadanie 1
### [Test cases](https://docs.google.com/spreadsheets/d/1SZTZz8OM2_jrhuyFVGiuhYWc3yNVn80e2h4A2Dd-aKg/edit?usp=share_link)

## Podzadanie 2
### [Test cases - code](https://github.com/WikMoz/challenge_automated_testing/tree/main/test_cases)

## Podzadanie 3
### [Screencasts](https://drive.google.com/drive/folders/13-Fy6u7Ag0Q4AnPPLt_SxCRiXCwA51wn?usp=share_link) 📽

## Podzadanie 4 
(dla chętnych)

### [Screenshots](https://github.com/WikMoz/challenge_automated_testing/tree/main/screenshots) 📸
### [Test results](https://github.com/WikMoz/challenge_automated_testing/tree/main/Test%20results)

## Podzadanie 5
(dla chętnych)

`if...else` --> [`def test_change_leg(self)`](https://github.com/WikMoz/challenge_automated_testing/blob/main/test_cases/adding_new_player.py)

---

# Zadanie 5
**ROBOT FRAMEWORK**

Cele zadania 5:
1. [x] dowiedzieć się czym jest Smoke Tests
2. [x] dowiedzieć się jak skonfigurować Suite Test
3. [x] poznać nowy framework,
4. [x] wygenerować automatycznie raport

## Podzadanie 1
[ROBOT FRAMEWORK](https://github.com/WikMoz/scoutspanel_robotframework)


---

# Zadanie 6
**RAPORTOWANIE BŁĘDÓW I RAPORT Z TESTÓW**

Cele zadania 6:
1. [x] wykorzystać projekty w jedynym słusznym celu - wyłapywaniu bugów,
2. [x] zapoznać się ze strukturą prawidłowo zgłoszonego buga,
3. [x] zapoznać się ze strukturą raportów z testów
4. [x] stworzyć repozytorium z funkcjonalnym portfolio w README file.

## Podzadanie 2
[Bug report](https://docs.google.com/spreadsheets/d/1Box018tjWX_dN2I6KCCwPfX5f0vzeeOLH3Y743uoJKg/edit?usp=share_link) 🐛

## Podzadanie 3
[Test report](https://docs.google.com/spreadsheets/d/10aMmj4evYu9VtLWLdEiC9k36R_p-sr50jVYqDm6iWgU/edit?usp=share_link) 📃

## Podzadanie 4
[Portfolio](https://github.com/WikMoz/Portfolio) 🖼

