# Algoritmo de Euclides estendido

Este programa mostra o passo-a-passo para a obtenção dos valores _x_, _y_ e _mdc(a, b)_ tal que:
<center>`(x * a) + (y * b) = mdc(a, b)`</center>

Mais informações em:
  - [Euclidean Algorithm](http://en.wikipedia.org/wiki/Euclidean_algorithm);
  - [Extended Euclidean Algorithm](http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)

## Autor
Escrito por Antonio Carlos Falcão Petri, BCC-014, UFSCar, Campus São Carlos

## Motivação
Trabalho desenvolvido para a disciplina de Estruturas Discretas, ministrada pelo Prof. Doutor Estevam Rafael Hruschka Júnior – 2º semestre de 2014

## Uso

```
python euclides.py
```

Para rodar os valores de teste, edite a _flag_ `testing` no começo do código

Testado com Python 2.7.6, compatível com Python 2.x

## Casos de Testes

####MDC(32, 76):
```
Calculando MDC(32, 76):
(1)	32/76 = 0 resta 32
(2)	76/32 = 2 resta 12
(3)	32/12 = 2 resta 8
(4)	12/8  = 1 resta 4
(5)	 8/4  = 2 resta 0


(1) => 32 = 32 * 1 + 76 * 0

(2) => 12 = 76 * 1 + 2 * -32
    => 12 = 76 * 1 + 2 * -(32 * 1 + 76 * 0)
    => 12 = 32 * -2 + 76 * 1

(3) => 8 = 32 * 1 + 2 * -12
    => 8 = (32 * 1 + 76 * 0) * 1 + 2 * -(32 * -2 + 76 * 1)
    => 8 = 32 * 5 + 32 * -2

(4) => 4 = 12 * 1 + 1 * -8
    => 4 = (32 * -2 + 76 * 1) * 1 + 1 * -(32 * 5 + 32 * -2)
    => 4 = 32 * -7 + 12 * 3

MDC(32, 76) = -7 * 32 + 3 * 76 = 4

```

####MDC(76, 92):
```
Calculando MDC(76, 92):
(1)	76/92 = 0 resta 76
(2)	92/76 = 1 resta 16
(3)	76/16 = 4 resta 12
(4)	16/12 = 1 resta 4
(5)	12/4  = 3 resta 0


(1) => 76 = 76 * 1 + 92 * 0

(2) => 16 = 92 * 1 + 1 * -76
    => 16 = 92 * 1 + 1 * -(76 * 1 + 92 * 0)
    => 16 = 76 * -1 + 92 * 1

(3) => 12 = 76 * 1 + 4 * -16
    => 12 = (76 * 1 + 92 * 0) * 1 + 4 * -(76 * -1 + 92 * 1)
    => 12 = 76 * 5 + 76 * -4

(4) => 4 = 16 * 1 + 1 * -12
    => 4 = (76 * -1 + 92 * 1) * 1 + 1 * -(76 * 5 + 76 * -4)
    => 4 = 76 * -6 + 16 * 5

MDC(76, 92) = -6 * 76 + 5 * 92 = 4

```

####MDC(15, 69):
```
Calculando MDC(15, 69):
(1)	15/69 = 0 resta 15
(2)	69/15 = 4 resta 9
(3)	15/9  = 1 resta 6
(4)	 9/6  = 1 resta 3
(5)	 6/3  = 2 resta 0


(1) => 15 = 15 * 1 + 69 * 0

(2) => 9 = 69 * 1 + 4 * -15
    => 9 = 69 * 1 + 4 * -(15 * 1 + 69 * 0)
    => 9 = 15 * -4 + 69 * 1

(3) => 6 = 15 * 1 + 1 * -9
    => 6 = (15 * 1 + 69 * 0) * 1 + 1 * -(15 * -4 + 69 * 1)
    => 6 = 15 * 5 + 15 * -1

(4) => 3 = 9 * 1 + 1 * -6
    => 3 = (15 * -4 + 69 * 1) * 1 + 1 * -(15 * 5 + 15 * -1)
    => 3 = 15 * -9 + 9 * 2

MDC(15, 69) = -9 * 15 + 2 * 69 = 3
```

####MDC(29, 83):
```
Calculando MDC(29, 83):
(1)	29/83 = 0 resta 29
(2)	83/29 = 2 resta 25
(3)	29/25 = 1 resta 4
(4)	25/4  = 6 resta 1
(5)	 4/1  = 4 resta 0


(1) => 29 = 29 * 1 + 83 * 0

(2) => 25 = 83 * 1 + 2 * -29
    => 25 = 83 * 1 + 2 * -(29 * 1 + 83 * 0)
    => 25 = 29 * -2 + 83 * 1

(3) => 4 = 29 * 1 + 1 * -25
    => 4 = (29 * 1 + 83 * 0) * 1 + 1 * -(29 * -2 + 83 * 1)
    => 4 = 29 * 3 + 29 * -1

(4) => 1 = 25 * 1 + 6 * -4
    => 1 = (29 * -2 + 83 * 1) * 1 + 6 * -(29 * 3 + 29 * -1)
    => 1 = 29 * -20 + 25 * 7

MDC(29, 83) = -20 * 29 + 7 * 83 = 1
```

####MDC(96, 11):
```
Calculando MDC(96, 11):
(1)	96/11 = 8 resta 8
(2)	11/8  = 1 resta 3
(3)	 8/3  = 2 resta 2
(4)	 3/2  = 1 resta 1
(5)	 2/1  = 2 resta 0


(1) => 8 = 96 * 1 + 11 * -8

(2) => 3 = 11 * 1 + 1 * -8
    => 3 = 11 * 1 + 1 * -(96 * 1 + 11 * -8)
    => 3 = 96 * -1 + 11 * 9

(3) => 2 = 8 * 1 + 2 * -3
    => 2 = (96 * 1 + 11 * -8) * 1 + 2 * -(96 * -1 + 11 * 9)
    => 2 = 96 * 3 + 8 * -26

(4) => 1 = 3 * 1 + 1 * -2
    => 1 = (96 * -1 + 11 * 9) * 1 + 1 * -(96 * 3 + 8 * -26)
    => 1 = 96 * -4 + 3 * 35

MDC(96, 11) = -4 * 96 + 35 * 11 = 1
```

####MDC(77, 55):
```
Calculando MDC(77, 55):
(1)	77/55 = 1 resta 22
(2)	55/22 = 2 resta 11
(3)	22/11 = 2 resta 0


(1) => 22 = 77 * 1 + 55 * -1

(2) => 11 = 55 * 1 + 2 * -22
    => 11 = 55 * 1 + 2 * -(77 * 1 + 55 * -1)
    => 11 = 77 * -2 + 55 * 3

MDC(77, 55) = -2 * 77 + 3 * 55 = 11
```
