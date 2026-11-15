<p align="center"><img src="https://raw.githubusercontent.com/informatica-administrativa-unah/.github/main/profile/marca/logo-1024.png" alt="Logo de la comunidad Informática Administrativa UNAH" width="180"></p>

# Informática Administrativa UNAH

Somos una comunidad de estudiantes de la carrera de Informática Administrativa de la Universidad Nacional Autónoma de Honduras. Aquí juntamos material para aprender y practicar lo que vemos en la carrera, y lo que nos piden afuera cuando buscamos trabajo.

Esta no es una cuenta oficial de la UNAH. No la administra la universidad, ni la facultad, ni ningún docente. La armamos estudiantes, por nuestra cuenta, y cualquiera de la carrera puede sumarse.

## Qué hay

| Repo | Qué tiene |
|---|---|
| [`sql-de-cero-a-avanzado`](https://github.com/informatica-administrativa-unah/sql-de-cero-a-avanzado) | Curso de SQL en 12 temas, con teoría, ejemplos, ejercicios y soluciones, y un revisor que corrige tus respuestas solo. Usa una empresa hondureña de práctica con ventas, inventario y planilla en lempiras |
| [`recursos`](https://github.com/informatica-administrativa-unah/recursos) | Recursos gratis para la carrera (programación, bases de datos, análisis y diseño, redes, web, Excel, Git, carrera profesional). Cada uno trae un ejercicio chico para probarlo el mismo día |
| [`redes`](https://github.com/informatica-administrativa-unah/redes) | Curso práctico de redes en 10 temas: OSI, IPv4, subneteo, VLSM, IPv6, VLANs, enrutamiento, DHCP, DNS, NAT y diagnóstico. Ejercicios de subneteo que se revisan solos y laboratorios para Packet Tracer |
| [`auditoria-informatica`](https://github.com/informatica-administrativa-unah/auditoria-informatica) | Auditoría informática de la teoría a la práctica: planeación, evidencias, hallazgos, riesgos y controles, informe, ética. Plantillas y una auditoría completa resuelta |
| [`ciberseguridad-e-iso-27002`](https://github.com/informatica-administrativa-unah/ciberseguridad-e-iso-27002) | Principios, amenazas, gestión de riesgos, controles (la organización de la ISO/IEC 27002 explicada con nuestras palabras, junto a CIS Controls y NIST CSF), contraseñas, respaldos e incidentes, con casos para resolver |

Todos los cursos usan la misma empresa inventada, Comercial El Guayabo, con sucursales en Tegucigalpa, San Pedro Sula y La Ceiba. Así lo que aprendés en un repo se conecta con los demás: la base de datos del curso de SQL es la que se audita en auditoría, y la red del curso de redes es la que se protege en ciberseguridad.

Vamos a ir sumando repos según lo que la comunidad necesite. Si hay una clase donde te hizo falta material, proponelo con un issue en el repo que más se parezca.

## Preguntas: en Discussions

Las dudas sobre el material van a [Discussions](https://github.com/orgs/informatica-administrativa-unah/discussions), no a los issues. Ahí puede responder cualquiera de la comunidad y la respuesta le queda a quien venga después. Los issues son para avisar de errores y proponer temas; cada repo tiene formularios para eso.

## Practicar con revisión automática

Los cursos de SQL y de redes traen un revisor que compara tus respuestas y te dice qué está bien y qué no, sin darte la solución. Para usarlo:

1. En el repo, botón verde "Use this template" y "Create a new repository": te crea tu propia copia. También sirve hacer fork.
2. Resolvé los ejercicios en tu copia.
3. Hacé commit y push. GitHub corre el revisor solo, y en la pestaña "Actions" ves verde o rojo con el detalle por ejercicio.

## Sin instalar nada: GitHub Codespaces

Si tu compu no tiene Python o no te deja instalar, abrí tu copia en Codespaces: botón "Code", pestaña "Codespaces", "Create codespace on main". Se abre un VS Code en el navegador con todo listo para correr los ejercicios y el revisor.

1. Las cuentas personales de GitHub traen horas gratis cada mes, y los estudiantes verificados en GitHub Education tienen más (la misma cuota que GitHub Pro). El detalle está en la [documentación de facturación de Codespaces](https://docs.github.com/es/billing/managing-billing-for-your-products/managing-billing-for-github-codespaces/about-billing-for-github-codespaces) y en [GitHub Education para estudiantes](https://docs.github.com/es/education/about-github-education/github-education-for-students/about-github-education-for-students).
2. Abrilo en tu copia, no en el repo de la organización, así el uso cuenta en tu cuota personal gratuita.
3. Cuando termines, detené el codespace ("Stop codespace") para no gastar horas, y borrá los que ya no usés.
4. Packet Tracer no corre en Codespaces; para los laboratorios de redes necesitás instalarlo en tu compu.

## Cómo contribuir

No hace falta saber mucho. Un ejercicio nuevo, un error corregido o un enlace que ya no funciona ya ayudan.

1. Hacé fork del repo donde querés aportar.
2. Creá una rama con un nombre que diga qué vas a hacer: `git checkout -b corrige-ejercicio-tema-05`
3. Hacé tus cambios y probalos. En los cursos de SQL y redes eso incluye correr `python herramientas/revisar.py --soluciones`.
4. Commit con un mensaje claro y push a tu fork.
5. Abrí un pull request contando qué cambiaste y por qué.

Cada repo tiene su README con los detalles. Si es tu primer pull request, te recomendamos practicar antes con [`first-contributions`](https://github.com/firstcontributions/first-contributions/blob/main/docs/translations/README.es.md), que tiene la guía en español.

## Reglas de convivencia

1. Respeto. Todos estamos aprendiendo, y preguntar algo básico está bien.
2. Nada de tareas o exámenes resueltos de clases en curso. Aquí se comparte para aprender, no para copiar.
3. Nada de material con derechos de autor sin permiso: PDF de libros pagados, presentaciones de docentes, guías internas.
4. Los datos de práctica son inventados. No subás datos reales de personas ni de empresas.

## Licencia

El material se comparte con licencia MIT: lo podés usar y adaptar, también en tus clases o tutorías, dejando el aviso de la licencia.

## Quién la empezó

La comunidad la arrancó [James V (@Dio77799)](https://github.com/Dio77799), estudiante de la carrera, y la vamos haciendo crecer entre todos. Si querés ayudar a mantenerla, escribile o abrí una propuesta.

## Sobre el logo

El logo es propio de la comunidad: un sello azul noche con dos anillos azules, el nombre de la carrera arriba, UNAH CU abajo y en el centro una base de datos con un gráfico de barras. No es el logo oficial de la carrera ni de la UNAH. Los archivos y el script con el que se dibuja están en `profile/marca/`.
