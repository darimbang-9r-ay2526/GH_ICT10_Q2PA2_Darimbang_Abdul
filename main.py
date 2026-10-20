# Working with Sets
from pyscript import document, display  # importing document and display package


def members(e):

    document.getElementById('output').innerHTML = ''
    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value
    full_name= first_name + last_name


    Grade7 = {'Austin Maneja', 'Anton Dela Rosa', 'Abdul Ibrahim', 'Ranbhir Sekhon'}
    Grade8 = {'Hans Ukwatte', 'Iohann Villanueva', 'Mani Tubo', 'Sinko Kaba'}
    Grade9 = {'Zhaimer Mamacotao', 'Zeeshan Dalidig', 'Arkin Estacio', 'Ben Bocarie'}
    Grade10 = {'Khail Resurreccion', 'Sebastian Uclaray', 'Raver Estacio', 'Zangief Briones'}
    members = (Grade7| Grade8 | Grade9 | Grade10)
    members.add(full_name)

    display(f'List of members {members} amount of members {len(members)}', target='output')


