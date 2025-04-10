# Analizador-Temperaturas
Parte Teórica  

1. SRP (Single Responsibility Principle): 

Este principio dice que una clase o función debe tener solo una responsabilidad o hacer una sola cosa. Si una clase o función hace muchas cosas, se vuelve difícil de mantener y de entender. Es mejor dividir tareas y que cada parte del código haga algo específico. Ejemplo: Si una clase se encarga de hacer cálculos y también de mostrar los resultados, lo ideal es separarlas en dos clases. 

 

2. Validar la entrada del usuario: 

Es importante validar lo que el usuario ingresa para evitar errores y posibles problemas de seguridad. Si no validamos, el usuario podría ingresar algo inesperado, como texto en vez de un número, lo que podría hacer que el programa falle o incluso permitir ataques maliciosos (como inyecciones de código). OWASP (un proyecto sobre seguridad en aplicaciones web) menciona que la validación de entrada es crucial para evitar vulnerabilidades en las aplicaciones. 

 

3. Separar el código en funciones o clases: 

Separar el código en funciones o clases tiene varios beneficios: 

Reusabilidad: Puedes usar el mismo código en diferentes partes sin duplicarlo. 

Mantenibilidad: Si algo necesita cambiar, lo puedes hacer en una sola parte del código, sin afectar otras. 

Claridad: El código se vuelve más fácil de entender, porque cada función o clase hace una tarea específica. 

Escalabilidad: Es más fácil agregar nuevas funcionalidades sin complicar el código existente. 

 

4. Clean Code vs Código que "funciona": 

Clean Code es un enfoque de programación donde el código es limpio, organizado y fácil de entender. Está escrito para que otros programadores puedan leerlo y mantenerlo fácilmente. En cambio, un código que solo "funciona" puede estar lleno de soluciones rápidas y desordenadas. Aunque funcione, no es fácil de entender ni de modificar. Clean Code usa nombres claros, estructura bien el código y se enfoca en la simplicidad y legibilidad. 

 

5. Errores comunes al pedir datos por consola: 

No validar lo que el usuario ingresa: Permitir que el usuario ingrese cualquier cosa puede causar errores si no se valida. Ejemplo: que el usuario ingrese texto cuando se espera un número. 

No dar mensajes claros: Si no le dices al usuario qué tipo de dato debe ingresar, puede confundirse. Por ejemplo, no decir que se espera un número o no informar qué error ocurrió. 

No manejar errores correctamente: Si el usuario ingresa algo incorrecto, el programa podría fallar si no manejas los errores de forma adecuada. Es importante usar estructuras try-except para evitar que el programa se cierre de manera inesperada. 