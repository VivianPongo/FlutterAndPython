import flet 
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    UserControl,
    border_radius,
    colors,
)

class CalculadoraApp(UserControl):
    def build(self):
        self.reseteo()
        self.resultado = Text(value="0", color=colors.WHITE, size=20)

        return Container(
            width=350,
            border_radius=border_radius.all(20),
            bgcolor=colors.BLACK,
            padding=20,
            content=Column(
                controls=[
                    Row(
                        controls=[
                            self.resultado
                        ],
                        alignment="end"
                    ),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="AC",
                                bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1.5,
                                width=70,
                                on_click=self.button_clicked, 
                                data= "AC"
                                ),
                            ElevatedButton(text="+/-",  bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1.5,width=70, on_click=self.button_clicked,
                                data= "+/-"),
                            ElevatedButton(text="%",  bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1.5,width=70, 
                                on_click=self.button_clicked,
                                data= "%"),
                            ElevatedButton(text="/",  bgcolor=colors.ORANGE,
                                color=colors.BLACK,
                                expand=1.5,width=70, 
                                on_click=self.button_clicked,
                                data= "/"),
                        ],
                    ),
                    Row(
                        controls=[
                            ElevatedButton(text="7", bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1.5, width=70, 
                                on_click=self.button_clicked,
                                data= "7"),
                            ElevatedButton(text="8", bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1.5,width=70, 
                                on_click=self.button_clicked,
                                data= "8"),
                            ElevatedButton(text="9", bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1.5,width=70, 
                                on_click=self.button_clicked,
                                data= "9"),
                            ElevatedButton(text="*", bgcolor=colors.ORANGE,
                                color=colors.BLACK,
                                expand=1.5,width=70, 
                                on_click=self.button_clicked,
                                data= "*"),
                        ]
                    ),
                    
                    Row(
                        controls=[
                            ElevatedButton(text="4", bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1.5,width=70, 
                                on_click=self.button_clicked,
                                data= "4"),
                            ElevatedButton(text="5", bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1.5,width=70, 
                                on_click=self.button_clicked,
                                data= "5"),
                            ElevatedButton(text="6", bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1.5,width=70, 
                                on_click=self.button_clicked,
                                data= "6"),
                            ElevatedButton(text="-", bgcolor=colors.ORANGE,
                                color=colors.BLACK,
                                expand=1.5,width=70, 
                                on_click=self.button_clicked,
                                data= "-"),
                        ]
                    ),
                    
                    Row(
                        controls=[
                            ElevatedButton(text="1", bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1.5,width=70, 
                                on_click=self.button_clicked,
                                data= "1"),
                            ElevatedButton(text="2", bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1.5,width=70, 
                                on_click=self.button_clicked,
                                data= "2"),
                            ElevatedButton(text="3", bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1.5,width=70,
                                on_click=self.button_clicked,
                                data= "3"),
                            ElevatedButton(text="+", bgcolor=colors.ORANGE,
                                color=colors.BLACK,
                                expand=1.5,width=70, data= "+",
                                on_click=self.button_clicked,),

                        ]
                    ),

                    Row(
                        controls=[
                            ElevatedButton(text="0", bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1.5,width=70,
                                on_click=self.button_clicked,
                                data= "0"),
                            ElevatedButton(text=".", bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1.5,width=70,
                                on_click=self.button_clicked,
                                data= "."),
                            ElevatedButton(text="=", bgcolor=colors.BLUE_GREY_100,
                                color=colors.BLACK,
                                expand=1.5,width=70, 
                                on_click=self.button_clicked,
                                data= "="
                                
                                ),

                        ]
                    ),

                ]
            )

        )
    
    def formato_numero(self, num):
        if num % 1 == 0:
            return int(num) #mira si es un numero o no
        else:
            return num
    
    def button_clicked(self, e):
        data = e.control.data
        if self.resultado.value == "Error" or data == "AC":
            self.resultado.value = "0"
            self.reseteo()

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.resultado.value == "0" or self.nueva_operacion == True:
                self.resultado.value = data

        elif data in ("+", "-", "*", "/"):
            self.resultado.value = self.calcular(
                self.numero1, float(self.resultado.value), self.operador
            )
            self.operador = data

            if self.resultado.value == "Error":
                self.numero1 = "0"
            else:
                self.numero1 = float(self.resultado.value)
            self.nueva_operacion = True

        elif data in ("="):
            self.resultado.value = self.calcular(
                self.numero1, float(self.resultado.value), self.operador
            )
            self.reseteo()

        elif data in ("%"):
            self.resultado.value = float(self.resultado.value)/100
            self.reseteo()

        elif data in ("+/-"):
            if float(self.resultado.value)>0:
                self.resultado.value = "-" + str(self.resultado.value)
            elif float(self.resultado.value)<0:
                self.resultado.value = str(self.formato_numero(abs(float(self.resultado.value))))


        self.update()
    
    def calcular(self, numero1, numero2, operador):
        if operador == "+":
            return self.formato_numero(numero1 + numero2)
        elif operador == "-":
            return self.formato_numero(numero1 - numero2)
        elif operador == "*":
            return self.formato_numero(numero1 * numero2)
        elif operador == "/":
            if numero2 == 0:
                return "Error"
            else:
                return self.formato_numero(numero1 / numero2)

    def reseteo(self):
        self.operador = "+" #atributo
        self.numero1=0
        self.nueva_operacion = True




def main(page: Page):
    page.title = "Calc App"
    # create application instance
    calc = CalculadoraApp()

    # add application's root control to the page
    page.add(
        calc, 
        Text("hola mundo")
    )


flet.app(target=main)