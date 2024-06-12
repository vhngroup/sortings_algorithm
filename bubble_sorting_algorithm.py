import flet as ft
import random
import time

#interfaz grafica
def main(page: ft.page):
    
    def create_containers(number):
        container_list=[]
        for _ in range(number):
        #El guion al piso "_" indica que no hare nada cone sa variable, no retornare nada.
            container_list.append(
                ft.Container(
                content=ft.Text(value=random.randint(1,100)),
                alignment=ft.alignment.center,
                width=50,
                height=50,
                bgcolor=ft.colors.ORANGE,
                border_radius=25,
                )
            )
        return container_list
    
    # contenedor = ft.Container(
    # content=ft.Text(value="hola2"),
    # alignment=ft.alignment.center,
    # width=50,
    # height=50,
    # bgcolor=ft.colors.ORANGE,
    # border_radius=25,
    # )
    #Burn in 10 elements but i can used input for user keyboard in.
    row = ft.Row(controls=(create_containers(10)))
    page.add(row) #Create a visual sorting row elements
    time.sleep(3)
#Logic part or algoritm
    arr = row.controls
    n = len(arr)
    for i in range(n):
        for  j in range(0, n-i-1):
            arr[j].bgcolor = ft.colors.YELLOW
            arr[j + 1].bgcolor = ft.colors.BLUE
            time.sleep(0.5)
            page.update()
            if int(arr[j].content.value) > int(arr[ j + 1].content.value): #Extraemos el valor por cada contenedor
                arr[j], arr[j + 1] = arr[ j + 1] , arr[j]
            arr[j].bgcolor = ft.colors.ORANGE
            arr[j + 1].bgcolor = ft.colors.ORANGE
        arr[n-i-1].bgcolor = ft.colors.GREY

    page.update()

ft.app(target=main)

