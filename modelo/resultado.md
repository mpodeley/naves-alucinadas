# Resultado del modelo

Los números ordenan juicios, no miden nada. Ver `comparar.py` y `rasgos.json`.

## Posterior según el prior

| Prior | Nave real | Montaje completo | Siembra barata | Acceso periférico inflado | Invención | Siembra de segunda mano |
|---|---|---|---|---|---|---|
| escéptico (prior) | <1% | 3% | 17% | 24% | 40% | 16% |
| escéptico (posterior) | <1% | 1% | 31% | 43% | 14% | 10% |
| referencia (prior) | 1% | 5% | 24% | 21% | 35% | 14% |
| referencia (posterior) | <1% | 2% | 42% | 36% | 12% | 9% |
| parejo (prior) | 17% | 17% | 17% | 17% | 17% | 17% |
| parejo (posterior) | <1% | 8% | 37% | 35% | 7% | 13% |
| creyente (prior) | 40% | 10% | 15% | 9% | 20% | 6% |
| creyente (posterior) | 1% | 7% | 47% | 27% | 12% | 7% |

## Sin un grupo de rasgos (prior: referencia)

| Grupo quitado | Nave real | Montaje completo | Siembra barata | Acceso periférico inflado | Invención | Siembra de segunda mano |
|---|---|---|---|---|---|---|
| exposición | <1% | 1% | 28% | 38% | 23% | 9% |
| demostraciones | <1% | 7% | 74% | 12% | 4% | 3% |
| carpetas | <1% | 1% | 17% | 52% | 17% | 13% |
| motivos | <1% | 2% | 41% | 35% | 14% | 8% |
| física | <1% | 2% | 42% | 35% | 12% | 9% |
| rastro institucional | <1% | 2% | 41% | 30% | 20% | 7% |
| blanco | <1% | 2% | 43% | 37% | 10% | 9% |
| linaje | <1% | 2% | 32% | 31% | 14% | 22% |

## Estabilidad (20000 sorteos, ruido logit sd 1.0)

| Hipótesis | Queda primera | p05 | mediana | p95 |
|---|---|---|---|---|
| Nave real | <1% | <1% | <1% | <1% |
| Montaje completo | <1% | <1% | 2% | 7% |
| Siembra barata | 53% | 12% | 39% | 73% |
| Acceso periférico inflado | 39% | 9% | 31% | 65% |
| Invención | 6% | 2% | 10% | 37% |
| Siembra de segunda mano | 2% | 2% | 8% | 27% |

## Peso de cada rasgo: Siembra barata contra Invención

Decibanes; positivo favorece a la primera. 10 dB equivale a una razón de 10 a 1.

| Rasgo | Grupo | dB |
|---|---|---|
| Un solo disco de cerca, segundos, con orden de mirar al frente; ocho de lejos | exposición | +7.3 |
| Todo lo extraterrestre viene de carpetas o de lo que le dijeron; su primera impresión fue que la nave era propia | carpetas | +7.3 |
| Él mismo dice desde 1989 que pudo ser desinformación y que el paso junto al disco fue deliberado | carpetas | +7.3 |
| W-2 con pagador real aunque de nombre inexistente; conocía vuelos, colectivos y EG&G | rastro institucional | +7.3 |
| Lazar descarta lo distintivo de Lear: Dulce, el tratado, las abducciones, la base subterránea de Groom | linaje | +7.3 |
| Unas seis visitas, de guardia, siempre escoltado | exposición | +2.0 |
| Hojas de una o dos páginas que mezclan propulsión, autopsias, religión y proyectos ajenos, leídas a solas | carpetas | +2.0 |
| Las 65 correcciones y los contenedores quedan registrados por primera vez bajo hipnosis; el hipnotizador llegó con temario y lecturas previas | motivos | +2.0 |
| Existe un Site 4 real en Tonopah con personal que vuela desde Las Vegas | rastro institucional | +2.0 |
| Los motivos de las carpetas coinciden con el papel de AFOSI de 1983, con lo que Lear decía en público desde 1987 y con el especial de televisión de octubre de 1988 | motivos | +0.0 |
| El elemento 115 falta en mayo de 1989 y aparece en noviembre; la física no se sostiene | física | +0.0 |
| Títulos del MIT y Caltech sin registro; en 1986 declaró ser procesador de fotos; en Los Alamos fue técnico contratista | física | +0.0 |
| Conocía a Lear, promotor público desde 1987, antes de postularse; según Lear, quien contrataba preguntó por ese vínculo | blanco | +0.0 |
| El vocabulario propio de las carpetas (containers, 65 corrections, the Kids, Reticulum 4, Galileo, Sidekick, Looking Glass, elemento 115) no aparece en Lear ni en el circuito de Kirtland antes de diciembre de 1988 | linaje | +0.0 |
| Ese vocabulario aparece en Lear después, en 1991, y Lear nombra a Lazar como fuente | linaje | +0.0 |
| El incidente con muertos lleva el año 1979, igual que el de Lear de 1987; Lear le atribuye a Lazar dichos sobre Datil que Lazar no reconoce | linaje | +0.0 |
| Sin instalación visible en Papoose en imágenes de 1988; sin registro suyo en las listas de seguridad | rastro institucional | -2.0 |
| Ya hacía excursiones a mirar Groom en septiembre de 1988, antes de ser contratado | blanco | -2.0 |
| Demostraciones de laboratorio con el reactor (pelota, vela, disco negro) | demostraciones | -7.3 |
| Presenció un vuelo corto del disco | demostraciones | -7.3 |
