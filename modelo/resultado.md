# Resultado del modelo

Los números ordenan juicios, no miden nada. Ver `comparar.py` y `rasgos.json`.

## Posterior según el prior

| Prior | Nave real | Montaje completo | Siembra barata | Acceso periférico inflado | Invención |
|---|---|---|---|---|---|
| escéptico (prior) | <1% | 3% | 17% | 40% | 40% |
| escéptico (posterior) | <1% | 1% | 23% | 60% | 16% |
| referencia (prior) | 1% | 5% | 24% | 35% | 35% |
| referencia (posterior) | <1% | 2% | 33% | 52% | 14% |
| parejo (prior) | 20% | 20% | 20% | 20% | 20% |
| parejo (posterior) | <1% | 9% | 38% | 41% | 11% |
| creyente (prior) | 40% | 10% | 15% | 15% | 20% |
| creyente (posterior) | 1% | 6% | 37% | 41% | 15% |

## Sin un grupo de rasgos (prior: referencia)

| Grupo quitado | Nave real | Montaje completo | Siembra barata | Acceso periférico inflado | Invención |
|---|---|---|---|---|---|
| exposición | <1% | 1% | 21% | 53% | 26% |
| demostraciones | <1% | 7% | 67% | 20% | 5% |
| carpetas | <1% | 1% | 12% | 69% | 18% |
| motivos | <1% | 2% | 31% | 50% | 17% |
| física | <1% | 2% | 32% | 52% | 14% |
| rastro institucional | <1% | 2% | 32% | 43% | 24% |
| blanco | <1% | 2% | 34% | 53% | 11% |

## Estabilidad (20000 sorteos, ruido logit sd 1.0)

| Hipótesis | Queda primera | p05 | mediana | p95 |
|---|---|---|---|---|
| Nave real | <1% | <1% | <1% | <1% |
| Montaje completo | <1% | <1% | 1% | 7% |
| Siembra barata | 32% | 8% | 31% | 68% |
| Acceso periférico inflado | 61% | 16% | 48% | 80% |
| Invención | 7% | 3% | 12% | 41% |

## Peso de cada rasgo: Siembra barata contra Invención

Decibanes; positivo favorece a la primera. 10 dB equivale a una razón de 10 a 1.

| Rasgo | Grupo | dB |
|---|---|---|
| Un solo disco de cerca, segundos, con orden de mirar al frente; ocho de lejos | exposición | +7.3 |
| Todo lo extraterrestre viene de carpetas o de lo que le dijeron; su primera impresión fue que la nave era propia | carpetas | +7.3 |
| Él mismo dice desde 1989 que pudo ser desinformación y que el paso junto al disco fue deliberado | carpetas | +7.3 |
| W-2 con pagador real aunque de nombre inexistente; conocía vuelos, colectivos y EG&G | rastro institucional | +7.3 |
| Unas seis visitas, de guardia, siempre escoltado | exposición | +2.0 |
| Hojas de una o dos páginas que mezclan propulsión, autopsias, religión y proyectos ajenos, leídas a solas | carpetas | +2.0 |
| Las 65 correcciones y los contenedores aparecen bajo hipnosis, con preguntas que inducen | motivos | +2.0 |
| Existe un Site 4 real en Tonopah con personal que vuela desde Las Vegas | rastro institucional | +2.0 |
| Los motivos de las carpetas coinciden con el papel de AFOSI de 1983 y con la declaración de Lear de 1987 | motivos | +0.0 |
| El elemento 115 falta en mayo de 1989 y aparece en noviembre; la física no se sostiene | física | +0.0 |
| Títulos del MIT y Caltech sin registro; en 1986 declaró ser procesador de fotos; en Los Alamos fue técnico contratista | física | +0.0 |
| Conocía a Lear, promotor público desde 1987, antes de postularse; según Lear, quien contrataba preguntó por ese vínculo | blanco | +0.0 |
| Sin instalación visible en Papoose en imágenes de 1988; sin registro suyo en las listas de seguridad | rastro institucional | -2.0 |
| Ya hacía excursiones a mirar Groom en septiembre de 1988, antes de ser contratado | blanco | -2.0 |
| Demostraciones de laboratorio con el reactor (pelota, vela, disco negro) | demostraciones | -7.3 |
| Presenció un vuelo corto del disco | demostraciones | -7.3 |
