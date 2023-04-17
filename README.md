# DARE IT - Testy automatyczne + Python
---
---
## Spis treści
* [Zadanie 1 - KONFIGURACJA OPROGRAMOWANIA](#zadanie-1)
  * [Podzadanie 1](#podzadanie-1) 
  * [Podzadanie 2](#podzadanie-2)
  * [Podzadanie 3](#podzadanie-3)
  * [Podzadanie 4](#podzadanie-4)

* [Zadanie 2 - SELEKTORY](#zadanie-2)
  * [Podzadanie 1](#podzadanie-1-1)
  * [Podzadanie 2](#podzadanie-2-1)
  * [Podzadanie 3](#podzadanie-3-1)
  * [Podzadanie 4](#podzadanie-4-1)
  * [Podzadanie 5](#podzadanie-5)
  * [Podzadanie 6](#podzadanie-6)
  
* [Zadanie 3](#zadanie-3)
  * [Podzadanie 1](#podzadanie-1-2) 
  * [Podzadanie 2](#podzadanie-2-2)
  * [Podzadanie 3](#podzadanie-3-2)
  * [Podzadanie 4](#podzadanie-4-2)
  * [Podzadanie 5](#podzadanie-5-1)
--- 
# Zadanie 1 
**KONFIGURACJA OPROGRAMOWANIA**

---
## Podzadanie 1
_Dlaczego zdecydowałam się wziąć udział w wyzwaniu Dare IT Challenge?_

Cześć! Zdecydowałam się wziąć udział w wyzwaniu, ponieważ chciałabym się rozwijać w tym kierunku ⬆️, nauczyć się jak 
najwięcej 🦉📚 i sprawdzić czy dam radę zmierzyć się z testami automatycznymi 🤖🤺.
Brałam udział w Waszym poprzednim challenge'u na testera manualnego i
testowanie z Wami sprawiło mi niesamowicie dużo frajdy 🤸 i dało bardzo dużo pozytwnej energii 🔋 i motywacji. 
Kontynuuję podróż w nieznane 🗽, ale teraz już w ten sposób:

![img_3.png](img_3.png)

## Podzadanie 2 
_Naprawienie problemu, który wyświetla się na konsoli (nie dotyczy każdego)._

## Podzadanie 3
_Dodanie kodu do własnego zdalnego repozytorium._

## Podzadanie 4
![2023-03-31_16h30_38](https://user-images.githubusercontent.com/122229411/229150021-6541ef57-bbb3-474c-bf86-b2e858834dbe.png)

---
# Zadanie 2
**SELEKTORY**

---

## Podzadanie 1  
(dla chętnych) 
_Utworzenie nowego branch'a._ 🌲

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

## Podzadanie 3
_Dodawanie selektorów do projektu - Login page._

## Podzadanie 4
_Dodawanie nowego pliku i klasy do Page Object Mode oraz wpisywanie selektorów - Dashboard._

## Podzadanie 5
_Dodawanie nowego pliku i klasy do Page Object Mode oraz wpisywanie selektorów - Add a match form._

## Podzadanie 6
(dla chętnych)
_Merdżowanie branchy._

---
# Zadanie 3
PIERWSZY TEST I ASSERT
---
## Podzadanie 1
*Uzupełnienie strony logowania* 
- login_page.py

## Podzadanie 2
*Nowy przypadek testowy*
- login_to_the_system.py

## Podzadanie 3
*Assert*

## Podzadanie 4
*Powtórzenie tego, co już wiemy* 
- pages\add_a_player_form.py
- test_cases\add_a_player_form.py

## Pozdadanie 5
*Zadanie dla chętnych*
