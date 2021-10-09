def Fechas_comunes(list):
    fecha1 = set(list)
    fecha2 = set(list)

    return fecha1 & fecha2



vacunas=[
    {
     'nombre':'sputnik V',
     'cantidad_de_dosis':2,
     'intervalo': 21,
     'edad_minima': 18
    },

    {
     'nombre':'Covishield',
     'cantidad_de_dosis':2,
     'intervalo': 56,
     'edad_minima': 18
     },

    {
     'nombre': 'Sinopharm',
     'cantidad_de_dosis': 2,
     'intervalo': 21,
     'edad_minima': 18
    },
    {
     'nombre': 'AstraZeneca',
     'cantidad_de_dosis': 2,
     'intervalo': 56,
     'edad_minima': 18
    },

]
personas=[
    {'nombre':'Ignacio','apellido':'Gomez','dni':'21323232','domicilio':'Madariaga 1900'},
    {'nombre':'Maria','apellido':'Palma','dni':'35465454','domicilio':'Rivadavia 1225'},
    {'nombre':'Miguel','apellido':'Gonzalez','dni':'43545455','domicilio':'Colon s/n'}
]



registro=[
    [personas[1],vacunas[0],1,'12/03/2021'],
    [personas[0],vacunas[2],1,'01/01/2021'],
    [personas[2],vacunas[1],1,'12/05/2021'],
    [personas[1],vacunas[0],2,'20/06/2021']
]



resultado = Fechas_comunes(registro)

print(resultado)