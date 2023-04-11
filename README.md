# DARE IT - Testy automatyczne + Python
---
---
## Spis treści
* [Zadanie 1 - Konfiguracja oprogramowania](#zadanie-1)
  * [Podzadanie 1](#podzadanie-1)
  * [Podzadanie 2](#podzadanie-2)
  * [Podzadanie 3](#podzadanie-3)
  * [Podzadanie 4](#podzadanie-4)
* [Zadanie 2 - Selektory](#zadanie-2)
  * [Podzadanie 1](#podzadanie-1-1)
  * [Podzadanie 2](#podzadanie-2-1)
  * [Podzadanie 3](#podzadanie-3-1)
  * [Podzadanie 4](#podzadanie-4-1)
  * [Podzadanie 5](#podzadanie-5)
  * [Podzadanie 6](#podzadanie-6)

--- 
# Zadanie 1 
**KONFIGURACJA OPROGRAMOWANIA**

---
## Podzadanie 1
Dlaczego zdecydowałam się wziąć udział w wyzwaniu Dare IT Challenge?

Cześć! Zdecydowałam się wziąć udział w wyzwaniu, ponieważ chciałabym się rozwijać w tym kierunku ⬆️, nauczyć się jak 
najwięcej 🦉📚 i sprawdzić czy dam radę zmierzyć się z testami automatycznymi 🤖🤺.
Brałam udział w Waszym poprzednim challenge'u na testera manualnego i
testowanie z Wami sprawiło mi niesamowicie dużo frajdy 🤸 i dało bardzo dużo pozytwnej energii 🔋 i motywacji. 
Kontynuuję podróż w nieznane 🗽, ale teraz już w ten sposób:

![img_3.png](img_3.png)

## Podzadanie 2 
Naprawienie problemu, który wyświetla się na konsoli (nie dotyczy każdego)

## Podzadanie 3
Dodanie kodu do własnego zdalnego repozytorium

## Podzadanie 4
![2023-03-31_16h30_38](https://user-images.githubusercontent.com/122229411/229150021-6541ef57-bbb3-474c-bf86-b2e858834dbe.png)

---
# Zadanie 2
**SELEKTORY**

---

## Podzadanie 1  
(dla chętnych)

## Podzadanie 2
Wypisz wszystkie elementy znajdujące się na stronie, a następnie, pod każdym elementem znalezionym na stronie, wymień 3 działające selektory.

<details>
  <summary>remind_password_hyperlink_xpath</summary>
  <p>
- ```//a[@tabindex='-1']```
- ```//a[starts-with(@class,'Mui')]```
- ```//form[@class='jss1']//child::a ```

<details>
  <summary>scouts_panel_header_xpath</summary>
  <p>
- ```//h5[text()='Scouts Panel']```
- ```//h5[contains(@class,'h5')]```
- ```//div/h5```

<details>
  <summary>login_input_xpath</summary>
  <p>
- ```//input[@id='login']```
- ```//input[@type='text' and @name='login']```
- ```//input[starts-with(@id,'log')] ```

<details>
  <summary>password_input_xpath</summary>
  <p>
- ```//input[@id='password']```
- ```//form[@class='jss1']//descendant::input[@name='password']```
- ```//input[@type='password']```

<details>
  <summary>language_select_menu_xpath</summary>
  <p>
- ```//div[@tabindex="0"]```
- ```//*[@id="__next"]/form/div/div[2]/div/div```
- ```//input[@value='en']//preceding-sibling::div```

<details>
  <summary>language_listbox_xpath</summary>
  <p>
- ```//ul```
- ```//ul[@role='listbox']```
- ```//*[@id="menu-"]/div[3]/ul```

<details>
  <summary>polish_language_option_xpath</summary>
  <p>
- ``` //li[@data-value='pl']```
- ``` //ul/li[1] ```
- ``` //*[@id="menu-"]/div[3]/ul/li[1]```

<details>
  <summary>english_language_option_xpath</summary>
  <p>
-```//ul/li[2]```
-```//li[contains(@data-value,'en')]```
- ```//li[@role='option']//following-sibling::li```

<details>
  <summary>english_language_button_xpath</summary>
  <p>
- ```//*[text()='English'and@role='button']```
- ```//div[starts-with(@class,'MuiSelect-root')]```
- ```//input[@value='en']//preceding-sibling::div```

<details>
  <summary>sign_in_button_xpath</summary>
  <p>
- ```//button[@type='submit']//child::span[1] ```
- ```//span[text()='Sign in']```
- ```//span[@class='MuiButton-label']```

## Podzadanie 3
## Podzadanie 4
## Podzadanie 5
## Podzadanie 6
(dla chętnych)