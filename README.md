# DARE IT - Testy automatyczne + Python

---
Zajrzyj tutaj :
- [pages](https://github.com/WikMoz/challenge_automated_testing/tree/main/pages)
- [test cases](https://github.com/WikMoz/challenge_automated_testing/tree/main/test_cases)
---
## Spis treści
* [Zadanie 1 - KONFIGURACJA OPROGRAMOWANIA](#zadanie-1)
  * [Podzadanie 1](#podzadanie-1)
  * [Podzadanie 4](#podzadanie-4)

* [Zadanie 2 - SELEKTORY](#zadanie-2)
  * [Podzadanie 2](#podzadanie-2)
  
* [Zadanie 3 - PIERWSZY TEST I ASSERT](#zadanie-3)
* [Zadanie 4 - REFACTOR, DEBUGGER I PRZYPADKI TESTOWE](#zadanie-4)
  * [Podzadania 1](#podzadanie-1-1)
  * [Podzadanie 2](#podzadanie-2-1)
  * [Podzadanie 3](#podzadanie-3)
  * [Podzadanie 4](#podzadanie-4-1)
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
## Podzadanie 1
_Dlaczego zdecydowałam się wziąć udział w wyzwaniu Dare IT Challenge?_

Cześć! Zdecydowałam się wziąć udział w wyzwaniu, ponieważ chciałabym się rozwijać w tym kierunku ⬆️, nauczyć się jak 
najwięcej 🦉📚 i sprawdzić czy dam radę zmierzyć się z testami automatycznymi 🤖🤺.
Brałam udział w Waszym poprzednim challenge'u na testera manualnego i
testowanie z Wami sprawiło mi niesamowicie dużo frajdy 🤸 i dało bardzo dużo pozytwnej energii 🔋 i motywacji. 
Kontynuuję podróż w nieznane 🗽, ale teraz już w ten sposób:

![img_3.png](img_3.png)

## Podzadanie 4
![2023-03-31_16h30_38](https://user-images.githubusercontent.com/122229411/229150021-6541ef57-bbb3-474c-bf86-b2e858834dbe.png)

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
### [Screencasts](https://drive.google.com/drive/folders/13-Fy6u7Ag0Q4AnPPLt_SxCRiXCwA51wn?usp=share_link)
## Podzadanie 4
### [Screenshots](https://github.com/WikMoz/challenge_automated_testing/tree/main/screenshots)
### [Test results](https://github.com/WikMoz/challenge_automated_testing/tree/main/Test%20results)

---